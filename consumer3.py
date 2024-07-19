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
# cursor.close()
# # def callback(ch, method, properties, body):
# #     print(f" [x] Received '{body.decode()}'")
# #     body=body.decode()
# #     values_list = body.split(',')
# #     item  = values_list
# #     cursor = cnx.cursor()
# #     cursor.execute(f"select total_available from mystore where item_name='{item}';")
# #     x=cursor.fetchOne()
# #     x=x-1
# #     cursor.execute(f"UPDATE mystore SET total_available = '{x}' WHERE item_name = '{item}';")
# #     cnx.commit()
# #     cursor.close()
# #     print(f"workdone")

# def callback(ch, method, properties, body):
#     print(f" [x] Received '{body.decode()}'")
#     body = body.decode()
#     values_list = body.split(',')
#     item = values_list[0]  # Extracting the item name from the received message
#     cnx = mysql.connector.connect(**config)  # Connect to MySQL database
#     cursor = cnx.cursor()
#     cursor.execute(f"SELECT total_available FROM mystore WHERE item_name='{item}';")
#     result = cursor.fetchone()
#     if result:
#         total_available = result[0]
#         total_available -= 1
#         cursor.execute(f"UPDATE mystore SET total_available = {total_available} WHERE item_name = '{item}';")
#         cnx.commit()
#         print(f"Updated total_available for item '{item}' to {total_available}")
#     else:
#         print(f"Item '{item}' not found in database.")
#     cursor.close()
#     cnx.close()

# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()
# channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
# result = channel.queue_declare('', exclusive=True)
# queue_name = result.method.queue
# channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key='topic3')
# print(' [*] Waiting for messages. To exit press CTRL+C')
# channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
# channel.start_consuming()









import pika
import mysql.connector
import threading
import time
print("33333333333333333333333333")
config = {
    'user': 'root',
    'password': 'password',
    'host': 'mysql',
    'database': 'store',
    'port': 3306
}

def callback(ch, method, properties, body):
    print(f" [x] Received '{body.decode()}'")
    body = body.decode()
    values_list = body.split(',')
    item = values_list[0]  # Extracting the item name from the received message
    cnx = mysql.connector.connect(**config)  # Connect to MySQL database
    cursor = cnx.cursor()
    cursor.execute(f"SELECT total_available FROM mystore WHERE item_name='{item}';")
    result = cursor.fetchone()
    if result:
        total_available = result[0]
        total_available -= 1
        cursor.execute(f"UPDATE mystore SET total_available = {total_available} WHERE item_name = '{item}';")
        cnx.commit()
        print(f"Updated total_available for item '{item}' to {total_available}")
    else:
        print(f"Item '{item}' not found in database.")
    cursor.close()
    cnx.close()

def send_heartbeat():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
    while True:
        # Send heartbeat message
        channel.basic_publish(exchange='topic_logs', routing_key='topic5', body='Heartbeat_3')
        print("Heartbeat sent")
        # Sleep for 5 seconds before sending the next heartbeat
        time.sleep(5)

# Start the heartbeat thread
heartbeat_thread = threading.Thread(target=send_heartbeat)
heartbeat_thread.start()

# Setup RabbitMQ consumer
print("33333333333333333333333333")
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key='topic3')
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
