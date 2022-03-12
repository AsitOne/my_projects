from tkinter import *
from tkinter import ttk
from tkinter import filedialog

DICTIONARY = {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '10',
              'K': '11', 'L': '12',
              'M': '13', 'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18', 'S': '19', 'T': '20', 'U': '21',
              'V': '22', 'W': '23',
              'X': '24', 'Y': '25', 'Z': '26', ',': '&', '.': '@', ' ': '%', '?': '|'}
CEZ = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890']
SYMBOL = ['.,/;:[]{}<>?!"| =', '\n']


def Cipher_Cae():
    """
    Функция шифрует сообщение методом Цезаря, т.е сдвигает буквы алфавита на k символов.
    """
    word = chip_ent.get()
    k = int(k_spin.get())
    word = list(word.upper())
    a = []
    p = 0
    for i in word:
        if i not in SYMBOL:
            for j in range(len(CEZ[0])):
                if CEZ[0][j] == i:
                    if p == 0:
                        a.append(CEZ[0][(j + k) % 36].upper())
                        p += 1
                    else:
                        a.append(CEZ[0][(j + k) % 36].lower())
        elif i in ".?!":
            p = 0
            a.append(i)
        else:
            a.append(i)
    res = ''
    for i in a:
        res += str(i)
    dechip_ent1.delete(0, END)
    dechip_ent1.insert(0, res)


def DeChipper_Cae():
    word = dechip_ent1.get()
    k = int(k_spin.get())
    word = list(word.upper())
    a = []
    p = 0
    for i in word:
        if i not in SYMBOL:
            for j in range(len(CEZ[0])):
                if CEZ[0][j] == i:
                    if p == 0:
                        a.append(CEZ[0][(j - k) % 36].upper())
                        p += 1
                    else:
                        a.append(CEZ[0][(j - k) % 36].lower())
        elif i in ".?!":
            p = 0
            a.append(i)
        else:
            a.append(i)
    res = ''
    for i in a:
        res += str(i)
    chip_ent.delete(0, END)
    chip_ent.insert(0, res)


def get_key(val):
    """
    Функция получает ключ словаря по значению.
    """
    for key, value in DICTIONARY.items():
        if val == value:
            return str(key.lower())
    return val


def Number_chip():
    """
    Функция шифрует сообщение подстановочным шифром, т.е заменяет букву на её индекс алфавита.
    """
    word = chip_ent_tab2.get()
    word = list(word.upper())
    a = []
    for i in word:
        try:
            a.append(DICTIONARY[i])
        except KeyError:
            a.append(i)
    res = '-'.join(a)
    chip_ent1_tab2.delete(0, END)
    chip_ent1_tab2.insert(0, res)


def Number_dechip():
    """
    Функция расшифровывает сообщения, зашифрованные подстановочным шифром, т.е цифры индекса буквы в алфавите.
    """
    word = [i for i in chip_ent1_tab2.get().split('-')]
    j = 0
    a = []
    for i in word:
        if get_key(i) == '.':
            j = -2
        if j == 0:
            a.append(get_key(i).upper())
        else:
            a.append(get_key(i))
        j += 1
    res = ''
    for i in a:
        res += str(i)
    chip_ent_tab2.delete(0, END)
    chip_ent_tab2.insert(0, res)


def Copy_tab1_in():
    """
    Функция добавляет в буфер обмена сообщение.
    """
    window.clipboard_clear()
    window.clipboard_append(chip_ent.get())


def Copy_tab1_out():
    """
    Функция добавляет в буфер обмена расшифрованное сообщение.
    """
    window.clipboard_clear()
    window.clipboard_append(dechip_ent1.get())


def Copy_tab2_in():
    """
    Функция добавляет в буфер обмена сообщение.
    """
    window.clipboard_clear()
    window.clipboard_append(chip_ent_tab2.get())


def Copy_tab2_out():
    """
    Функция добавляет в буфер обмена расшифрованное сообщение.
    """
    window.clipboard_clear()
    window.clipboard_append(chip_ent1_tab2.get())


