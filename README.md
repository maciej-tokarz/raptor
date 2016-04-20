![Raptor](/Docs/icon.png)
## Raptor

Maciej Tokarz © My-Poi!

##Instalacja Raspbiana Jessie

Jako podstawę działania posłuży wersja:

[Minimal image based on Debian Jessie](https://www.raspberrypi.org/downloads/raspbian/)

Po zainstalowaniu należy:

- zmienić hasło administratora,
- rozszerzyć partycję na całą objętość karty,
- włączyć kamerę,
- włączyć obsługę GPIO
- włączyć obsługę Serial

##Instalacja karty WiFi

$ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

```
network={
    ssid="nazwa_sieci"
    psk="hasło"
}
```
##Instalacja Pythona

[INSTALLING PYTHON PACKAGES](https://www.raspberrypi.org/documentation/linux/software/python.md)

$ sudo apt-get update

$ sudo apt-get install python-picamera

$ sudo apt-get upgrade

##Usunięcie plików alarmu

$ sudo rm -rf /home/pi/alarms

##Instalacja modemu GSM

$ sudo apt-get install ppp usb-modeswitch

$ sudo reboot

##Instalacja Python Serial

$ sudo apt-get install python-serial

$ sudo apt-get update

$ sudo apt-get upgrade

##Instalacja klienta NTP

$ sudo cp /home/pi/ntplib.py /usr/lib/python2.7/ntplib.py

##Uruchamianie wraz z systemem modemu i Raptora

$ sudo nano /etc/rc.local

```
/usr/sbin/usb_modeswitch -v 12d1 -p 15ca -V 12d1 -P 1506 -M "55534243123456780000000000000011062000000100000000000000000000"
lsusb
cd /home/pi/raptor.app
python raptor.app.py
```

##Instalacja Schedule

$ sudo su -

$ pip install schedule

##Aktualizacja Raspberry

$ sudo apt-get install rpi-update && sudo rpi-update && sudo reboot 

##Usuwanie pamięci tymczasowej instalatora na wypadek przerwania jego pracy

$ sudo rm /var/lib/dpkg/lock

$ sudo dpkg --configure -a

##Sprawdzenie wolnej przestrzeni systemu plików

$ df -Bm

##Uruchomienie skryptu Pythona

$ sudo python /home/pi/raptor.app/raptor.app.py