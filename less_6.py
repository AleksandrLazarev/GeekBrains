# t_1 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""какие-то строки могут быть закомментировавны"""

# ngnx_log = open(r'd:\tmp\nginx_logs.txt', 'r', encoding = 'utf-8')
# content = ((i.split()[0], i.split()[5][1:], i.split()[6]) for i in ngnx_log)
# for a in content:
#     print(a)



# t_2 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
with open(r'd:\tmp\nginx_logs.txt', 'r', encoding = 'utf-8') as f:
    my_dict = {}
    content_t2 = (line.split()[0] for line in f)
    for i in content_t2:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

sorted_keys = sorted(my_dict, key=my_dict.get)
print(f'spamer {sorted_keys[-1]} - {my_dict[sorted_keys[-1]]} times')

# t_3 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

from json import dump
from itertools import zip_longest

with open(r'd:\tmp\users.csv', 'r', encoding='utf-8') as users:
    with open(r'd:\tmp\hobby.csv', 'r', encoding='utf-8') as hobby:

        all_list = zip_longest((' '.join(us.split(',')) for us in users), hobby, fillvalue=None)
        my_dct = {str(el[0]).strip(): (el[1].strip()) for el in all_list}

        with open(r'd:\tmp\dict_n_h.json', 'w', encoding='utf-8') as f:
            if 'None' in my_dct:
                print(1)
            else:
                dump(my_dct, f, ensure_ascii=False, indent=4)
                print(my_dct)

# t_3 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *







