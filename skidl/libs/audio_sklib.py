from skidl import Pin, Part, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

audio = SchLib(tool=SKIDL).add_parts(*[
        Part(name='LL1587',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='LM1875',dest=TEMPLATE,tool=SKIDL,keywords='LM1875 Amplifier 20W',description='20W Audio Power Amplifier, TO220-5',ref_prefix='U',num_units=1,fplist=['TO*'],do_erc=True,pins=[
            Pin(num='1',name='IN+',do_erc=True),
            Pin(num='2',name='IN-',do_erc=True),
            Pin(num='3',name='VEE',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='OUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='VCC',func=Pin.PWRIN,do_erc=True)]),
        Part(name='LM1876',dest=TEMPLATE,tool=SKIDL,keywords='LM1876 Overture Amplifier Dual 20W',description='Dual 20W Overture Seriers Audio Power Amplifier, with Mute Standby Mode, TO220-15 (MultiWatt)',ref_prefix='U',num_units=2,fplist=['TO*'],do_erc=True,pins=[
            Pin(num='2',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='OUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='4',name='VEE',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='6',name='MUTE',do_erc=True),
            Pin(num='7',name='IN-',do_erc=True),
            Pin(num='8',name='IN+',do_erc=True),
            Pin(num='9',name='STB',do_erc=True),
            Pin(num='1',name='OUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='4',name='VEE',func=Pin.PWRIN,do_erc=True),
            Pin(num='10',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='11',name='MUTE',do_erc=True),
            Pin(num='12',name='IN-',do_erc=True),
            Pin(num='13',name='IN+',do_erc=True),
            Pin(num='14',name='STB',do_erc=True),
            Pin(num='15',name='VCC',func=Pin.PWRIN,do_erc=True)]),
        Part(name='LM1877M',dest=TEMPLATE,tool=SKIDL,keywords='Dual Audio Amplifier 2W 24V',description='2W/8R Dual Audio Power Amplifier, Supply Voltage 6-24V, SO14L',ref_prefix='U',num_units=1,fplist=['SO*'],do_erc=True,pins=[
            Pin(num='1',name='BIAS',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='OUT1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='3',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='6',name='IN1',do_erc=True),
            Pin(num='7',name='IN1',do_erc=True),
            Pin(num='8',name='IN2',do_erc=True),
            Pin(num='9',name='IN2',do_erc=True),
            Pin(num='10',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='11',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='12',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='13',name='OUT2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='14',name='V+',func=Pin.PWRIN,do_erc=True)]),
        Part(name='LM1877N',dest=TEMPLATE,tool=SKIDL,keywords='Dual Audio Amplifier 2W 24V',description='2W/8R Dual Audio Power Amplifier, Supply Voltage 6-24V, DIP14',ref_prefix='U',num_units=1,fplist=['DIP*', 'PDIP*'],do_erc=True,pins=[
            Pin(num='1',name='BIAS',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='OUT1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='3',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='6',name='IN1',do_erc=True),
            Pin(num='7',name='IN1',do_erc=True),
            Pin(num='8',name='IN2',do_erc=True),
            Pin(num='9',name='IN2',do_erc=True),
            Pin(num='10',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='11',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='12',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='13',name='OUT2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='14',name='V+',func=Pin.PWRIN,do_erc=True)]),
        Part(name='LM3886T',dest=TEMPLATE,tool=SKIDL,keywords='LM3886 Overture Amplifier Single 86W',description='Single 68W Overture Seriers Audio Power Amplifier, with Mute Mode, PFM-11 (Plastic MultiWatt)',ref_prefix='U',num_units=1,fplist=['TO*'],do_erc=True,aliases=['LM3886TF'],pins=[
            Pin(num='1',name='V+',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='OUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='4',name='V-',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='V+',func=Pin.PWRIN,do_erc=True),
            Pin(num='7',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='MUTE',do_erc=True),
            Pin(num='9',name='IN-',do_erc=True),
            Pin(num='10',name='IN+',do_erc=True)]),
        Part(name='LM4950TA',dest=TEMPLATE,tool=SKIDL,keywords='LM4950 Stereo Power Aplifier 3.1W',description='Audio 3.1W Stereo Power Amplifier, TO220-9',ref_prefix='U',num_units=1,fplist=['TO220*'],do_erc=True,pins=[
            Pin(num='1',name='INA',do_erc=True),
            Pin(num='2',name='~SHD~',do_erc=True),
            Pin(num='3',name='OUTA',func=Pin.OUTPUT,do_erc=True),
            Pin(num='4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='6',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='7',name='OUTB',func=Pin.OUTPUT,do_erc=True),
            Pin(num='8',name='BP',func=Pin.OUTPUT,do_erc=True),
            Pin(num='9',name='INB',do_erc=True),
            Pin(num='10',name='TAP',do_erc=True)]),
        Part(name='LM4950TS',dest=TEMPLATE,tool=SKIDL,keywords='LM4950 Stereo Power Aplifier 3.1W',description='Audio 3.1W Stereo Power Amplifier, TO263-9',ref_prefix='U',num_units=1,fplist=['TO263*'],do_erc=True,pins=[
            Pin(num='1',name='INA',do_erc=True),
            Pin(num='2',name='~SHD~',do_erc=True),
            Pin(num='3',name='OUTA',func=Pin.OUTPUT,do_erc=True),
            Pin(num='4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='6',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='7',name='OUTB',func=Pin.OUTPUT,do_erc=True),
            Pin(num='8',name='BP',func=Pin.OUTPUT,do_erc=True),
            Pin(num='9',name='INB',do_erc=True),
            Pin(num='10',name='TAP',do_erc=True)]),
        Part(name='LM4990',dest=TEMPLATE,tool=SKIDL,keywords='Audio Boomer BTL Mono Amplifier',description='Audio 1.25W Mono Power Amplifier, VSSOP',ref_prefix='U',num_units=1,fplist=['MSOP-*_3x3mm_Pitch0.65mm*'],do_erc=True,pins=[
            Pin(num='1',name='~SHTD',do_erc=True),
            Pin(num='2',name='BYPS',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='+IN',do_erc=True),
            Pin(num='4',name='-IN',do_erc=True),
            Pin(num='5',name='VO1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='6',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='7',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='VO2',func=Pin.OUTPUT,do_erc=True)]),
        Part(name='MSGEQ7',dest=TEMPLATE,tool=SKIDL,keywords='equalizer filter',description='Graphic Equalizer Display Filter',ref_prefix='U',num_units=1,fplist=['SOIC*', 'DIP*'],do_erc=True,pins=[
            Pin(num='1',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='VSS',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='OUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='4',name='STROBE',do_erc=True),
            Pin(num='5',name='IN',do_erc=True),
            Pin(num='6',name='GND',func=Pin.PWROUT,do_erc=True),
            Pin(num='7',name='RESET',do_erc=True),
            Pin(num='8',name='CKIN',do_erc=True)]),
        Part(name='NSL-32',dest=TEMPLATE,tool=SKIDL,keywords='OPTO',description='Opto resistor',ref_prefix='U',num_units=1,do_erc=True,pins=[
            Pin(num='1',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='R',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='R',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='PAM8301',dest=TEMPLATE,tool=SKIDL,keywords='Audio Mono Filterless Class-D Amplifier',description='Audio 1.5W Filterless Class-D Mono Amplifier, TSOT-23-6',ref_prefix='U',num_units=1,fplist=['SOT-23*'],do_erc=True,pins=[
            Pin(num='1',name='OUT-',func=Pin.OUTPUT,do_erc=True),
            Pin(num='2',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='IN',do_erc=True),
            Pin(num='4',name='~SD',do_erc=True),
            Pin(num='5',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='6',name='OUT+',func=Pin.OUTPUT,do_erc=True)]),
        Part(name='PGA4311',dest=TEMPLATE,tool=SKIDL,keywords='AUDIO',description='4 channels Audio Volume Control',ref_prefix='U',num_units=1,do_erc=True,pins=[
            Pin(num='1',name='MUTE',do_erc=True),
            Pin(num='2',name='AGND-1',do_erc=True),
            Pin(num='3',name='Ain-1',do_erc=True),
            Pin(num='4',name='AGND-1',do_erc=True),
            Pin(num='5',name='Ain-1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='6',name='VA-',func=Pin.PWRIN,do_erc=True),
            Pin(num='7',name='VA+',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='Aout-3',func=Pin.OUTPUT,do_erc=True),
            Pin(num='9',name='AGND-3',do_erc=True),
            Pin(num='10',name='Ain-3',do_erc=True),
            Pin(num='20',name='AGND_4',do_erc=True),
            Pin(num='11',name='AGND-3',do_erc=True),
            Pin(num='21',name='Aout-4',func=Pin.OUTPUT,do_erc=True),
            Pin(num='12',name='VD+',func=Pin.PWRIN,do_erc=True),
            Pin(num='22',name='VA+',func=Pin.PWRIN,do_erc=True),
            Pin(num='13',name='SDI',do_erc=True),
            Pin(num='23',name='VA-',func=Pin.PWRIN,do_erc=True),
            Pin(num='14',name='CS',do_erc=True),
            Pin(num='24',name='Aout-2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='15',name='SCLK',do_erc=True),
            Pin(num='25',name='AGND-2',do_erc=True),
            Pin(num='16',name='SDO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='26',name='Ain-2',do_erc=True),
            Pin(num='17',name='DGND',func=Pin.PWRIN,do_erc=True),
            Pin(num='27',name='AGND-2',do_erc=True),
            Pin(num='18',name='AGND_4',do_erc=True),
            Pin(num='28',name='ZCEN',do_erc=True),
            Pin(num='19',name='Ain-4',do_erc=True)]),
        Part(name='SSM-2017P',dest=TEMPLATE,tool=SKIDL,keywords='Audio PREAMP',description='Audio low noise preamp',ref_prefix='U',num_units=1,do_erc=True,pins=[
            Pin(num='1',name='Gain',do_erc=True),
            Pin(num='2',name='-',do_erc=True),
            Pin(num='3',name='+',do_erc=True),
            Pin(num='4',name='V-',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='Ref',do_erc=True),
            Pin(num='6',name='~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='7',name='V+',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='Gain',do_erc=True)]),
        Part(name='SSM-2018T',dest=TEMPLATE,tool=SKIDL,keywords='AUDIO VCA',description='audio VCA',ref_prefix='U',num_units=1,do_erc=True,pins=[
            Pin(num='9',name='Comp3',do_erc=True),
            Pin(num='1',name='+I1-G',func=Pin.OUTPUT,do_erc=True),
            Pin(num='2',name='V+',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='-Ig',func=Pin.OUTPUT,do_erc=True),
            Pin(num='4',name='-I1-G',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='Comp1',do_erc=True),
            Pin(num='6',name='+',do_erc=True),
            Pin(num='7',name='-',do_erc=True),
            Pin(num='8',name='Comp2',do_erc=True),
            Pin(num='10',name='V-',func=Pin.PWRIN,do_erc=True),
            Pin(num='11',name='Vctrl',do_erc=True),
            Pin(num='12',name='MODE',do_erc=True),
            Pin(num='13',name='GND',do_erc=True),
            Pin(num='14',name='Vg',func=Pin.OUTPUT,do_erc=True),
            Pin(num='15',name='BAL',do_erc=True),
            Pin(num='16',name='V1-g',func=Pin.OUTPUT,do_erc=True)]),
        Part(name='SSM2120P',dest=TEMPLATE,tool=SKIDL,keywords='AUDIO VCA',description='Dual VCA & level detectors',ref_prefix='U',num_units=2,do_erc=True,pins=[
            Pin(num='10',name='Iref',do_erc=True),
            Pin(num='11',name='V-',func=Pin.PWRIN,do_erc=True),
            Pin(num='21',name='V+',func=Pin.PWRIN,do_erc=True),
            Pin(num='22',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='1',name='Thresh',do_erc=True),
            Pin(num='2',name='LOGav',do_erc=True),
            Pin(num='3',name='CTR',do_erc=True),
            Pin(num='4',name='~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='+Vc',do_erc=True),
            Pin(num='6',name='CFT',do_erc=True),
            Pin(num='7',name='-Vc',do_erc=True),
            Pin(num='8',name='E',do_erc=True),
            Pin(num='9',name='RecIn',do_erc=True),
            Pin(num='20',name='~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='12',name='Thresh',do_erc=True),
            Pin(num='13',name='LOGav',do_erc=True),
            Pin(num='14',name='CTR',do_erc=True),
            Pin(num='15',name='RecIn',do_erc=True),
            Pin(num='16',name='E',do_erc=True),
            Pin(num='17',name='-Vc',do_erc=True),
            Pin(num='18',name='CFT',do_erc=True),
            Pin(num='19',name='+Vc',do_erc=True)]),
        Part(name='SSM2122P',dest=TEMPLATE,tool=SKIDL,keywords='AUDIO VCA',description='Dual VCA',ref_prefix='U',num_units=2,do_erc=True,pins=[
            Pin(num='7',name='Iref',do_erc=True),
            Pin(num='8',name='V-',func=Pin.PWRIN,do_erc=True),
            Pin(num='9',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='15',name='V+',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='~',func=Pin.OUTPUT,do_erc=True),
            Pin(num='3',name='+Vc',do_erc=True),
            Pin(num='4',name='CFT',do_erc=True),
            Pin(num='5',name='-Vc',do_erc=True),
            Pin(num='6',name='E',do_erc=True),
            Pin(num='10',name='E',do_erc=True),
            Pin(num='11',name='-Vc',do_erc=True),
            Pin(num='12',name='CFT',do_erc=True),
            Pin(num='13',name='+Vc',do_erc=True),
            Pin(num='14',name='~',func=Pin.OUTPUT,do_erc=True)]),
        Part(name='SSM2165',dest=TEMPLATE,tool=SKIDL,keywords='AUDIO',description='8 pins microphone preamp and compressor',ref_prefix='U',num_units=1,do_erc=True,pins=[
            Pin(num='1',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='VCAIN',do_erc=True),
            Pin(num='3',name='BUFOUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='4',name='IN+',do_erc=True),
            Pin(num='5',name='AVG',do_erc=True),
            Pin(num='6',name='COMP',do_erc=True),
            Pin(num='7',name='VOUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='8',name='V+',func=Pin.PWRIN,do_erc=True)]),
        Part(name='SSM2210',dest=TEMPLATE,tool=SKIDL,description='Audio dual matched NPN transistor',ref_prefix='U',num_units=2,do_erc=True,pins=[
            Pin(num='1',name='C',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='B',do_erc=True),
            Pin(num='3',name='E',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='E',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='B',do_erc=True),
            Pin(num='8',name='C',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='SSM2220',dest=TEMPLATE,tool=SKIDL,keywords='AUDIO',description='Audiao dual Matched PNP transistor (low noise)',ref_prefix='U',num_units=2,do_erc=True,pins=[
            Pin(num='1',name='C',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='B',do_erc=True),
            Pin(num='3',name='E',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='E',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='B',do_erc=True),
            Pin(num='8',name='C',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='STK435',dest=TEMPLATE,tool=SKIDL,keywords='STK443 Dual 25W Amplifier Audio',description='Dual 25W Audio Power Amplifier, 4010',ref_prefix='U',num_units=2,do_erc=True,aliases=['STK433', 'STK436', 'STK437', 'STK439', 'STK441', 'STK443'],pins=[
            Pin(num='1',name='IN+',do_erc=True),
            Pin(num='2',name='IN-',do_erc=True),
            Pin(num='3',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='OUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='6',name='BST',do_erc=True),
            Pin(num='7',name='VCC',do_erc=True),
            Pin(num='8',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='9',name='VCC2',func=Pin.PWRIN,do_erc=True),
            Pin(num='7',name='VCC',do_erc=True),
            Pin(num='8',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='9',name='VCC2',func=Pin.PWRIN,do_erc=True),
            Pin(num='10',name='BST',do_erc=True),
            Pin(num='11',name='OUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='12',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='13',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='14',name='IN-',do_erc=True),
            Pin(num='15',name='IN+',do_erc=True)]),
        Part(name='TDA2003H',dest=TEMPLATE,tool=SKIDL,keywords='TDA2003H Amplifier 10W Pentawatt',description='10W Car Radio Audio Amplifier, TO220-5 (PentaWatt5H)',ref_prefix='U',num_units=1,fplist=['TO*'],do_erc=True,pins=[
            Pin(num='1',name='IN+',do_erc=True),
            Pin(num='2',name='IN-',do_erc=True),
            Pin(num='3',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='OUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='VCC',func=Pin.PWRIN,do_erc=True)]),
        Part(name='TDA2003V',dest=TEMPLATE,tool=SKIDL,keywords='TDA2003V Amplifier 10W Pentawatt',description='10W Car Radio Audio Amplifier, PentaWatt5V',ref_prefix='U',num_units=1,fplist=['TO*'],do_erc=True,pins=[
            Pin(num='1',name='IN+',do_erc=True),
            Pin(num='2',name='IN-',do_erc=True),
            Pin(num='3',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='OUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='VCC',func=Pin.PWRIN,do_erc=True)]),
        Part(name='TDA2005R',dest=TEMPLATE,tool=SKIDL,keywords='TDA2005 Amplifier 20W Multiwatt',description='20W Bidge/Stereo Audio Amplifier for Car Radio, TO220-11 (MultiWatt11)',ref_prefix='U',num_units=2,fplist=['TO*'],do_erc=True,pins=[
            Pin(num='3',name='SVRR',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='9',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='1',name='IN+',do_erc=True),
            Pin(num='2',name='IN-',do_erc=True),
            Pin(num='10',name='OUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='11',name='BST',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='IN-',do_erc=True),
            Pin(num='5',name='IN+',do_erc=True),
            Pin(num='7',name='BST',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='OUT',func=Pin.OUTPUT,do_erc=True)]),
        Part(name='TDA2030',dest=TEMPLATE,tool=SKIDL,keywords='TDA2030 Amplifier14W Pentawatt',description='14W Hi-Fi Audio Amplifier, TO220-5 (PentaWatt)',ref_prefix='U',num_units=1,fplist=['TO*'],do_erc=True,pins=[
            Pin(num='1',name='IN+',do_erc=True),
            Pin(num='2',name='IN-',do_erc=True),
            Pin(num='3',name='VEE',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='OUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='VCC',func=Pin.PWRIN,do_erc=True)]),
        Part(name='TDA2050',dest=TEMPLATE,tool=SKIDL,keywords='TDA2050 Amplifier 32W Pentawatt',description='32W Hi-Fi Audio Amplifier, TO220-5 (PentaWatt)',ref_prefix='U',num_units=1,fplist=['TO*'],do_erc=True,pins=[
            Pin(num='1',name='IN+',do_erc=True),
            Pin(num='2',name='IN-',do_erc=True),
            Pin(num='3',name='VEE',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='OUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='VCC',func=Pin.PWRIN,do_erc=True)]),
        Part(name='TDA7294HS',dest=TEMPLATE,tool=SKIDL,keywords='TDA7294 Amplifier Single 100W',description='Single 100W Audio Power Amplifier, with Mute and Standby Mode, MultiWatt15H',ref_prefix='U',num_units=1,fplist=['TO*'],do_erc=True,pins=[
            Pin(num='1',name='STBY-GND',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='IN-',do_erc=True),
            Pin(num='3',name='IN+',do_erc=True),
            Pin(num='4',name='IN+MUTE',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='BST',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='Vs+',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='Vs-',func=Pin.PWRIN,do_erc=True),
            Pin(num='9',name='STBY',do_erc=True),
            Pin(num='10',name='MUTE',do_erc=True),
            Pin(num='13',name='PWVs+',func=Pin.PWRIN,do_erc=True),
            Pin(num='14',name='OUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='15',name='PWVs-',func=Pin.PWRIN,do_erc=True)]),
        Part(name='TDA7294V',dest=TEMPLATE,tool=SKIDL,keywords='TDA7294 Amplifier Single 100W',description='Single 100W Audio Power Amplifier, with Mute and Standby Mode, TO220-15 (MultiWatt15V)',ref_prefix='U',num_units=1,fplist=['TO*'],do_erc=True,pins=[
            Pin(num='1',name='STBY-GND',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='IN-',do_erc=True),
            Pin(num='3',name='IN+',do_erc=True),
            Pin(num='4',name='IN+MUTE',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='BST',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='Vs+',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='Vs-',func=Pin.PWRIN,do_erc=True),
            Pin(num='9',name='STBY',do_erc=True),
            Pin(num='10',name='MUTE',do_erc=True),
            Pin(num='13',name='PWVs+',func=Pin.PWRIN,do_erc=True),
            Pin(num='14',name='OUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='15',name='PWVs-',func=Pin.PWRIN,do_erc=True)]),
        Part(name='THAT2180',dest=TEMPLATE,tool=SKIDL,keywords='AUDIO VCA',description='VCA (THAT Corporation)',ref_prefix='U',num_units=1,do_erc=True,aliases=['THAT2181'],pins=[
            Pin(num='5',name='V-',func=Pin.PWRIN,do_erc=True),
            Pin(num='6',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='7',name='V+',func=Pin.PWRIN,do_erc=True),
            Pin(num='1',name='E',do_erc=True),
            Pin(num='2',name='+Vc',do_erc=True),
            Pin(num='3',name='-Vc',do_erc=True),
            Pin(num='4',name='Sym',do_erc=True),
            Pin(num='8',name='~',func=Pin.OUTPUT,do_erc=True)]),
        Part(name='TR-AUDIO-2P',dest=TEMPLATE,tool=SKIDL,keywords='TRANSFO',description='Microphone Input Transformer (2 P 1S)',ref_prefix='T',num_units=1,do_erc=True,pins=[
            Pin(num='1',name='P1+',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='P1-',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='P2-',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='P2+',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='S-',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='S+',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='~',do_erc=True)])])