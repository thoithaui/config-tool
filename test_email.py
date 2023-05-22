import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(sender_email, sender_password, receiver_email, subject, message):
    # Tạo đối tượng MIMEMultipart để xây dựng email
    email = MIMEMultipart()
    email["From"] = sender_email
    email["To"] = receiver_email
    email["Subject"] = subject

    # Thêm nội dung email
    email.attach(MIMEText(message, "plain"))

    # Thiết lập kết nối SMTP
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)

    # Gửi email
    smtp_server.sendmail(sender_email, receiver_email, email.as_string())
    smtp_server.quit()


# Thông tin tài khoản email
sender_email = "ducthogt127@gmail.com"
sender_password = "edidybyighnbhcqn"

# Thông tin người nhận
receiver_email = "123"

# Nội dung email
subject = "Test Email"
message = "Đây là một email được gửi từ Python."

# Gửi email
send_email(sender_email, sender_password, receiver_email, subject, message)
