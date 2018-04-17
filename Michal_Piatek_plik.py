print 'Dla rownania kwadratowego ax2+bx+c=0'
a=int(raw_input('podaj wartosc parametru a: '))
b=int(raw_input('podaj wartosc parametru b: '))
c=int(raw_input('podaj wartosc parametru c: '))
delta = b**2-4*a*c
if delta > 0:
    x1 = (-b-delta**(1/2))/(2*a)
    x2 = (-b+delta**(1/2))/(2*a)
    print 'x1 = ', x1, ', x2= ', x2
elif delta == 0:
    x0 = -b/(2*a)
    print 'x0 = ', x0
else:
    print 'brak rozwiazan'