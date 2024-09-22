# Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.
# The formula for the volume of a cylinder is V= pi*r2*h
import math

radius = float(input("Enter the radius of the cylinder (in meters): "))
height = float(input("Enter the height of the cylinder (in meters): "))
v=math.pi*(radius**2)*height
print(f"The volume of the cylinder is {v:.2f} liters.")
total_cost= v*1000 * 40
print(f"The cost of milk for this volume is Rs. {total_cost:.2f}.")