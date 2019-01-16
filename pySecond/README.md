# python-django-sample/pyFirst
## 環境構築（Windows）
* 新規アプリケーションの作成
```
py manage.py startapp diary
```

* DBのマイグレーション
```
py manage.py makemigrations diary
py manage.py migrate
```

## 管理画面
* 管理ユーザーの作成
```
py manage.py createsuperuser

# Git Bashの場合
winpty py manage.py createsuperuser
```