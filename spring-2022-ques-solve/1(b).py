fee = 10000
result = 3.7

if result > 3.5:
    print(f"Waiver amount is: {fee-(fee*0.2)}")
elif result >=3.00 and result <= 3.5:
    print(f"Waiver amount is: {fee-(fee*0.1)}")  
else:
    print(f"Waiver amount is: {fee-(fee*0.05)}")      