# napisz program wypisujacy liczby podzielne przez 3 i przez 7 z zakresu od 1 do 50
l = 50
l7 = 0
l3 = 0
l37 = 0
print('Podzielna przez 7 i przez 3:')
for n in range(1,l+1):
    if n%7==0 and n%3==0:
       print(n)
print('Podzielna przez 3:')
for n in range(1,l+1):
    if n%3==0:
       print(n)
print('Podzielna przez 7:')
for n in range(1,l+1):
    if n%7==0:
       print(n)



