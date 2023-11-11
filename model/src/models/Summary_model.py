from typing import Any
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from scipy.spatial.distance import cosine

class SummaryModel:
    def __init__(self, centers, thr:float=0.3):
        self.tokenizer = AutoTokenizer.from_pretrained("zaaabik/t5-russian-summarization-detox-finetuning")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("zaaabik/t5-russian-summarization-detox-finetuning")
        self.centers = centers
        self.thr = thr
    def __call__(self, sentence) -> Any:
        tokens = torch.Tensor(self.tokenizer(sentence).input_ids).int()
        emb = self.model.encoder(tokens[None, ...]).mean(dim=1).suqeeze()
        stop = []
        for name, t_emb in self.centers.items():
            if cosine(emb, t_emb) > self.thr:
                stop.append(name)

        return stop

        