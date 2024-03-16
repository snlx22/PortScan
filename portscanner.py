import socket
import threading
import sys

def scan_port(target_host, target_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, target_port))
        if result == 0:
            print(f"Port {target_port} is open")
    except Exception as e:
        print(f"Error scanning port {target_port}: {e}")
    finally:
        sock.close()

def port_scanner(target_host):
    print(f"Scanning ports on {target_host}")
    for port in range(1, 1025):
        thread = threading.Thread(target=scan_port, args=(target_host, port))
        thread.start()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        target_host = sys.argv[1]
        port_scanner(target_host)
    else:
        print("Usage: python simples_portscanner.py <TargetHost>")
        sys.exit(1)