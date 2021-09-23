# Author : Aditya Kamlesh Yadav
# B. Tech CSE, 3rd Year
# Artificial Intelligence & Machine Learning LAB 02
# Date : 23rd September, 2021

class TransposeMatrix:
    def __init__(self):
        self.matrix = []
        self.result_matrix = []
        self.m = 0
        self.n = 0

    def getData(self):
        m = int(input("Enter m : "))
        n = int(input("Enter n : "))
        self.m = m
        self. n = n

        print("Please enter data row wise!!")
        print()
        print("Enter Data for Matrix : ")

        for i in range(m):          # A for loop for row entries
            a =[]
            for j in range(n):      # A for loop for column entries
                    a.append(int(input()))
            self.matrix.append(a)

        print("Matrix : ")
        for i in range(self.m):
            for j in range(self.n):
                print(self.matrix[i][j], end = " ")
            print()

        print()

    def solve(self):
        self.result_matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]

        print("Transpose of Matrix : ")
        for i in range(self.n):
            for j in range(self.m):
                print(self.result_matrix[i][j], end = " ")
            print()

        print()

tr = TransposeMatrix()
tr.getData()
tr.solve()
