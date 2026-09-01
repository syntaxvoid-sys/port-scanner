import socket
target_ip = input("Enter targets ip here:")

for port in range(input("enter port number start: "), input("enter port number end: ")):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try: 
        s.connect((target_ip, port))
        print(f"Port {port} is open")
    except:
        print(f"Port {port} failed")
