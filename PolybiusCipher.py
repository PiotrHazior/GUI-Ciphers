from tkinter import *
from tkinter import ttk

def create_polybius_cipher_window():
    polybius_window = Tk()
    polybius_window.geometry("600x750")
    polybius_window.title("Polybius Cipher GUI")

    # TOP PART
    frame_top = Frame(polybius_window, height=375)
    frame_top.pack(fill="both", expand=True)

    # SEPARATOR
    separator = ttk.Separator(polybius_window, orient="horizontal")
    separator.pack(fill="x", padx=0, pady=0)

    # BOTTOM PART
    frame_bottom = Frame(polybius_window, height=375)
    frame_bottom.pack(fill="both", expand=True)

    # STYLE
    polybius_window.config(background="#1b1c1b")
    frame_top.config(background="#1b1c1b")
    frame_bottom.config(background="#1b1c1b")


    FirstRow = ["A", "Ą", "B", "C", "Ć", "D", "E"]
    SecondRow = ["Ę", "F", "G", "H", "I", "J", "K"]
    ThirdRow = ["L", "Ł", "M", "N", "Ń", "O", "Ó"]
    FourthRow = ["P", "Q", "R", "S", "Ś", "T", "U"]
    FifthRow = ["V", "W", "X", "Y", "Z", "Ź", "Ż"]



    ##### ENCRYPT #####

    # BUTTON ENCRYPT
    lst = []
    def encryptClick():
        encryptText = normalText.get()
        encryptCode = encryptText.replace(" ", "").upper()
        for letter in encryptCode:
            lst.append(letter.upper())
        x = 0 #Counts rows
        y = 0 #Counts columns

        rows = []
        columns = []

        for letter in lst:
            for element in FirstRow:
                y += 1
                if letter == element:
                    print(element)
                    print(y)
                    columns += [y]
                    x += 1
                if y == 7:
                    y = 0
            for element in SecondRow:
                y += 1
                if letter == element:
                    print(element)
                    print(y)
                    columns += [y]
                    x += 2
                if y == 7:
                    y = 0
            for element in ThirdRow:
                y += 1
                if letter == element:
                    print(element)
                    print(y)
                    columns += [y]
                    x += 3
                if y == 7:
                    y = 0
            for element in FourthRow:
                y += 1
                if letter == element:
                    print(element)
                    print(y)
                    columns += [y]
                    x += 4
                if y == 7:
                    y = 0
            for element in FifthRow:
                y += 1
                if letter == element:
                    print(element)
                    print(y)
                    columns += [y]
                    x += 5
                if y == 7:
                    y = 0        
            print(x)
            rows += [x]
            x = 0
            y = 0
        encryptWord = [int(str(a) + str(b)) for a, b in zip(rows, columns)]
        encText.config(text=encryptWord)


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
        decryptCode = decryptText.replace(" ","").upper()
        lst2 = list(decryptCode)  # Reset list for each decryption
        rowDecrypt = [int(row) for row in lst2[::2]]
        colDecrypt = [int(col) for col in lst2[1::2]]
        decryptedList = []
        for row, col in zip(rowDecrypt, colDecrypt):
            if row == 1:
                print(FirstRow[col - 1])
                decryptedList.append(FirstRow[col - 1])
            elif row == 2:
                print(SecondRow[col - 1])
                decryptedList.append(SecondRow[col - 1])
            elif row == 3:
                print(ThirdRow[col - 1])
                decryptedList.append(ThirdRow[col - 1])
            elif row == 4:
                print(FourthRow[col - 1])
                decryptedList.append(FourthRow[col - 1])
            else:
                print(FifthRow[col - 1])
                decryptedList.append(FifthRow[col - 1])
        decryptedWord = ''.join(decryptedList)
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



    polybius_window.mainloop()