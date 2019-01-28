from zipfile import ZipFile
import os

def human_read_format(kek):
    convs = ['Б', 'КБ', "МБ", "ГБ"]
    oldbytes = 0
    while True:
        if kek // 1024 == 0 or oldbytes == 3:
            return ''.join([str(round(kek)), convs[oldbytes]])
        else:
            kek = round(kek / 1024)
            oldbytes += 1


def recurs(path):
    nlist = os.listdir(path)
    direct = []
    for i in nlist:
        pth = '{}/{}'.format(path, i)
        if not os.path.isfile(pth):
            direct.append(recurs(pth))
        else:
            direct.append([pth, os.path.getsize(pth)])
    print(direct)
    return direct


with ZipFile('input.zip') as myzip:
    namelist = [i.split('/') for i in myzip.namelist()]
    info = {}
    for i in myzip.infolist():
        info[i.filename] = i.file_size



print(os.listdir('C:/'))
print(os.path.getsize('C:/config.sys'))
print(os.path.isfile('C:/config.sys'))

print(recurs('C:/'))