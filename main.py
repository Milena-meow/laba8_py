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



