EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:adapters-cache
LIBS:raptor.adapters-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L CAMERA_CONN_01X15 P1
U 1 1 593486FE
P 600 1300
F 0 "P1" H 798 300 50  0000 C CNN
F 1 "CAMERA_CONN_01X15" V 698 1100 50  0000 C CNN
F 2 "raptor:FFC_connector_15x1.0mm" V 798 1100 50  0000 C CNN
F 3 "" H 798 1100 50  0000 C CNN
	1    600  1300
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X16-RESCUE-adapters P3
U 1 1 593487BA
P 3100 1500
F 0 "P3" V 2300 1700 50  0000 C CNN
F 1 "CONN_01X16-RESCUE-adapters" H 3100 1800 50  0000 C CNN
F 2 "raptor:Przejscie_tasma_druk_2x08x2.54mm" H 3100 1700 50  0000 C CNN
F 3 "" V 3100 1700 50  0000 C CNN
	1    3100 1500
	0    1    1    0   
$EndComp
$Comp
L CONN_01X04-RESCUE-adapters P2
U 1 1 5934886F
P 2750 2650
F 0 "P2" H 2748 2994 50  0000 C CNN
F 1 "CONN_01X04-RESCUE-adapters" V 2854 2689 50  0000 C CNN
F 2 "raptor:Pin_Header_Straight_1x04_Pitch2.54mm" V 2750 2650 50  0000 C CNN
F 3 "" H 2750 2650 50  0000 C CNN
	1    2750 2650
	0    1    1    0   
$EndComp
$Comp
L CONN_01X16-RESCUE-adapters P6
U 1 1 59349525
P 6250 1500
F 0 "P6" V 5450 1700 50  0000 C CNN
F 1 "CONN_01X16-RESCUE-adapters" H 6250 1800 50  0000 C CNN
F 2 "raptor:Przejscie_tasma_druk_2x08x2.54mm" H 6250 1700 50  0000 C CNN
F 3 "" V 6250 1700 50  0000 C CNN
	1    6250 1500
	0    1    1    0   
$EndComp
$Comp
L CONN_01X04-RESCUE-adapters P5
U 1 1 5934952B
P 5900 2650
F 0 "P5" H 5898 2994 50  0000 C CNN
F 1 "CONN_01X04-RESCUE-adapters" V 6004 2689 50  0000 C CNN
F 2 "raptor:Pin_Header_Straight_1x04_Pitch2.54mm" V 5900 2650 50  0000 C CNN
F 3 "" H 5900 2650 50  0000 C CNN
	1    5900 2650
	0    1    1    0   
$EndComp
$Comp
L CAMERA_CONN_01X15_LEFT P4
U 1 1 59349C0E
P 3700 1300
F 0 "P4" H 3898 300 50  0000 C CNN
F 1 "CAMERA_CONN_01X15_LEFT" V 3798 1100 50  0000 C CNN
F 2 "raptor:FFC_connector_15x1.0mm_LEFT" V 3898 1100 50  0000 C CNN
F 3 "" H 3898 1100 50  0000 C CNN
	1    3700 1300
	1    0    0    -1  
$EndComp
Wire Wire Line
	2950 2450 2950 2300
Wire Wire Line
	2950 2300 3100 2300
Wire Wire Line
	2850 2450 2850 2100
Wire Wire Line
	2850 2100 3100 2100
Wire Wire Line
	2750 2450 2750 1900
Wire Wire Line
	2750 1900 3100 1900
Wire Wire Line
	2650 2450 2650 1700
Wire Wire Line
	2650 1700 3100 1700
Wire Wire Line
	1000 2200 3100 2200
Wire Wire Line
	1100 1300 1100 2200
Wire Wire Line
	1100 1900 1000 1900
Connection ~ 1100 2200
Wire Wire Line
	1100 1600 1000 1600
Connection ~ 1100 1900
Wire Wire Line
	1100 1300 1000 1300
Connection ~ 1100 1600
Wire Wire Line
	1000 2100 2550 2100
Wire Wire Line
	2550 2100 2550 2000
Wire Wire Line
	2550 2000 3100 2000
Wire Wire Line
	1000 2000 2450 2000
Wire Wire Line
	2450 2000 2450 1800
Wire Wire Line
	2450 1800 3100 1800
