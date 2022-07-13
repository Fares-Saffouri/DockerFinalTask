pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub-fares')
	}

	stages {

		stage('Build') {

			steps {
				sh 'docker build -t fares111/docker_final_task:latest .'
			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push fares111/docker_final_task:latest'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}
