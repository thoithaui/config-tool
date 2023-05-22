import socket

def receive_message(receiver_ip, receiver_port):
    # Tạo socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Ràng buộc socket với địa chỉ IP và cổng nhận
    sock.bind((receiver_ip, receiver_port))

    # Chờ nhận thông báo
    data, addr = sock.recvfrom(1024)

    # In thông báo nhận được
    print("Received message:", data.decode())

    # Đóng socket
    sock.close()

# Thông tin máy nhận
receiver_ip = "192.168.0.100"  # Địa chỉ IP của máy nhận
receiver_port = 12345  # Cổng nhận trên máy nhận

# Nhận thông báo
receive_message(receiver_ip, receiver_port)
