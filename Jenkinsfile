pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from Git repository
                git branch: 'testbranch', url: 'https://github.com/yourusername/yourproject.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Install Python dependencies using pip
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Collect Static Files') {
            steps {
                // Collect static files for Django
                sh 'python manage.py collectstatic --no-input'
            }
        }
        
        stage('Database Migration') {
            steps {
                // Apply database migrations
                sh 'python manage.py migrate'
            }
        }
        
        stage('Run Tests') {
            steps {
                // Run tests (optional)
                sh 'python manage.py test'
            }
        }
        
        stage('Deploy') {
            steps {
                // Restart the Django server (assuming it's running via WSGI, adjust as needed)
                sh 'sudo systemctl restart gunicorn'
            }
        }
    }
    
    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}

