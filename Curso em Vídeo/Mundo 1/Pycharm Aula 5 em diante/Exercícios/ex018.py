from math import cos, sin, tan, radians
a = float(input('Digite um ângulo '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('o Seno, cosseno e a tangente do número {} é:'
      '\n{:.2f}'
      '\n{:.2f}'
      '\n{:.2f}'.format(a, s, c, t))
