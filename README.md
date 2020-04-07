## 설치
먼저 Django 크론탭을 한 번 설치해봅시다.  

`pipenv install django_crontab` or `(venv) ~/dev/django/myproject pip install django_crontab`  
환경에 맞게 잘 깔아줍시다.


```python
# myproject/settings.py

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_crontab",
]
``` 
`django_crontab` 을 `INSTALLED_APPS` 에 추가해줍시다. 


```bash
 ~/dev/django/cron_tutorial   master ●  python manage.py crontab show
Currently active jobs in crontab:
```  
`python manage.py crontab show` 를 입력해서 잘 설치되었는지 체크해봅시다.

