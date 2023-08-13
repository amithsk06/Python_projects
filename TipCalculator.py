bill = float(input("Enter the Bill Amount: "))
tip = int(input("What percetnage tip would you like to give:10,12 or 15 ? "))
n = int(input("Enter the number of people: "))
t = bill + (bill * (tip / 100))
each = t / n
each = round(each, 2)
each_amount = "{:.2f}".format(each)
print(f"Each person should pay : {each_amount}")