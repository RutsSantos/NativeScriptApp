pipeline {
    agent any

    environment {
        BRANCH_NAME = env.GIT_BRANCH
        DOCKER_IMAGE = 'mi-aplicacion:latest'
        DEPLOY_SERVER = 'usuario@mi-servidor.com' // Reemplazar con el servidor real
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                script {
                    echo "Branch actual: ${BRANCH_NAME}"
                }
            }
        }

        stage('Build & Test') {
            when {
                not {
                    anyOf {
                        branch 'main'
                        branch 'develop'
                    }
                }
            }
            steps {
                echo 'Instalando dependencias y ejecutando pruebas...'
                sh '''
                    npm install
                    npm run build
                    npm test
                '''
            }
        }

        stage('PR Validation') {
            when {
                allOf {
                    branch 'main'
                    triggeredBy 'PullRequest'
                }
            }
            steps {
                echo 'Validando Pull Request para main...'
                sh '''
                    npm run lint
                    npm run test
                '''
            }
        }

        stage('Build Docker Image') {
            when {
                branch 'main'
            }
            steps {
                echo 'Construyendo imagen Docker...'
                sh '''
                    docker build -t $DOCKER_IMAGE .
                    docker tag $DOCKER_IMAGE usuario/$DOCKER_IMAGE
                '''
            }
        }

        stage('Push Docker Image') {
            when {
                branch 'main'
            }
            steps {
                echo 'Enviando imagen a Docker Hub...'
                withCredentials([string(credentialsId: 'docker-hub-cred', variable: 'DOCKER_PASSWORD')]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login -u usuario --password-stdin
          
