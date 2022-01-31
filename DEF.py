def yolochka (a1,a2,a3, a4=100, a5=200, a6='maks'):

    var_1 = a1 * 2
    var_2 = a2 * 10
    var_3 = a3 * 3
    result = [var_1, var_2, var_3, a5]

    return result

get_f1 = yolochka (2, 5, 10, a5=500)
print ('get_f1 ==', get_f1)
# print ('get_f11 ==', get_f11)
# print ('get_f111 ==', get_f111)

print('2=================================')

def sosna (*args):
    print(args)

a1, a2, a3 = 1,2,3
sosna(a1,a2,a3)

print('3=================================')

def bereza (**kwargs):
    print(kwargs)

bereza(a1=1,a2=2,a3=3)


print('4=================================')

def yasen (*args, **kwargs):
    print(args, kwargs)
yasen(a1,a2,a3, a4=100, a5=200, a6='maks')

print('5=================================')

def yasen (salary, *args, **kwargs):
    print(salary, args, kwargs)
yasen(1000, a1,a2,a3, a4=100, a5=200, a6='maks')

print('6=================================')

def yasen (salary, *args, **kwargs):

    for k,v, in kwargs.item():
       n1 = v * 2
       print('K=', k, 'V=', n1)
    print(salary, args, kwargs)

yasen(1000, a1=5, a2=10)