Wire Wire Line
	1000 1800 2350 1800
Wire Wire Line
	2350 1800 2350 1600
Wire Wire Line
	2350 1600 3100 1600
Wire Wire Line
	1000 1700 2250 1700
Wire Wire Line
	2250 1700 2250 1400
Wire Wire Line
	2250 1400 3100 1400
Wire Wire Line
	1000 1500 2150 1500
Wire Wire Line
	2150 1500 2150 1200
Wire Wire Line
	2150 1200 3100 1200
Wire Wire Line
	1000 1400 2050 1400
Wire Wire Line
	2050 1400 2050 1000
Wire Wire Line
	2050 1000 3100 1000
Wire Wire Line
	1000 1200 1950 1200
Wire Wire Line
	1950 1200 1950 800 
Wire Wire Line
	1950 800  3100 800 
Wire Wire Line
	1000 800  2350 800 
Wire Wire Line
	2350 800  2350 1500
Wire Wire Line
	2350 1500 3100 1500
Wire Wire Line
	1000 900  2450 900 
Wire Wire Line
	2450 900  2450 1300
Wire Wire Line
	2450 1300 3100 1300
Wire Wire Line
	1000 1000 2550 1000
Wire Wire Line
	2550 1000 2550 1100
Wire Wire Line
	2550 1100 3100 1100
Wire Wire Line
	1000 1100 2650 1100
Wire Wire Line
	2650 1100 2650 900 
Wire Wire Line
	2650 900  3100 900 
Wire Wire Line
	6100 2450 6100 2300
Wire Wire Line
	6100 2300 6250 2300
Wire Wire Line
	6000 2450 6000 2100
Wire Wire Line
	6000 2100 6250 2100
Wire Wire Line
	5900 2450 5900 1900
Wire Wire Line
	5900 1900 6250 1900
Wire Wire Line
	5800 2450 5800 1700
Wire Wire Line
	5800 1700 6250 1700
Wire Wire Line
	6250 2200 5700 2200
Wire Wire Line
	5700 2200 5700 800 
Wire Wire Line
	5700 800  4100 800 
Wire Wire Line
	4200 800  4200 1700
Wire Wire Line
	4200 1100 4100 1100
Connection ~ 4200 800 
Wire Wire Line
	4200 1400 4100 1400
Connection ~ 4200 1100
Wire Wire Line
	4200 1700 4100 1700
Connection ~ 4200 1400
Wire Wire Line
	6250 2000 5600 2000
Wire Wire Line
	5600 2000 5600 900 
Wire Wire Line
	5600 900  4100 900 
Wire Wire Line
	6250 1800 5500 1800
Wire Wire Line
	5500 1800 5500 1000
Wire Wire Line
	5500 1000 4100 1000
Wire Wire Line
	6250 1600 5400 1600
Wire Wire Line
	5400 1600 5400 1200
Wire Wire Line
	5400 1200 4100 1200
Wire Wire Line
	4100 1300 5300 1300
Wire Wire Line
	5300 1300 5300 1400
Wire Wire Line
	5300 1400 6250 1400
Wire Wire Line
	6250 1200 5200 1200
Wire Wire Line
	5200 1200 5200 1500
Wire Wire Line
	5200 1500 4100 1500
Wire Wire Line
	6250 1000 5100 1000
Wire Wire Line
	5100 1000 5100 1600
Wire Wire Line
	5100 1600 4100 1600
Wire Wire Line
	6250 800  5000 800 
Wire Wire Line
	5000 800  5000 1800
Wire Wire Line
	5000 1800 4100 1800
Wire Wire Line
	6250 900  4900 900 
Wire Wire Line
	4900 900  4900 1900
Wire Wire Line
	4900 1900 4100 1900
Wire Wire Line
	6250 1100 4800 1100
Wire Wire Line
	4800 1100 4800 2000
Wire Wire Line
	4800 2000 4100 2000
Wire Wire Line
	6250 1300 4700 1300
Wire Wire Line
	4700 1300 4700 2100
Wire Wire Line
	4700 2100 4100 2100
Wire Wire Line
	6250 1500 4600 1500
Wire Wire Line
	4600 1500 4600 2200
Wire Wire Line
	4600 2200 4100 2200
