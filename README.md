![Raptor](/Docs/icon.png)
#Raptor

###Udostępniony kod wykorzystujesz na własną odpowiedzialność!

##Wstęp

Projekt jest moim pierwszym napisanym w Pythonie więc proszę o wyrozumiałość :-)

Raptor to aplikacja, dzięki której możliwe jest dozorowanie wybranego miejsca za pomocą czujki PIR, która identyfikuje naruszenie obszaru przez intruza. 
W takim przypadku wzbudzany jest alarm, który powiadamia ustalonych odbiorców o zdarzeniu sms-em oraz przez określony czas co sekundę rejestruje zdjęcia z kamery. 
Na zakończenie alarmu pierwszych sześć zdjęć jest wysyłanych e-mailem. Całość działa w oparciu o komputer Raspberry Pi.

Zainteresowanych zapraszam do współtworzenia Raptora.

[Dyskusja na grupie Malinowe Pi (Facebook) o projekcie](https://www.facebook.com/groups/malinowepi/permalink/433256330178355/) <<< Serdeczne dzięki za uwagi!

##Podstawowe funkcje programu

- Raptor na starcie ustawia czas systemowy na podstawie wzorca wg. pool.ntp.org,
- dozoruje obszar czujką i śledzi jej wskazania,
- po otrzymaniu określonej ilości wskazań pozytywnych czujki aktywuje alarm,
- rozpoczęcie alarmu sygnalizowane jest sms-em o przykładowej treści “Raptor: alarm 2016-04-14 1123”, gdzie data i godzina to początek alarmu,
- alarm realizuje przede wszystkim swoją podstawową funkcję, to znaczy zapisuje serię 90 zdjęć w odstępach sekundowych,
- wykonanie zdjęcia determinuje wskazanie czujki – zdjęcie nie zostanie wykonane jeśli nie ma ruchu w chronionym obszarze,
- po zakończeniu serii, pierwszych sześć zdjęć zostanie wysłane e-mailem do określonych odbiorców,
- po wysłaniu e-maila alarm będzie ponownie gotowy do działania i wskazania czujki mogą wywołać następny alarm,
- przed zapisem zdjęć Raptor sprawdza ilość dostępnego miejsca na karcie i jeśli będzie go mniej niż 500MB to 10 najstarszych alarmów zostanie automatycznie usuniętych,
- codziennie o ustalonej godzinie Raptor wysyła kontrolne zdjęcie e-mailem,

Do przesyłania sms-ów wykorzystuję API dostępne np. tutaj: [mail2sms](https://www.smsapi.pl/mail2sms)

##Podzespoły

- Raspberry Pi,
- dedykowana kamera wraz podświetleniem IR,
- taśma łącząca kamerę, np. o długości dwóch metrów,
- czujka PIR,
- HUB USB niezbędny do zasilenia modemu GSM,
- modem GSM np. Huawei E3131h-2,
- UPS opisany poniżej,

##UPS

Dzięki pomocy Piotra "pimowo" z forum [nettemp.pl](http://nettemp.pl/forum/viewtopic.php?f=8&t=653&hilit=ups) będę również składał mini UPS do Raspberry. Piotr udostępnił [schemat](/Docs/UPS_mini.png) do którego potrzebne są następujące podzespoły:

- 2 lub 3 ogniwa 18650 wraz z koszykiem
- zasilacz sieciowy 5V minimum 3A 
- ładowarka ogniw 18650 np. TP4056
- przetwornica STEP-UP np. SX1308 
- dwie diody np. 1N5822

Piotr - serdeczne dzięki!

##Do zrobienia

Projekt można, a nawet trzeba rozwijać. Do zrobienia jest choćby:

- zebranie ustawień w jednym miejscu (smtp, numery telefonów i adresy e-mail odbiorców)
- interfejs graficzny do zmiany powyższych ustawień oraz przeglądania zdjęć alarmów
- sterowanie programem komendami sms
- dodanie - po sms-ie informacyjnym o alarmie - połączenia z telefonem odbiorcy
- listę uzupełnię o informacje zebrane w [dyskusji na grupie Malinowe Pi na Facebook-u](https://www.facebook.com/groups/malinowepi/permalink/433256330178355/)

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

##Usunięcie plików alarmu

$ sudo rm -rf /home/pi/alarms

##Uruchomienie skryptu Pythona

$ sudo python /home/pi/raptor.app/raptor.app.py

___
Maciej Tokarz © My-Poi!
