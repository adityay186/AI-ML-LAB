# Author : Aditya Kamlesh Yadav
# B. Tech CSE, 3rd Year
# Artificial Intelligence & Machine Learning LAB 02
# Date : 23rd September, 2021

class AddTwoArrays:

    def __init__(self):
        self.matrix1 = []
        self.matrix2 = []
        self.matrix_sum = []
        self.n = 0

    def getData(self):
        n = int(input("Enter Dimensions : "))
        self.n = n
        print("Please enter data row wise!!")
        print()
        print("Enter Data for Matrix 1 : ")

        for i in range(self.n):          # A for loop for row entries
            a =[]
            for j in range(self.n):      # A for loop for column entries
                    a.append(int(input()))
            self.matrix1.append(a)

        print("Matrix 1 : ")
        for i in range(self.n):
            for j in range(self.n):
                print(self.matrix1[i][j], end = " ")
            print()

        print()

        print("Enter Data for Matrix 2 : ")

        for i in range(self.n):          # A for loop for row entries
            a =[]
            for j in range(self.n):      # A for loop for column entries
                    a.append(int(input()))
            self.matrix2.append(a)

        print("Matrix 2 : ")
        for i in range(self.n):
            for j in range(self.n):
                print(self.matrix2[i][j], end = " ")
            print()

        print()

    def solve(self):
        for i in range(self.n):          # A for loop for row entries
            a =[]
            for j in range(self.n):      # A for loop for column entries
                    a.append(self.matrix1[i][j] + self.matrix2[i][j])
            self.matrix_sum.append(a)

        print("Sum : ")
        for i in range(self.n):
            for j in range(self.n):
                print(self.matrix_sum[i][j], end = " ")
            print()

        print()

ar = AddTwoArrays()
ar.getData()
ar.solve()
