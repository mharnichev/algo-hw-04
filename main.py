
from salary_calculator import total_salary
from cats_info import get_cats_info

def salary_task():
    file_path = "data/salary_file.md"

    try:
        total, average = total_salary(file_path)
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")

def cats_task():
    file_path = "data/cats_file.md"

    try: 
        cats_info = get_cats_info(file_path)
        print(cats_info)
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")


def main():
    salary_task()
    cats_task()
    
if __name__ == "__main__":
    main()