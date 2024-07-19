# from flask import Flask, render_template, request
# import pika

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/send_message', methods=['POST'])
# def send_message():
#     topic = request.form['topic']
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()
#     channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
#     message = f'Message for {topic}'
#     channel.basic_publish(exchange='topic_logs', routing_key=topic, body=message)
#     print(f"Sent '{message}' to topic '{topic}'")
#     connection.close()
#     return 'Message sent successfully'

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     text = request.form['text']
#     print("Text entered:", text)  # Print the entered text on the server side
#     return 'Text entered: ' + text

# if __name__ == '__main__':
#     app.run(debug=True)







import time
import pika
from flask import Flask, render_template, request
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/template1')
def template1():
    return render_template('template1.html')

@app.route('/order')
def template2():
    return render_template('order.html')

@app.route('/new_item')
def template3():
    return render_template('new_item.html')

@app.route('/send_message1', methods=['POST'])
def send_message():
    topic = "topic1"
    item_name = request.form['item_name']
    total_available = request.form['total_available']
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
    message=f'{item_name},{total_available}'
    channel.basic_publish(exchange='topic_logs', routing_key=topic, body=message)
    print(f"Sent '{message}' to topic '{topic}'")
    connection.close()
    return render_template('index.html')

@app.route('/send_message2', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        topic = "topic2"
        item_name = request.form['item_name']
        total_available = request.form['total_available']
        price = request.form['price']
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()
        channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
        message=f'{item_name},{total_available},{price}'
        channel.basic_publish(exchange='topic_logs', routing_key=topic, body=message)
        print(f"Sent '{message}' to topic '{topic}'")
        connection.close()
        return f"Item Name: {item_name}, Total Available: {total_available}, Price: {price}"
    

@app.route('/send_message3', methods=['POST'])
def submit_form1():
    if request.method == 'POST':
        topic = "topic3"
        item_name = request.form['item_name']
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()
        channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
        message=f'{item_name}'
        channel.basic_publish(exchange='topic_logs', routing_key=topic, body=message)
        print(f"Sent '{message}' to topic '{topic}'")
        connection.close()
        return f"Item Name: {item_name}"


    



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
    

