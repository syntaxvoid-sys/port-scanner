import socket
target_ip = input("Enter targets ip here:")

for port in range(int((input("enter start of port range: ")), int(input("enter end of port range: "))):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try: 
        s.connect((target_ip, port))
        print(f"Port {port} is open")
    except:
        print(f"Port {port} failed")
