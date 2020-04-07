## 설치
먼저 Django 크론탭을 한 번 설치해봅시다.  

`pipenv install django_crontab` or `(venv) ~/dev/django/myproject pip install django_crontab`  
환경에 맞게 잘 깔아줍시다.

`django_crontab` 을 `INSTALLED_APPS` 에 추가해줍시다. 

```python
# settings.py

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

`python manage.py crontab show` 를 입력해서 잘 설치되었는지 체크해봅시다.

```bash
 ~/dev/django/cron_tutorial   master ●  python manage.py crontab show
Currently active jobs in crontab:
```  

## 사용하기
django crontab은 settings.py 에 등록된 task를 주기적으로 실행해줍니다.

CRONJOBS에 task 를 등록해서 사용해봅시다.

```python
# settings.py
CRONJOBS = [
    ("* * * * *", "utils.a.function_a", ">> log.txt")
]
```
settings.CRONJOBS 는 리스트이고 해당 리스트에 들어있는 task들은 `python manage.py crontab add` 명령어를 통해 크론으로 등록시킬 수 있습니다.
(첫 번째 인자, 두 번째 인자, 세 번째 인자)
- 첫 번째 인자는 해당 task 를 실행할 주기를 등록하는 자리입니다. 예를 들어 "* * * * *" 은 매 분마다 라는 뜻입니다.
- 두 번째 인자는 task 자체를 말합니다. 베이스 디렉토리에서 시작하며, 특정 모듈을 "."을 이용해서 지정해줍니다.
- 세 번째 인자는 해당 task 를 실행할 때 뒤에 붙이고 싶은 명령어입니다. cron 자체가 윈도우에서는 동작하지 않기 때문에 대부분 unix 기반의 터미널 명령어를 추가해 줍니다. 여기서는 cronjob 에 오류가 났을 때 디버깅 하기 쉽도록 로그를 찍는 코드를 적어놓았습니다.



ref
(https://pypi.org/project/django-crontab/)[https://pypi.org/project/django-crontab/]

