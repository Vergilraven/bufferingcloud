pipeline {
//     agent {
//         kubernetes {
//             yaml """
// apiVersion: v1
// kind: Pod
// metadata:
//   namespace: agents-pool
//   labels:
//     app: jenkins-manager
// spec:
//   containers:
//   - name: jenkins-manager
//     image: 'registry.cn-shenzhen.aliyuncs.com/vergil-private/python:3.9.19-slim-bullseye' 
//     command:
//       - sleep
//       - "360"
//     env:
//     - name: AMC_PLATFORM
//       value: "automation-platform"
//     resources:
//       limits:
//         cpu: 1Gi
//         memory: 512m
//       requests:
//         cpu: 256m
//         memory: 256m
//     tty: true
// """
//         }
//     }

    stages {
        stage('Repository Clone') {
            steps {
                container('jenkins-manager') {
                    script {
                        def repositoryURL = 'git@codeup.aliyun.com:624281366d47d593cb37fe84/infrastructure/cloud-sdk.git'
                        def gitCommand = "git ls-remote ${repositoryURL}"
                        def result = sh(script: gitCommand, returnStatus: true)

                        if (result == 0) {
                            echo "收到触发条件,更新云上基础设施开发者套件代码"
                        } else {
                            error "仓库不存在或无法访问,开始执行python3脚本为您重新配置登录的权限配置"
                            echo '******************************开始克隆仓库代码******************************'
                            sh "git clone ${repositoryURL}"
                        }
                    }
                }
            }
        }
        stage('Starter Execute') {
            steps {
                container('jenkins-manager') {
                    script {
                        def listDirectory = 'ls -al | grep sdk | wc -l'
                        def codeResult = sh(script: listDirectory, returnStdout: true).trim()

                        if (codeResult.toInteger() <= 0) {
                            echo "判空失败,开始为您执行bastion启动脚本"
                            def checkPythonExecutor = "python3 -V"
                            def installDependcy = "pip3 install -r requirements.txt" 
                            def startBastionScript = "python3 runner.py"
                            echo sh(script: checkPythonExecutor, returnStdout: true)
                            sh(script: installDependcy)
                            sh(script: startBastionScript)
                        } else {
                            error "代码目录检查失败或已存在，进行下一步操作或处理逻辑"
                        }
                    }
                }
            }
        }
    }
}