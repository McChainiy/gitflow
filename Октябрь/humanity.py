def human_read_format(bytes):
    convs = ['Б', 'КБ', "МБ", "ГБ"]
    oldbytes = 0
    while True:
        newbytes = round(bytes / 1024)
        if newbytes == 0 or oldbytes == 3:
            return ''.join([str(bytes), convs[oldbytes]])
        else:
            bytes = newbytes
            oldbytes += 1
