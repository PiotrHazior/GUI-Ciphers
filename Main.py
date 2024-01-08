from tkinter import *
from tkinter import ttk
from CaesarCipher import create_caesar_cipher_window
from PolybiusCipher import create_polybius_cipher_window
from HomophonicCipher import create_homophonic_cipher_window

window = Tk()
window.geometry("600x750")
window.title("Cipher GUI")
window.config(background="#1b1c1b")

def open_caesar_cipher():
    create_caesar_cipher_window()
    
def open_polybius_cipher():
    create_polybius_cipher_window()
    
def open_homophonic_cipher():
    create_homophonic_cipher_window()
    
# BUTTONS
btn_caesar = Button(window,
                    text="Szyfr Cezara",
                    command=open_caesar_cipher,
                    font=("Comic Sans", 15),
                    fg="#1b1c1b",
                    bg="#117827",
                    activeforeground="#1b1c1b",
                    activebackground="#117827")
btn_caesar.pack(fill="both", expand=True, pady=(20, 10), padx=5)

btn_polibius = Button(window,
                      text="Szyfr Polibiusza",
                      command=open_polybius_cipher,
                      font=("Comic Sans", 15),
                      fg="#1b1c1b",
                      bg="#117827",
                      activeforeground="#1b1c1b",
                      activebackground="#117827")
btn_polibius.pack(fill="both", expand=True, pady=10, padx=5)

btn_homophonic = Button(window,
                        text="Szyfr Homofoniczny",
                        command=open_homophonic_cipher,
                        font=("Comic Sans", 15),
                        fg="#1b1c1b",
                        bg="#117827",
                        activeforeground="#1b1c1b",
                        activebackground="#117827")
btn_homophonic.pack(fill="both", expand=True, pady=(10, 20), padx=5)

# AUTHOR BLOCK
author_text = Label(window,
                text="Piotr Hazior",
                font="Arial, 10",
                width=10,
                height=1,
                fg="#1b1c1b",
                bg="#117827")
author_text.pack(side="left", pady=0)

window.mainloop()