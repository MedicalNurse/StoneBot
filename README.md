# StoneBot

StoneBot, ekran görüntüsünde belirli görselleri arayarak otomatik tıklama işlemleri yapan bir Python uygulamasıdır. Görsel arama ve tıklama işlemleri için PyAutoGUI, OpenCV ve Pillow gibi kütüphaneleri kullanır. Uygulama, görsel arama ve hata tespiti için iki farklı arayüz sunar.

## Özellikler
- Belirli görselleri ekranda arar ve tıklar
- Hata görseli tespit edildiğinde ekran görüntüsü alır
- Tkinter ile kullanıcı arayüzü
- Tıklama aralığı ve bekleme süresi ayarlanabilir
- Sürüklenebilir pencere

## Dosyalar
- `stone_search_method.py`: Ana bot uygulaması ve arayüz
- `click_method.py`: Basit görsel arama ve tıklama arayüzü
- `imagesearch.py`: Görsel arama fonksiyonu (OpenCV ile)
- `requirements.txt`: Gerekli Python paketleri

## Kurulum
1. Python 3.8+ kurulu olmalıdır.
2. Gerekli paketleri yükleyin:
   ```powershell
   pip install -r requirements.txt
   ```
3. Görsellerinizi `C:/img/` klasörüne yerleştirin (örnek: hata.png, all1.png, deneme.png).

## Kullanım
### stone_search_method.py
Ana botu başlatmak için:
```powershell
python stone_search_method.py
```
Arayüzden tıklama aralığı ve bekleme süresi ayarlanabilir. Bot, belirlediğiniz görselleri ekranda arar ve bulduğunda otomatik olarak tıklar.

### click_method.py
Daha basit bir tıklama aracı için:
```powershell
python click_method.py
```
Görsel yolu ve bekleme süresi arayüzden girilir. Belirtilen görsel ekranda bulunduğunda otomatik tıklama yapılır.

## Gereksinimler
- keyboard
- numpy
- opencv-python
- Pillow
- pyautogui

Tüm gereksinimler `requirements.txt` dosyasında listelenmiştir.

## Notlar
- Görsel dosyalarını ve yollarını kendinize göre düzenleyin.
- Uygulama Windows ortamında test edilmiştir.

## Katkı
Geliştirmeler ve geri bildirimler için pull request gönderebilirsiniz.

---

**StoneBot** ile ekran üzerindeki görselleri kolayca tespit edip otomatik tıklama işlemleri gerçekleştirebilirsiniz.
