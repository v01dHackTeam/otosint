# otosint – Passive OSINT Aracı

otosint, hedef hakkında tamamen pasif bilgi toplamak için hazırlanmış basit ve hızlı bir OSINT aracıdır.
Domain veya IP girildiğinde otomatik olarak:

IP çözümleme

IPInfo sorgusu

Whois

DNS kayıtları

Reverse DNS

Subdomain bilgileri


çıktılarını toplar ve ekrana basar.


---

# Kurulum

Repo’yu klonla:
```
git clone https://github.com/v01dHackTeam/otosint.git
cd otosint
```
setup.py ile kur:
```
python3 setup.py
```
direkt çalıştır:
```
otosint
```

---

# Kullanım

Çalıştırdığında hedef sorar:

Enter Target Domain:

Domain veya IP gir.
Araç otomatik olarak tüm pasif verileri toplar ve çıktı dosyalarına kaydeder:

example.com_osint.txt
example.com_osint.json

Hepsi bu. Kodun yaptığı iş net, ekstra hiçbir zırvalık yok.
