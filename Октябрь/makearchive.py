from shutil import make_archive
from time import gmtime


def make_reserve_arc(source, dest):
    gm = [str(i) for i in gmtime()[:]]
    make_archive('{}\\{}'.format(dest, '{} {}'.format('.'.join(gm[3:6]), '.'.join(gm[2::-1]))),
                 'zip', source)
