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
        stage('Hello') {
            steps {
                script{
                    dir("C:\\BMSAgent\\Temp"){
                    latest_basis_package = bat(returnStdout: true, script:'dir /b /a-d | findstr /i /v /r ".*#A.7z" || dir /b /a-d | findstr /i /r ".*#A.7z"').trim().split("\\n")[-1]
                    println(latest_basis_package)
                    }
                }
            }
        }
        stage('Get Agent IP Address') {
            steps {
                script {
                    sh 'python3 new.py'
                }
            }
        }
    }
}
