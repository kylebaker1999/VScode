from datetime import datetime

subtotal = int(input("What is the subtotal? "))

now = datetime.now()

weekday = now.weekday()

weekday = 2

if subtotal > 50:
    if weekday == 1 or weekday == 2:
        subtotal = subtotal * .9
        
        
    else:
        subtotal = subtotal

tax = subtotal * .06
total = tax + subtotal

print(f"tax: ${tax:.2f}")
print(f"your total is ${total:.2f}")
