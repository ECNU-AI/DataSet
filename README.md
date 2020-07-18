# DataSet

## 初始化环境

path: /Users/xxx/PycharmProjects/DataSet

生成虚拟环境
```shell script
python -m venv ./venv
```
激活(mac)
```shell script
source ./venv/bin/activate
```
退出
```shell script
deactivate
```

## 统一依赖管理

生成requirements.txt文件
```shell script
pip freeze > requirements.txt
```
安装requirements.txt依赖
```shell script
pip install -r requirements.txt
```
