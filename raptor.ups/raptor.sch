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
LIBS:raptor
LIBS:raptor-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Raptor UPS"
Date ""
Rev ""
Comp "My-Poi!"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L PWR_FLAG #FLG01
U 1 1 5738DE46
P 2000 2450
F 0 "#FLG01" H 2000 2545 50  0001 C CNN
F 1 "PWR_FLAG" H 2000 2630 50  0000 C CNN
F 2 "" H 2000 2450 50  0000 C CNN
F 3 "" H 2000 2450 50  0000 C CNN
	1    2000 2450
	1    0    0    -1  
$EndComp
$Comp
L PWR_FLAG #FLG02
U 1 1 5738DE5A
P 2600 2450
F 0 "#FLG02" H 2600 2545 50  0001 C CNN
F 1 "PWR_FLAG" H 2600 2630 50  0000 C CNN
F 2 "" H 2600 2450 50  0000 C CNN
F 3 "" H 2600 2450 50  0000 C CNN
	1    2600 2450
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR03
U 1 1 5738DEC0
P 4600 1950
F 0 "#PWR03" H 4600 1800 50  0001 C CNN
F 1 "VCC" H 4600 2100 50  0000 C CNN
F 2 "" H 4600 1950 50  0000 C CNN
F 3 "" H 4600 1950 50  0000 C CNN
	1    4600 1950
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR04
U 1 1 5738DED4
P 4600 3600
F 0 "#PWR04" H 4600 3350 50  0001 C CNN
F 1 "GND" H 4600 3450 50  0000 C CNN
F 2 "" H 4600 3600 50  0000 C CNN
F 3 "" H 4600 3600 50  0000 C CNN
	1    4600 3600
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR05
U 1 1 5738DF09
P 5000 1950
F 0 "#PWR05" H 5000 1800 50  0001 C CNN
F 1 "VCC" H 5000 2100 50  0000 C CNN
F 2 "" H 5000 1950 50  0000 C CNN
F 3 "" H 5000 1950 50  0000 C CNN
	1    5000 1950
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR06
U 1 1 5738DF14
P 8250 1950
F 0 "#PWR06" H 8250 1800 50  0001 C CNN
F 1 "VCC" H 8250 2100 50  0000 C CNN
F 2 "" H 8250 1950 50  0000 C CNN
F 3 "" H 8250 1950 50  0000 C CNN
	1    8250 1950
	1    0    0    -1  
$EndComp
$Comp
L TP4056 P1
U 1 1 5738EA09
P 5600 2900
F 0 "P1" H 5600 3100 60  0000 C CNN
F 1 "TP4056" V 5600 2750 60  0000 C CNN
F 2 "my-poi:TP4056" H 5600 3450 60  0001 C CNN
F 3 "" H 5600 3450 60  0000 C CNN
	1    5600 2900
	1    0    0    -1  
$EndComp
Wire Wire Line
	5000 1950 5000 2600
Wire Wire Line
	5000 2600 5150 2600
$Comp
L GND #PWR07
U 1 1 5738EAC3
P 5000 3600
F 0 "#PWR07" H 5000 3350 50  0001 C CNN
F 1 "GND" H 5000 3450 50  0000 C CNN
F 2 "" H 5000 3600 50  0000 C CNN
F 3 "" H 5000 3600 50  0000 C CNN
	1    5000 3600
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR08
U 1 1 5738EAD2
P 6250 3600
F 0 "#PWR08" H 6250 3350 50  0001 C CNN
F 1 "GND" H 6250 3450 50  0000 C CNN
F 2 "" H 6250 3600 50  0000 C CNN
F 3 "" H 6250 3600 50  0000 C CNN
	1    6250 3600
	1    0    0    -1  
$EndComp
Wire Wire Line
	5150 3200 5000 3200
Wire Wire Line
	6100 3200 6250 3200
$Comp
L Battery BT1
U 1 1 573A1195
P 6850 2900
F 0 "BT1" H 6950 2950 50  0000 L CNN
F 1 "18650" H 6950 2850 50  0000 L CNN
F 2 "my-poi:18650" V 6850 2940 50  0001 C CNN
F 3 "" V 6850 2940 50  0000 C CNN
	1    6850 2900
	1    0    0    -1  
$EndComp
$Comp
L Battery BT2
U 1 1 573A11EC
P 7350 2900
F 0 "BT2" H 7450 2950 50  0000 L CNN
F 1 "18650" H 7450 2850 50  0000 L CNN
F 2 "my-poi:18650" V 7350 2940 50  0001 C CNN
F 3 "" V 7350 2940 50  0000 C CNN
	1    7350 2900
	1    0    0    -1  
$EndComp
Wire Wire Line
	6850 2750 6850 2700
Wire Wire Line
	6350 2700 7350 2700
Wire Wire Line
	6350 2700 6350 2800
Wire Wire Line
	6350 2800 6100 2800
Wire Wire Line
	6100 3000 6350 3000
Wire Wire Line
	6350 3000 6350 3100
Wire Wire Line
	6350 3100 7350 3100
Wire Wire Line
	6850 3100 6850 3050
Wire Wire Line
	7350 2700 7350 2750
Connection ~ 6850 2700
Wire Wire Line
	7350 3100 7350 3050
