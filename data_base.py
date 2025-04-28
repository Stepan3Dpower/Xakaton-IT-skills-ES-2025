import sqlite3

connection = sqlite3.connect('data_base.db')

cursor = connection.cursor()

def add_row(st_fio, st_bd, st_section, st_address, can_go_byy, parent_fio, parent_phn, parent_email):
    global cursor
    cursor.execute('INSERT INTO students (student_FIO, student_date_of_birth, student_section, student_address, student_can_go_by_yourself, parent_FIO, parent_phone_number, parent_email, student_FIO_F, student_FIO_I, student_FIO_O) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (st_fio, st_bd, st_section, st_address, can_go_byy, parent_fio, parent_phn, parent_email, st_fio.split(" ")[0],  st_fio.split(" ")[1],  st_fio.split(" ")[2]))
    connection.commit()

    cursor.execute('SELECT * FROM students')
    items = cursor.fetchall()
    return items

def select_all_from_students_fetchall():
    cursor.execute('SELECT * FROM students')
    items = cursor.fetchall()
    return items

def find_all_equal_fio(fio):
    cursor.execute('SELECT * FROM students WHERE student_FIO = ?', (fio,))
    all_fio = cursor.fetchall()
    return all_fio

def delete_raw_by_id(id):
    cursor.execute('DELETE FROM students WHERE student_id = ?', (id,))
    connection.commit()

def delete_all():
    cursor.execute('DELETE FROM students')
    connection.commit()

def search_by_args(list):
    try:
        sql_text = 'SELECT * FROM students WHERE '
        for i in list:
            temp = str(i[0]) + " = ?, "
            sql_text += temp
        sql_text = sql_text[:-2]
        if len(list) == 5: cursor.execute(sql_text, (list[0][1], list[1][1], list[2][1], list[3][1], list[4][1]))
        elif len(list) == 4: cursor.execute(sql_text, (list[0][1], list[1][1], list[2][1], list[3][1]))
        elif len(list) == 3: cursor.execute(sql_text, (list[0][1], list[1][1], list[2][1]))
        elif len(list) == 2: cursor.execute(sql_text, (list[0][1], list[1][1]))
        elif len(list) == 1: cursor.execute(sql_text, (list[0][1],))
        items = cursor.fetchall()
        return items

    except Exception as e:
        print(e)
        return []
