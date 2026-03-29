# Вимоги до завдання:

# Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
# Функція має повертати список словників, де кожен словник містить інформацію про одного кота.

# ========================================================================================================

from pathlib import Path
from shared.helpers import load_data

default_result = []

def get_cats_info(path: str):
    file_path = Path(path)

    if not file_path.exists():
        return default_result.copy()

    try:
        raw_data = load_data(path)
    except OSError:
        return default_result.copy()

    info_list = []

    for cat in raw_data:
        cat_data = cat.split(',')

        if len(cat_data) < 3:
            continue

        info_list.append({
            "id": cat_data[0].strip(),
            "name": cat_data[1].strip(),
            "age": cat_data[2].strip()
        })

    return info_list

        
        
