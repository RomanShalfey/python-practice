weight = 1.5

print("Ground Shipping")

if weight <= 2: 
  cost = weight * 1.5
elif weight <= 6:
  cost = weight * 3
elif weight <= 10:
  cost = weight * 4
else :
  cost = weight * 4.75

print(cost + 20)



cost_ground_premium = 125
print(cost_ground_premium)

print("Drone Shipping")
if weight <= 2: 
  cost = 4.50  * 1.5
elif weight <= 6:
  cost = 9 * 1.5
elif weight <= 10:
  wcost = 12 * 1.5
else :
  cost = 10 * 1.5

print(cost)