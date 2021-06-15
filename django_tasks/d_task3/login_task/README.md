# Login_task

### About:
Due to time constraints, I had to use the "ready-to-use Django addon", my apologies for that. 
I used django-allauth library, which I usually use in my projects.

### Installation:
1. Download and install [Python](https://www.python.org/downloads/).
2. Unzip the "login_task.zip" file to the working folder.
3. Open the "login_task" folder in the terminal by following commands:
```
1) $ cd (path to saved login_task folder)
2) $ cd login_task
```
4. Enter `pip install -r requirements.txt` to install/update all necessary libraries.

### Usage:
At the moment application doesn't upload to the server. So You need to start it using the Django command.

1. Open the "Login_task" folder in the terminal by following commands:
```
1) $ cd (path to saved login_task folder)
2) $ cd login_task
```
2. Run server. In the command line type:
```
$ python manage.py runserver
```
3. Further to the received link (`http://127.0.0.1:8000/accounts/login`).
4. Enter Username and Password or choose Google > Your Google Account to become logged in.

If success, You will be redirekted to profile page.
![profile page]()

##### How to logout?
1. Further to admin page `http://127.0.0.1:8000/admin`
2. Login like `admin`, password: `1`
3. Logout
4. Further to `http://127.0.0.1:8000/accounts/login`

