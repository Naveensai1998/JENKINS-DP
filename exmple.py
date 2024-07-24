pipeline {
    agent {
        label 'ITE_BEA2_EB'
    }
    stages {
        stage('Get Agent IP Address') {
            steps {
                script {
                    def agentIP = bat(script: 'powershell.exe -Command "(Test-Connection -ComputerName localhost -Count 1).IPV4Address.IPAddressToString"', returnStdout: true).trim()
                    echo "IP address of agent: ${agentIP}"
                }
            }
        }
    }
}
