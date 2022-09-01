pipeline {
    agent any
    enviroment{
        MYSQL_DATABASE=credentials('MYSQL_DATABASE')
        MYSQL_ROOT_PASSWORD=credentials('MYSQL_ROOT_PASSWORD')
        DATABASE_URI=credentials('DATABASE_URI')
    }
    stages{
        stage('SHOW CREDENTIALS'){
            steps{
                echo '${MYSQL_DATABASE}'
            }
        }
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
                sh 'ansible-playbook -i inventory.yaml playbook.yaml'
            }
        }
    }
}