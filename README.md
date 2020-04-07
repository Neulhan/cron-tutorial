## 설치
먼저 Django 크론탭을 한 번 설치해봅시다.  

`pipenv install django_crontab` or `(venv) ~/dev/django/myproject pip install django_crontab`  


```python
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
add `django_crontab` on INSTALLED_APPS 


```bash
 ~/dev/django/cron_tutorial   master ●  python manage.py crontab show
Currently active jobs in crontab:
```  

