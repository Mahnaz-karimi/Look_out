### A Web application with Python, Django, Bootstrap and CI/CD with GitHub actions, which I used pytest to test the scripts. This project has been  automated testing, integratet and deployed for a test environment and a production environment on Heroku cloud platform, used Postgresql as Database tecnology, used Amazon Web Services, AWS, for the files storage.

# Demo

![image](https://user-images.githubusercontent.com/72239384/160517033-2d92de62-7b06-4d83-b79a-59bb513c150e.png)


### How To Set up
```
git clone https://github.com/Mahnaz-karimi/Look_out.git
```
```
cd Look_out
```
```
python3 -m venv venv
```
```
source venv/bin/activate
```
### Installation
```
pip install -r requirements.txt
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```
```
python manage.py runserver
```
#### For adding all installed programs in requirement.txt 
```
pip freeze > requirements.txt
```
### For overwriting existing static files or write static files
```
python3 manage.py collectstatic
```

### For changing or access to the heroku app

```
heroku git:remote -a app-name
```

### For deploying the project to the Heroku websites via different branches

```
git push heroku master
```
```
git push heroku branch-name:master    
```
### For integrating the project to the Heroku 
```
heroku run python manage.py migrate
```
```
heroku run python manage.py collectstatic
```
#### From CLI run the comando to find out if any database resources are deleted
```
heroku releases -a <app-name> 
```

#### For run the test
```
python -m pytest
```


  

  

