import pika
import os
import logging
import time

logging.basicConfig()

url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@rabbitmq/%2f')
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)  # Connect to CloudAMQP
channel = connection.channel()  # start a channel

# Declare a fanout exchange
channel.exchange_declare(exchange='pdf_exchange', exchange_type='fanout')

for x in range(1000):
    # Message to send to rabbitmq
    body = 'data ke ' + str(x + 1)

    # Publish message to the fanout exchange
    channel.basic_publish(exchange='pdf_exchange', routing_key='', body=body)

    print("[x] Message sent to exchange = " + body)
    a = x % 100
    if a == 0:
        time.sleep(2)

connection.close()
