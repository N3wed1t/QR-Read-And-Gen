import keyboard
from pyzbar.pyzbar import decode
from PIL import ImageGrab
import tkinter as tk
# Flag to track key presses
win_pressed = False
shift_pressed = False
left_click = False

# Define the key combinations
win_key = 'win+left shift'
capture_key = 'Q'

# Define a function to capture the screen
def capture_screen():
    screenshot = ImageGrab.grab()
    decoded_list = decode(screenshot)
    decoded_data = decoded_list[0].data.decode()
    print(decoded_data)
# Define a function to handle key presses
def on_keyboard_event(e):
    global win_pressed, shift_pressed

    if e.event_type == keyboard.KEY_DOWN:
        if e.name == 'left windows':
            win_pressed = True
        elif e.name == 'shift':
            shift_pressed = True
        # Check for the specific key combination
        print(f"Keys={e.name}, Win={win_pressed}, Shift={shift_pressed}")
        
        if win_pressed and shift_pressed and e.name == capture_key:
            print('Screen Capture Start!')
            capture_screen()
    elif e.event_type == keyboard.KEY_UP:
        if e.name == 'windows':
            win_pressed = False
        elif e.name == 'shift':
            shift_pressed = False
keyboard.hook(on_keyboard_event)

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.grid

# Run the script
if __name__ == "__main__":
    myapp = App()
    myapp.master.title("QR Code Reader/Generator")
    myapp.master.maxsize(800, 400)
    myapp.master.minsize(800, 400)
    myapp.mainloop()
    # keyboard.wait()

# the program should have gui that have button use to capture screen and decode qr code
# qr code generator
# keyboard shortcut