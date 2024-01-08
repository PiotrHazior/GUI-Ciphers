from tkinter import *
from tkinter import ttk
import random

def create_homophonic_cipher_window():
    homophonic_window = Tk()
    homophonic_window.geometry("600x750")
    homophonic_window.title("Homophonic Cipher GUI")

    # TOP PART
    frame_top = Frame(homophonic_window, height=375)
    frame_top.pack(fill="both", expand=True)

    # SEPARATOR
    separator = ttk.Separator(homophonic_window, orient="horizontal")
    separator.pack(fill="x", padx=0, pady=0)

    # BOTTOM PART
    frame_bottom = Frame(homophonic_window, height=375)
    frame_bottom.pack(fill="both", expand=True)

    # STYLE
    homophonic_window.config(background="#1b1c1b")
    frame_top.config(background="#1b1c1b")
    frame_bottom.config(background="#1b1c1b")

    letter_dict = {
        "A" : ["007", "123", "530", "241", "532", "777", "020", "321", "466"],
        "Ą" : ["567"],
        "B" : ["888"],
        "C" : ["999", "245", "111", "001"],
        "Ć" : ["120"],
        "D" : ["566", "744", "113"],
        "E" : ["987", "022", "543", "921", "488", "107", "729", "527"],
        "Ę" : ["076"],
        "F" : ["004"],
        "G" : ["504"],
        "H" : ["765"],
        "I" : ["666", "009", "200", "334", "053", "284", "104", "092"],
        "J" : ["477", "655"],
        "K" : ["984", "337", "222", "096"], 
        "L" : ["344", "890"],
        "Ł" : ["808", "006"],
        "M" : ["770", "032", "992"],
        "N" : ["228", "044", "656", "926", "199", "672"],
        "Ń" : ["155"],
        "O" : ["900", "555", "292", "336", "100", "021", "170", "444"],
        "Ó" : ["234"],
        "P" : ["403", "443", "106"],
        "Q" : ["600"],
        "R" : ["700", "030", "510", "449", "601"],
        "S" : ["558", "223", "589", "041"],
        "Ś" : ["171"],
        "T" : ["683", "629", "933", "508"],
        "U" : ["661", "506", "702"],
        "V" : ["333"],
        "W" : ["633", "110", "442", "420", "922"],
        "X" : ["153"],
        "Y" : ["724", "717", "818", "873"],
        "Z" : ["325", "165", "147", "324", "552", "562"],
        "Ź" : ["479"],
        "Ż" : ["550"]
    }

    ##### ENCRYPT #####
    # BUTTON ENCRYPT
    def encryptClick():
        encryptText = normalText.get().upper()
        encrypt_lst = []
        
        for letter in encryptText:
            if letter in letter_dict:
                random_letter = random.choice(letter_dict[letter])
                encrypt_lst.append(random_letter)
                
        encrypted_word = " ".join(encrypt_lst)
        encText.config(text=encrypted_word)

    # word = input("Prosze podać słowo: ").upper()

    encrypt = Button(frame_top,
                    text="ENCRYPT",
                    command=encryptClick,
                    font=("Comic Sans", 20),
                    fg="#1b1c1b",
                    bg="#117827",
                    activeforeground="#1b1c1b",
                    activebackground="#117827")
    encrypt.pack(side="top", pady=20)

    # TEXT BLOCK BEFORE ENCRYPT
    normalText = Entry(frame_top,
                    font="Arial, 20",
                    fg="#1b1c1b",
                    bg="#117827")
    normalText.pack(side="top", pady=20)

    # TEXT BLOCK AFTER ENCRYPT
    encText = Label(frame_top,
                    text="",
                    font="Arial, 19",
                    width=20,
                    height=1,
                    fg="#1b1c1b",
                    bg="#117827"
                    )
    encText.pack(side="top", pady=20)



    ####### DECRYPT ######

    # BUTTON DECRYPT
    def decryptClick():
        decryptText = secretText.get()
        lst = decryptText.split()
        decrypt_lst = []

        for i in lst:
            if len(i) == 3 and i.isdigit():
                decrypt_lst.append(i)
        
        decrypted_lst = []

        for i in decrypt_lst:
            for letter, numbers in letter_dict.items():
                for number in numbers:
                    if i == number:
                        decrypted_lst.append(letter)
                    
        decryptedWord = ''.join(decrypted_lst)
        decText.config(text=decryptedWord)
        

    decrypt = Button(frame_bottom,
                    text="DECRYPT",
                    command=decryptClick,
                    font=("Comic Sans", 20),
                    fg="#1b1c1b",
                    bg="#117827",
                    activeforeground="#1b1c1b",
                    activebackground="#117827")
    decrypt.pack(side="top", pady=20)


    # TEXT BLOCK BEFORE DECRYPT
    secretText = Entry(frame_bottom,
                    font="Arial, 20",
                    fg="#1b1c1b",
                    bg="#117827")
    secretText.pack(side="top", pady=20)


    # TEXT BLOCK AFTER DECRYPT
    decText = Label(frame_bottom,
                    text="",
                    font="Arial, 19",
                    width=20,
                    height=1,
                    fg="#1b1c1b",
                    bg="#117827")
    decText.pack(side="top", pady=20)


    # AUTHOR BLOCK
    author_text = Label(frame_bottom,
                    text="Piotr Hazior",
                    font="Arial, 10",
                    width=10,
                    height=1,
                    fg="#1b1c1b",
                    bg="#117827")
    author_text.pack(side="left", pady=0)



    homophonic_window.mainloop()