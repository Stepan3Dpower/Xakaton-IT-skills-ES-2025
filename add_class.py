from PySide6.QtWidgets import QWidget
import faker
from main import *
from gen_add_design import Ui_Form  # Импорт дизайна дополнительного окна
from PySide6.QtCore import Qt

class AddWindow(QWidget):
    def __init__(self, main_window=None):
        super(AddWindow, self).__init__()
        self.main_window = main_window  # Сохраняем ссылку на основное окно
        self.ui = Ui_Form()  # Загружаем дизайн дополнительной формы
        self.ui.setupUi(self)  # Устанавливаем UI на виджет
        self.ui.add_btn.clicked.connect(self.on_add_clicked)  # Подключаем событие добавления записи
        self.ui.generate_btn.clicked.connect(self.generate)

    def error_1(self):
        err_box = QMessageBox()
        err_box.setText("🚨Все поля обязательны к заполнению!🚨")
        err_box.setWindowTitle("Ошибка!")
        err_box.setIcon(QMessageBox.Icon.Critical)
        err_box.exec()

    def namesake(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("Ошибка!")
        msg_box.setText("Найдена полная тёзка!")
        msg_box.setInformativeText("Всё равно записать в базу данных?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        ret = msg_box.exec()
        if ret == QMessageBox.StandardButton.Yes:
            return True
        elif ret == QMessageBox.StandardButton.No:
            return False

    def success(self, text):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("Успех!")
        msg_box.setText(text)
        msg_box.exec()

    def add_to_data_base(self, notifications = True):
        st_fio = self.ui.SFIO.text()
        st_bd = self.ui.SDOB.text()
        st_section = self.ui.SS.text()
        st_address = self.ui.SA.text()
        can_go_byy = "Да" if self.ui.checkBox.isChecked() else "Нет"
        parent_fio = self.ui.PFIO.text()
        parent_phn = self.ui.PPN.text()
        parent_email = self.ui.PEM.text()

        # Добавляем запись в базу данных
        if st_fio and st_bd and st_section and st_address and parent_fio and parent_phn and parent_email:
            if not data_base.find_all_equal_fio(st_fio):
                data_base.add_row(st_fio, st_bd, st_section, st_address, can_go_byy, parent_fio, parent_phn,
                                  parent_email)
                self.main_window.view_db()  # Обновляем список записей в главном окне
                self.ui.SFIO.clear()
                self.ui.SDOB.clear()
                self.ui.SS.clear()
                self.ui.SA.clear()
                self.ui.PFIO.clear()
                self.ui.PPN.clear()
                self.ui.PEM.clear()
                if notifications: self.success(f"Запись на имя {st_fio} успешно добавлена в базу данных!")
            else:
                if self.namesake():
                    data_base.add_row(st_fio, st_bd, st_section, st_address, can_go_byy, parent_fio, parent_phn,
                                      parent_email)
                    if notifications: self.success(f"Запись на имя {st_fio} успешно добавлена в базу данных!")
                    self.main_window.view_db()  # Обновляем список записей в главном окне
                    self.ui.SFIO.clear()
                    self.ui.SDOB.clear()
                    self.ui.SS.clear()
                    self.ui.SA.clear()
                    self.ui.PFIO.clear()
                    self.ui.PPN.clear()
                    self.ui.PEM.clear()
        else:
            self.error_1()

    def on_add_clicked(self):
        self.add_to_data_base()

    def generate(self):

        def massive_add(count):
            for i in range(count):
                fios = faker.generate_full_name()
                self.ui.SFIO.setText(fios[0])
                self.ui.SDOB.setText(faker.generate_birth_date())
                self.ui.SS.setText(faker.section())
                self.ui.SA.setText(faker.generate_address())
                self.ui.PFIO.setText(fios[1])
                self.ui.PPN.setText(faker.generate_phone_number())
                self.ui.PEM.setText(faker.to_email(fios[1]))
                self.ui.checkBox.setChecked(faker.state())
                self.add_to_data_base(notifications=False)

        if QApplication.keyboardModifiers() & Qt.ControlModifier:
            massive_add(20)
        elif QApplication.keyboardModifiers() & Qt.ShiftModifier:
            massive_add(100)
        else:
            fios = faker.generate_full_name()
            self.ui.SFIO.setText(fios[0])
            self.ui.SDOB.setText(faker.generate_birth_date())
            self.ui.SS.setText(faker.section())
            self.ui.SA.setText(faker.generate_address())
            self.ui.PFIO.setText(fios[1])
            self.ui.PPN.setText(faker.generate_phone_number())
            self.ui.PEM.setText(faker.to_email(fios[1]))
            self.ui.checkBox.setChecked(faker.state())