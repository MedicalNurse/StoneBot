import tkinter as tk
from tkinter import font as tkfont, messagebox
import pyautogui
import keyboard
import threading
import time
from PIL import Image, ImageGrab, ImageDraw
from imagesearch import imagesearch
import os

class BotApplication:
    def __init__(self):
        self.running = False
        self.click_delay = 16
        self.stop_event = threading.Event()
        self.bot_thread = None
        self.last_click_time = None
        self.sleep_duration = 10
        self.waiting_for_sleep = False
        self.root = tk.Tk()
        self.root.withdraw()
        self.show_main_window()
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

    def send_error_screenshot(self, error_pos):
        try:
            screenshot = ImageGrab.grab()
            draw = ImageDraw.Draw(screenshot)
            x, y = error_pos
            w, h = Image.open('C:/img/hata.png').size
            draw.rectangle([x, y, x + w, y + h], outline='red', width=3)
            screenshot.save('error_screenshot.png')
            print('Hata ekran görüntüsü kaydedildi: error_screenshot.png')
        except Exception as e:
            print(f'Hata görüntüsü kaydedilemedi: {e}')

    def check_error_image(self):
        try:
            error_pos = imagesearch('C:/img/hata.png')
            if error_pos[0] != -1:
                print("Hata görseli bulundu, ekran görüntüsü alınıyor...")
                self.send_error_screenshot(error_pos)
                return True
            else:
                print("Görsel bulunamadı: C:/img/hata.png") # yüklediğiniz görseli ekranda arar, bulamadığında böyle hata verir.
        except Exception as e:
            print(f'Hata kontrolü sırasında sorun oluştu: {e}')
        return False

    def show_main_window(self):
        self.root.deiconify()
        self.setup_main_window()

    def setup_main_window(self):
        self.root.title('M.D.')
        self.root.geometry('320x400')
        self.root.configure(bg='#2e2e2e')
        self.root.resizable(False, False)

        title_frame = tk.Frame(self.root, bg='#2e2e2e')
        title_frame.pack(fill=tk.X, padx=5, pady=5)
        tk.Label(title_frame, text='M.D.', font=tkfont.Font(size=14, weight='bold'), fg='#ffffff', bg='#2e2e2e').pack()

        settings_frame = tk.Frame(self.root, bg='#2e2e2e')
        settings_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(settings_frame, text='Tıklama Aralığı (saniye):', bg='#2e2e2e', fg='#ffffff').grid(row=0, column=0, sticky='w')
        self.click_delay_entry = tk.Entry(settings_frame, width=5)
        self.click_delay_entry.insert(0, str(self.click_delay))
        self.click_delay_entry.grid(row=0, column=1, padx=5)

        tk.Label(settings_frame, text='Bekleme Süresi (saniye):', bg='#2e2e2e', fg='#ffffff').grid(row=1, column=0, sticky='w')
        self.sleep_duration_entry = tk.Entry(settings_frame, width=5)
        self.sleep_duration_entry.insert(0, str(self.sleep_duration))
        self.sleep_duration_entry.grid(row=1, column=1, padx=5)

        self.status_label = tk.Label(self.root, text='Durum: Kapalı', bg='#2e2e2e', fg='white')
        self.status_label.pack(pady=5)

        self.son_tiklama_label = tk.Label(self.root, text='Geçen süre: -', bg='#2e2e2e', fg='white')
        self.son_tiklama_label.pack(pady=5)
        self.update_timer()

        button_frame = tk.Frame(self.root, bg='#2e2e2e')
        button_frame.pack(pady=10)
        tk.Button(button_frame, text='Başlat', width=10, command=self.start_bot).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text='Durdur', width=10, command=self.stop_bot).grid(row=0, column=1, padx=10)

        self.make_window_draggable(self.root)

    def update_timer(self):
        if self.last_click_time:
            elapsed = time.time() - self.last_click_time
            self.son_tiklama_label.config(text=f'Geçen süre: {elapsed:.1f} saniye')
        else:
            self.son_tiklama_label.config(text='Geçen süre: -')

        if self.running:
            self.status_label.config(text='Durum: Aktif')
        else:
            self.status_label.config(text='Durum: Kapalı')

        self.root.after(100, self.update_timer)

    def make_window_draggable(self, window):
        def on_press(event):
            window._drag_data = {'x': event.x, 'y': event.y}
        def on_drag(event):
            x = window.winfo_pointerx() - window._drag_data['x']
            y = window.winfo_pointery() - window._drag_data['y']
            window.geometry(f'+{x}+{y}')
        window.bind('<Button-1>', on_press)
        window.bind('<B1-Motion>', on_drag)

    def start_bot(self):
        if not self.running:
            self.running = True
            self.stop_event.clear()
            self.bot_thread = threading.Thread(target=self.run_bot, daemon=True)
            self.bot_thread.start()
            print('Bot başlatıldı')

    def stop_bot(self):
        if self.running:
            self.running = False
            self.stop_event.set()
            if self.bot_thread and self.bot_thread.is_alive():
                self.bot_thread.join(timeout=1)
            print('Bot durduruldu')

    def run_bot(self):
        # image_paths = ['C:/img/pembe1.png', 'C:/img/pembe2.png', 'C:/img/pembe3.png']
        # image_paths = ['C:/img/yesil1.png', 'C:/img/yesil2.png', 'C:/img/yesil3.png']
        image_paths = ['C:/img/all1.png', 'C:/img/all2.png', 'C:/img/all3.png']
        # image_paths = ['C:/img/tas1.png', 'C:/img/tas2.png', 'C:/img/tas3.png']
        # image_paths = ['C:/img/cadı1.png', 'C:/img/cadı2.png', 'C:/img/cadı3.png']


        while not self.stop_event.is_set() and self.running:
            self.check_error_image()
            positions = []
            for path in image_paths:
                if self.check_image_file(path):
                    pos = imagesearch(path)
                    if pos[0] != -1:
                        positions.append((pos[0] + 30, pos[1] + 80))
            if positions:
                closest = min(positions, key=lambda p: (p[0] - pyautogui.position().x) ** 2 + (p[1] - pyautogui.position().y) ** 2)
                self.safe_click(closest[0], closest[1])
            else:
                time.sleep(0.5)  

    def check_image_file(self, file_path):
        try:
            Image.open(file_path).verify()
            return True
        except:
            return False

    def safe_click(self, x, y, delay=None):
        try:
            self.last_click_time = time.time()
            current_delay = float(delay) if delay else float(self.click_delay_entry.get())
            pyautogui.moveTo(x, y)
            pyautogui.click(x, y, clicks=2, interval=0.1)
            print(f'Tıklama yapıldı: ({x}, {y}) - Bekleniyor...')
            time.sleep(float(self.sleep_duration_entry.get()))
        except Exception as e:
            print(f'Tıklama hatası: {e}')

    def on_closing(self):
        self.stop_bot()
        self.root.destroy()

if __name__ == '__main__':
    app = BotApplication()
    app.root.mainloop()
