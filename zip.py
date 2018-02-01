string="AABCAAADA"
k=3
for part in zip(*[iter(string)]*k):
        mark=dict()
        print(''.join([mark.setdefault(val,val) for val in part if val not in mark]))