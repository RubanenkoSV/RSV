print('\n', '-1-')
text='asjdlkajsdlak fksjdflkj sdkfj sldkf'
a={}
for i in text:
    a[i]=text.count(i)

print(a)

print('\n', '-2-')
abc =  'abcdefghijklmnopqrstuvwxyz '
for key in abc:
    if text.count(key)!=0:
        print(key, text.count(key))

print('\n', '-3-')
List = list(text)
Uniq = set(List)
print (Uniq)

for key in Uniq:
    print (key, text.count(key))