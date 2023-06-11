
# Client-Server Interaction with AES and Password Manager

Database Server with AES Encryption and Client UI

## Description

This project aims to create a database server, establish a local socket-based server-client communication, and provide a user interface for the client to interact with the server and retrieve information from the database. The project incorporates AES encryption to ensure the confidentiality and integrity of sensitive information. A password manager is also included to securely encrypt all data.

## Features

- Database creation: The project allows for the creation of a database to store relevant information securely.

- Server setup: The server is set up on a localhost socket, enabling client-server communication.

- Client User Interface: A user-friendly interface is provided for the client to interact with the server. It enables sending requests to pull specific information from the database.

- AES Encryption: All communication and sensitive data transfers between the client and server are protected using AES encryption, ensuring confidentiality and integrity.

- Password Manager: The project incorporates a password manager to securely store and handle encryption keys, ensuring the security of sensitive information.

## Installation

1. Clone the project repository:

```shell
git clone https://github.com/your-username/project-repo.git
```

2. Install the required dependencies:
```shell
python -m pip install pickle
pip install tk
python -m pip install tk
```

3. Setup and configure the database:
```shell
python sqlCon.py
```
4. Start the server:
```shell
python server.py
```
5.Launch the client user interface:
```shell
python client.py
```

## Usage
Launch the client user interface.

Connect to the server by providing the necessary connection details.

Use the client interface to send requests to the server for pulling information from the database.

All data transfers and communications are securely encrypted using AES encryption, ensuring the confidentiality and integrity of sensitive information.


## Contributors
DiAndEn0

## License
This project is licensed under the MIT License.
