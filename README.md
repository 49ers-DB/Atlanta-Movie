# Atlanta-Movie

## Installation of dev environment

Install python 3.6 or higher and conda on your machine

```
conda env create -f atlanta_movie_env.yml 
```

To start the server
```
FLASK_APP=$PWD/app/http/api/endpoints.py run python -m flask run --port 4433
```