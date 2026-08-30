import socket
target_ip = input("Enter targets ip here:")

for port in range(80, 444): #change the port range here i dont know how to do it in a input yet. Remember at the end 444 is 443 and for example 334 is 333
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try: 
        s.connect((target_ip, port))
        print(f"Port {port} is open")
    except:
        print(f"Port {port} failed")