def wind_tab1():
    """
    Функция создаёт новое окно, в котором поддерживается работа с большими файлами.
    """
    def Cipher_Cae_2():
        """
        Функция шифрует сообщение методом Цезаря, т.е сдвигает буквы алфавита на k символов.
        """
        word = text_in.get('0.0', END)
        k = int(btn_k.get())
        word = list(word.upper())
        a = []
        p = 0
        for i in word:
            if (i not in SYMBOL[0]) and (i not in SYMBOL[1]):
                for j in range(len(CEZ[0])):
                    if CEZ[0][j] == i:
                        if p == 0:
                            a.append(CEZ[0][(j + k) % 36].upper())
                            p += 1
                        else:
                            a.append(CEZ[0][(j + k) % 36].lower())
            elif i in ".?!":
                p = 0
                a.append(i)
            else:
                a.append(i)
        res = ''
        for i in a:
            res += str(i)
        text_out.delete('0.0', END)
        text_out.insert('0.0', res)

    def DeChipper_Cae_2():
        """
        Функция расшифровывает сообщение методом Цезаря, т.е сдвигает буквы алфавита на k символов.
        """
        word = text_out.get('0.0', END)
        k = int(btn_k.get())
        word = list(word.upper())
        a = []
        p = 0
        for i in word:
            if (i not in SYMBOL[0]) and (i not in SYMBOL[1]):
                for j in range(len(CEZ[0])):
                    if CEZ[0][j] == i:
                        if p == 0:
                            a.append(CEZ[0][(j - k) % 36].upper())
                            p += 1
                        else:
                            a.append(CEZ[0][(j - k) % 36].lower())
            elif i in ".?!":
                p = 0
                a.append(i)
            else:
                a.append(i)
        res = ''
        for i in a:
            res += str(i)
        text_in.delete('0.0', END)
        text_in.insert('0.0', res)

    def open_file_tab1L():
        """
        Функция открывает txt файл в текстовое поле слева.
        """
        filepath = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        text_in.delete("0.0", END)
        with open(filepath, "r", encoding="utf-8") as input_file:
            text = input_file.read()
            text_in.insert(END, text)
        root.title(f"Шифр Цезаря - {filepath}")

    def save_file_tab1L():
        """
        Функция сохраняет txt файл из текстового поля слева.
        """
        filepath = filedialog.asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = text_in.get("0.0", END)
            output_file.write(text)
        root.title(f"Шифр Цезаря - {filepath} - Сохранено")

    def open_file_tab1R():
        """
        Функция открывает txt файл в текстовое поле справа.
        """
        filepath = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        text_out.delete("0.0", END)
        with open(filepath, "r", encoding="utf-8") as input_file:
            text = input_file.read()
            text_out.insert(END, text)
        root.title(f"Шифр Цезаря - {filepath}")

    def save_file_tab1R():
        """
        Функция сохраняет txt файл из текстового поля справа.
        """
        filepath = filedialog.asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = text_out.get("0.0", END)
            output_file.write(text)
        root.title(f"Шифр Цезаря - {filepath} - Сохранено")

    root = Tk()
    root.title('Шифр Цезаря')
    root.geometry('1325x800')
    menu = Menu(root)
    open_file = Menu(menu, tearoff=0)
    open_file.add_command(label='Открыть(слева)...', command=open_file_tab1L)
    open_file.add_command(label='Сохранить(слева)...', command=save_file_tab1L)
    open_file.add_separator()
    open_file.add_command(label='Открыть(справа)...', command=open_file_tab1R)
    open_file.add_command(label='Сохранить(справа)...', command=save_file_tab1R)
    menu.add_cascade(label='Файл', menu=open_file)
    root.config(menu=menu)

    text_in = Text(root, width=5, height=5)
    text_in.pack(side=LEFT, fill='both', padx=2, expand=1)

    frame_btn = Frame(root)
    frame_btn.pack(side=LEFT, fill='both', padx=2)

    nwind_btn_in = Button(frame_btn, text='\N{RIGHTWARDS BLACK ARROW}', width=5, height=2, font=('Montserrat', 20), command=Cipher_Cae_2)
    nwind_btn_in.pack(pady=10)

    lbl = Label(frame_btn, text='Сдвиг алфавита:', font=('Montserrat', 11))
    lbl.pack(pady=5)

    btn_k = Spinbox(frame_btn, from_=0, to=10, width=3, font=('Montserrat', 11))
    btn_k.pack(pady=5)

    nwind_btn_out = Button(frame_btn, text='\N{LEFTWARDS BLACK ARROW}', width=5, height=2, font=('Montserrat', 20), command=DeChipper_Cae_2)
    nwind_btn_out.pack(side=BOTTOM, pady=10)

    text_out = Text(root, width=5, height=5)
    text_out.pack(side=LEFT, fill='both', padx=2, expand=1)

    frame_ = Frame(root)
    frame_.pack(side=LEFT, fill='both', padx=2)


