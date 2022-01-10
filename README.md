# Name（リポジトリ/プロジェクト/OSSなどの名前）

omh-app

医療現場で使えるアプリ。

# DEMO

# Features

みんなで作り上げる勉強用の資料共有サイト。

# Requirement

* Django>=4.0,<5.0
* gunicorn==20.0.4
* mysqlclient
* Pillow
* Docker version 20.10.11
* Docker Compose version v2.2.1

# Installation

docker pull google/cloud-sdk:latest
docker run -ti --name gcloud-config google/cloud-sdk gcloud auth login
docker run --rm -ti --volumes-from gcloud-config google/cloud-sdk gcloud compute instances list --project myapp-omh

# Usage

```bash
git clone https://github.com/yktt-nuane/omh-app.git
python manage.py makemigrations
python manage.py migrate
docker compose up -d --build
docker compose up
```

# Note

注意点

# Author

作成情報を列挙する

* 作成者
* 所属
* E-mail

# License
ライセンスを明示する
