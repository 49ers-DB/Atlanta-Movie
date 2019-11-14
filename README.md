# Atlanta-Movie

## Installation of dev environment

Install python 3.6 or higher and conda on your machine

```
conda env create -f atlanta_movie_env.yml 
```

To start the server
```
FLASK_APP=$PWD/app/http/api/endpoints.py python -m flask run --port 4433
```

## Git Help

Add file to be tracked as a change by git
```
git add <file_name>
```

Save changes locally
```
git commit -m "message describing commit"
```

Get changes from Github
```
git pull
```

Push changes to Github
```
git push
```
