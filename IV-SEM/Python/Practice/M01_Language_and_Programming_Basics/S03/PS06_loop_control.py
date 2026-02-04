'''
for i in range(1, 11):
    if i == 5:
        continue  # Skip even numbers
    print(i)  # Print only odd numbers
else:
    print("Loop completed.")
    if i == 8:
        print("The loop reached 8.")

'''
'''
Password retry system (max 3 attempts)
If password is correct show login successful
else ask for password 3 times
Once attempts exceed show account locked
'''
p1 = "abc123"
for i in range(3):
    p2 = input()
    if p1 == p2:
        print("Login successful")
        break
else:
    print("Account locked")