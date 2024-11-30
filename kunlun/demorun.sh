#!/bin/bash

# Variables
script=$1                   # Locust script path (passed as an argument)
local_ip=$2                 # Local IP address for master and workers
master_port=$3              # Port for master to bind to
web_port=$4                 # Web UI port for Locust
worker_count=$5             # Number of worker nodes to spawn
tag=$6                      # Tag (optional for environment specific behavior)
env_info=$7                 # Additional environment info (optional)

# Start the Locust master node
echo "Starting master with script $script"
nohup locust -f "$script" --logfile=locust.log --master --master-bind-host="$local_ip" --master-bind-port="$master_port" --web-host="$local_ip" --web-port="$web_port" --html=index.html $tag $env_info &

# Wait for a brief moment to ensure the master starts before workers
sleep 0.5
echo "Master started"

# Start worker nodes
for ((i=1; i<=worker_count; i++))
do
  echo "Starting worker $i"
  nohup locust -f "$script" --logfile=locust.log --worker --master-host="$local_ip" --master-port="$master_port" $tag $env_info &
  echo "Worker $i started"
  sleep 0.5  # Brief pause between starting workers
done

# Output the URL for accessing the web UI
echo "Access the Locust web UI at: http://$local_ip:$web_port"
