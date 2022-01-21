# Inputs
power = 0
num_tier_5s = 1 # Excludes first 3

num_normals = 62
price_per_normal = 85+160+340+6800+185+120

pops = 16000000
income = 0

# Tier 5 calculation
from_5s = num_tier_5s * 10000
if(from_5s > 90000):
    power += 90000
    print("Max tier 5 hit")
else:
    power += from_5s
    r = 90000 - from_5s
    print("Remaining from tier 5's: ", r)


# Normals Calculation
num_upgrades = num_normals * 6
amount_spent = num_normals * price_per_normal
print("Number of normals is: ", num_normals)
print("Price per nomal is: ", price_per_normal)
print("Total amount spent on normals is: ", amount_spent)

# From Upgrades
from_upgrades = num_upgrades * 100
if(from_upgrades > 10000):
    power += 10000
    print("Max upgrades hit")
else:
    power += from_upgrades
    r = 10000 - from_upgrades
    print("Remaining from upgrades: ", r)

# From amount spent
from_money = amount_spent / 25
if(from_money > 10000):
    power += 10000
    print("Max money hit")
else:
    power += from_money
    r = 10000 - from_money
    print("Remaining from money: ", r)

# Pops Calculation
pops += income * 4

from_pops = pops / 180
if(from_pops > 90000):
    power += 90000
    print("Max pops hit")
else:
    power += from_pops
    r = 90000 - from_pops
    print("Remaining from pops: ", r)
    estimated_pops_remaining = r * 180
    print("Estimated pops reamining: ", estimated_pops_remaining)

# Degree Calculation
print("Current power is: ", power)
deg = 1
while(deg < 100):
    required_power = ((50 * (deg**3)) + (5025 * (deg**2)) + (168324 * deg) + 843000)/600
    if(power >= required_power):
        current_degree = deg
    
    deg += 1 # loop iterator

print("Current estimated degree would be: ", current_degree)