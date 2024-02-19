
 Project-RS

### Introduction

This is a simple Python project that allows two computers to connect and share files and execute commands on each other's computers. This can be useful for remote troubleshooting, file sharing, and other tasks.

### Prerequisites

To use this project, you will need:

* Two computers with Python 3 installed
* A local area network (LAN) connection between the two computers

### Setup

1. Clone this repository to both computers.
2. On each computer, open a terminal window and navigate to the directory where you cloned the repository.
3. Run the following command to install the required Python modules:

```
pip install -r requirements.txt
```

4. Start the server on one of the computers by running the following command:

```
python Server.py
```

5. Start the client on the other computer by running the following command:

```
python Client.py
```

### Usage

Once the server and client are running, you can connect to the server from the client by entering the following command:

```
connect <server_ip_address>
```

For example:

```
connect 192.168.1.100
```

Once you are connected, you can execute commands on the server by typing them into the client terminal window. For example, to list the files in the current directory on the server, you would type the following command:

```
ls
```

The output of the command will be displayed in the client terminal window.

You can also transfer files between the two computers using the `send` and `receive` commands. To send a file from the client to the server, you would type the following command:

```
send <file_path>
```

For example:

```
send /home/user/file.txt
```

To receive a file from the server to the client, you would type the following command:

```
receive <file_path>
```

For example:

```
receive /home/user/file.txt
```

### Conclusion

This is a simple but powerful tool that can be used for a variety of tasks. It is easy to use and can be set up in just a few minutes.

