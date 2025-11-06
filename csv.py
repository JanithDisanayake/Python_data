

f1=open("new.csv","w")
for i in range(1,11):
         en=input("Enter your name")
         num=int(input("Enter your age:"))
         f1.write(en)
         f1.write(num)
f1.close()