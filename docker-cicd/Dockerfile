node{
   stage('SCM Checkout'){
       git credentialsId: 'git-creds', url: 'https://github.com/AmirKourdi/Jenkis-execrise.git'
   }
   stage('Mvn Package'){
     def mvnHome = tool name: 'maven-3', type: 'maven'
     def mvnCMD = "${mvnHome}/bin/mvn"
     sh "${mvnCMD} clean package"
   }
   stage('Build Docker Image'){
     sh 'docker build -t 85575/test_sqreeam:latest .'
   }
   stage('Push Docker Image'){
     withCredentials([string(credentialsId: 'docker-pwd', variable: 'dockerHubPwd')]) {
        sh "docker login -u kammana -p ${dockerHubPwd}"
     }
     sh 'docker push 85575/test_sqreeam:latest'
   }
   stage('Run Container on Dev Server'){
     def dockerRun = 'docker run -p 8080:8080 -d --name my-app 85575/test_sqreeam:latest'
     sshagent(['dev-server']) {
       sh "ssh -o StrictHostKeyChecking=no ec2-user@172.31.18.198 ${dockerRun}"
     }
   }