$Comp
L CONN_01X16-RESCUE-adapters P9
U 1 1 5934AA48
P 9550 1500
F 0 "P9" V 8750 1700 50  0000 C CNN
F 1 "CONN_01X16-RESCUE-adapters" H 9550 1800 50  0000 C CNN
F 2 "raptor:Przejscie_tasma_druk_2x08x2.54mm" H 9550 1700 50  0000 C CNN
F 3 "" V 9550 1700 50  0000 C CNN
	1    9550 1500
	0    1    1    0   
$EndComp
$Comp
L CONN_01X04-RESCUE-adapters P8
U 1 1 5934AA4E
P 9200 2650
F 0 "P8" H 9198 2994 50  0000 C CNN
F 1 "CONN_01X04-RESCUE-adapters" V 9304 2689 50  0000 C CNN
F 2 "raptor:Pin_Header_Straight_1x04_Pitch2.54mm" V 9200 2650 50  0000 C CNN
F 3 "" H 9200 2650 50  0000 C CNN
	1    9200 2650
	0    1    1    0   
$EndComp
$Comp
L CAMERA_CONN_01X15_LEFT P7
U 1 1 5934AA54
P 7000 1300
F 0 "P7" H 7198 300 50  0000 C CNN
F 1 "CAMERA_CONN_01X15_LEFT" V 7098 1100 50  0000 C CNN
F 2 "raptor:FFC_connector_15x1.0mm_LEFT" V 7198 1100 50  0000 C CNN
F 3 "" H 7198 1100 50  0000 C CNN
	1    7000 1300
	1    0    0    -1  
$EndComp
Wire Wire Line
	9400 2450 9400 2300
Wire Wire Line
	9400 2300 9550 2300
Wire Wire Line
	9300 2450 9300 2100
Wire Wire Line
	9300 2100 9550 2100
Wire Wire Line
	9200 2450 9200 1900
Wire Wire Line
	9200 1900 9550 1900
Wire Wire Line
	9100 2450 9100 1700
Wire Wire Line
	9100 1700 9550 1700
Wire Wire Line
	9550 2200 9000 2200
Wire Wire Line
	9000 2200 9000 800 
Wire Wire Line
	9000 800  7400 800 
Wire Wire Line
	7500 800  7500 1700
Wire Wire Line
	7500 1100 7400 1100
Connection ~ 7500 800 
Wire Wire Line
	7500 1400 7400 1400
Connection ~ 7500 1100
Wire Wire Line
	7500 1700 7400 1700
Connection ~ 7500 1400
Wire Wire Line
	9550 2000 8900 2000
Wire Wire Line
	8900 2000 8900 900 
Wire Wire Line
	8900 900  7400 900 
Wire Wire Line
	9550 1800 8800 1800
Wire Wire Line
	8800 1800 8800 1000
Wire Wire Line
	8800 1000 7400 1000
Wire Wire Line
	9550 1600 8700 1600
Wire Wire Line
	8700 1600 8700 1200
Wire Wire Line
	8700 1200 7400 1200
Wire Wire Line
	7400 1300 8600 1300
Wire Wire Line
	8600 1300 8600 1400
Wire Wire Line
	8600 1400 9550 1400
Wire Wire Line
	9550 1200 8500 1200
Wire Wire Line
	8500 1200 8500 1500
Wire Wire Line
	8500 1500 7400 1500
Wire Wire Line
	9550 1000 8400 1000
Wire Wire Line
	8400 1000 8400 1600
Wire Wire Line
	8400 1600 7400 1600
Wire Wire Line
	9550 800  8300 800 
Wire Wire Line
	8300 800  8300 1800
Wire Wire Line
	8300 1800 7400 1800
Wire Wire Line
	9550 900  8200 900 
Wire Wire Line
	8200 900  8200 1900
Wire Wire Line
	8200 1900 7400 1900
Wire Wire Line
	9550 1100 8100 1100
Wire Wire Line
	8100 1100 8100 2000
Wire Wire Line
	8100 2000 7400 2000
Wire Wire Line
	9550 1300 8000 1300
Wire Wire Line
	8000 1300 8000 2100
Wire Wire Line
	8000 2100 7400 2100
Wire Wire Line
	9550 1500 7900 1500
Wire Wire Line
	7900 1500 7900 2200
Wire Wire Line
	7900 2200 7400 2200
$EndSCHEMATC
