from zipfile import ZipFile


with ZipFile('input.zip') as myzip:
    namelist = myzip.namelist()
namelist = [i.split('/') for i in namelist]


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
            print('  ' * inlevel, nlist[i][inlevel], sep='')


recurs(namelist)