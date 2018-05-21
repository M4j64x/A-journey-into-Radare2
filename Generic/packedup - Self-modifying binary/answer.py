# Rotate right lambda
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

# Byte array from 0x004007A0, modified from the generated results of `pcp 44 @ 0x4007a0`
arr = [0x0F, 0xC9, 0xA8, 0x86, 0xAC, 0xE0, 0x18, 0x93, 0x8A, 0xAF, 0x91, 0xA2, 0xE4, 0x64, 0x7A, 0x5A, 0x08, 0x8B, 0xA8, 0x9A, 0xB4, 0xD1, 0x1F, 0x84, 0xB4, 0xD1, 0x71, 0x52, 0x1C, 0x8A, 0x80, 0xD2, 0x14, 0x95, 0x82, 0x97, 0x80, 0xD2, 0x1F, 0x90, 0x8F, 0x91, 0x93, 0xA6]

# Initial key value 
key = 0xdc77df87

flag = []

# Iterate the array backwards
for b in reversed(arr):
    # ror the key 
    key = ror(key,1,32)
    # xor the 8 lower bits of the key with current byte in array
    char = chr(b ^ (key & 0xff))
    # Add char to final flag
    flag.insert(0, char)


print '[+] Flag: ', ''.join(flag)