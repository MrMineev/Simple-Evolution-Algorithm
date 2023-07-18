from random import*
from re import S

#evo

class Evo:
    INF = 10**5
    error = 100
    goal = 628 # how good you want the object to be
    LOW = 0.01 # how close to the goal you need to be to stop the program
    N = 800 # number of clones that are created after finding the best object
    MAX_DIF = 5 # how much the object changes
    HROM = 5 # number of HROM inside the object
    SKIP = 1 # after how many steps you want the program to show the error (how far the best object is from the goal)

    DNK = []
    for j in range(N):
        row = []
        for i in range(HROM):
            row.append(0)
        DNK.append(row)

    def __init__(self, Goal, Num, Hrom, Low, Skip, Max_dif, function):
        self.goal = Goal
        self.N = Num
        self.HROM = Hrom
        self.LOW = Low
        self.SKIP = Skip
        self.MAX_DIF = Max_dif
        self.DNK = []
        for g in range(self.N):
            row = []
            for i in range(self.HROM):
                row.append(0)
            self.DNK.append(row)

        if (function == None): return

        self.FunctionForGrading = function


    def FunctionForGrading(self, obj, mas): # the function to get how good the object 
        print("mas : ", mas)
        sum = 0
        for i in range(self.HROM):
            sum += mas[i]
        return sum

    def GetRDif(self, l, r): # calculating the change in the object
        '''
        return uniform(l, r)

        you can use this function if the task requires non-integer numbers
        '''
        return randint(l, r)

    def GetRQwe(self, l, r): # finding the HROM to be changed in the object
        return randint(l, r)

    def multi(self, n): # creating slightly modified objects
        DNK_now = list(n) # DNK_NOW is the DNK of the best object
        for i in range(self.N - 1):
            DNK_now = list(n)
            qwe = self.GetRQwe(0, len(DNK_now) -1) # get the HROM that we change in the DNK_NOW
            dif = self.GetRDif(-self.MAX_DIF, self.MAX_DIF) # calculating how does the HROM of DNK_NOW change
            DNK_now[qwe] = DNK_now[qwe] + dif
            self.DNK[i] = DNK_now # changing the DNK
        DNK_now = list(n)
        self.DNK[self.N - 1] = DNK_now

    def grade(self): # giving the grad to every object to find the best
        ans = [0] * self.N # ans is an array of all the grades of the objects
        for i in range(self.N):
            # code in this loop is just creating the problem in this case the problem is to create an object with maximum sum of HROM
            ans[i] = self.FunctionForGrading(self, self.DNK[i])
        return ans

    def f(self, n): # calculating the error (how far the object is from perfect)
        '''
        1. return 100 * ((n / goal) ** 2)
        2. return 100 * ((goal - n) / goal)
        3. return 100 * (abs(goal - n) / goal)

        these are functions that you can play with and see how the result changes
        '''
        return (self.goal - n) ** 2
    
    def run(self): # main code
        error = 100
        best = 0
        cnt = 0
        while (error > self.LOW): # self.LOW is how small should the error be to finish the program
            cnt += 1
            self.multi(self.DNK[best])
            ans = self.grade()
            max = self.INF
            num = -1
            v = -1
            for i in range(len(ans)):
                if max > self.f(ans[i]):
                    max = self.f(ans[i])
                    num = ans[i]
                    v = i
            best = v
            error = self.f(num)
            if (cnt % self.SKIP == 0): # outputing sometimes the error value
                print("best", best, num)
                print("error", error)
        print("----> ", error)
        print(self.DNK[best]) # outputing the solution


def FunctionGet(evo, mas):
    sum = 0
    for i in range(len(mas)):
        sum += mas[i]
    return sum

evo = Evo(100, 800, 15, 0.01, 5, 5, FunctionGet)
evo.run()
