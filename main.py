#
# A program to show change in coin denominations
#
change = int(input("Enter the amount of change (in cents) you have : "))

while change > 0:
# Number of quarters
    q = change//25
    change = change - q*25
# Number of dimes
    d = change//10
    change = change - d*10
# Number of nickels
    n = change//5
    change = change - n*5
# Number of pennies
    p = change//1
    change = change - p*1
else:
    print("quarters: " + str(q))
    print("dimes: " + str(d))
    print("nickels: " + str(n))
    print("pennies: " + str(p))