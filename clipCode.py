# last updated : 1/25/2025

import tkinter as tk
import pyperclip
import pyautogui
import tkinter as tk
import time

def insertCode():
    unit = {}

    def addToDic():
        text = textBox.get("1.0", tk.END).strip()
        code = codeBox.get("1.0", tk.END).strip()
        unit[text] = [code]
        textBox.delete("1.0", tk.END)
        codeBox.delete("1.0", tk.END)

    root = tk.Tk()
    root.title("وارد کردن درس ها")

    textLable = tk.Label(root, text="درس به انگلیسی:")
    textLable.pack(padx=1, pady=1)
    textBox = tk.Text(root, height=1, width=12)
    textBox.pack(padx=50, pady=5)

    codeLable = tk.Label(root, text="کد درس به انگلیسی:")
    codeLable.pack(padx=1, pady=1)
    codeBox = tk.Text(root, height=1, width=12)
    codeBox.pack(padx=50, pady=5)

    submitButton = tk.Button(root, text="ثبت کردن", command=addToDic)
    submitButton.pack(padx=50, pady=50)

    root.mainloop()
    return unit


def linkingUnit(unit):
    key_list = list(unit.keys())
    i = 0
    for item in unit:
        if i != (len(key_list)-1):
            unit[item].append(key_list[i+1])
            unit[item].insert(0, key_list[i-1])
            i+=1
        else:
            unit[item].append(key_list[0])
            unit[item].insert(0, key_list[i-1])
            break
    return unit


def showItem(unit):
    key = list(unit.keys())[0]

    def update_display(key):
        root = tk.Tk()
        root.title(key)

        backButton = tk.Button(root, text="قبلی", command=lambda:back(key, root))
        insertButton = tk.Button(root, text=key, command=lambda:insert(key))
        nextButton = tk.Button(root, text="بعدی", command=lambda:next(key, root))

        backButton.pack(padx=100, pady=10)
        insertButton.pack(padx=100, pady=10)
        nextButton.pack(padx=100, pady=10)

        root.mainloop()
    
    def insert(key):
        pyperclip.copy(unit[key][1])
        time.sleep(1.5)
        pyautogui.hotkey('ctrl', 'v')
    def back(key, root):
        root.destroy()
        backKey = unit[key][0]
        update_display(backKey)
    def next(key, root):
        root.destroy()
        nextKey = unit[key][2]
        update_display(nextKey)
        
    
    update_display(key)


unit = insertCode()
newunit = linkingUnit(unit)
showItem(newunit)