from skidl import Pin, Part, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

dsp = SchLib(tool=SKIDL).add_parts(*[
        Part(name='DSP96002',dest=TEMPLATE,tool=SKIDL,keywords='DSP 32bit Dual Port Processor',description='32-bit General Purpose Floating-point DSP, Dual Port, PGA-223',ref_prefix='U',num_units=1,fplist=['PGA-223*'],do_erc=True,pins=[
            Pin(num='A1',name='B.A23',func=Pin.TRISTATE,do_erc=True),
            Pin(num='B1',name='B.A20',func=Pin.TRISTATE,do_erc=True),
            Pin(num='C1',name='B.A17',func=Pin.TRISTATE,do_erc=True),
            Pin(num='D1',name='B.A15',func=Pin.TRISTATE,do_erc=True),
            Pin(num='E1',name='B.A13',func=Pin.TRISTATE,do_erc=True),
            Pin(num='F1',name='B.A12',func=Pin.TRISTATE,do_erc=True),
            Pin(num='G1',name='B.A9',func=Pin.TRISTATE,do_erc=True),
            Pin(num='H1',name='B.A8',func=Pin.TRISTATE,do_erc=True),
            Pin(num='J1',name='A.TACK',do_erc=True),
            Pin(num='K1',name='B.A4',func=Pin.TRISTATE,do_erc=True),
            Pin(num='L1',name='B.A3',func=Pin.TRISTATE,do_erc=True),
            Pin(num='M1',name='B.A0',func=Pin.TRISTATE,do_erc=True),
            Pin(num='N1',name='B.AENB',do_erc=True),
            Pin(num='P1',name='B.R/W',func=Pin.TRISTATE,do_erc=True),
            Pin(num='R1',name='B.BUS_STR',func=Pin.OUTPUT,do_erc=True),
            Pin(num='T1',name='B.BG',do_erc=True),
            Pin(num='U1',name='B.HOSTREQ',func=Pin.OUTPUT,do_erc=True),
            Pin(num='V1',name='DSO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='A2',name='B.A27',func=Pin.TRISTATE,do_erc=True),
            Pin(num='B2',name='B.A25',func=Pin.TRISTATE,do_erc=True),
            Pin(num='C2',name='B.A21',func=Pin.TRISTATE,do_erc=True),
            Pin(num='D2',name='B.A18',func=Pin.TRISTATE,do_erc=True),
            Pin(num='E2',name='B.A16',func=Pin.TRISTATE,do_erc=True),
            Pin(num='F2',name='B.A14',func=Pin.TRISTATE,do_erc=True),
            Pin(num='G2',name='B.A10',func=Pin.TRISTATE,do_erc=True),
            Pin(num='H2',name='CLK',do_erc=True),
            Pin(num='J2',name='B.TACK',do_erc=True),
            Pin(num='K2',name='B.A5',func=Pin.TRISTATE,do_erc=True),
            Pin(num='L2',name='B.A1',func=Pin.TRISTATE,do_erc=True),
            Pin(num='M2',name='B.S1',func=Pin.TRISTATE,do_erc=True),
            Pin(num='P2',name='B.T_STROBE',func=Pin.TRISTATE,do_erc=True),
            Pin(num='R2',name='B.BR',func=Pin.OUTPUT,do_erc=True),
            Pin(num='T2',name='B.BA',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='U2',name='DSCK/OS1',func=Pin.BIDIR,do_erc=True),
            Pin(num='V2',name='DSI/OS0',func=Pin.BIDIR,do_erc=True),
            Pin(num='A3',name='B.A29',func=Pin.TRISTATE,do_erc=True),
            Pin(num='B3',name='B.A28',func=Pin.TRISTATE,do_erc=True),
            Pin(num='C3',name='B.A26',func=Pin.TRISTATE,do_erc=True),
            Pin(num='D3',name='B.A24',func=Pin.TRISTATE,do_erc=True),
            Pin(num='E3',name='B.A22',func=Pin.TRISTATE,do_erc=True),
            Pin(num='F3',name='B.A19',func=Pin.TRISTATE,do_erc=True),
            Pin(num='G3',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='H3',name='B.A11',func=Pin.TRISTATE,do_erc=True),
            Pin(num='J3',name='B.A7',func=Pin.TRISTATE,do_erc=True),
            Pin(num='K3',name='B.A6',func=Pin.TRISTATE,do_erc=True),
            Pin(num='L3',name='B.A2',func=Pin.TRISTATE,do_erc=True),
            Pin(num='M3',name='B.S0',func=Pin.TRISTATE,do_erc=True),
            Pin(num='P3',name='B.BUS_LOCK',func=Pin.OUTPUT,do_erc=True),
            Pin(num='R3',name='B.BB',do_erc=True),
            Pin(num='T3',name='A.HOSTREQ',func=Pin.OUTPUT,do_erc=True),
            Pin(num='V3',name='B.HOSTACK',do_erc=True),
            Pin(num='A4',name='B.A31',func=Pin.TRISTATE,do_erc=True),
            Pin(num='B4',name='B.A30',func=Pin.TRISTATE,do_erc=True),
            Pin(num='C4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='E4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='F4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='G4',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='H4',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='J4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='K4',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='L4',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='M4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='N4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='P4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='R4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='T4',name='DEBUGREQ',do_erc=True),
            Pin(num='U4',name='A.HOSTACK',do_erc=True),
            Pin(num='V4',name='B.HOSTSEL',do_erc=True),
            Pin(num='A5',name='MODA/IRQA',do_erc=True),
            Pin(num='B5',name='MODB/IRQB',do_erc=True),
            Pin(num='C5',name='MODC/IRQC',do_erc=True),
            Pin(num='D5',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='R5',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='T5',name='A.HOSTSEL',do_erc=True),
            Pin(num='U5',name='B.DENB',do_erc=True),
            Pin(num='V5',name='B.D30',func=Pin.TRISTATE,do_erc=True),
            Pin(num='A6',name='A.BB',do_erc=True),
            Pin(num='B6',name='A.BG',do_erc=True),
            Pin(num='C6',name='RESET',do_erc=True),
            Pin(num='D6',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='R6',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='T6',name='B.D31',func=Pin.TRISTATE,do_erc=True),
            Pin(num='U6',name='B.D29',func=Pin.TRISTATE,do_erc=True),
            Pin(num='V6',name='B.D28',func=Pin.TRISTATE,do_erc=True),
            Pin(num='A7',name='A.BR',func=Pin.OUTPUT,do_erc=True),
            Pin(num='B7',name='A.BA',func=Pin.OPENCOLL,do_erc=True),
            Pin(num='C7',name='A.BUS_LOCK',func=Pin.OUTPUT,do_erc=True),
            Pin(num='D7',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='R7',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='T7',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='U7',name='B.D27',func=Pin.TRISTATE,do_erc=True),
            Pin(num='V7',name='B.D25',func=Pin.TRISTATE,do_erc=True),
            Pin(num='B8',name='B.T_TYPE',func=Pin.OUTPUT,do_erc=True),
            Pin(num='C8',name='A.T_TYPE',func=Pin.OUTPUT,do_erc=True),
            Pin(num='D8',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='R8',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='T8',name='B.D26',func=Pin.TRISTATE,do_erc=True),
            Pin(num='U8',name='B.D24',func=Pin.TRISTATE,do_erc=True),
            Pin(num='V8',name='B.D23',func=Pin.TRISTATE,do_erc=True),
            Pin(num='A9',name='A.R/W',func=Pin.TRISTATE,do_erc=True),
            Pin(num='B9',name='A.S1',func=Pin.TRISTATE,do_erc=True),
            Pin(num='D9',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='R9',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='T9',name='B.D22',func=Pin.TRISTATE,do_erc=True),
            Pin(num='U9',name='B.D21',func=Pin.TRISTATE,do_erc=True),
            Pin(num='V9',name='B.D20',func=Pin.TRISTATE,do_erc=True),
            Pin(num='A10',name='A.S0',func=Pin.TRISTATE,do_erc=True),
            Pin(num='B10',name='A.BUS_STR',func=Pin.OUTPUT,do_erc=True),
            Pin(num='C10',name='A.A1',func=Pin.TRISTATE,do_erc=True),
            Pin(num='D10',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='R10',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='T10',name='B.D17',func=Pin.TRISTATE,do_erc=True),
            Pin(num='U10',name='B.D18',func=Pin.TRISTATE,do_erc=True),
            Pin(num='V10',name='B.D19',func=Pin.TRISTATE,do_erc=True),
            Pin(num='A11',name='A.T_STROBE',func=Pin.TRISTATE,do_erc=True),
            Pin(num='B11',name='A.A0',func=Pin.TRISTATE,do_erc=True),
            Pin(num='C11',name='A.A5',func=Pin.TRISTATE,do_erc=True),
            Pin(num='D11',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='R11',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='T11',name='B.D14',func=Pin.TRISTATE,do_erc=True),
            Pin(num='U11',name='B.D15',func=Pin.TRISTATE,do_erc=True),
            Pin(num='V11',name='B.D16',func=Pin.TRISTATE,do_erc=True),
            Pin(num='A12',name='A.AENB',do_erc=True),
            Pin(num='B12',name='A.A3',func=Pin.TRISTATE,do_erc=True),
            Pin(num='C12',name='A.A8',func=Pin.TRISTATE,do_erc=True),
            Pin(num='D12',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='R12',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='T12',name='B.D11',func=Pin.TRISTATE,do_erc=True),
            Pin(num='U12',name='B.D12',func=Pin.TRISTATE,do_erc=True),
            Pin(num='V12',name='B.D13',func=Pin.TRISTATE,do_erc=True),
            Pin(num='A13',name='A.A2',func=Pin.TRISTATE,do_erc=True),
            Pin(num='B13',name='A.A6',func=Pin.TRISTATE,do_erc=True),
            Pin(num='C13',name='A.A12',func=Pin.TRISTATE,do_erc=True),
            Pin(num='D13',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='R13',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='T13',name='B.D7',func=Pin.TRISTATE,do_erc=True),
            Pin(num='U13',name='B.D9',func=Pin.TRISTATE,do_erc=True),
            Pin(num='V13',name='B.D10',func=Pin.TRISTATE,do_erc=True),
            Pin(num='A14',name='A.A4',func=Pin.TRISTATE,do_erc=True),
            Pin(num='B14',name='A.A9',func=Pin.TRISTATE,do_erc=True),
            Pin(num='C14',name='A.A15',func=Pin.TRISTATE,do_erc=True),
            Pin(num='D14',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='R14',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='T14',name='B.D4',func=Pin.TRISTATE,do_erc=True),
            Pin(num='U14',name='B.D6',func=Pin.TRISTATE,do_erc=True),
            Pin(num='V14',name='B.D8',func=Pin.TRISTATE,do_erc=True),
            Pin(num='A15',name='A.A7',func=Pin.TRISTATE,do_erc=True),
            Pin(num='B15',name='A.A11',func=Pin.TRISTATE,do_erc=True),
            Pin(num='C15',name='A.A17',func=Pin.TRISTATE,do_erc=True),
            Pin(num='D15',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='E15',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='F15',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='G15',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='H15',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='J15',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='K15',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='L15',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='M15',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='N15',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='P15',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='R15',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='T15',name='B.D1',func=Pin.TRISTATE,do_erc=True),
            Pin(num='U15',name='B.D3',func=Pin.TRISTATE,do_erc=True),
            Pin(num='V15',name='B.D5',func=Pin.TRISTATE,do_erc=True),
            Pin(num='A16',name='A.A10',func=Pin.TRISTATE,do_erc=True),
            Pin(num='B16',name='A.A14',func=Pin.TRISTATE,do_erc=True),
            Pin(num='C16',name='A.A19',func=Pin.TRISTATE,do_erc=True),
            Pin(num='D16',name='A.A22',func=Pin.TRISTATE,do_erc=True),
            Pin(num='E16',name='A.A24',func=Pin.TRISTATE,do_erc=True),
            Pin(num='F16',name='A.A27',func=Pin.TRISTATE,do_erc=True),
            Pin(num='G16',name='A.A31',func=Pin.TRISTATE,do_erc=True),
            Pin(num='H16',name='A.D28',func=Pin.TRISTATE,do_erc=True),
            Pin(num='J16',name='A.D24',func=Pin.TRISTATE,do_erc=True),
            Pin(num='K16',name='A.D20',func=Pin.TRISTATE,do_erc=True),
            Pin(num='L16',name='A.D16',func=Pin.TRISTATE,do_erc=True),
            Pin(num='M16',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='N16',name='A.D11',func=Pin.TRISTATE,do_erc=True),
            Pin(num='P16',name='A.D7',func=Pin.TRISTATE,do_erc=True),
            Pin(num='R16',name='A.D5',func=Pin.TRISTATE,do_erc=True),
            Pin(num='T16',name='A.D2',func=Pin.TRISTATE,do_erc=True),
            Pin(num='U16',name='B.D0',func=Pin.TRISTATE,do_erc=True),
            Pin(num='V16',name='B.D2',func=Pin.TRISTATE,do_erc=True),
            Pin(num='A17',name='A.A13',func=Pin.TRISTATE,do_erc=True),
            Pin(num='B17',name='A.A18',func=Pin.TRISTATE,do_erc=True),
            Pin(num='C17',name='A.A21',func=Pin.TRISTATE,do_erc=True),
            Pin(num='D17',name='A.A25',func=Pin.TRISTATE,do_erc=True),
            Pin(num='E17',name='A.A28',func=Pin.TRISTATE,do_erc=True),
            Pin(num='F17',name='A.A30',func=Pin.TRISTATE,do_erc=True),
            Pin(num='G17',name='A.D30',func=Pin.TRISTATE,do_erc=True),
            Pin(num='H17',name='A.D27',func=Pin.TRISTATE,do_erc=True),
            Pin(num='J17',name='A.D25',func=Pin.TRISTATE,do_erc=True),
            Pin(num='K17',name='A.D21',func=Pin.TRISTATE,do_erc=True),
            Pin(num='L17',name='A.D18',func=Pin.TRISTATE,do_erc=True),
            Pin(num='M17',name='A.DENB',do_erc=True),
            Pin(num='N17',name='A.D14',func=Pin.TRISTATE,do_erc=True),
            Pin(num='P17',name='A.D12',func=Pin.TRISTATE,do_erc=True),
            Pin(num='R17',name='A.D9',func=Pin.TRISTATE,do_erc=True),
            Pin(num='T17',name='A.D6',func=Pin.TRISTATE,do_erc=True),
            Pin(num='U17',name='A.D3',func=Pin.TRISTATE,do_erc=True),
            Pin(num='V17',name='A.D0',func=Pin.TRISTATE,do_erc=True),
            Pin(num='A18',name='A.A16',func=Pin.TRISTATE,do_erc=True),
            Pin(num='B18',name='A.A20',func=Pin.TRISTATE,do_erc=True),
            Pin(num='C18',name='A.A23',func=Pin.TRISTATE,do_erc=True),
            Pin(num='D18',name='A.A26',func=Pin.TRISTATE,do_erc=True),
            Pin(num='E18',name='A.A29',func=Pin.TRISTATE,do_erc=True),
            Pin(num='F18',name='A.D31',func=Pin.TRISTATE,do_erc=True),
            Pin(num='G18',name='A.D29',func=Pin.TRISTATE,do_erc=True),
            Pin(num='H18',name='A.D26',func=Pin.TRISTATE,do_erc=True),
            Pin(num='J18',name='A.D23',func=Pin.TRISTATE,do_erc=True),
            Pin(num='K18',name='A.D22',func=Pin.TRISTATE,do_erc=True),
            Pin(num='L18',name='A.D19',func=Pin.TRISTATE,do_erc=True),
            Pin(num='M18',name='A.D17',func=Pin.TRISTATE,do_erc=True),
            Pin(num='N18',name='A.D15',func=Pin.TRISTATE,do_erc=True),
            Pin(num='P18',name='A.D13',func=Pin.TRISTATE,do_erc=True),
            Pin(num='R18',name='A.D10',func=Pin.TRISTATE,do_erc=True),
            Pin(num='T18',name='A.D8',func=Pin.TRISTATE,do_erc=True),
            Pin(num='U18',name='A.D4',func=Pin.TRISTATE,do_erc=True),
            Pin(num='V18',name='A.D1',func=Pin.TRISTATE,do_erc=True)]),
        Part(name='TMS320LF2406PZ',dest=TEMPLATE,tool=SKIDL,keywords='16BIT DSP TMS320 Obsolete',description='16bit DSP Controller 32Kx16B Flash 2.5Kx16B RAM, Obsolete NRND, PQFP-100',ref_prefix='U',num_units=1,fplist=['PQFP-100*'],do_erc=True,pins=[
            Pin(num='1',name='TRST',do_erc=True),
            Pin(num='2',name='TDIRB/IOPF4',func=Pin.BIDIR,do_erc=True),
            Pin(num='3',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='T4PWM/T4CMP/IOPF3',func=Pin.BIDIR,do_erc=True),
            Pin(num='6',name='PDPINTA',do_erc=True),
            Pin(num='7',name='T3PWM/T3CMP/IOPF2',func=Pin.BIDIR,do_erc=True),
            Pin(num='8',name='PLLF2',func=Pin.PASSIVE,do_erc=True),
            Pin(num='9',name='PLLF',func=Pin.PASSIVE,do_erc=True),
            Pin(num='10',name='PLLVcca',func=Pin.PASSIVE,do_erc=True),
            Pin(num='20',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='30',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='40',name='VccPROG_5V',func=Pin.PASSIVE,do_erc=True),
            Pin(num='50',name='CANTX/IOPC6',func=Pin.BIDIR,do_erc=True),
            Pin(num='60',name='CAP4/QEP3/IOPE7',func=Pin.BIDIR,do_erc=True),
            Pin(num='70',name='ADCIN04',do_erc=True),
            Pin(num='80',name='ADCIN08',do_erc=True),
            Pin(num='90',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='11',name='TDIRA/IOPB6',func=Pin.BIDIR,do_erc=True),
            Pin(num='21',name='SPI_SIMO/IOPC2',func=Pin.BIDIR,do_erc=True),
            Pin(num='31',name='PWM5/IOPB2',func=Pin.BIDIR,do_erc=True),
            Pin(num='41',name='PWM9/IOPE3',func=Pin.BIDIR,do_erc=True),
            Pin(num='51',name='CLKOUT/IOPE0',func=Pin.BIDIR,do_erc=True),
            Pin(num='61',name='EMU0',func=Pin.BIDIR,do_erc=True),
            Pin(num='71',name='ADCIN13',do_erc=True),
            Pin(num='81',name='VrefLO',func=Pin.PASSIVE,do_erc=True),
            Pin(num='91',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='12',name='T1PWM/T1CMP/IOPB4',func=Pin.BIDIR,do_erc=True),
            Pin(num='22',name='SPI_SOMI/IOPC3',func=Pin.BIDIR,do_erc=True),
            Pin(num='32',name='PWM11/IOPE5',func=Pin.BIDIR,do_erc=True),
            Pin(num='52',name='CAP3/IOPA5',func=Pin.BIDIR,do_erc=True),
            Pin(num='62',name='EMU1/OFF-',func=Pin.BIDIR,do_erc=True),
            Pin(num='72',name='ADCIN03',do_erc=True),
            Pin(num='82',name='VrefHI',func=Pin.PASSIVE,do_erc=True),
            Pin(num='92',name='IOPF6',func=Pin.BIDIR,do_erc=True),
            Pin(num='13',name='T2PWM/T2CMP/IOPB5',func=Pin.BIDIR,do_erc=True),
            Pin(num='23',name='SPI_TE-/IOPC5',func=Pin.BIDIR,do_erc=True),
            Pin(num='33',name='PWM4/IOPB1',func=Pin.BIDIR,do_erc=True),
            Pin(num='43',name='PWM8/IOPE2',func=Pin.BIDIR,do_erc=True),
            Pin(num='53',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='63',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='73',name='ADCIN12',do_erc=True),
            Pin(num='83',name='VCCA',func=Pin.PWRIN,do_erc=True),
            Pin(num='93',name='RESET',do_erc=True),
            Pin(num='14',name='IOPC0',func=Pin.BIDIR,do_erc=True),
            Pin(num='24',name='SPI_CLK/IOPC4',func=Pin.BIDIR,do_erc=True),
            Pin(num='34',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='54',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='64',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='74',name='ADCIN02',do_erc=True),
            Pin(num='84',name='VSSA',func=Pin.PWRIN,do_erc=True),
            Pin(num='94',name='TCK',do_erc=True),
            Pin(num='15',name='XINT2/IOPD0',func=Pin.BIDIR,do_erc=True),
            Pin(num='25',name='TMS2',do_erc=True),
            Pin(num='35',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='45',name='PWM7/IOPE1',func=Pin.BIDIR,do_erc=True),
            Pin(num='55',name='CAP2/QEP2/IOPA4',func=Pin.BIDIR,do_erc=True),
            Pin(num='65',name='ADCIN15',do_erc=True),
            Pin(num='75',name='ADCIN11',do_erc=True),
            Pin(num='85',name='BIO-/IOPC1',func=Pin.BIDIR,do_erc=True),
            Pin(num='95',name='PDPINTB',do_erc=True),
            Pin(num='16',name='XINT1/IOPA2',func=Pin.BIDIR,do_erc=True),
            Pin(num='26',name='TCLKINA/IOPB7',func=Pin.PASSIVE,do_erc=True),
            Pin(num='36',name='PWM3/IOPB0',func=Pin.BIDIR,do_erc=True),
            Pin(num='46',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='56',name='CAP5/QEP4/IOPF0',func=Pin.PASSIVE,do_erc=True),
            Pin(num='66',name='ADCIN07',do_erc=True),
            Pin(num='76',name='ADCIN10',do_erc=True),
            Pin(num='86',name='~BOOT_EN~/XF',func=Pin.OUTPUT,do_erc=True),
            Pin(num='96',name='TDI',do_erc=True),
            Pin(num='17',name='TXD/IOPA0',func=Pin.BIDIR,do_erc=True),
            Pin(num='27',name='PWM12/IOPE6',func=Pin.BIDIR,do_erc=True),
            Pin(num='37',name='PWM2/IOPA7',func=Pin.BIDIR,do_erc=True),
            Pin(num='47',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='57',name='CAP1/QEP1/IOPA3',func=Pin.BIDIR,do_erc=True),
            Pin(num='67',name='ADCIN06',do_erc=True),
            Pin(num='77',name='ADCIN01',do_erc=True),
            Pin(num='87',name='XTAL/CLKIN',do_erc=True),
            Pin(num='97',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='18',name='RXD/IOPA1',func=Pin.BIDIR,do_erc=True),
            Pin(num='28',name='PWM6/IOPB3',func=Pin.BIDIR,do_erc=True),
            Pin(num='38',name='PWM10/IOPE4',func=Pin.BIDIR,do_erc=True),
            Pin(num='48',name='CAP6/IOPF1',func=Pin.BIDIR,do_erc=True),
            Pin(num='58',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='68',name='ADCIN14',do_erc=True),
            Pin(num='78',name='ADCIN09',do_erc=True),
            Pin(num='88',name='XTAL2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='98',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='19',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='29',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='39',name='PWM1/IOPA6',func=Pin.BIDIR,do_erc=True),
            Pin(num='49',name='CANRX/IOPC7',func=Pin.BIDIR,do_erc=True),
            Pin(num='59',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='69',name='ADCIN05',do_erc=True),
            Pin(num='79',name='ADCIN00',do_erc=True),
            Pin(num='89',name='TCLKINB/IOPF5',func=Pin.BIDIR,do_erc=True),
            Pin(num='99',name='TDO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='100',name='TMS',do_erc=True)])])