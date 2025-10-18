# VIRUS

Keylogger 

Este es un script se diseñó para registrar los tipeos del teclado en un archivo de texto.

NOTA 1: Este programa ignora cualquierletra de teclado que tenga de tamaño de nombre más de un caracter
      ejemplo: "Shift", "Ctrl", "BloqMayus"

NOTA 2: Se usa la función ".hook", esta función lee tanto la selcción de tecla como cuando se la suelta (KEY_DOWN y KEY_UP).
        Sin embargo para esta practica solo se desee mostra el "KEY_DOWN"



⚙️ Requisitos

Para ejecutar este script, solo necesitas tener Python instalado y la librería keyboard.

Instalación

  Abre tu terminal o símbolo del sistema y ejecuta el siguiente comando:

  pip install keyboard


🚀 Uso

1. Guarda el código de arriba en un archivo llamado main.py.

Ejecuta el Script: Abre tu terminal en la misma ubicación del archivo y corre:

python main.py

NOTA 3: El script se iniciará y verás el mensaje de inicio. Todas las pulsaciones de letras, números y puntuación se registrarán en segundo plano.
    Además:
    1. Tecla "space" se registra como un espacio.
    2. La tecla enter se registra como un salto de línea (\n).
    3.Teclas como Shift, Ctrl y Alt son ignoradas.
    4. Para finalizar el keylogger, regresa a la terminal y presiona la tecla ESC.

📝 Archivo de Logs

El registro de las pulsaciones se guardará automáticamente en el archivo:

archivo.txt

El archivo se crea en la misma carpeta donde ejecutas el script.

Ejemplo de Log

Si escribes la frase: "Hola mundo. [Enter] Esto es facil."

El archivo "archivo.txt" contendrá:

Hola mundo. 

Esto es facil.
