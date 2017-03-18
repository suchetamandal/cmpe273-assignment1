FROM python:2.7.13
MAINTAINER Your Name "sucheta.mandal@sjsu.edu"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
