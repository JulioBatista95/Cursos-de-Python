frase = 'Curso em Vídeo Python'
print(frase[::2])
print(frase.upper().count('o'))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))  #Para realmente trocar o valor em sua
# base, acrescenta-se a variável que deseja receber a mudança. exemplo:
#frase = frase.replace('Python', 'Android')

frase = frase.replace('Python', 'Android')
print(frase)
print(frase.replace('o', 'r'))
dividido = frase.split()
print(dividido[2][3])
print("em" in frase)
'''print(sdjfjsndfjonsdjofnosjdnf
sndofnksdofnsjodnfjsndf
nsdojfnsjonfjsndfjsndfjns
sjfnsjodnfjosdnfjsndfjon
nsodfnsjodnfjsdnfojsnofjns)'''