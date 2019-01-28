import os, shutil
from zipfile import ZipFile

def recurs(pth):
    print(pth)
    b = (os.path.dirname(pth))
    if pth == b:
        return
    recurs(b)

recurs(os.path.abspath('files'))

print(os.name)
print(os.getcwd())
print(os.path.dirname(os.getcwd()))

print(shutil.get_archive_formats())
shutil.make_archive('new/extremlynew', 'zip', root_dir='kek')
print()
with ZipFile('new/extremlynew.zip', 'w') as myzip:
    with open('darova.txt', 'w') as file:
        file.write('privet, hay')
    myzip.write('darova.txt')