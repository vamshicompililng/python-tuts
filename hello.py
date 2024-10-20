num=3

if num%2==0:
    print("its a even number")
else:
    print("its a odd number")

n1=int(input("enter value of a: "))
n2=int(input("enter value of b: "))
n3=int(input("enter value of c: "))
n4=int(input("enter value of d: "))
if n1>=n2 and n1>=n3 and n1>=n4:
    print("n1 is greater")
elif n2>=n1 and n2>=n3 and n2>=n4:
    print("n2 is greater")
elif n3>=n4:
    print("n3 is gretaer")
else:
    print("n4 is greater")


tup=(1,2,3,4,5,1)

a=tup.count(1)
# print(a)
l1=[1,2,2,1]
l2=l1.reverse()
# l2.reverse()
if l1==l2:
    print("its a palindrome")
else:
    print("its not a palindrome")
