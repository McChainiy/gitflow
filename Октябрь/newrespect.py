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


def recurs(nlist, inlevel=0):
    deathnote = []
    for i in range(len(nlist)):
        if i in deathnote:
            continue
        if nlist[i][-1] == '':
            print('  ' * inlevel, nlist[i][inlevel], sep='')
            reclist = list(filter(lambda x: x[inlevel] == nlist[i][inlevel], nlist))[1:]
            for z in reclist:
                deathnote.append(nlist.index(z))
            recurs(reclist, inlevel + 1)
        else:
            print('  ' * inlevel, nlist[i][inlevel], ' ',
                  human_read_format(info['/'.join(nlist[i])]), sep='')


with ZipFile('input.zip') as myzip:
    namelist = [i.split('/') for i in myzip.namelist()]
    info = {}
    for i in myzip.infolist():
        info[i.filename] = i.file_size
    recurs(namelist)
print(os.listdir('C:/'))