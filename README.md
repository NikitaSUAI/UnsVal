# client - ReactApp

To run dev-server execute the folowing commands:
```sh
npm i
npm start
```
The dev-server starts on [http://localhost:3000](http://localhost:3000)

# server - DjangoRestFramework

### Run dev-server for the first time: 

1. Run docker container with postgres-database
>NOTE: Execute this line every time you need run dev-server
```
docker run --name server -e POSTGRES_PASSWORD=demo -e POSTGRES_USER=demo -e POSTGRES_DB=core -d -p 5433:5432 postgres
```

2. Install dependencies
> Into __server__ dir run following commands
```sh
python3 -m venv .venv
source .venv/bin/activate
.venv/bin/pip install -r r.txt

python manage.py migrate
```

3. Create super user
```sh
python manage.py createsuperuser
```

4. Run dev-server
```sh
python manage.py runserver
```

### Soon to start server run following commands into __server__ dir:
```sh
python3 -m venv .venv
source .venv/bin/activate
python manage.py runserver
```

The dev-server starts on:  [http://localhost:8000](http://localhost:8000)

### Enabled endpoints
- admin/ - admin-panel for manage models & users & auth-tokens
- api/registration/ - user registration
- api/login/ - user auth
- api/answer/ - get answer from model into chatbot

Look up API parametrs see:
- swagger/ - interactive API docs with Swagger-UI
- redoc/ - interactive API docs with ReDoc

# model - PyTorch Model
The Unsver validator for LLM chatbots (Russian lang)

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    |
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions
        │   ├── predict_model.py
        │   └── train_model.py
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
            └── visualize.py