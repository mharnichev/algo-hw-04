# Вимоги до завдання:

# Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
# Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
# Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.

#  ========================================================================================================

from pathlib import Path

default_result = (0, 0)

def load_data(filename):
    with open(filename, "r") as file:
        return file.readlines()


def get_total_sum(list: list[int]) -> int:
    return sum(list)

def get_average(total: int, length: int) -> int:
    return round(total / length)

def total_salary(path: str) -> tuple[int, int]:
    file_path = Path(path)

    if not file_path.exists():
        print(f'{path} does not exist')
        return default_result

    raw_data = load_data(path)
    salary_list = []

    for employee in raw_data:
        employee_data = employee.split(',')
        if employee_data[1].strip() and employee_data[1].strip().isdigit():
            salary_list.append(int(employee_data[1].strip()))
        

    if not salary_list:
        print('No valid salary data found')
        return default_result

    total_sum = get_total_sum(salary_list)
    average = get_average(total_sum, len(salary_list))

    return (total_sum, average)
    


