import socket

def send_message(message, receiver_ip, receiver_port):
    # Tạo socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Gửi thông báo đến địa chỉ IP và cổng nhận
    sock.sendto(message.encode(), (receiver_ip, receiver_port))

    # Đóng socket
    sock.close()

# Thông tin máy nhận
receiver_ip = "192.168.0.100"  # Địa chỉ IP của máy nhận
receiver_port = 12345  # Cổng nhận trên máy nhận

# Nội dung thông báo
message = "Hello, this is a notification from the sender."

# Gửi thông báo
send_message(message, receiver_ip, receiver_port)
