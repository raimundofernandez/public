Bubblegum = 202
Toffee = 118
Ice_cream = 2250
Milk_chocolate = 1680
Doughnut = 1075
Pancake = 80

Cleaner = 850
Vendor = 1120
Manager = 1300
Loader = 900

Electricity = 100
Municipal_service = 90
Security = 30

Income = float(Bubblegum + Toffee + Ice_cream + Milk_chocolate + Doughnut + Pancake)

print("Earned amount:")
print("Bubblegum: $202")
print("Toffee: $118")
print("Ice cream: $2250")
print("Milk chocolate: $1680")
print("Doughnut: $1075")
print("Pancake: $80")
print("")
print("Income:", Income, "$")
print("Staff expenses:")
Staff = int(input())
print("Other expenses:")
Other = int(input())

Outcome = float(Cleaner + Vendor + Manager + Loader + Electricity + Municipal_service + Security + Staff + Other)
Total = Income - Outcome

print("Net income:", Total, "$")
