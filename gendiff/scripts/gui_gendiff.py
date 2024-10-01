#!/usr/bin/env python3.10
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as mb
from tkinter import filedialog as fd

from gendiff.formatters.output_formatter import FORMATTERS
from gendiff import generate_diff


class DiffApp:
    def __init__(self, root, width=750, height=700):
        self.root = root
        self.root.title('MyDiff')
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(True, True)

        self.file1 = None
        self.file2 = None

        self.create_widgets()

    def create_widgets(self):
        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(pady=10)

        self.middle_frame = tk.Frame(self.root)
        self.middle_frame.pack(pady=10)

        self.bottom_frame = tk.Frame(self.root)
        self.bottom_frame.pack(pady=10, fill='both', expand=True)

        self.instruction_label = tk.Label(
            self.top_frame,
            text="Выберите два файла формата .json или .yaml для сравнения.")

        self.instruction_label.pack()

        self.button1 = tk.Button(self.middle_frame,
                                 text="Открыть первый файл",
                                 command=self.load_file1)
        self.button1.grid(row=0, column=0, padx=10)

        self.button2 = tk.Button(self.middle_frame,
                                 text="Открыть второй файл",
                                 command=self.load_file2)
        self.button2.grid(row=0, column=1, padx=10)

        self.file1_label = tk.Label(self.middle_frame,
                                    text="Файл 1: Не выбран",
                                    anchor='w')
        self.file1_label.grid(row=1, column=0, pady=10)

        self.file2_label = tk.Label(self.middle_frame,
                                    text="Файл 2: Не выбран",
                                    anchor='w')
        self.file2_label.grid(row=1, column=1, pady=10)

        self.result_text = ScrolledText(self.bottom_frame, height=20,
                                        width=85, wrap='word')
        self.result_text.pack(pady=10, fill='both', expand=True)

        self.quit_button = tk.Button(self.root,
                                     text="Выход",
                                     command=self.exit_app)
        self.quit_button.pack(side='bottom', pady=10)


        self.button_to_json = tk.Button(
            self.bottom_frame, text='Показать в json формате',
            command=lambda: self.update_diff('json')
        )
        self.button_to_plain = tk.Button(
            self.bottom_frame, text='Показать в plain формате',
            command=lambda: self.update_diff('plain')
        )
        self.button_to_stylish = tk.Button(
            self.bottom_frame, text='Показать в stylish формате',
            font=('Arial', 11),
            command=lambda: self.update_diff('stylish')
        )

        self.button_to_json.pack_forget()
        self.button_to_plain.pack_forget()
        self.button_to_stylish.pack_forget()
    def load_file1(self):
        file_path = self.open_file_dialog("Выберите первый файл")
        if file_path:
            self.file1 = file_path
            self.update_status(self.file1_label, "Файл 1: Загружен")
            self.update_diff()

    def load_file2(self):
        file_path = self.open_file_dialog("Выберите второй файл")
        if file_path:
            self.file2 = file_path
            self.update_status(self.file2_label, "Файл 2: Загружен")
            self.update_diff()

    def open_file_dialog(self, title):
        file_path = fd.askopenfilename(
            title=title,
            filetypes=[("JSON and YAML files", "*.json *.yaml *.yml")]
        )
        if not file_path:
            mb.showwarning("Ошибка", "Вы не выбрали файл.")
        return file_path

    def update_status(self, label, text):
        label.config(text=text)

    def update_diff(self, formats='stylish'):
        if self.file1 and self.file2:
            try:
                self.show_format_buttons()
                result_diff = generate_diff(self.file1, self.file2, formatters=formats)
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, result_diff)
            except Exception as e:
                mb.showerror("Ошибка", f"Не удалось сравнить файлы: {str(e)}")

    def show_format_buttons(self):
        self.button_to_json.pack(side='left', padx=5)
        self.button_to_plain.pack(side='left', padx=5)
        self.button_to_stylish.pack(side='left', padx=5)

    def exit_app(self):
        if mb.askyesno("Выход", "Вы точно хотите выйти?"):
            self.root.destroy()

    def run(self):
        self.root.mainloop()


def main():
    root = tk.Tk()
    app = DiffApp(root)
    app.run()


if __name__ == "__main__":
    main()
