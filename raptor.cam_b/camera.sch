EESchema Schematic File Version 2
LIBS:camera-cache
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
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Raptor"
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L CONN_01X05 P2
U 1 1 58DDF822
P 7300 3200
F 0 "P2" H 7300 3500 50  0000 C CNN
F 1 "CONN_01X05" V 7400 3200 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x05_Pitch2.54mm" H 7300 3200 50  0000 C CNN
F 3 "" H 7300 3200 50  0000 C CNN
	1    7300 3200
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X15 P1
U 1 1 58DDF909
P 5900 4300
F 0 "P1" V 5200 4100 50  0000 C CNN
F 1 "CONN_01X15" H 6000 4000 50  0000 C CNN
F 2 "objects:FFC_connector_15x1.0mm" V 6000 4100 50  0000 C CNN
F 3 "" V 6000 4100 50  0000 C CNN
	1    5900 4300
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X16 P3
U 1 1 58DE03D8
P 6000 2700
F 0 "P3" V 5200 2900 50  0000 C CNN
F 1 "CONN_01X16" H 6000 3000 50  0000 C CNN
F 2 "Connectors_Multicomp:Multicomp_MC9A12-1634_2x08x2.54mm_Straight" V 6000 2900 50  0000 C CNN
F 3 "" V 6000 2900 50  0000 C CNN
	1    6000 2700
	1    0    0    -1  
$EndComp
Wire Wire Line
	5300 4300 5300 2700
Wire Wire Line
	5400 4300 5400 2700
Wire Wire Line
	5500 4300 5500 2700
Wire Wire Line
	5600 4300 5600 2700
Wire Wire Line
	5700 4300 5700 2700
Wire Wire Line
	5900 4300 5900 4200
Wire Wire Line
	5900 4200 5800 4200
Wire Wire Line
	5800 4200 5800 2700
Wire Wire Line
	6000 4300 6000 4100
Wire Wire Line
	6000 4100 5900 4100
Wire Wire Line
	5900 4100 5900 2700
Wire Wire Line
	6200 4300 6200 4000
Wire Wire Line
	6200 4000 6000 4000
Wire Wire Line
	6000 4000 6000 2700
Wire Wire Line
	6300 4300 6300 3900
Wire Wire Line
	6300 3900 6100 3900
Wire Wire Line
	6100 3900 6100 2700
Wire Wire Line
	6500 4300 6500 3800
Wire Wire Line
	6500 3800 6200 3800
Wire Wire Line
	6200 3800 6200 2700
Wire Wire Line
	6600 4300 6600 3700
Wire Wire Line
	6600 3700 6300 3700
Wire Wire Line
	6300 3700 6300 2700
Wire Wire Line
	6400 2700 6400 3400
Wire Wire Line
	6400 3400 7100 3400
Wire Wire Line
	6500 2700 6500 3300
Wire Wire Line
	6500 3300 7100 3300
Wire Wire Line
	6600 2700 6600 3200
Wire Wire Line
	6600 3200 7100 3200
Wire Wire Line
	6700 2700 6700 3100
Wire Wire Line
	6700 3100 7100 3100
Wire Wire Line
	6800 2700 6800 3000
Wire Wire Line
	6800 3000 7100 3000
$EndSCHEMATC
