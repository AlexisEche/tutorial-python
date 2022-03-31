

array=[4,5,5,9,1,-5]

best = 0
sum1 = 0

for k in range(0,len(array)):
  print("array[k]",array[k])
  sum1 = max(array[k],sum1+array[k])
  print("sum1",sum1)
  best = max(best,sum1)
  print("best",best)

print(best)
print(sum1)

print(4+5+5+9+1-5)
