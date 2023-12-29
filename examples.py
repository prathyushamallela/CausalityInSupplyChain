#climbing stairs
#dynamic programming
import random
n= 45
one=1
two=2
stepsum=10
a=[]
for i in range(10):
  if stepsum<=10 and stepsum>=1:
    c=random.choice([1,2])
    if(stepsum-c==-1):
        c=1
    a.append(c)
    stepsum=stepsum-c
  else:
      break

print(a)
print(len(a))
print(sum(a))