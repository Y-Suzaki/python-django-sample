# python-django-sample/pyFirst
## 環境構築（Windows）
* 新規アプリケーションの作成
```
py manage.py startapp myapp
py manage.py startapp diary
```

* DBのマイグレーション
```
py manage.py makemigrations diary
py manage.py migrate
```