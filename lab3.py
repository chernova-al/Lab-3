import tkinter as tk
from keygeneration import gen
def close():
    window.destroy()

def key():
    b = arg_B.get()
    lbl_key.configure(text=gen(b))

window = tk.Tk()
window.geometry('750x463')
bg_img = tk.PhotoImage(file='bg750x.png')

lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

lbl_B = tk.Label(frame, text='Enter the six-letter word:', font=('Arial', 15))
lbl_B.grid(column=1, row=0, padx=10, pady=15)
arg_B = tk.Entry(frame, width=15)
arg_B.insert(0, '')
arg_B.grid(column=1, row=1, padx=10, pady=15)

lbl_key = tk.Label(frame, text='Your key:', font=('Arial', 15))
lbl_key.grid(column=1, row=2)
lbl_key = tk.Label(frame, text='None yet.', font=('Arial', 10))
lbl_key.grid(column=1, row=4)

btn_calc = tk.Button(frame, text='Generate the key!', command=key)
btn_calc.grid(column=1, row=2, padx=15, pady=15)

window.mainloop()
