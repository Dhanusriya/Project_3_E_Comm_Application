pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Generate HTML Report') {
            steps {
                bat 'pytest --html=reports/report.html --self-contained-html'
            }
        }
    }
}