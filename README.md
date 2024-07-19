# Distributed-Inventory-management-system

This project is a messaging and inventory management system using Flask, RabbitMQ, MySQL, and Docker. It consists of a web application (`app.py`) that interacts with a messaging system (RabbitMQ) and a MySQL database to manage and update an inventory of items. Additionally, there are several consumers (`consumer1.py`, `consumer2.py`, `consumer3.py`, and `consumer4.py`) that process messages from RabbitMQ queues and update the inventory database.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Web Application**: The Flask-based web application (`app.py`) allows users to interact with the system through a web interface.
- **Messaging System**: Uses RabbitMQ for message handling between the web application and the consumers.
- **Inventory Management**: Consumers process messages from RabbitMQ queues and update the MySQL inventory database accordingly.
- **Heartbeats**: Consumers send heartbeats to monitor their health status.

## Project Structure

- **`app.py`**: The Flask-based web application that handles user input and sends messages to RabbitMQ.
- **`consumer1.py`, `consumer2.py`, `consumer3.py`, `consumer4.py`**: Consumers that listen to different topics in RabbitMQ, process messages, and update the MySQL database.
- **`wait_c1.sh`, `wait_c2.sh`**: Shell scripts for ensuring RabbitMQ and MySQL are running before executing consumer scripts.
- **`docker-compose.yaml`**: Docker Compose file to define and manage the different services (MySQL, RabbitMQ, Flask app, and consumers).
- **`Dockerfile-app`, `Dockerfile-consumer1`, `Dockerfile-consumer2`, `Dockerfile-consumer3`, `Dockerfile-consumer4`**: Dockerfiles for the Flask app and the consumers.
- **`Dockerfile.mysql`**: Dockerfile for setting up the MySQL database with the required schema.

## Setup

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)
- **Docker Images**:
    - **Python 3.8**: Make sure to pull the Python 3.8 Docker image if not already pulled.
    - **RabbitMQ**: Pull the RabbitMQ Docker image if not already pulled.
    - **MySQL**: Pull the MySQL Docker image if not already pulled.
    
    Run the following commands to pull these images if not already done:
    ```bash
    docker pull python:3.8
    docker pull rabbitmq
    docker pull mysql
    ```

### Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Build and start the services using Docker Compose:

    ```bash
    docker-compose up --build
    ```

3. The application will be available at `http://localhost:5000/`.

## Usage

- **Web Application**: Access the web application at `http://localhost:5000/` to interact with the system.
- **Consumers**: The consumers (`consumer1.py`, `consumer2.py`, `consumer3.py`, `consumer4.py`) listen to different topics in RabbitMQ and update the MySQL database accordingly.

## Contributing

Contributions are welcome! Please fork this repository and open a pull request with your changes.

## License

This project is licensed under the [MIT License](LICENSE).
