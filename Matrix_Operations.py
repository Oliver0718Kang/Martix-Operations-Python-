#===============================================
#Menu
def menu():
    done = False
    print("Matrix Manipulation")
    while (not done):
        print("1: Create Matrices")
        print("2: Multiply Matrices")
        print("3: Add Matrices")
        print("4: Quit")
        print("Make sure to enter appropriate option!")
        print("="*45, end="")
        go()

#===============================================
#Matrices Class

class Matrices:
    def __init__(self):
        self.data=[[1,0,0],[0,1,0],[0,0,1]] #Set to Identity
    def __add__(self,other):
        result = Matrices()
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result
    def __mul__(self,other):
        result = Matrices()
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                sum = 0
                for k in range(len(self.data)):
                    sum += self.data[i][k] * other.data[k][j]
                result.data[i][j] = sum
        return result
    def __str__(self):
        result = ''
        for i in self.data:
            result += "|{:^8} {:^8} {:^8}|\n".format(i[0], i[1], i[2])
        return result

#===============================================
#Matrix A and B
def go():
    inputval = 1 
    inputval = int(input('\nEnter your option:'))
    global matA
    global matB
    if inputval == 1: #(Creating Matrix)
        matA = Matrices()
        matB = Matrices()
        matA.data = [[1,1,2],[3,5,8],[13,21,34]]
        matB.data = [[2,3,5],[7,11,13],[17,19,23]]
        print(matA)
        print(matB)
    elif inputval == 2: #(Multiply Martix)
        print(matA)
        print(matB)
        matC = matA * matB
        print(matC)
    elif inputval == 3: #(Add)
        print(matA)
        print(matB)
        matD = matA + matB
        print(matD)
    elif inputval == 4: #(Quit)
        exit(0)
    else:
        print('Try again! Please, enter a valid option! (num:1, 2, 3, 4)')

#===============================================
# MAIN
menu()






    

