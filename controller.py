import config
import user_interface as ui
import json_io

notes_list = []


def run_app(args: list):
    init()
    if len(args) > 1:
        pass
    main_polling()


def init():
    global notes_list
    notes_list = json_io.read_json()


def main_polling():
    print('Для выхода просто нажмите Enter')
    func = True
    while func:
        ui.show_menu_commands(config.main_menu)
        func = ui.select_func_menu(show_notes, add_note, edit_note, del_note)
        if func:
            func()


def sample_by_date(notes_lst):
    sample_date = input('Введите дату в формате "YYYY-MM-DD": ')
    sample_notes = [note for note in notes_lst if note["date"].startswith(sample_date)]
    ui.show_notes(sample_notes)


def show_notes():
    ui.show_menu_commands(('Весь список', 'За определенный день'), False)
    show_func = ui.select_func_menu(ui.show_notes, sample_by_date)
    if show_func:
        show_func(notes_list)


def add_note():
    global notes_list
    new_note = ui.prompt_note()
    notes_list.append(new_note)
    json_io.write_json(notes_list)


def edit_note():
    global notes_list
    ui.show_notes(notes_list)
    note_number = ui.safe_digit_input('Введите номер заметки для редактирования: ', len(notes_list)) - 1
    new_note = ui.prompt_note()
    notes_list[note_number] = new_note
    json_io.write_json(notes_list)


def del_note():
    global notes_list
    ui.show_notes(notes_list)
    note_number = ui.safe_digit_input('Введите номер заметки для удаления: ', len(notes_list)) - 1
    if note_number != -1 and \
            ui.confirm_input(f'Точно хотите удалить заметку "{notes_list[note_number]["title"]}"'):
        print(f'Заметка {notes_list[note_number]["title"]} удалена')
        del notes_list[note_number]
    json_io.write_json(notes_list)
