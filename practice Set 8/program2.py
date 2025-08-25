#  convert celsius to fahrenheit
#  c/5 = (f-32)/9
def calculateFahrenheit(f):
    c= 5* (f-32)/9
    return c
f= int(input('enter a fahrenheit :  '))  
res = calculateFahrenheit(f)
print(res)

