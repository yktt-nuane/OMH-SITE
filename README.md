# OMH-SITE

![模式図](https://user-images.githubusercontent.com/61369434/152098775-f1fe7ae4-bbdd-4979-8634-7b6d45fce597.png)

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

```bash
git clone https://github.com/yktt-nuane/OMH-SITE.git
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Installation

```bash
docker pull google/cloud-sdk:latest
docker run -ti --name gcloud-config google/cloud-sdk gcloud auth login
docker run --rm -ti --volumes-from gcloud-config google/cloud-sdk gcloud compute instances list --project myapp-omh
```

## Usage

add `myapp-omh-b44933797972.json` to `omh-app/`

```bash
docker compose up -d --build
docker compose run web python manage.py migrate
```

## Note

None

## Author

* yktt-nuane
* shin-sforzando

## License

"OMH-SITE" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
