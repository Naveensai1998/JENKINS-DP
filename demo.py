pipeline {
    agent any  // Executes on any available agent
    
    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
                // Insert build steps here (e.g., compiling code, running tests)
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                // Insert test execution steps here
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Insert deployment steps here (e.g., copying artifacts to server)
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline successfully completed!'
            // Additional actions to perform on successful completion
        }
        failure {
            echo 'Pipeline failed!'
            // Actions to take if the pipeline fails
        }
        always {
            echo 'Pipeline completed, performing cleanup...'
            // Cleanup tasks that should always run, regardless of pipeline outcome
        }
    }
}
