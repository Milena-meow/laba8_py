import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import random

def generate_file():
    """Создает новый текстовый файл с заданным количеством случайных чисел."""
    try:
        count = int(number_entry.get())
        if count <= 0:
            raise ValueError("Количество чисел должно быть больше нуля.")
        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filepath:
            with open(filepath, "w") as file:
                for _ in range(count):
                    file.write(str(random.randint(1, 100)) + "\n")
            messagebox.showinfo("Успех", f"Файл '{filepath}' создан с {count} случайных чисел.")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))


def read_and_calculate(filepath):
    """Читает текстовый файл с числами, вычисляет среднее и выводит результат."""
    try:
        with open(filepath, "r") as file:
            numbers = [int(line.strip()) for line in file if line.strip().isdigit()]
            if not numbers:
                raise ValueError("Файл пуст или содержит нечисловые данные.")
            avg = sum(numbers) / len(numbers)
            result_text = f"Содержимое файла:\n{numbers}\n\nСреднее значение: {avg:.2f}"
            result_label.config(text=result_text, wraplength=300) #wraplength for better text wrap

    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл не найден.")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла непредвиденная ошибка: {e}")


def calculate_all():
    """Выполняет все математические операции и выводит результаты."""
    try:
        num1 = float(a_value.get())
        num2 = float(b_value.get())

        results = {
            "Сложение": num1 + num2,
            "Вычитание": num1 - num2,
            "Умножение": num1 * num2,
            "Деление": num1 / num2 if num2 != 0 else "Ошибка: деление на ноль",
            "Возведение в степень": num1 ** num2,
        }

        result_text = ""
        for operation, result in results.items():
            result_text += f"{operation}: {result}\n"

        result_label.config(text=result_text, wraplength=300) #wraplength for better text wrap

    except ValueError as e:
        messagebox.showerror("Ошибка", f"Некорректный ввод: {e}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла непредвиденная ошибка: {e}")


def read_file():
    """Открывает диалоговое окно для выбора файла и вычисляет среднее значение."""
    filepath = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filepath:
        read_and_calculate(filepath)



root = tk.Tk()
root.title("Обработка данных")
root.geometry("400x900")
root.configure(bg="#f2f2f2")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", padding=10, font=("Arial", 12), background="#4CAF50", foreground="white")
style.map("TButton", background=[("active", "#45a049")])
style.configure("TLabel", font=("Arial", 12), padding=5)
style.configure("TEntry", font=("Arial", 12), padding=5, borderwidth=2, relief="solid")
style.configure("TLabelframe", background="#f2f2f2", foreground="#333333")

result_frame = ttk.LabelFrame(root, text="Результат", padding=10, style="TLabelframe")
result_label = ttk.Label(result_frame, text="", wraplength=350, justify="left", font=("Arial", 10), anchor="nw")
result_label.pack(pady=10)
result_frame.grid(row=4, column=0, columnspan=2, sticky="nsew", pady=10, padx=10)

file_frame = ttk.LabelFrame(root, text="Генерация файла", padding=10, style="TLabelframe")
number_label = ttk.Label(file_frame, text="Кол-во случайных чисел:", style="TLabel")
number_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
number_entry = ttk.Entry(file_frame, width=15, style="TEntry")
number_entry.grid(row=0, column=1, padx=5, pady=5, sticky="e")
generate_button = ttk.Button(file_frame, text="Создать файл", command=generate_file, style="TButton")
generate_button.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")
file_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=10, padx=10)

open_file_frame = ttk.LabelFrame(root, text="Открытие файла", padding=10, style="TLabelframe")
read_button = ttk.Button(open_file_frame, text="Открыть файл", command=read_file, style="TButton")
read_button.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")
open_file_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=10, padx=10)

calc_frame = ttk.LabelFrame(root, text="Арифметические операции", padding=10, style="TLabelframe")
number_value = ttk.Label(calc_frame, text="Введите два числа:", style="TLabel")
number_value.grid(row=0, column=0, columnspan=2, pady=(5,10), sticky="w")

a_value = ttk.Entry(calc_frame, width=15, style="TEntry")
a_value.grid(row=1, column=0, padx=5, pady=5, sticky="e")
b_value = ttk.Entry(calc_frame, width=15, style="TEntry")
b_value.grid(row=1, column=1, padx=5, pady=5, sticky="e")

calculate_all_button = ttk.Button(calc_frame, text="Выполнить все операции", command=calculate_all, style="TButton")
calculate_all_button.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")
calc_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=10, padx=10)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.mainloop()