Build docker container:
    sudo docker build -t flask_app .

Run docker container:
    sudo docker run -p 8080:8080 flask_app

Example endpoint: "http://172.17.0.2:8080/ZUO"
