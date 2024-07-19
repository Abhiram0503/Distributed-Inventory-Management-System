# import pika
# import mysql.connector
# config = {
#  'user': 'root',
#  'password': 'password',
#  'host': '127.0.0.1',
#  'database': 'store',
#  'port': 3006
# }
# # Connect to the MySQL database
# cnx = mysql.connector.connect(**config)
# cursor = cnx.cursor()
# def callback(ch, method, properties, body):
#     print(f" [x] Received '{body.decode()}'")
#     body=body.decode()
#     values_list = body.split(',')
#     item, total, price = values_list
#     total=int(total)
#     price=float(price)
#     cursor.execute("INSERT INTO mystore (item_name, total_available, price) VALUES (%s, %s, %s)", (item, total, price))
#     cnx.commit()
#     print("done")


# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()

# channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# # Declare a queue with a random name
# result = channel.queue_declare('', exclusive=True)
# queue_name = result.method.queue

# # Bind the queue to the exchange with routing keys
# channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key='topic2')

# print(' [*] Waiting for messages. To exit press CTRL+C')

# channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

# channel.start_consuming()









import pika
import mysql.connector
import threading
import time
print("22222222222222222222222222222222")
config = {
    'user': 'root',
    'password': 'password',
    'host': 'mysql',
    'database': 'store',
    'port': 3306
}

# Connect to the MySQL database
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

def callback(ch, method, properties, body):
    print(f" [x] Received '{body.decode()}'")
    body = body.decode()
    values_list = body.split(',')
    item, total, price = values_list
    total = int(total)
    price = float(price)
    try:
        cursor.execute("INSERT INTO mystore (item_name, total_available, price) VALUES (%s, %s, %s)", (item, total, price))
        cnx.commit()
    except:
        print("the operation failed due to existing product")
    print("done")

def send_heartbeat():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
    while True:
        # Send heartbeat message
        channel.basic_publish(exchange='topic_logs', routing_key='topic5', body='Heartbeat_2')
        print("Heartbeat sent")
        # Sleep for 5 seconds before sending the next heartbeat
        time.sleep(5)

# Start the heartbeat thread
heartbeat_thread = threading.Thread(target=send_heartbeat)
heartbeat_thread.start()
print("22222222222222222222222222222222")
# Setup RabbitMQ consumer
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key='topic2')
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
