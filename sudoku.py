

from cell import cell
from cellmat import cellmat
import random
mat = cellmat()
mat.print()

for i in range(5):
    while(True):
        origmat = mat.__copy__()
        i = random.randrange(0,9)
        j = random.randrange(0,9)
        mat.mat[i][j].kill()
        newmat = mat.__copy__()
        mat.solve()
        if not mat.iscomplete():
            mat = origmat
            break
        mat = newmat
mat.print()
#mat.mat[0][1].set(6)
# mat.mat[0][2].set(1)
# mat.mat[0][5].set(4)
# mat.mat[1][0].set(3)
# mat.mat[1][6].set(4)
# mat.mat[1][8].set(6)
# mat.mat[2][0].set(2)
# mat.mat[2][2].set(9)
# mat.mat[2][4].set(6)
# mat.mat[2][5].set(8)
# mat.mat[2][7].set(7)
# mat.mat[2][8].set(1)
# mat.mat[3][0].set(9)
# mat.mat[3][3].set(6)
# mat.mat[3][8].set(3)
# mat.mat[4][1].set(3)
# mat.mat[4][3].set(5)
# mat.mat[4][4].set(2)
# mat.mat[4][5].set(1)
# mat.mat[4][7].set(9)
# mat.mat[5][0].set(6)
# mat.mat[5][5].set(3)
# mat.mat[5][8].set(8)
# mat.mat[6][0].set(4)
# mat.mat[6][1].set(8)
# mat.mat[6][3].set(7)
# mat.mat[6][4].set(1)
# mat.mat[6][6].set(9)
# mat.mat[6][8].set(2)
# mat.mat[7][0].set(7)
# mat.mat[7][2].set(2)
# mat.mat[7][8].set(5)
# mat.mat[8][3].set(4)
# mat.mat[8][6].set(8)
# mat.mat[8][7].set(6)
