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
                bat 'python -m pytest'
            }
        }

        stage('Generate HTML Report') {
            steps {
                bat 'python -m pytest --html=reports/report.html --self-contained-html'
            }
        }
    }
}