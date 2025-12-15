# Bytes
print(bytes(4))

smileyBytes = bytes ('🙄', 'utf-8')
print(smileyBytes)

print(smileyBytes.decode('utf-8'))

smileyBytes = bytearray('🙄','utf-8')

print(bytearray)

smileyBytes[3] = int('85', 16)

print(smileyBytes.decode('utf-8'))