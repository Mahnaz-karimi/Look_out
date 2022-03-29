####  This is a Web application with i.a. Python, Django and Bootstrap, automated testing and CI/CD with GitHub actions, which I used to pytest, integrate and deploy an application for both a test environment and a production environment, connected to Postgresql Database, used Amazon Web Services, AWS, for file storage.

# Demo

![image](https://user-images.githubusercontent.com/72239384/160517033-2d92de62-7b06-4d83-b79a-59bb513c150e.png)

### To run the project

```
python3 manage.py runserver

```


### To change of heroku websites

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

  

  

