#!/bin/bash

RABBITMQ_HOST="rabbitmq"
RABBITMQ_PORT=5672

MYSQL_HOST="mysql"
MYSQL_PORT=3306

check_services() {
    # Check RabbitMQ server
    rabbitmq_running=false
    while ! nc -zv "$RABBITMQ_HOST" "$RABBITMQ_PORT"; do
        echo "Waiting for RabbitMQ server to start..."
        sleep 1
    done
    echo "RabbitMQ server is up and running."
    rabbitmq_running=true

    # Check MySQL server
    mysql_running=false
    while ! nc -zv "$MYSQL_HOST" "$MYSQL_PORT"; do
        echo "Waiting for MySQL server to start..."
        sleep 1
    done
    echo "MySQL server is up and running."
    mysql_running=true
}

check_services

# If both RabbitMQ and MySQL are running, then run the Python file
if [ "$rabbitmq_running" = true ] && [ "$mysql_running" = true ]; then
    echo "Both RabbitMQ and MySQL servers are running. Running app.py."
    python3 consumer1.py
    echo "i idk bruhhh from c1"
else
    echo "Cannot run c1.py. RabbitMQ or MySQL server is down."
fi
