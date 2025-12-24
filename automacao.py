import pyautogui

# escreve o texto "Ola, mundo!" com intervalo de 0.1 segundos entre cada letra
pyautogui.typewrite('Ola, mundo!', interval=0.1)

# Pressiona a tecla "Enter"
pyautogui.press('enter')


# Segura a tecla "Ctrl" e pressiona a tecla "c"
pyautogui.keyDown('ctrl')
pyautogui.press('c')
pyautogui.keyUp('ctrl')

# Segura a tecla "Ctrl" e pressiona a tecla "v"
pyautogui.keyDown('ctrl')
pyautogui.press('v')
pyautogui.keyUp('ctrl')