Connection ~ 6850 3100
$Comp
L D D2
U 1 1 573A14A2
P 7950 2600
F 0 "D2" H 7950 2700 50  0000 C CNN
F 1 "D" H 7950 2500 50  0000 C CNN
F 2 "Diodes_ThroughHole:Diode_DO-201AD_Horizontal_RM15" H 7950 2600 50  0001 C CNN
F 3 "" H 7950 2600 50  0000 C CNN
	1    7950 2600
	-1   0    0    1   
$EndComp
$Comp
L D D1
U 1 1 573A14D3
P 8250 2300
F 0 "D1" H 8250 2400 50  0000 C CNN
F 1 "D" H 8250 2200 50  0000 C CNN
F 2 "Diodes_ThroughHole:Diode_DO-201AD_Horizontal_RM15" H 8250 2300 50  0001 C CNN
F 3 "" H 8250 2300 50  0000 C CNN
	1    8250 2300
	0    -1   -1   0   
$EndComp
Wire Wire Line
	6100 2600 7800 2600
Wire Wire Line
	8100 2600 8400 2600
Wire Wire Line
	8250 2600 8250 2450
Wire Wire Line
	8250 1950 8250 2150
$Comp
L STEP-UP S1
U 1 1 573A18DA
P 8900 2500
F 0 "S1" H 8900 2450 60  0000 C CNN
F 1 "STEP-UP" V 8900 2150 60  0000 C CNN
F 2 "my-poi:STEP-UP" H 8900 2500 60  0001 C CNN
F 3 "" H 8900 2500 60  0000 C CNN
	1    8900 2500
	1    0    0    -1  
$EndComp
Wire Wire Line
	5000 3200 5000 3600
Wire Wire Line
	6250 3200 6250 3600
$Comp
L GND #PWR09
U 1 1 573A2330
P 8250 3600
F 0 "#PWR09" H 8250 3350 50  0001 C CNN
F 1 "GND" H 8250 3450 50  0000 C CNN
F 2 "" H 8250 3600 50  0000 C CNN
F 3 "" H 8250 3600 50  0000 C CNN
	1    8250 3600
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR010
U 1 1 573A2479
P 9550 3600
F 0 "#PWR010" H 9550 3350 50  0001 C CNN
F 1 "GND" H 9550 3450 50  0000 C CNN
F 2 "" H 9550 3600 50  0000 C CNN
F 3 "" H 9550 3600 50  0000 C CNN
	1    9550 3600
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR011
U 1 1 573A254A
P 9950 3600
F 0 "#PWR011" H 9950 3350 50  0001 C CNN
F 1 "GND" H 9950 3450 50  0000 C CNN
F 2 "" H 9950 3600 50  0000 C CNN
F 3 "" H 9950 3600 50  0000 C CNN
	1    9950 3600
	1    0    0    -1  
$EndComp
Connection ~ 8250 2600
Wire Wire Line
	8400 3050 8250 3050
Wire Wire Line
	8250 3050 8250 3600
Wire Wire Line
	9400 3050 9550 3050
Wire Wire Line
	9550 3050 9550 3600
$Comp
L CONN_01X02 P2
U 1 1 573A2AD6
P 10300 2650
F 0 "P2" H 10300 2800 50  0000 C CNN
F 1 "CONN_RPI+HUB" V 10400 2650 50  0000 C CNN
F 2 "Terminal_Blocks:TerminalBlock_Pheonix_PT-3.5mm_2pol" H 10300 2650 50  0001 C CNN
F 3 "" H 10300 2650 50  0000 C CNN
	1    10300 2650
	1    0    0    -1  
$EndComp
Wire Wire Line
	9400 2600 10100 2600
Wire Wire Line
	10100 2700 9950 2700
Wire Wire Line
	9950 2700 9950 3600
$Comp
L Zasilacz Z1
U 1 1 573A5D6C
P 3800 2650
F 0 "Z1" H 3400 2400 60  0000 C CNN
F 1 "Zasilacz" H 3850 2400 60  0000 C CNN
F 2 "my-poi:GPV-20-5" H 3800 2650 60  0001 C CNN
F 3 "" H 3800 2650 60  0000 C CNN
	1    3800 2650
	1    0    0    -1  
$EndComp
Wire Wire Line
	4600 1950 4600 2800
Wire Wire Line
	4600 2800 4450 2800
Wire Wire Line
	4600 3600 4600 3000
Wire Wire Line
	4600 3000 4450 3000
$Comp
L CONN_01X02 P3
U 1 1 573A2ACA
P 1600 2850
F 0 "P3" H 1600 3000 50  0000 C CNN
F 1 "CONN_220V" V 1700 2850 50  0000 C CNN
F 2 "Terminal_Blocks:TerminalBlock_Pheonix_PT-3.5mm_2pol" H 1600 2850 50  0001 C CNN
F 3 "" H 1600 2850 50  0000 C CNN
	1    1600 2850
	-1   0    0    1   
$EndComp
Wire Wire Line
	3000 2800 1800 2800
Wire Wire Line
	2600 2450 2600 2800
Connection ~ 2600 2800
Wire Wire Line
	3000 3000 1800 3000
Wire Wire Line
	1800 3000 1800 2900
Wire Wire Line
	2000 2450 2000 3000
Wire Wire Line
	2000 3000 2050 3000
Connection ~ 2050 3000
$EndSCHEMATC
