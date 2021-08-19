# Your code below: 
first_names=["Ainsley", "Ben","Chani","Depak"]

preferred_size=["Small","Large","Medium"]

preferred_size.append("Medium")
print(preferred_size)

customer_data=[["Ainsley","Small", True], ["Ben", "Large",False],["Chani", "Medium", True],["Depak","Medium", False]]


customer_data[2][2]=False
#Best way to remove anything in the 2D
customer_data[1].remove(False)
print(customer_data)
#Adding someone new to the customer data 2D
customer_data_final= customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]

print(customer_data_final)