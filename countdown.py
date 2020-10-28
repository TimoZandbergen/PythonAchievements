import time
print("je countdown gaat nu beginnen je heb 15 seconde, succes!")
time.sleep( 2 )
count = 15
while count >0:
	count = count - 1
	print("hij vermindert steeds met 1")
	print(str(count))
	time.sleep( 0.5 ) 
print("YOU lOSE!")