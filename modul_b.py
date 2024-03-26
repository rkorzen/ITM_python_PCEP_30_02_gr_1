import sys
# print(sys.path)
#
# sys.path.insert(0, )

import xsxsxsxsx


# import modul_a
#
# modul_a.funkcja()
# print(modul_a.STALA + 1)

from modul_a import funkcja, STALA
# from modul_a import * # raczej unikamy tego

from modul_c import funkcja as funkcja_c
from package_d import funkcja as funkcja_d
from package_d import mul, div

funkcja()
print(STALA + 1)
funkcja_c()
funkcja_d()

print(mul(2, 3))
print(div(2, 3))