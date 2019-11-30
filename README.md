# Atlanta-Movie

## Installation of dev environment

Install python 3.6 or higher and [miniconda](https://docs.conda.io/en/latest/miniconda.html) on your machine and then navigate to the main folder with package.json in it.

Then create the environment with

```
conda env create -f atlanta_movie_env.yml 
```

Enable the environment with

```
conda activate atlanta_movie
```

To install node packages needed to build the frontend React code.
```
npm install
```

Then build the client using our npm build script.
```
npm run build
```

## Database Config

The database is configured to be used by user `flask` and password `1234`. If you need to change it, please navigate to app/services/DBService.py and change the user and password to whatever is necessary.

## Running the server

Navigate in a terminal to the main folder with package.json in it and run this command.
```
FLASK_APP=$PWD/app/http/api/endpoints.py python -m flask run --port 4433
```

Now open a browser to http://localhost:4433




