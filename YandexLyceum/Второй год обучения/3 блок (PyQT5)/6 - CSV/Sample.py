with open('Снимок.bmp', 'rb') as file_read, open('dsadsa.bmp', 'wb') as file_write:
    header = file_read.read(54)
    data = [255 - byte for byte in file_read.read()]
    file_write.write(header)
    file_write.write(bytes(data))


