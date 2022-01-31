# import time
# count = 0
# nn = bool
# while nn:
#     #time.sleep(.500)
#     print('hello', count)
#     count+= 1
#     nn = count<10
#
#
#     if count == 100:
#         break



while True:
    input_value = int((input('input your value: ')))

    nn = input_value * 2
    print('Your value x2 = ', nn)
    if nn  > 100:
        break