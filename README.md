## 项目设计模式
```Bash
singleton单例
依赖注入
dependency_injector
Provider
Configuration
https://github.com/SchedMD/slurm.git
python setup.py develop
cookiecutter https://github.com/audreyfeldroy/cookiecutter-pypackage.git
```

## 项目架构 Arcitecture

## 组件 Component
### 1. 对象存储 job request uuid 36 submit 异步
### 2. bufferingcloud-dashboard python3 flask 生成表单信息 提交 buffering-parameters.json 
### 3. bufferingcloud-model-manager golang orm beego 
### 4. bufferingcloud-slurm 提交作业 客户端服务
### 5. bufferingcloud-views 前端页面 vue3 or react TypeScript Javascript
### SAML single sign on 
### 然后还有一个                        
## 项目采取了异步的方法保障了sdk调用的稳定性以及可靠性
## 