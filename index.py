#Dependencies
import sys
import socket

#Variables
open_ports = []

#Main
try:
    for port in range(50, 85):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        result = sock.connect_ex(("192.168.0.1", port))
        
        print(f"Checking port {port}")
        
        if result == 0:
            print(f"Port {port} | Open")
            
            open_ports.append(str(port))
        else:
            print(f"Port {port} | Close")
            
        sock.close()
    
    open_ports = ", ".join(open_ports)
    print(f"Open ports: {open_ports}")
    print("Finished.")
except NameError:
    pass