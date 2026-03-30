from actions.contacts import add_contact, show_phone, show_all_phones, change_contact

def init_cli_bot():
    print('Hello sir! How can i help you?')
    db = {}

    while True:
        user_input = input('write something: ')
        if not user_input.strip(): continue
        user_command, user_command_args = parse_input(user_input)

        if user_command == 'hello':
            print("How can I help you?")
        elif user_command == 'add':
            if len(user_command_args) < 2:
                print('You forgot write Name or Number')
            else:
                print(add_contact(db, user_command_args))
        elif user_command == 'phone':
            if len(user_command_args) < 1:
                print('You forgot write Name')
            else:
                print(show_phone(db, user_command_args))
        elif user_command == 'all':
            print(show_all_phones(db))
        elif user_command == 'change':
            if len(user_command_args) < 2:
                print('You forgot write Name or New Number')
            else:
                print(change_contact(db, user_command_args))
        elif user_command in ['exit', 'close']:
            print('Good bye!')
            break
        else:
            print("Invalid command.")
            

def parse_input(user_input: str):
    command, *args = user_input.split()
    return command.lower(), args

def main():
    init_cli_bot()

if __name__ == "__main__":
    main()
