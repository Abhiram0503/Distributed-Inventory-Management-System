# import pika
# import threading
# import time

# def callback(ch, method, properties, body):
#     print(f" [x] Received heartbeat: '{body.decode()}'")
#     # Reset the flag on receiving a heartbeat message
#     global received_heartbeat
#     received_heartbeat = True

# def check_heartbeat():
#     global received_heartbeat
#     while True:
#         if not received_heartbeat:
#             print("No heartbeat received!")
#         received_heartbeat = False
#         time.sleep(5)  # Check heartbeat every 5 seconds

# # Global flag to track whether heartbeat is received
# received_heartbeat = False

# # Setup RabbitMQ consumer
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()
# channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
# result = channel.queue_declare('', exclusive=True)
# queue_name = result.method.queue
# channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key='topic5')
# print(' [*] Waiting for heartbeat messages. To exit press CTRL+C')
# channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

# # Start checking for heartbeat
# heartbeat_thread = threading.Thread(target=check_heartbeat)
# heartbeat_thread.start()

# channel.start_consuming()









import pika
import threading
import time
import logging 
logging.basicConfig(level=logging.INFO)
print("44444444444444444444444444444444")
def callback(ch, method, properties, body):
    producer_id = body.decode().split('_')[1]  # Extract producer identifier
    print(f" [x] Received heartbeat from producer {producer_id}")
    logging.info(f" [x] Received heartbeat from producer {producer_id}")
    # Mark the producer as received a heartbeat
    global received_producers
    received_producers.add(producer_id)

def check_heartbeat():
    global received_producers
    while True:
        # Check which producers have not sent a heartbeat
        missing_producers = expected_producers - received_producers
        if missing_producers:
            print(f"No heartbeat received from producers: {', '.join(missing_producers)}")
            logging.info(f"No heartbeat received from producers: {', '.join(missing_producers)}")
        # Reset the set of received producers
        received_producers = set()
        time.sleep(5)  # Check heartbeat every 5 seconds

# Set of expected producers
expected_producers = {'1', '2', '3'}

# Set to track which producers have sent a heartbeat
received_producers = set()

# Setup RabbitMQ consumer
print("44444444444444444444444444444444")
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key='topic5')
print(' [*] Waiting for heartbeat messages. To exit press CTRL+C')
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

# Start checking for heartbeat
heartbeat_thread = threading.Thread(target=check_heartbeat)
heartbeat_thread.start()

channel.start_consuming()
