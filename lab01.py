# AI ML Lab 01
# Aditya Kamlesh Yadav
# PRN : 20190802060


import numpy as np
import matplotlib.pyplot as plt

class GradientDescent: # class for GradientDescent Calculations
    def __init__(self, num_iter, learning_rate):
        self.learning_rate = learning_rate
        self. num_iter = num_iter
        self.theta = [0, 0] # initial values of theta array, theta0 = 0, theta1 = 0
        self.X = np.random.uniform(low=1, high=10, size=(20,))
        self.y = np.random.uniform(low=1, high=10, size=(20,))

    def hypothesis(self, x):
        return self.theta[0] + self.theta[1] * x    # mathematical hypothesis to predict the outcome

    def cost(self): # cost function also called as the sum of squares of errors or losses
        m = len(self.X)
        sumLoss = 0
        for i in range(m):
            sumLoss = sumLoss + (self.X[i] - self.y[i])**2

        return sumLoss / (2 * m)

    def gradientDescent(self):   # gradientDescent function uses the mathematical formula for calculations
        m = len(self.X)

        for j in range(self.num_iter):

            h = list(map(self.hypothesis, self.X))


            dsum0 = 0
            for i in range(m):
                dsum0 = dsum0 + (h[i] - self.y[i])
            deri_th0 = dsum0 / m

            dsum1 = 0
            for i in range(m):
                dsum1 = dsum1 + (h[i] - self.y[i]) * self.X[i]
            deri_th1 = dsum1 / m

            self.theta[0] = self.theta[0] - self.learning_rate * deri_th0   # updating the values of theta0 and theta1
            self.theta[1] = self.theta[1] - self.learning_rate * deri_th1

    def plot(self): # method used to plot the random values generated and also plot the line using the generated solution
        plt.scatter(self.X, self.y)
        plt.plot(self.X, list(map(self.hypothesis, self.X)))
        plt.show()

    def main(self): # main method to call the needed methods
        self.gradientDescent()
        print()
        print("y = ", self.theta[0], "+", self.theta[1], "* X")
        print()
        print("Most Optimal Solution : ")
        print("m = ", self.theta[1])
        print("b = ", self.theta[0]) # print solution
        print()
        self.plot()

gd = GradientDescent(1000, 0.03)    # creating an GradientDescent object containing 1000 as number of iterations and 0.03 as the learning rate
gd.main()   # calling the main method from the GradientDescent object we created
