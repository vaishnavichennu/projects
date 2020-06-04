def even_or_odd(x):
 if x%2==0:
  print("it is even")
 else:
  print("it is odd")
def sum_of_digits(x):
 rem=0
 sum=0
 while x>0:
  rem=x%10
  sum=sum+rem
  x=x//10
 print("sum=",sum)
a=int(input("enter the value="))
even_or_odd(a)
sum_of_digits(a)
