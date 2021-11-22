#program to compute the net salary of the employ by entering percentage of HRA,TA,DA.
name=input("Enter the name of the employ : ")
Basic_pay=float(input("Enter the basic pay of the employ : "))
Hra_percent=float(input("Enter the HRA percentage : "))
Ta_percent=float(input("Enter the TA percentage : "))
Da_percent=float(input("Enter the DA percentage : "))
Hra=(Hra_percent*Basic_pay)/100;
Ta=(Ta_percent*Basic_pay)/100;
Da=(Da_percent*Basic_pay)/100;
Net_salary=Basic_pay+Hra+Ta+Da;
print("The name of the employ is",name)
print("Net salary of the employ is = {} rupees .\n".format(Net_salary))
