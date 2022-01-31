import sys
import argparse

# print("Hello !!! yolochka")
# params = sys.argv [1:3] # функция возвращет список. В кв. скобках срез. Элементы указываем как параметры в
#                        # в консоле
# sum_l = []
# for i in params[1:3]:
#     sum_l.append(int(i))
#     print('sum 3 = ', i)
# sum_3 = sum(sum_l)
# print('params = ', params)




# parser = argparse.ArgumentParser()
# parser.add_argument('--name', type=str, default='no')
# parser.add_argument('--age', type=int, default=20)
#
# args = parser.parse_args()
# # print('Name =', args.name) # способ 1
# # print('Age =', args.age)
#
# args_dict = args.__dict__       #способ 2
# for k,v in args_dict.items():
#     print(k,v)

parser = argparse.ArgumentParser()
parser.add_argument('--num_1', type=int)
parser.add_argument('--num_2', type=int, required=True)
parser.add_argument('--action', type=str)

args = parser.parse_args()
kotik_1 = args.num_1
kotik_2 = args.num_2
action = args.action

if action == 'sum':
    result = kotik_1 + kotik_2
    print('result=', result)
elif action == 'multi':
    result = kotik_1 * kotik_2
    print('result=', result)
elif action == 'div':
    result = kotik_1 / kotik_2
    print('result=', result)
elif action == 'sub':
    result = kotik_1 - kotik_2
    print('result=', result)

