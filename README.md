# OMH-SITE

![模式図](https://user-images.githubusercontent.com/61369434/152098775-f1fe7ae4-bbdd-4979-8634-7b6d45fce597.png)
OMH: OgakiMunicipalHospital</br>
OMH-SITE is the site for anesthsiologists and intencivists to study real world medicine.

## DEMO

|![スクリーンショット 2022-01-18 13 44 33](https://user-images.githubusercontent.com/61369434/149872436-7522d921-33fc-4f85-84cc-f8eebb901ae1.png)|![スクリーンショット 2022-01-18 13 47 07](https://user-images.githubusercontent.com/61369434/149872641-befd0c1f-260e-423a-b220-1cd48b44a531.png)|
|:---:|:---:|
|![スクリーンショット 2022-01-18 13 48 14](https://user-images.githubusercontent.com/61369434/149872772-9286dd16-6c47-4635-be33-084c2a28209a.png)|![スクリーンショット 2022-01-18 13 48 14](https://user-images.githubusercontent.com/61369434/149872772-9286dd16-6c47-4635-be33-084c2a28209a.png)|

## Features

* 麻酔の勉強ができる
* 記事の投稿・編集が出来る
* 栄養の投与量を計算出来る
* 薬剤の投与量を計算できる

## Requirement

* Docker version 20.10.11
* Docker Compose version v2.2.1

## Installation

```bash
git clone https://github.com/yktt-nuane/OMH-SITE.git
docker pull google/cloud-sdk:latest
docker run -ti --name gcloud-config google/cloud-sdk gcloud auth login
docker run --rm -ti --volumes-from gcloud-config google/cloud-sdk gcloud compute instances list --project myapp-omh
```

### requirements.txt

```bash
Django>=4.0,<5.0
gunicorn==20.0.4
mysqlclient
Pillow
django-ckeditor
django-import-export
django-environ
```

## Usage

Add `CloudSQL-management.json` and `secrets.yml` to `/` .

## Initialize

```bash
docker compose up -d --build
```

## Develop

### Start

```bash
docker compose run web python manage.py migrate
```

### View

Access to `http://0.0.0.0:8000/` .

## Note

### secrets.yml

```bash
SECRET_KEY=********
DEBUG=********
DB_URL=********
DB_USERNAME=********
DB_USERPASS=********
DB_CONNECTION=********
```

## Author

* yktt-nuane
* shin-sforzando

## License

"OMH-SITE" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