def wind_tab2():
    def get_key(val):
        """
        Функция получает ключ словаря по значению.
        """
        for key, value in DICTIONARY.items():
            if val == value:
                return str(key.lower())
        return val

    def Number_chip():
        """
        Функция шифрует сообщение подстановочным шифром, т.е заменяет букву на её индекс алфавита.
        """
        word = text_in.get('0.0', END).strip()
        word = list(word.upper())
        a = []
        for i in word:
            try:
                a.append(DICTIONARY[i])
            except KeyError:
                a.append(i)
        res = '-'.join(a)
        text_out.delete('0.0', END)
        text_out.insert('0.0', res)

    def Number_dechip():
        """
        Функция расшифровывает сообщения, зашифрованные подстановочным шифром, т.е цифры индекса буквы в алфавите.
        """
        word = [i for i in text_out.get('0.0', END).strip().split('-')]
        j = 0
        a = []
        for i in word:
            if get_key(i) == '.':
                j = -2
            if j == 0:
                a.append(get_key(i).upper())
            else:
                a.append(get_key(i))
            j += 1
        res = ''
        for i in a:
            res += str(i)
        text_in.delete('0.0', END)
        text_in.insert('0.0', res)

    def open_file_tab1L():
        """
        Функция открывает txt файл в текстовое поле слева.
        """
        filepath = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        text_in.delete("0.0", END)
        with open(filepath, "r", encoding="utf-8") as input_file:
            text = input_file.read()
            text_in.insert(END, text)
        root.title(f"Шифр номером - {filepath}")

    def save_file_tab1L():
        """
        Функция сохраняет txt файл из текстового поля слева.
        """
        filepath = filedialog.asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = text_in.get("0.0", END)
            output_file.write(text)
        root.title(f"Шифр номером - {filepath} - Сохранено")

    def open_file_tab1R():
        """
        Функция открывает txt файл в текстовое поле справа.
        """
        filepath = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        text_out.delete("0.0", END)
        with open(filepath, "r", encoding="utf-8") as input_file:
            text = input_file.read()
            text_out.insert(END, text)
        root.title(f"Шифр номером - {filepath}")

    def save_file_tab1R():
        """
        Функция сохраняет txt файл из текстового поля справа.
        """
        filepath = filedialog.asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = text_out.get("0.0", END)
            output_file.write(text)
        root.title(f"Шифр номером - {filepath} - Сохранено")

    root = Tk()
    root.title('Шифр номером')
    root.geometry('1325x800')
    menu = Menu(root)
    open_file = Menu(menu, tearoff=0)
    open_file.add_command(label='Открыть(слева)...', command=open_file_tab1L)
    open_file.add_command(label='Сохранить(слева)...', command=save_file_tab1L)
    open_file.add_separator()
    open_file.add_command(label='Открыть(справа)...', command=open_file_tab1R)
    open_file.add_command(label='Сохранить(справа)...', command=save_file_tab1R)
    menu.add_cascade(label='Файл', menu=open_file)
    root.config(menu=menu)

    text_in = Text(root, width=5, height=5)
    text_in.pack(side=LEFT, fill='both', padx=2, expand=1)

    frame_btn = Frame(root)
    frame_btn.pack(side=LEFT, fill='both', padx=2)

    nwind_btn_in = Button(frame_btn, text='\N{RIGHTWARDS BLACK ARROW}', width=5, height=2, font=('Montserrat', 20), command=Number_chip)
    nwind_btn_in.pack(pady=10)

    nwind_btn_out = Button(frame_btn, text='\N{LEFTWARDS BLACK ARROW}', width=5, height=2, font=('Montserrat', 20), command=Number_dechip)
    nwind_btn_out.pack(side=BOTTOM, pady=10)

    text_out = Text(root, width=5, height=5)
    text_out.pack(side=LEFT, fill='both', padx=2, expand=1)

    frame_ = Frame(root)
    frame_.pack(side=LEFT, fill='both', padx=2)


"""
ТЕЛО ПРИЛОЖЕНИЯ
"""
window = Tk()
window.title('Шифр машина')
window.geometry('650x250')
window.resizable(width=False, height=False)
tab_control = ttk.Notebook(window)
tab_1 = ttk.Frame(tab_control)
tab_2 = ttk.Frame(tab_control)
tab_control.add(tab_1, text='Шифр Цезаря')
tab_control.add(tab_2, text='Шифр номером')
tab_control.pack(expand=1, fill='both')

""" 
ПЕРВАЯ ВКЛАДКА
"""

welcome_lbl = Label(tab_1, text='Шифр Цезаря', font=('Montserrat', 25))
welcome_lbl.pack()

big_text_tab1 = Button(tab_1, text='Big text', font=('Montserrat', 11), command=wind_tab1)
big_text_tab1.pack()

