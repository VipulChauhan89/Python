#program to take the length, breadth, round of fencing and cost of fencing of the farm from the user and then print the total cost of fencing the farm with wire.
length=int(input("Enter the length of the farm in meters : "))
breadth=int(input("Enter the breadth of the farm in meters : "))
rounds=int(input("Enter the number of times you want to fence the farm : "))
cost=int(input("Enter the cost of fencing in rupees per meter : "))
parameter=2*(length+breadth)
total_length=rounds*parameter
total_cost=cost*total_length
print("The parameter of the farm is {} meters".format(parameter))
print("Total wire required to fence the farm  {0} times is {1} meters\n".format(rounds,total_length))
print("Total cost of fencing the farm is {} rupees\n".format(total_cost))
