import datetime
from config import fields


def show_menu_commands(menu_list: tuple, highlight: bool = True):
    line_fill = '-'
    separator = ' | '
    menu = separator.join(f'{str(index + 1).zfill(2)}: {menu_item}' for index, menu_item in enumerate(menu_list))
    if highlight:
        print()
        print(line_fill * len(menu))
    print(menu)
    if highlight:
        print(line_fill * len(menu))
        print()


def safe_digit_input(prompt: str, max: int = False):
    while True:
        answer = input(prompt)
        if answer == '':
            return 0
        if not answer.isdigit():
            print('Введите число', f'от 1 до {max}' if max else '')
        elif max and int(answer) not in range(1, max + 1):
            print(f'Введите число от 1 до {max}')
        else:
            break
    return int(answer)


def confirm_input(text=''):
    answer = input(f'{text} (для подтверждения введите "да"/"yes"/"y")?')
    return answer.lower() in ('да', 'yes', 'y')


def select_func_menu(*funcs):
    choice = safe_digit_input('Выберите номер команды: ', len(funcs))
    if choice == 0:
        return ''
    return funcs[choice - 1]


def show_notes(notes_list: list):
    width = sum([f[1] for f in fields]) + len(fields) * 2  # ширина записи дела
    id_width = len(str(len(notes_list)))  # узнаем какого размера должен быть id контакта для выравнивания
    print('-' * width)
    print(f'{"N".ljust(id_width)}  {"  ".join([f[0].ljust(f[1]) for f in fields])}')
    print('-' * width)
    for id, note in enumerate(notes_list):
        print(str(id + 1).zfill(id_width), end='  ')
        print(note["title"].ljust(fields[0][1]), end='  ')
        print(note["text"].ljust(fields[1][1]), end='  ')
        print(note["date"].ljust(fields[2][1]))
    print('-' * width)

def prompt_note():
    title = input('Введите заголовок заметки: ')
    text = input('Введите тело заметки: ')
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    return {'title': title, 'text': text, 'date': date}