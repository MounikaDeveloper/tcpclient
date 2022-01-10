import socket
PORT=5050
def extract_ip():
    st=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255',1))
        ip=st.getsockname()[0]
    except Exception:
        ip='127.0.0.1'
    finally:
        st.close()
    return ip
HOST=extract_ip()
#HOST =socket.gethostbyname(socket.gethostname())
#HOST='172.18.144.2'
client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
client.connect((HOST,PORT))
#print(c.rev(1024).decode())

