FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
#1000 workers are comimg then 1000 will divide in 4 parts
#gunicorn aceept the server request and map that request into logical code






