###  This is a Web application using i.a. Python, Django, Bootstrap and CI/CD with GitHub actions, which I used pytest to test the scripts. This project has been  automated testing, integratet and deployed for a test environment and a production environment on Heroku cloud platform, used Postgresql as Database tecnology, used Amazon Web Services, AWS, for the files storage.

# Demo

![image](https://user-images.githubusercontent.com/72239384/160517033-2d92de62-7b06-4d83-b79a-59bb513c150e.png)


### How To Setup
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

### To overwrite existing static files or write static files
```
python3 manage.py collectstatic
```

### To change or access to the heroku app

```
heroku git:remote -a app-name
```

### To deploy the project to the heroku websites via different branches

```
git push heroku master
```
```
git push heroku branch-name:master    
```
### To integration the project to the heroku 
```
heroku run python manage.py migrate
```
```
heroku run python manage.py collectstatic
```


  

  

