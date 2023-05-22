import re
string="AAAAAAAAAAAAAAAAAABBBBBBCCCCDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDAAAAAAAA"
result=''
pattern=re.finditer(r'(.)\1*',string)
for i in pattern:
    selection=i.group()[0]
    counter=i.group().count(selection)
    if counter>9 and counter%9:
        result += f'9{selection}' * int(counter / 9) + f'{counter % 9}{selection}'
    elif counter>9 and not counter%9:
        result += f'9{selection}' * int(counter / 9)
    else:
        result += str(counter) + selection
#list comprehension solution one-liner
print(''.join([f'9{i.group()[0]}' * int(i.group().count(i.group()[0]) / 9) + f'{i.group().count(i.group()[0]) % 9}{i.group()[0]}' if i.group().count(i.group()[0])>9 and i.group().count(i.group()[0])%9 else f'9{i.group()[0]}' * int(i.group().count(i.group()[0]) / 9) if i.group().count(i.group()[0])>9 and not i.group().count(i.group()[0])%9 else str(i.group().count(i.group()[0])) + i.group()[0] for i in re.finditer(r'(.)\1*',string)]))












































# for i in string:
#     print(i)
#     obj=re.match(f'(?<!{i}){i}+(?!{i})',string)
#     if obj is not None:
#         string=string.replace(str(obj.group()),'')
#         print(string)
#         counter=obj.group().count(i)
#         if str(counter)+i not in array:
#               if counter>9 and counter%9:
#                 array+=[f"9{i}"]*int(counter/9)+[f"{counter%9}{i}"]
#               elif counter>9 and not counter%9:
#                   array += [f"9{i}"] * int(counter / 9)
#               else:
#                 array+=[f"{counter%9}{i}"]
#     print(obj)
# print(array)
# print(''.join(array))




