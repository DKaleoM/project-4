FROM python:3.8
LABEL maintainer="kaleom@uoregon.edu"
RUN apt-get update -y
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT ["python", "-B"]
CMD ["flask_brevets.py"]
