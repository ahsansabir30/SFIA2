pipeline {
    agent any
     environment{
        DATABASE_URI=credentials('DATABASE_URI')
        MYSQL_ROOT_PASSWORD=credentials('MYSQL_ROOT_PASSWORD')
        MYSQL_DATABASE=credentials('MYSQL_DATABASE')
        USERNAME=credentials('USERNAME')
        PASSWORD=credentials('PASSWORD')
    }
    stages{
        stage('Setup Jenkins VM'){
            steps{
                sh 'sudo apt install python3 python3-pip python3-venv -y'
            }
        }
        stage('Run Test for API'){
            steps{
                sh 'sudo chmod +x ./test-script.sh'
                sh './test-script.sh'
            }
        }
        stage('Docker Swarm and NGINX Load Balancer'){
            steps{
                sh 'ansible-playbook -i inventory.yaml playbook.yaml -e DATABASE_URI=${DATABASE_URI} -e MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} -e MYSQL_DATABASE=${MYSQL_DATABASE} -e USERNAME=${USERNAME} -e PASSWORD=${PASSWORD}'
            }
        }
    }
}