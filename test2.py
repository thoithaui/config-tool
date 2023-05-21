import time
from elasticsearch import Elasticsearch
import tkinter as tk
from tkinter import messagebox


# Hàm thực thi truy vấn Elasticsearch
def execute_query():
    # Hàm chạy truy vấn
    def run_query():
        query_elasticsearch()

    # Hàm thoát chương trình
    def exit_program():
        if messagebox.askyesno("Exit", "Do you want to exit the program?"):
            root.destroy()

    # Tạo cửa sổ giao diện
    root = tk.Tk()
    root.title("Elasticsearch Query Tool")

    # Label và input cho đường dẫn Elasticsearch
    elasticsearch_label = tk.Label(root, text="Elasticsearch URL:")
    elasticsearch_label.pack()

    elasticsearch_entry = tk.Entry(root, width=50)
    elasticsearch_entry.pack()

    # Label và input cho tên datastream
    datastream_label = tk.Label(root, text="Datastream Name:")
    datastream_label.pack()

    datastream_entry = tk.Entry(root, width=50)
    datastream_entry.pack()

    # Nút Run
    run_button = tk.Button(root, text="Run", command=run_query)
    run_button.pack()

    # Nút Exit
    exit_button = tk.Button(root, text="Exit", command=exit_program)
    exit_button.pack()

    root.mainloop()

    # Lấy giá trị từ các input
    elasticsearch_url = elasticsearch_entry.get()
    datastream_name = datastream_entry.get()

    # Kiểm tra xem đường dẫn Elasticsearch và tên datastream có được cung cấp hay không
    if not elasticsearch_url or not datastream_name:
        messagebox.showerror(
            "Error", "Please provide Elasticsearch URL and Datastream Name"
        )
        return

    # Kết nối tới Elasticsearch
    es = Elasticsearch([elasticsearch_url])

    # Hàm truy vấn Elasticsearch
    def query_elasticsearch():
        # Truy vấn Elasticsearch
        query = {
            "query": {"match_all": {}},
            "sort": [{"@timestamp": {"order": "desc"}}],
            "size": 10,
        }

        # Gửi truy vấn và lấy kết quả
        result = es.search(index=datastream_name, body=query)

        # Lấy danh sách bản ghi
        hits = result["hits"]["hits"]

        # In kết quả
        for hit in hits:
            source = hit["_source"]
            print(source)

        print("------------------------------------")


# Thực thi ứng dụng
if __name__ == "__main__":
    execute_query()
