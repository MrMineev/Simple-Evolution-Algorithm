from algo import Evo

def FunctionGet(obj, mas):
    sum = 0
    for i in range(len(mas)):
        sum += mas[i]
    return sum

evo = Evo(100, 800, 15, 0.01, 5, 5, FunctionGet) 
evo.run()
