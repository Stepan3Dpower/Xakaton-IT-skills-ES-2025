from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView
from table_design import Ui_MainWindow  # Импорт дизайна главного окна
import add_class
import search_class
import data_base
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.add_main_btn.clicked.connect(self.open_add_window)
        self.ui.del_main_btn.clicked.connect(self.delete)
        self.ui.search_main_btn.clicked.connect(self.open_search_window)
        self.ui.pushButton.clicked.connect(self.view_db)

        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        self.add_window = add_class.AddWindow
        self.search_window = search_class.SearchWindow

        self.list_of_searching_items = []

        self.view_db()

    def open_add_window(self):
        self.add_window = add_class.AddWindow(main_window=self)  # Передаем ссылку на главное окно
        self.add_window.show()

    def open_search_window(self):
        self.search_window = search_class.SearchWindow(main_window=self)  # Передаем ссылку на главное окно
        self.search_window.show()

    @staticmethod
    def y_n_msg(text, title, icon = QMessageBox.Icon.Question):
        msg_box = QMessageBox()
        msg_box.setIcon(icon)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        ret = msg_box.exec()
        if ret == QMessageBox.StandardButton.Yes:
            return True
        elif ret == QMessageBox.StandardButton.No:
            return False

    def delete(self):
        item = self.ui.tableWidget.currentItem()
        if item is not None and item.column() == 0:
            if self.y_n_msg(text=f'Вы уверены, что хотите удалить запись с ID {item.text()}?', title="Удалить запись?"):
                data_base.delete_raw_by_id(item.text())
                self.view_db()
        else:
            if self.list_of_searching_items:
                if self.y_n_msg(text=f'Вы уверены, что хотите удалить все найденные записи?', title="Удалить записи?"):
                    deleted_ids = ""
                    for i in self.list_of_searching_items:
                        data_base.delete_raw_by_id(i[0])
                        deleted_ids += str(i[0]) + ", "
                    self.view_db()
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Icon.Information)
                    msg_box.setWindowTitle("Успех!")
                    msg_box.setText(f"Успешно удалены найденые элементами с ID {deleted_ids}")
                    msg_box.exec()
                    return
            if self.y_n_msg(text=f'Вы уверены, что хотите удалить все записи?', title="Удалить записи?"):
                data_base.delete_all()
                self.view_db()


    def view_db(self, list_of_items = None):
        if list_of_items:
            items = list_of_items
            self.list_of_searching_items = list_of_items
        else:
            items = data_base.select_all_from_students_fetchall()
            self.list_of_searching_items = []
        self.ui.tableWidget.setColumnCount(9)
        self.ui.tableWidget.setRowCount(len(items))
        self.ui.tableWidget.setHorizontalHeaderLabels(['ID', 'ФИО ученика', 'дата рождения ученика', 'посещаемый кружок', 'ФИО родителя', 'телефон родителя', 'E-mail родителя', 'адрес проживания', 'добирается сам'])

        for row in enumerate(items):
            for column in enumerate(row[1]):
                self.ui.tableWidget.setItem(row[0], column[0], QTableWidgetItem(str(column[1])))

        self.ui.tableWidget.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())