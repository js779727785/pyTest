#!/bin/bash

# 设置参数
local_ip="127.0.0.1" # 修改为实际的本地 IP
master_port=5557     # 主节点端口
web_port=8089        # Web 界面端口
script="locust_test.py" # Locust 脚本文件
worker_count=2       # 启动的工作节点数量
tag=""               # 可选标记参数
env_info=""          # 可选环境信息

# 启动主节点
echo "Starting Locust master..."
nohup locust -f ${script} --logfile=locust_master.log --master --master-bind-host=${local_ip} --master-bind-port=${master_port} --web-host=${local_ip} -P ${web_port} --html=report.html ${tag} ${env_info} &

sleep 0.5
echo "Master node started at http://${local_ip}:${web_port}"

# 启动工作节点
for ((i=1; i<=${worker_count}; i++)); do
    echo "Starting worker $i..."
    nohup locust -f ${script} --logfile=locust_worker_${i}.log --worker --master-host=${local_ip} --master-port=${master_port} ${tag} ${env_info} &
    sleep 0.5
    echo "Worker $i started"
done

echo "All workers started. Access the Locust Web UI at http://${local_ip}:${web_port}"
