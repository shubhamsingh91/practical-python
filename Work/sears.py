bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
sears_height = 442 # Height (meters)
num_bills = 1
day = 1

# test comment 
while (num_bills * bill_thickness) < sears_height:
    day+=1
    num_bills = 2*(num_bills)
    # print("day :", day)
    # print("bills = ", num_bills)

print("\nfinal day =", day)
print("num_bills = ", num_bills)

height = 1
print(height)
height = "string height"
print(height)

height = input("Enter your height:")
print("your height is", height)

a = 13
b = 34

if (a>b):
   pass
else:
    print("a < b")