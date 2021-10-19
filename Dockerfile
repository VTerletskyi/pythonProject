FROM ubuntu:20.04
WORKDIR /pythonProject
RUN apt-get update && apt-get install -y python python3-pip
COPY . .
RUN pip install -r requirements.txt
#ENTRYPOINT ['python 3']
CMD [ "python3", "app.py" ]


#FROM ubuntu:20.04
#RUN apt-get update && apt-get install -y python python3-pip
#RUN pip install flask
#COPY app.py /opt/
#ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080