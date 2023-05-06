import time
from pynput import mouse, keyboard
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener

# Função para salvar no arquivo TXT
def save_to_file(text):
    with open("C:\\registro_tempo.txt", "a") as file:
        file.write(text + "\n")

# Variáveis globais
waiting = True
start_time = None

# Funções para tratar eventos do mouse e teclado
def on_move(x, y):
    global waiting, start_time
    if not waiting:
        elapsed_time = time.time() - start_time
        save_to_file(f"Tempo decorrido desde a última contagem: {elapsed_time:.2f} segundos")
        waiting = True
        start_time = None

def on_click(x, y, button, pressed):
    on_move(x, y)

def on_scroll(x, y, dx, dy):
    on_move(x, y)

def on_press(key):
    on_move(None, None)

# Função principal
def main():
    global waiting, start_time

    mouse_listener = MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
    keyboard_listener = KeyboardListener(on_press=on_press)

    mouse_listener.start()
    keyboard_listener.start()

    try:
        while True:
            if waiting:
                time.sleep(60 * 20)  # Espera 20 minutos
                waiting = False
                start_time = time.time()
    except KeyboardInterrupt:
        mouse_listener.stop()
        keyboard_listener.stop()

if __name__ == "__main__":
    main()
