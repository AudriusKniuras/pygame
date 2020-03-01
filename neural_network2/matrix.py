import random
import math



def multiply(m1, m2):
    if m1.cols != m2.rows:
        print('Matrix mismatch when multiplying')
        return False
    result = Matrix(m1.rows, m2.cols)

    for i in range(result.rows):
            for j in range(result.cols):
                # dot product
                sum = 0
                for k in range(m1.cols):
                    sum += m1.matrix[i][k] * m2.matrix[k][j]
                result.matrix[i][j] = sum

    return result

def fromArray(arr):
    m = Matrix(len(arr), 1)
    for i in range(len(arr)):
        m.matrix[i][0] = arr[i]

    return m

def subtract(a, b):
    result = Matrix(a.rows, a.cols)

    for i in range(a.rows):
        for j in range(a.cols):
            result.matrix[i][j] = a.matrix[i][j] - b.matrix[i][j]
    
    return result

def transpose(a):
    result = Matrix(a.cols, a.rows)
    for i in range(a.rows):
        for j in range(a.cols):
            result.matrix[j][i] += a.matrix[i][j]
    return result

class Matrix():

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []

        for i in range(self.rows):
            self.matrix.append([])
            for j in range(self.cols):
                self.matrix[i].append(0)

    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = round(random.uniform(-1,1), 2)





    def multiply(self, n):
        # perform a scalar operations - multiply by a value, or add a value
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] *= n

    def map(self, func):
        # apply a function to every element
        for i in range(self.rows):
            for j in range(self.cols):
                val = self.matrix[i][j]
                self.matrix[i][j] = func(val)

    def add(self, n):
        
        if type(n) is Matrix:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] += n.matrix[i][j]
        else:
            # perform a scalar operation - multiply by a value, or add a value
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] += n

    def toArray(self):
        arr = []
        for i in range(self.rows):
            for j in range(self.cols):
                arr.append(self.matrix[i][j])
        return arr

    def print(self):
        print(self.matrix)