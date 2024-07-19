import pika
import os
import logging

logging.basicConfig()

url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@rabbitmq/%2f')
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)  # Connect to CloudAMQP
channel = connection.channel()  # start a channel .

# Declare a fanout exchange
channel.exchange_declare(exchange='pdf_exchange', exchange_type='fanout')

# Declare a queue with a random name (exclusive=True ensures the queue is deleted when consumer disconnects)
result = channel.queue_declare(queue='c1', exclusive=True)
queue_name = result.method.queue

# Bind the queue to the fanout exchange
channel.queue_bind(exchange='pdf_exchange', queue=queue_name)

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received from (1) %r" % body)

# Set up consumer callback
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

# Start consuming messages
channel.start_consuming()
