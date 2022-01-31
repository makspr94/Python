import sys
print("Hello !!! yolochka")
params = sys.argv [1:3] # функция возвращет список. В кв. скобках срез. Элементы указываем как параметры в
                       # в консоле
sum_l = []
for i in params[1:3]:
    sum_l.append(int(i))
    print('sum 3 = ', i)
sum_3 = sum(sum_l)
print('params = ', params)