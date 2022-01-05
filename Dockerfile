FROM python:3.9-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN python -m pip install Pillow
RUN pip install -r requirements.txt
COPY . /code/

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
