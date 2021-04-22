#import math
#b = float(input('Digite o valor do cateto oposto '))
#c = float(input('Digite o valor do cateto adjacente '))
#a = b**2+c**2
#h = math.sqrt(a)
#print('Com o cateto oposto de {}, e com o cateto adjacente de {},\na hipotenusa é {:.2f}'.format(b, c, h))
from math import hypot
b = float(input('Digite o valor do cateto oposto '))
c = float(input('Digite o valor do cateto adjacente '))
h = hypot(b, c)
print('com o cateto oposto {}, e o cateto adjacente {}, o valor da \nhipotenusa é {:.2f}'.format(b, c, h))
