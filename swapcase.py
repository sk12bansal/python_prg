s=input();
s=list(s)
for idx,val in enumerate(s):
    if val>='A' and val<='Z':
        s[idx]=s[idx].lower()
    elif val.isdigit():
        continue
    else:
       	s[idx]=s[idx].upper()
print(''.join(s))
