import time
import threading
import pyautogui
import keyboard

TOGGLE_KEY = "O"
clicking = False

def clicker():
    global clicking  # Позволяет функции видеть изменение переменной из основного цикла
    while True:      # Исправлено с 'true' на 'True'
        if clicking:
            pyautogui.click()
            time.sleep(0.01)
        else:
            time.sleep(0.1)

# Запуск фонового потока для кликов
threading.Thread(target=clicker, daemon=True).start()

# Основной цикл переключения
while True:
    keyboard.wait(TOGGLE_KEY)
    clicking = not clicking
    time.sleep(0.2)  # Защита от дребезга контактов клавиатуры
