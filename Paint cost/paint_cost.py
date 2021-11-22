#program to calculate the area of rectangle in meter square and then find the paint cost to paint the rectangle.
length=int(input("Enter the length of the rectangle in meters : "))
breadth=int(input("Enter the breadth of the rectangle in meters : "))
area=length*breadth
cost=int(input("Enter the cost of paint per square meters in rupees : "))
totalcost=cost*area
print("The area of rectangle is {0} meter square and the total cost of paint that is required to paint the rectangle is {1} rupees".format(area,totalcost))
