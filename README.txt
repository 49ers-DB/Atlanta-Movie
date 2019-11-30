# Atlanta-Movie

## Installation of dev environment

Install python 3.6 or higher and conda on your machine

```
conda env create -f atlanta_movie_env.yml 
```

To install the client
```
npm install
```

Then Build the client
```
npm run build
```

## Running the server

To start the server
```
FLASK_APP=$PWD/app/http/api/endpoints.py python -m flask run --port 4433
```

Now Navigate to http://localhost:4433




