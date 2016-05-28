###Udostępniony kod wykorzystujesz na własną odpowiedzialność!

##Realizacja UPS-a do Raptora

Jak wspomniałem w README, dzięki uprzejmości Piotra "pimowo" z forum [nettemp.pl](http://nettemp.pl/forum/viewtopic.php?f=8&t=653&hilit=ups) otrzymałem [schemat](/docs/UPS_mini.png) mini UPS-a.
Aby wykonać zadanie posłużyłem się darmowym programem [KiCad](http://kicad-pcb.org/).
Nie miałem nigdy styczności z tego typu programami oraz mam mgliste pojęcie o elektronice, ale udało się :-)

Utworzenie schematu sprowadza się do przygotowania symboli dla poszczególnych podzespołów (określenia pinów wejść i wyjść) oraz połączenia wszystkich punktów w całość:

![schemat](images/ups/001.jpg)
Schemat

![symbol](images/ups/002.jpg)
Symbol

Trzeba jeszcze wskazać flagi zasilania i wykonać parę dodatkowych operacji np. założyć własną bibliotekę na elementy projektu.
Program KiCad jest spolszczony i dobrze opisany w necie zatem wyszukanie podstawowych zasad pracy z nim nie stanowi problemu.

Aby wykonać płytkę należy opracować (bądź wyszukać w sieci) tzw. footprinty.
Po mojemu są to dokładnie zwymiarowane rzeczywiste podzespoły z rozmieszczonymi na planie takiego footprinta miejscami połączeń (nóżkami) czy otworami montażowymi.

![footprint](images/ups/003.jpg)
Footprint

Mając powyższe opracowane dla wszystkich elementów schematu można przejść do utworzenia płytki.

![pcb](images/ups/004.jpg)
PCB

Footprinty można przesuwać, pady (miejsca połączeń z podzespołami) łączyć ścieżkami, wyznaczać strefy do automatycznego wypełnienia połączeniami czy też dodawać strefy chroniące przed takim wypełnieniem.
W efekcie otrzymamy projekt płytki, który można wydrukować laserowo na papierze kredowym:

![papier kredowy](images/ups/005.jpg)

a następnie żelazkiem (metoda tzw. termotransferu) na płytkę:

![pcb 1](images/ups/006.jpg)

aby po wytrawieniu otrzymać taki efekt:

![pcb 1](images/ups/007.jpg)

Prace nad płytką to szereg czynności jak: wiercenie otworów montażowych (elektroniki, wsporników płytki czy mocowania np. koszyków na ogniwa), lutowanie elementów, podłączanie przewodów zasilających, włącznika itp.

![pcb 1](images/ups/008.jpg)
![pcb 1](images/ups/009.jpg)
![pcb 1](images/ups/010.jpg)
![pcb 1](images/ups/011.jpg)
![pcb 1](images/ups/012.jpg)
![pcb 1](images/ups/013.jpg)
![pcb 1](images/ups/014.jpg)

Nawet mając mgliste pojęcie o elektronice można wykonać takiego UPS-a. Pewnie wiele mu brakuje do świetności np. zabezpieczenia na wejściu 220V, powiększonych średnic niektórych padów do 4 mm itp.

Zawsze można coś zmienić i nie jest powiedziane, że tak się nie stanie. Z czasem mam nadzieję, że przy współpracy z fanami komputerków Raspberry, uda się projekt doszlifować.

Wykaz podzespołów:

* Obudowa Z-40 183x120x76mm czarna
* Ogniwa 18650 2 szt.
* Zasilacz GLP GPV-20-5 (5V 3A)
* Ładowarka ogniw 18650 np. TP4056 z zabezpieczeniem przed nadmiernym rozładowaniem
* Przetwornica STEP-UP np. SX1308 
* Diody np. 1N5822 2 szt.
* Terminal block 2pin 3 szt.

___
Maciej Tokarz © My-Poi!