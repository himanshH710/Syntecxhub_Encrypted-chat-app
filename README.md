# 🔐 Encrypted Multi-Client Chat Application

## Overview

This project is a secure multi-client chat application developed using Python. It uses TCP socket programming for communication and Fernet (AES-based symmetric encryption) from the Cryptography library to ensure that messages are transmitted securely between clients.

The server supports multiple clients simultaneously using multithreading and provides secure group communication.

---

# Features

* Secure message encryption using Fernet (AES)
* Multi-client support
* Real-time messaging
* Username-based communication
* Group chat functionality
* Chat history logging
* Thread-based client handling
* Exception handling for network errors

---

# Technologies Used

* Python 3
* Socket Programming
* Threading
* Cryptography (Fernet)
* TCP/IP Networking

---

# Project Structure

```
Encrypted-Chat-App/

│── client.py
│── server.py
│── crypto_utils.py
│── key_generation.py
│── requirements.txt
│── chat_history.txt
│── README.md
```

---

# Installation

Clone the repository

```bash
git clone <repository-link>
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

Start the server

```bash
python server.py
```

Open another terminal and start a client

```bash
python client.py
```

Open multiple terminals to connect multiple clients.

---

# How It Works

1. The server starts and listens for incoming client connections.
2. Each client enters a username and connects to the server.
3. Messages are encrypted using Fernet before transmission.
4. The server receives and decrypts the message.
5. The message is broadcast to all connected clients.
6. Each client decrypts the received message before displaying it.

---

# Concepts Learned

* Socket Programming
* Client-Server Architecture
* TCP Communication
* Symmetric Encryption (AES/Fernet)
* Multithreading
* Network Programming
* File Handling
* Exception Handling

---

# Future Improvements

* Private Messaging
* User Authentication
* GUI using Tkinter or PyQt
* Database Integration
* Secure Key Exchange
* File Sharing
* End-to-End Encryption with Public-Key Cryptography

---

# Author

Himanshu

Information Technology Student | Python Developer | Cybersecurity Enthusiast
