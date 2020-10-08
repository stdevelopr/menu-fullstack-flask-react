# pull official base image
FROM python:3.7.1

LABEL Author="Richard M Turra"
LABEL E-mail="stdevelopr@gmail.com"

# set work directory
WORKDIR /usr/src/backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "app"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

# install dependencies
# RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

EXPOSE 5000

CMD flask db migrate && flask db upgrade && flask run --host=0.0.0.0