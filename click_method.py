import pyautogui
from imagesearch import imagesearch
import time
import threading
import tkinter as tk
from tkinter import messagebox

def start_clicking():
    try:
        delay = int(delay_entry.get())
    except ValueError:
        messagebox.showerror('Hata', 'Lütfen geçerli bir sayı girin.')
        return

    def click_loop():
        png_path = 'C:/img/deneme.png'
        while True:
            position = imagesearch(png_path)
            if position[0] != -1:
                print(f'Görsel bulundu: {position}, tıklanıyor...')
                pyautogui.click(position[0], position[1])
            else:
                print('Görsel bulunamadı.')
            time.sleep(delay)

    t = threading.Thread(target=click_loop, daemon=True)
    t.start()

def make_draggable(window):
    def on_press(event):
        window._drag_data = {'x': event.x, 'y': event.y}
    def on_drag(event):
        deltax = event.x - window._drag_data['x']
        deltay = event.y - window._drag_data['y']
        window.geometry(f'+{window.winfo_x() + deltax}+{window.winfo_y() + deltay}')
    window.bind('<ButtonPress-1>', on_press)
    window.bind('<B1-Motion>', on_drag)

root = tk.Tk()
root.title('Oto Tıklayıcı')
make_draggable(root)
tk.Label(root, text='Bekleme süresi (saniye):').pack(pady=5)
delay_entry = tk.Entry(root)
delay_entry.insert(0, '10')
delay_entry.pack(pady=5)
start_button = tk.Button(root, text='Başlat', command=start_clicking)
start_button.pack(pady=10)
root.mainloop()
