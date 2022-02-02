# Name（リポジトリ/プロジェクト/OSSなどの名前）

omh-app

![模式図](https://user-images.githubusercontent.com/61369434/152098775-f1fe7ae4-bbdd-4979-8634-7b6d45fce597.png)

## DEMO

![スクリーンショット 2022-01-18 13 44 33](https://user-images.githubusercontent.com/61369434/149872436-7522d921-33fc-4f85-84cc-f8eebb901ae1.png)
![スクリーンショット 2022-01-18 13 47 07](https://user-images.githubusercontent.com/61369434/149872641-befd0c1f-260e-423a-b220-1cd48b44a531.png)
![スクリーンショット 2022-01-18 13 48 14](https://user-images.githubusercontent.com/61369434/149872772-9286dd16-6c47-4635-be33-084c2a28209a.png)
![スクリーンショット 2022-01-18 13 48 14](https://user-images.githubusercontent.com/61369434/149872772-9286dd16-6c47-4635-be33-084c2a28209a.png)

## Features

* 麻酔の勉強ができる
* 記事の投稿・編集が出来る
* 栄養の投与量を計算出来る
* 薬剤の投与量を計算できる

## Requirement

* Django>=4.0,<5.0
* gunicorn==20.0.4
* mysqlclient
* Pillow
* Docker version 20.10.11
* Docker Compose version v2.2.1
* django-ckeditor
* django-import-export

```bash
python3.9 -m venv venv
source venv/bin/activate
git clone https://github.com/yktt-nuane/omh-app.git
pip install --upgrade pip
pip install -r requirements.txt
```

## Installation

```bash
docker pull google/cloud-sdk:latest
docker run -ti --name gcloud-config google/cloud-sdk gcloud auth login
docker run --rm -ti --volumes-from gcloud-config google/cloud-sdk gcloud compute instances list --project myapp-omh
```

## Usage

add 'myapp-omh-b44933797972.json' to omh-app/

```bash
python manage.py migrate
docker compose up -d --build
```

## Note

注意点

## Author

作成情報を列挙する

* 作成者
* 所属
* E-mail

## License

ライセンスを明示する
