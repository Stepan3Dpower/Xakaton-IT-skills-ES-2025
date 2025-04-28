from main import *

from PySide6.QtWidgets import QWidget

from search_design import Ui_Form  # Импорт дизайна дополнительного окна

import data_base

class SearchWindow(QWidget):
    def __init__(self, main_window=None):
        super(SearchWindow, self).__init__()
        self.main_window = main_window  # Сохраняем ссылку на основное окно
        self.ui = Ui_Form()  # Загружаем дизайн дополнительной формы
        self.ui.setupUi(self)  # Устанавливаем UI на виджет
        self.ui.Search_btn.clicked.connect(self.search_click)

    def search_click(self):
        search_args_list = []

        if self.ui.FN_CHB.isChecked():  search_args_list.append(('student_FIO_F', self.ui.FN_INP.text()))
        if self.ui.LN_CHB.isChecked(): search_args_list.append(('student_FIO_I', self.ui.LN_INP.text()))
        if self.ui.F_CHB.isChecked(): search_args_list.append(('student_FIO_O', self.ui.F_INP.text()))
        if self.ui.SEC_CHB.isChecked(): search_args_list.append(('student_section', self.ui.SEC_INP.text()))
        if self.ui.PN_CHB.isChecked(): search_args_list.append(('parent_phone_number', self.ui.PN_INP.text()))

        def check_inputs(searching_arguments_list):
            for tpl in searching_arguments_list:
                if not tpl[1]:
                    error_message_box = QMessageBox()
                    error_message_box.setText(f"🚨 Все выбранные поля должны быть заполнены! 🚨")
                    error_message_box.setWindowTitle("Ошибка!")
                    error_message_box.setIcon(QMessageBox.Icon.Critical)
                    error_message_box.exec()
                    return False
            return True

        if check_inputs(search_args_list):
            result = data_base.search_by_args(search_args_list)
            if result:
               self.main_window.view_db(result)
            else:
                err_box = QMessageBox()
                requst_text = ""
                for i in search_args_list: requst_text += str(i[1]) + " "
                err_box.setText(f"Ничего не найдено по запросу {requst_text}")
                err_box.setWindowTitle("Не найдено!")
                err_box.setIcon(QMessageBox.Icon.Information)
                err_box.exec()