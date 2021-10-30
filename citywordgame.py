Spic_town = set([
'здесь будут города'
])
dob=set([])
def runner():
i=1
a = str(input())
print('used - ',a)
dob.add(a)
posl = a[-1]
if posl == 'ь': posl = a[-2]
posl = posl.title()

while(a in dob):
i+=1
if (i%2==1):
a = str(input())
if posl1==a[0]:
print('used - ',a)
dob.add(a)
posl = a[-1]
if posl == 'ь': posl = a[-2]
posl = posl.title()
else:
print('Не та буква!')
else:
if a in spic_town:
for b in spic_town.difference(dob):
if posl==b[0]:
print('bot - ',b)
dob.add(b)
posl1 = b[-1]
if posl1 == 'ь': posl1 = b[-2]
posl1 = posl1.title()
break
else:
print('Нет такого города!')