frm_k = Frame(tab_1, relief=SUNKEN)
frm_k.pack(fill=BOTH, pady=5)

k_lbl = Label(frm_k, text='Сдвиг алфавита:', font=('Montserrat', 11))
k_lbl.pack(side=LEFT, fill=BOTH)

k_spin = Spinbox(frm_k, from_=0, to=10, width=3, font=('Montserrat', 12))
k_spin.pack(side=LEFT, fill=BOTH)

frm_chip = Frame(tab_1, relief=SUNKEN)
frm_chip.pack(fill=BOTH, pady=5)

chip_lbl = Label(frm_chip, text='Сообщение для шифра:', font=('Montserrat', 11))
chip_lbl.pack(side=LEFT, fill=BOTH)

chip_ent = Entry(frm_chip, font=('Montserrat', 12))
chip_ent.pack(side=LEFT, fill=BOTH)

chip_btn = Button(frm_chip, text='Зашифровать', font=('Montserrat', 10), command=Cipher_Cae)
chip_btn.pack(side=LEFT, fill=BOTH, padx=4)

btn_copy_in = Button(frm_chip, text='Скопировать расшифровку', font=('Montserrat', 8), command=Copy_tab1_in)
btn_copy_in.pack(side=LEFT, fill=BOTH, padx=5)

frm_out = Frame(tab_1, relief=SUNKEN)
frm_out.pack(fill=BOTH, pady=5)

dechip_lbl = Label(frm_out, text='Сообщение для расшифровки:', font=('Montserrat', 11))
dechip_lbl.pack(side=LEFT, fill=BOTH)

dechip_ent1 = Entry(frm_out, font=('Montserrat', 12))
dechip_ent1.pack(side=LEFT, fill=BOTH)

dechip_btn = Button(frm_out, text='Расшифровать', font=('Montserrat', 10), command=DeChipper_Cae)
dechip_btn.pack(side=LEFT, fill=BOTH, padx=4)

btn_copy_out = Button(frm_out, text='Скопировать шифровку', font=('Montserrat', 8), command=Copy_tab1_out)
btn_copy_out.pack(side=LEFT, fill=BOTH, padx=5)

""" 
ВТОРАЯ ВКЛАДКА
"""

welcome_lbl_tab2 = Label(tab_2, text='Шифр номером', font=('Montserrat', 25))
welcome_lbl_tab2.pack()

big_text_tab1 = Button(tab_2, text='Big text', font=('Montserrat', 11), command=wind_tab2)
big_text_tab1.pack()

frm_k_tab2 = Frame(tab_2, relief=SUNKEN)
frm_k_tab2.pack(fill=BOTH, pady=5)

frm_chip_tab2 = Frame(tab_2, relief=SUNKEN)
frm_chip_tab2.pack(fill=BOTH, pady=5)

chip_lbl_tab2 = Label(frm_chip_tab2, text='Сообщение для шифра:', font=('Montserrat', 11))
chip_lbl_tab2.pack(side=LEFT, fill=BOTH)

chip_ent_tab2 = Entry(frm_chip_tab2, font=('Montserrat', 12))
chip_ent_tab2.pack(side=LEFT, fill=BOTH)

chip_btn_tab2 = Button(frm_chip_tab2, text='Зашифровать', font=('Montserrat', 10), command=Number_chip)
chip_btn_tab2.pack(side=LEFT, fill=BOTH, padx=4)

btn_copy_in_tab2 = Button(frm_chip_tab2, text='Скопировать расшифровку', font=('Montserrat', 8), command=Copy_tab2_in)
btn_copy_in_tab2.pack(side=LEFT, fill=BOTH, padx=5)

frm_out_tab2 = Frame(tab_2, relief=SUNKEN)
frm_out_tab2.pack(fill=BOTH, pady=5)

chip_lbl_tab2 = Label(frm_out_tab2, text='Сообщение для расшифровки:', font=('Montserrat', 11))
chip_lbl_tab2.pack(side=LEFT, fill=BOTH)

chip_ent1_tab2 = Entry(frm_out_tab2, font=('Montserrat', 12))
chip_ent1_tab2.pack(side=LEFT, fill=BOTH)

chip_btn2_tab2 = Button(frm_out_tab2, text='Расшифровать', font=('Montserrat', 10), command=Number_dechip)
chip_btn2_tab2.pack(side=LEFT, fill=BOTH, padx=4)

btn_copy_out_tab2 = Button(frm_out_tab2, text='Скопировать шифр', font=('Montserrat', 8), command=Copy_tab2_out)
btn_copy_out_tab2.pack(side=LEFT, fill=BOTH, padx=5)

window.mainloop()
