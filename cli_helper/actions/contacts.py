def get_normolazid_info(user_info: list[str]):
    user = user_info[0] if len(user_info) > 0 else ''
    phone = user_info[1] if len(user_info) > 1 else ''
    normalized_name = user.strip().lower()

    return user, normalized_name, phone

def add_contact(db: dict, user_info: list[str]):
    user, normalized_name, phone = get_normolazid_info(user_info)

    if normalized_name in db:
        return f'Contact "{user}" is already exist'

    db[normalized_name] = {"display_name": user, "phone": phone}
    return f'Contact "{user}" is created'

def change_contact(db: dict, user_info: list[str]):
    user, normalized_name, phone = get_normolazid_info(user_info)

    if normalized_name not in db:
        return f'User "{user}" not exist'

    db[normalized_name]['phone'] = phone
    return f'The "{user}" phone number is updated'

def show_phone(db: dict, user_info: list[str]):
    user, normalized_name, _ = get_normolazid_info(user_info)

    if normalized_name not in db:
        return f'User "{user}" not exist'

    return f'"{user}" phone is: {db[normalized_name]["phone"]}'

def show_all_phones(db: dict):
    if not db:
        return 'You didnt add any contact at list'

    lines = ['Your contacts:']
    for contact in db.values():
        lines.append(f'{contact["display_name"]}: {contact["phone"]}')

    return '\n'.join(lines)
