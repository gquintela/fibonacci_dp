import time


def truncate(n):
  return int(n * 1000) / 1000


def fib1(n):
  if (n<3):
    return 1
  else:
    return (fib1(n-1)+fib1(n-2))


start = time.time()
res = fib1(30)
end = time.time()
total = truncate((end - start))
print('\n\nFIBONACCI N 30:'+ str(res) + '\n tiempo transcurrido usando recursion simple: '+ str(total) + ' segundos.\n' )

matriz =[]
for i in range(0,901):
  matriz.append(-1)
matriz[0]=0
matriz[1]=1

def fib2(n):
  if (n == 0):
    return 0
  if (n == 1):
    return 1
  else:
    if(matriz[n]==-1):
      matriz[n] = fib2(n-1) + fib2(n-2)
    return matriz[n]
    
    
    
start = time.time()
res =fib2(900)
end = time.time()
total = truncate((end - start))

print('FIBONACCI N 900:\n' + str(res) + '\ntiempo transcurrido usando programacion dinamica: '+ str(total) + ' segundos.' )
