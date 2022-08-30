import pyautogui

import time

pyautogui.alert(
    "O código será executado. Não use nada do seu PC enquanto o código está rodando")

pyautogui.hotkey('win', 'e')

time.sleep(3)

pyautogui.hotkey('ctrl', 'l')

pyautogui.write('documentos/pasta1/excel1.xlsx')

pyautogui.press('enter')

time.sleep(7)

pyautogui.write('Celio Amaral')

time.sleep(3)

pyautogui.hotkey('ctrl', 'b')

pyautogui.hotkey('ctrl', 'c')

pyautogui.hotkey('alt', 'f4')

time.sleep(3)

pyautogui.hotkey('ctrl', 'l')

pyautogui.write('documentos/pasta2/excel2.xlsx')

pyautogui.press('enter')

time.sleep(7)

pyautogui.press(['right', 'down'])

pyautogui.hotkey('ctrl', 'v')

pyautogui.hotkey('ctrl', 'b')

time.sleep(4)

pyautogui.hotkey('alt', 'f4')
