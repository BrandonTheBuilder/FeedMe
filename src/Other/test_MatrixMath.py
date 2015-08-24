import unittest
import Util.MatrixMath as MM
from unittest import skip

class testMatrixMath(unittest.TestCase):
    
    def test_noDeterminant(self):
        try:
            MM.Det([[0,1],[1,0],[0,1]])
        except Exception as ex:
            self.assertEquals(True, isinstance(ex, ValueError))
            
    def test_FirstSubmatrix(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        i=1
        j=1
        subMatrix = [[1,3],[7,9]]
        self.assertEquals(subMatrix,MM.FirstSubMatrix(i,j,matrix))
        
    
    def test_twoByTwoDet(self):
        matrix = [[3,4],[6,7]]
        det = -3
        self.assertEquals(det, MM.Det(matrix))
        
       
    def test_fourByFour(self):
        matrix =  [[2,2,9,4],[5,2,7,8],[9,10,8,12],[13,14,15,0]]
        det = -4080
        self.assertEquals(det, MM.Det(matrix))
        
    def test_Cofactor(self):
        matrix = [[1,2,3],[4,5,6],[5,4,3]]
        cofactor = [[-9,18,-9],[6,-12,6],[-3,6,-3]]
        self.assertEquals(cofactor, MM.Cofactor(matrix))
        
    def test_Transpose(self):
        matrix = [[1,2,3,4],[5,6,7,8],[8,7,6,5],[4,3,2,1]]
        transpose = [[1,5,8,4],[2,6,7,3],[3,7,6,2],[4,8,5,1]]
        self.assertEquals(transpose, MM.Transpose(matrix))
        
    def test_Inverse(self):
        matrix = [[1,0,1,0],[0,1,0,1],[1,-1,0,1],[1,0,1,-1]]
        inverse = [[-2,1,1,2],[-1,1,0,1],[3,-1,-1,-2],[1,0,0,-1]]
        self.assertEquals(inverse, MM.Inv(matrix))
        
    def test_multiply(self):
        A = [[1,4,7],[2,5,8],[3,6,9]]
        B = [[2],[0],[1]]
        C = [[9],[12],[15]]
        self.assertEquals(C, MM.Multiply(A,B))
    
    def test_matrices(self):
        matrix = [[1, 0, 3, 2], [5, 7, 3, 2], [6, 1, 3, 2], [9, 11, 1, 2]]
        inverse = MM.Inv(matrix)
        identity = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        mi = MM.Multiply(inverse, matrix)
        for i in range(0, len(identity)):
            for j in range(0, len(identity[0])):
                self.assertAlmostEquals(identity[i][j], mi[i][j])
        
        
        