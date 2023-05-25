import socket
from win10toast import ToastNotifier


def send_notification(ip, message):
    notifier = ToastNotifier()
    notifier.show_toast("Notification", message, duration=10)


def broadcast_notifications(ip_list, message):
    for ip in ip_list:
        try:
            send_notification(ip, message)
        except socket.error:
            print(f"Failed to send notification to {ip}")


# Danh sách các IP cần gửi thông báo
ip_list = ["192.168.0.1", "192.168.0.2", "192.168.0.3"]

# Nội dung thông báo
message = "Hello from the notification tool!"

# Gửi thông báo đến tất cả các máy trong danh sách
broadcast_notifications(ip_list, message)


mongostat

Số lượng kết nối đồng thời: Theo dõi số lượng kết nối đồng thời đến máy chủ MongoDB. Nếu số lượng kết nối này vượt quá giới hạn được cấu hình hoặc khả năng xử lý của máy chủ, đó là một dấu hiệu cho thấy máy chủ bị quá tải.

Thời gian phản hồi: Đo thời gian phản hồi từ máy chủ MongoDB. Nếu thời gian phản hồi ngày càng tăng hoặc vượt quá một ngưỡng xác định, đó có thể là một dấu hiệu cho thấy máy chủ đang bị quá tải và không thể xử lý yêu cầu kịp thời.

Số lượng yêu cầu chờ (queued operations): Kiểm tra số lượng yêu cầu đang chờ xử lý trên máy chủ MongoDB. Nếu số lượng yêu cầu chờ tăng lên và không được xử lý kịp thời, đó là một dấu hiệu cho thấy máy chủ đang bị quá tải.

Các lỗi hoặc thông báo cảnh báo: Kiểm tra các lỗi hoặc thông báo cảnh báo từ máy chủ MongoDB. Nếu có sự gia tăng đáng kể trong số lượng lỗi hoặc thông báo cảnh báo, điều đó có thể cho thấy máy chủ đang gặp vấn đề hoặc quá tải.

MySQL

Nhật ký hoạt động (Error Log): File nhật ký hoạt động của MySQL ghi lại thông tin về các lỗi, cảnh báo và các tình huống xung đột có thể xảy ra trên máy chủ. Đường dẫn mặc định cho file nhật ký hoạt động là error.log. Bạn có thể kiểm tra file nhật ký này để tìm kiếm thông tin về xung đột.

Nhật ký truy vấn (Query Log): MySQL cung cấp khả năng ghi lại các truy vấn vào file nhật ký truy vấn. Bằng cách kiểm tra file nhật ký truy vấn, bạn có thể phân tích các truy vấn và xem xét sự cạnh tranh và xung đột giữa các truy vấn.

Các bảng hệ thống: MySQL cung cấp một số bảng hệ thống như information_schema.INNODB_LOCKS và information_schema.INNODB_LOCK_WAITS để xem thông tin về khóa và xung đột trong hệ thống InnoDB. Bằng cách truy vấn các bảng này, bạn có thể kiểm tra xem có khóa và xung đột nào đang xảy ra trên cơ sở dữ liệu.

Tomcat

Tệp log chính của Tomcat là catalina.out hoặc catalina.log. Bạn có thể tìm thấy các tệp log này trong thư mục logs của cài đặt Tomcat.