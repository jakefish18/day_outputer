import sys
import calendar
import datetime

from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QLineEdit, QMessageBox, QPushButton

class DateWriter():
    """Класс для управления с текстовым файлом."""
    def __init__(self, year_num: int, week_day_num: int):
        self.year_num = year_num
        self.week_day_num = week_day_num
        self.week_day_text = self._get_week_name(self.week_day_num)

    def create_txt(self):
        """Создание файла со всеми датами заданного дня недели."""
        with open(f"{self.week_day_text}_{self.year_num}_года.txt", "w") as file:
            #Проход по всем дням и проверка даты на подходящий день недели.
            for month in range(1, 12 + 1):
                for day in range(1, calendar.monthrange(self.year_num, month)[1] + 1):
                    #Проверка.
                    if self._is_week_day(self.year_num, month, day):
                        file.write(f"{day}.{month}.{self.year_num}\n")                  

    def _get_week_name(self, week_day_num: int) -> str:
        """Возвращает текст дня недели, принимая его порядковый номер."""
        week_day_names = {
            1: "Понедельники",
            2: "Вторники",
            3: "Среды",
            4: "Четверги",
            5: "Пятницы",
            6: "Субботы",
            7: "Воскресеньи"
        }

        return week_day_names[week_day_num]

    def _is_week_day(self, year:int, month: int, day: int) -> bool:
        """Проверка является ли день нужным нам днем недели."""
        date = datetime.datetime(year, month, day)
        
        if date.weekday() == self.week_day_num - 1:
            return True
        
        else:
            return False


class Gui(QDialog):
    """Класс окна в котором можно задать день и все даты загрузяться в файл."""
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Учет дат")
        self.setFixedSize(600, 600)

        self.ui_init()

        self.show()

    def ui_init(self):
        """Инициализация интерфейса."""
        #Подсказка для дня недели.
        self.lbl_week_promt = QLabel(self)
        self.lbl_week_promt.setText("Введите цифру для получения дат всех дней недели под этой цифрой.\n1 - Понедельник\n2 - Вторник\n3 - Среда\n4 - Четверг\n5 - Пятница\n6 - Суббота\n7 - Воскресенье")
        self.lbl_week_promt.move(10, 10)

        #Поле для ввода цифры.
        self.led_week_day_num = QLineEdit(self)
        self.led_week_day_num.setPlaceholderText('День недели...')
        self.led_week_day_num.move(10, 150)

        #Подсказка для ввода года.
        self.lbl_year_promp = QLabel(self)
        self.lbl_year_promp.setText("Введите год для которого вы хотите получить даты:")
        self.lbl_year_promp.move(10, 180)

        #Поле для ввода года.
        self.led_year_num = QLineEdit(self)
        self.led_year_num.setPlaceholderText('Год...')
        self.led_year_num.move(10, 200)


        #Кнопка для создания тестового файла с датами.
        self.btn_write_dates = QPushButton('Получить данные', self)
        self.btn_write_dates.clicked.connect(self.create_txt)   
        self.btn_write_dates.move(10, 230)     

    def create_txt(self):
        """Передача данных в DateWriter."""
        year_num = int(self.led_year_num.text())
        week_day_num = int(self.led_week_day_num.text())

        if week_day_num >= 1 and week_day_num <= 7:
            date_writer = DateWriter(year_num, week_day_num)
            date_writer.create_txt()            
            message = QMessageBox.information(self, "Успешно!", "Файл успшно записан!")

        else:
            message = QMessageBox.warning(self, "Ошибка!", "Неправильный день недели!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Gui()
    sys.exit(app.exec())