# Broccoli 分布式队列

## celery 安装

pip install celery

pip install eventlet



## redis 服务

redis-server.exe

redis://localhost:6379/0



## worker 运行
pip install eventlet

cd D:\GitHub\Broccoli\

celery -A brocTask worker -l INFO  -P eventlet



## Flower 监控
pip install flower

celery flower -A brocTask --address=127.0.0.1 --port=5555

http://127.0.0.1:5555



## 提交
