# This file is created by Parambir Singh
print('Find Simple Interest...')
p = input('Type Principal- ')
r = input('Type Rate of interest- ')
t = input('Type time- ')
p = float(p)
r = float(r)
t = float(t)
print('Simple interest on ', p ,' and rate ',r , ' and time ', t , 'is' ,p*r*t/100)
si = p*r*t/100 
print('and the amount is =' , si+p)