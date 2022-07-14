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
<br/>
![image](https://user-images.githubusercontent.com/70641137/178855978-b71c2adf-8620-4ef6-9063-f3a11208a9e6.png)
![image](https://user-images.githubusercontent.com/70641137/178855990-c636d0c1-dab6-4c10-84cb-4a29e54e4bc2.png)<br/>
<br/>Access from the browser: localhost:8000<br/><br/>
![image](https://user-images.githubusercontent.com/70641137/178851406-f06081c8-c18c-4453-abf4-5c8831ad7aa6.png)
![image](https://user-images.githubusercontent.com/70641137/178857493-ed1cab17-5256-4577-a7b3-3778a2977844.png)
![image](https://user-images.githubusercontent.com/70641137/178857539-740087ac-bb82-4945-b4fa-de2299a8e80b.png)
![image](https://user-images.githubusercontent.com/70641137/178857592-eb575332-933b-4bb9-a93b-ce9555f6c818.png)

