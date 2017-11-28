from skidl import Pin, Part, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

cmos_ieee = SchLib(tool=SKIDL).add_parts(*[
        Part(name='4001',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4002',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4006',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4008',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4009',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4010',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='40104',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='40106',dest=TEMPLATE,tool=SKIDL,do_erc=True,aliases=['4584']),
        Part(name='4011',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='40110',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4012',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4013',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4014',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4015',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4016',dest=TEMPLATE,tool=SKIDL,do_erc=True,aliases=['4066']),
        Part(name='4017',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='40174',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='40175',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4018',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4019',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='40192',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='40193',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='40194',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4020',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4021',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4022',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4023',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4024',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='40240',dest=TEMPLATE,tool=SKIDL,do_erc=True,aliases=['40244']),
        Part(name='40245',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4025',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4027',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4028',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4029',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4030',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='40373',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='40374',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4040',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4041',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4042',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4043',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4044',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4046',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4048',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4049',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4050',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4051',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4052',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4053',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4067',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4068',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4069',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4070',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4071',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4072',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4073',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4075',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4077',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4078',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4081',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4082',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4093',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4095',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4096',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4099',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4104',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4160',dest=TEMPLATE,tool=SKIDL,do_erc=True,aliases=['40160']),
        Part(name='4161',dest=TEMPLATE,tool=SKIDL,do_erc=True,aliases=['40161']),
        Part(name='4162',dest=TEMPLATE,tool=SKIDL,do_erc=True,aliases=['40162']),
        Part(name='4163',dest=TEMPLATE,tool=SKIDL,do_erc=True,aliases=['40163']),
        Part(name='4174',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4175',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4502',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4504',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4507',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4508',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4510',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4511',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4512',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4514',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4515',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4518',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4520',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4529',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4530',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4538',dest=TEMPLATE,tool=SKIDL,do_erc=True,aliases=['4528']),
        Part(name='4539',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4543',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4555',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4556',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='4585',dest=TEMPLATE,tool=SKIDL,do_erc=True)])