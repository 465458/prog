import random
import tkinter as tk
from tkinter import messagebox



DOUBLE_ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
DOUBLE_NUMB = "01234567890123456789"
NUMB_AND_ALPH = "012345678ABCDEFGHIJKLMNOPQRSTUVWXYZ"
the_key = []



def keysmaker(x):
    main_key = ""
    part = ""

    for i in range(5):
        part += random.choice(NUMB_AND_ALPH)
    main_key += part

    for i in range(3):

        part = list(part)
        part.pop(random.randint(0,len(part)-1))

        if len(part) == 4:
            for n in range(4):
                if part[n] in DOUBLE_ALPH:
                    part[n] = DOUBLE_ALPH[DOUBLE_ALPH.index(part[n])+int(x[0])]
                if part[n] in DOUBLE_NUMB:
                    part[n] = DOUBLE_NUMB[DOUBLE_NUMB.index(part[n])+int(x[0])]

        if len(part) == 3:
            for n in range(3):
                if part[n] in DOUBLE_ALPH:
                    part[n] = DOUBLE_ALPH[DOUBLE_ALPH.index(part[n])-int(x[1])]
                if part[n] in DOUBLE_NUMB:
                    part[n] = DOUBLE_NUMB[DOUBLE_NUMB.index(part[n])-int(x[1])]

        if len(part) == 2:
            for n in range(2):
                if part[n] in DOUBLE_ALPH:
                    part[n] = DOUBLE_ALPH[DOUBLE_ALPH.index(part[n])+int(x[2])]
                if part[n] in DOUBLE_NUMB:
                    part[n] = DOUBLE_NUMB[DOUBLE_NUMB.index(part[n])+int(x[2])]
        part = "".join(part)
        main_key += '-'+ part

    return main_key



def action():
    number = input_window.get()
    if len(number) != 3 or number[0] == "0" or number.isdigit() == False:
        messagebox.showwarning('Ошибка','У кого-то проблемы с числами или чтением условий!')
        return 0
    else:
        if number.isdigit():
            main_key = keysmaker(number)
            main_key = tk.Label(
                window,
                text= main_key,
                font=('Arial_Black', 20),
                bg = '#163a6a',
                fg = 'white',
                highlightbackground="#000000",
                highlightthickness=2,
                width=20
            )
            main_key.place(x=50,y=350)
            the_key.append(main_key)
            if len(the_key) > 1:
                previous_key = the_key.pop(0)
                previous_key.destroy()



window = tk.Tk()
window.title('Генератор паролей')
window.geometry('768x432')
window.resizable(width=False, height=False)
window_image = tk.PhotoImage(file='picture.png')
window_lbl = tk.Label(window, image=window_image)
window_lbl.place(x=0, y=0, relwidth=1, relheight=1)



input = tk.Label(
    window,
    text='Введите трёхзначное число',
    font=('Arial_Black', 20),
    bg = '#163a6a',
    fg = 'white',
    highlightbackground="#000000",
    highlightthickness=2
)
window.after(5,input)
input.place(x=200,y=10)



input_window = tk.Entry(window, width=10,borderwidth=5, font=('Arial_Black', 40))
input_window.place(x=60, y=200)



part_lbl = tk.Label(
    window,
    text='Сгенерированный ключ: ',
    font=('Arial_Black', 20),
    bg = '#163a6a',
    fg = 'white',
    highlightbackground="#000000",
    highlightthickness=2
)
part_lbl.place(x=50,y=300)



the_button = tk.Button(
    window,
    text = "Отправить",
    borderwidth =5,
    height=4,
    width=20,
    command=action
)
the_button.place(x=550,y=200)



window.mainloop()