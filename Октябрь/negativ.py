f = open('input.bmp', 'rb').read()
end = open('res.bmp', 'wb')
end.write(f[:54] + bytes(map(lambda x: 255 - int(x), f[54:])))