n = float(input('Digite um valor em metros: '))
km = n/1000
dm = n*10
cm = n*100
mm = n*1000
print('O valor de {}m em outras medidas, equivale a:'.format(n))
print('km: {:.5f}'.format(km))
print('dm: {:.5f}'.format(dm))
print('cm: {:.5f}'.format(cm))
print('mm: {:.5f}'.format(mm))
