from PyQt6 import uic, QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtGui import QPixmap, QShortcut, QKeySequence, QIcon, QKeyEvent
from PyQt6.QtCore import QTimer, Qt

import time
import threading

# ----------------------------------------------------------------------------------------------------------------------

Form, Window = uic.loadUiType("ui.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
errorWindow = QMessageBox()

# ----------------------------------------------------------------------------------------------------------------------

def conditional():
    i = 5
    slider_1 = QPixmap("img/deepforest.jpg")
    slider_2 = QPixmap("img/forest.jpg")
    slider_3 = QPixmap("img/lake.jpg")
    slider_4 = QPixmap("img/mountain.jpg")
    slider_5 = QPixmap("img/winter.jpg")
    if i == 1:
        form.slider.setPixmap(slider_1)
    elif i == 2:
        form.slider.setPixmap(slider_2)
    elif i == 3:
        form.slider.setPixmap(slider_3)
    elif i == 4:
        form.slider.setPixmap(slider_4)
    elif i == 5:
        form.slider.setPixmap(slider_5)

# ----------------------------------------------------------------------------------------------------------------------

current_image_index = 0
slider_images = [
    QPixmap("img/deepforest.jpg"),
    QPixmap("img/forest.jpg"),
    QPixmap("img/lake.jpg"),
    QPixmap("img/mountain.jpg"),
    QPixmap("img/winter.jpg")
]

def clicking():
    global current_image_index
    form.slider.setPixmap(slider_images[current_image_index])

def keyPressEvent(event):
    global current_image_index
    if event.key() == Qt.Key.Key_Left:
        current_image_index = (current_image_index - 1) % len(slider_images)
    elif event.key() == Qt.Key.Key_Right:
        current_image_index = (current_image_index + 1) % len(slider_images)
    clicking()

window.keyPressEvent = keyPressEvent

# ----------------------------------------------------------------------------------------------------------------------

def main():
    window.showFullScreen()

    # conditional()
    clicking()

    app.exec()

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()