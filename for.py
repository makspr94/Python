ll = [0,1,2,3,4,5, 'qw', True, False, 7, [12,'sw'], {'nn':55}]

dict_data = {
    'name': 'max',
    'age': 27,
    'weight': 84,
    'food': {'milk': ['sirnichki', 'milk', 'tvorog'],
             'meat': ['pelmeni', 'meat', 'kolbasa']},
    'salaty' : [250, 320, 700, 1100, 1200, 1500, 2000]
    }

count = 0
key_list = []

for key, value in dict_data.items():
    if key == 'food':
        value['milk']
        key_list = value['milk']
    key_list.append(key)
    print (key,  '==', value)

print(key_list)
#
# for i in key_list:
#     print(i)