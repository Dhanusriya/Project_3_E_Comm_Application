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
                bat '"C:\\Users\\ASUS\\AppData\\Local\\Python\\bin\\python.exe" -m pytest'
            }
        }

        stage('Generate HTML Report') {
            steps {
                bat '"C:\\Users\\ASUS\\AppData\\Local\\Python\\bin\\python.exe" -m pytest --html=reports/report.html --self-contained-html'
            }
        }
    }
}