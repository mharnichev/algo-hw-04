
from salary_calculator import total_salary 

def main():
    file_path = "text.md"
    
    try:
        total, average = total_salary(file_path)
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")

if __name__ == "__main__":
    main()