import pytorch_lightning as pl
from torch_ema import ExponentialMovingAverage
from torch import nn
import torch
from transformers import AutoModelForSequenceClassification
import torch.nn.functional as F

class AAMSoftmaxLoss(nn.Module):
    # Additive angular margin softmax loss

    def __init__(self, nOut, nClasses,
                 ):
        super(AAMSoftmaxLoss, self).__init__()
        self.in_feats = nOut
        self.weight = torch.nn.Parameter(torch.FloatTensor(nClasses, nOut), requires_grad=True)

    def forward(self, x):


        # cos(theta)
        cosine = F.linear(F.normalize(x), F.normalize(self.weight))
        return cosine


class Model(pl.LightningModule):
    def __init__(
        self,
        lr=0.1,
        steps=10,
        batch_size_train=32,
        batch_size_val=1,

    ):
        super().__init__()
        self.save_hyperparameters()

        self.model = AutoModelForSequenceClassification.from_pretrained("philschmid/RoBERTa-Banking77")
        self.model.classifier.out_proj = nn.Identity()
        self.head = AAMSoftmaxLoss(768, 3)

    def training_step(self, batch, batch_idx):
        feats = self.model(torch.stack(batch["input_ids"]).T,
                           torch.stack(batch["attention_mask"]).T)["logits"]
        loss, accuracy = self.head(feats, batch["sentiment"])
        self.log("Train_accuracy", accuracy, on_epoch=True,
                 on_step=True, prog_bar=True,)
        self.log(
              "Train_loss",
              loss,
              on_epoch=True,
              on_step=True,
              prog_bar=True,
              batch_size=self.hparams.batch_size_train,
          )
        return loss


    def validation_step(self, batch, batch_idx):
        feats = self.model(torch.stack(batch["input_ids"]).T,
                           torch.stack(batch["attention_mask"]).T)["logits"]
        loss, accuracy = self.head(feats, batch["sentiment"])
        self.log("Validation_accuracy", accuracy, on_epoch=True,
                 on_step=True, prog_bar=True,)
        self.log(
              "Validation_loss",
              loss,
              on_epoch=True,
              on_step=True,
              prog_bar=True,
              batch_size=self.hparams.batch_size_train,
          )
        return loss

    def configure_optimizers(self):
        opt = torch.optim.AdamW(list(self.model.parameters()) + list(self.head.parameters()),
                                  lr=self.hparams.lr)

        sch = torch.optim.lr_scheduler.OneCycleLR(opt, max_lr=self.hparams.lr,
                                                   total_steps=self.hparams.steps,
                                                  pct_start=0.05,)

        self.ema = ExponentialMovingAverage(list(self.model.parameters()) + list(self.head.parameters()), 0.97)
        return ([opt,],
                [{"scheduler": sch, "interval": "step"},])

    def optimizer_step(self, *args, **kwargs):
      super().optimizer_step(*args, **kwargs)
      self.ema.update(list(self.model.parameters()) + list(self.head.parameters()))