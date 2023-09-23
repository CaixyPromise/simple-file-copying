# tkcopy.py

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from fileutil import copy
from tkinter import messagebox


class FileCopyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Copy Utility")

        # 标签
        tk.Label(self, text = "原始文件").grid(row = 0, column = 0, padx = 10, pady = 10)
        tk.Label(self, text = "目标文件").grid(row = 1, column = 0, padx = 10, pady = 10)

        # 输入
        self.source_entry = tk.Entry(self, width = 40)
        self.source_entry.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.dest_entry = tk.Entry(self, width = 40)
        self.dest_entry.grid(row = 1, column = 1, padx = 10, pady = 10)

        # 进度条
        self.progress = ttk.Progressbar(self, orient = "horizontal", length = 300, mode = "determinate")
        self.progress.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 10)

        # 按钮
        self.open_button = tk.Button(self, text = "Open...", command = self.open_file)
        self.open_button.grid(row = 0, column = 2, padx = 10, pady = 10)

        self.save_button = tk.Button(self, text = "Save...", command = self.save_file)
        self.save_button.grid(row = 1, column = 2, padx = 10, pady = 10)

        self.copy_button = tk.Button(self, text = "Copy", command = self.start_copy, state = tk.NORMAL)
        self.copy_button.grid(row = 2, column = 2, padx = 10, pady = 10)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.source_entry.delete(0, tk.END)
            self.source_entry.insert(0, file_path)

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            self.dest_entry.delete(0, tk.END)
            self.dest_entry.insert(0, file_path)

    def show_progress(self, copied, total):
        self.progress['value'] = (copied / total) * 100
        self.update_idletasks()

    def start_copy(self):
        source = self.source_entry.get()
        dest = self.dest_entry.get()
        self.copy_button.config(state = tk.DISABLED)
        try:
            copy(source, dest, tellprogress = self.show_progress)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        self.copy_button.config(state = tk.NORMAL)
        messagebox.showinfo("Info", "Copy completed!")


if __name__ == "__main__":
    app = FileCopyApp()
    app.mainloop()
