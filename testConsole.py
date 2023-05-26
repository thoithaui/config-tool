import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor


class ConsoleWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Console Window")

        # Tạo một QTextEdit để hiển thị thông tin từ console
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(
            True
        )  # Đặt chế độ chỉ đọc để ngăn người dùng chỉnh sửa văn bản
        self.text_edit.setStyleSheet(
            "font-family: Courier; font-size: 10pt"
        )  # Đặt kiểu cho văn bản

        # Đặt QTextEdit làm widget chính
        self.setCentralWidget(self.text_edit)

    def write(self, text):
        # Ghi văn bản vào QTextEdit
        cursor = self.text_edit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.text_edit.setTextCursor(cursor)
        self.text_edit.ensureCursorVisible()


# Tạo ứng dụng Qt
app = QApplication(sys.argv)

# Tạo một cửa sổ console
console_window = ConsoleWindow()
console_window.show()

# Ghi đè sys.stdout để chuyển thông tin từ console vào QTextEdit
sys.stdout = console_window
print("1234")
print("1234")
print("1234")
print("1234")
# Chạy chương trình chính của bạn

# Chạy vòng lặp chính của ứng dụng
sys.exit(app.exec_())
