# Task Requirements
1 - Create a Python Web APP (use either Flask or FastAPI libraries) that: Presents the Current BitCoin Price, Stores the price in a Redis Database, Presents the Average Price for the last 10 minutes.<br/>
2 - Dockerize the applications (Create Dockerfile and docker-compose.yml)<br/>
3 - Create a Jenkinsfile for CI/CD that creates and pushes the generated Web application Docker image to Docker Hub.<br/>
# steps
1 - Write the code in python and upload it to github.<br/>
2 - Add the Dockerfile and docker-compose.yml.<br/>
3 - Install Docker in which the Jenkins server installed on.<br/>
4 - Create credentials with username and password(token) to access dockerhub from jenkins.<br/>
5 - Add the jenkins pipeline, Jenkinsfile. (https://medium.com/codex/how-to-push-a-docker-image-to-docker-hub-using-jenkins-487fb1fcbe25 : a good example of how to push image to dockerhub using jenkins).<br/>
# run the app
1 - git clone https://github.com/Fares-Saffouri/DockerFinalTask.git && cd DockerFinalTask<br/>
2 - docker compose up -d<br/>
3 - to stop the app: docker compose down<br/>
Access from the browser: localhost:8000<br/>
<br/>
![image](https://user-images.githubusercontent.com/70641137/178851406-f06081c8-c18c-4453-abf4-5c8831ad7aa6.png)
![image](https://user-images.githubusercontent.com/70641137/178851442-cda4611d-e6dd-473d-8bbc-88b3894b6e7f.png)
![image](https://user-images.githubusercontent.com/70641137/178851456-5dcd4e7f-0ee0-487e-8bae-0b2f77fcd31b.png)
![image](https://user-images.githubusercontent.com/70641137/178851471-89333179-4acb-4250-9ff3-a846467ed79e.png)

