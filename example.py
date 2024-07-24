pipeline {
    agent {
        label 'ITE_BEA2_EB'
    }
    stages {
        stage('Get Agent IP Address') {
            steps {
                script {
                    bat """ipconfig | findstr /C:"IPv4" """
                }
            }
        }
    }
}
