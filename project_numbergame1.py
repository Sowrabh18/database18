secret_number=619

x = int(input("Enter secret number :"))
while x!=secret_number:
     print("Wrong...!!!")
     print("Try again...!!")
     x = int(input("Enter secret number :"))

else:
    if x == secret_number:
        print("CORRECT...!!!")





