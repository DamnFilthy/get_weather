# Import of libraries
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from file2 import Ui_Dialog
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# Create app
app = QtWidgets.QApplication(sys.argv)

# Init
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

# Hook Logic
def get_weather_city():
    owm = OWM('token')
    mgr = owm.weather_manager()
    city = ui.lineEdit.text()
    observation = mgr.weather_at_place(city)

    w = observation.weather

    w.detailed_status                        # 'clouds'
    w.wind()                                 # {'speed': 4.6, 'deg': 330}
    w.humidity                               # 87
    all_temp = w.temperature('celsius')      # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    w.rain                                   # {}
    w.heat_index                             # None
    clouds = w.clouds                        # 75

    # Output
    s_temp = w.temperature('celsius')['temp']
    wind = w.wind()['speed']
    humidity = w.humidity
    rain = w.rain
    ui.label.setText(f'Температура воздуха: {s_temp}')
    ui.label_2.setText(f'Облачность: {clouds}')
    ui.label_3.setText(f'Скорость ветра: {wind} м\с')
    ui.label_4.setText(f'Влажность: {humidity}')
    ui.label_5.setText(f'Дождь: {rain}')

# Clicked
ui.pushButton.clicked.connect(get_weather_city)

# Main loop
sys.exit(app.exec_())
