###  This is a Web application written by i.a. Python, Django and Bootstrap, automated testing and CI/CD with GitHub actions, which I used pytest for test scripts. this project is been integratet and deployed for both a test environment and a production environment on Heroku cloud platform, used Postgresql as Database tecnology, used Amazon Web Services, AWS, for file storage.

# Demo

![image](https://user-images.githubusercontent.com/72239384/160517033-2d92de62-7b06-4d83-b79a-59bb513c150e.png)

### To run the project

```
python3 manage.py runserver
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
### To overwrite existing static files or write static files
```
python3 manage.py collectstatic
```

  

  

