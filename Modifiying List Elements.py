#line 4 is taking out adam and adding CALLA. 
garden_waitlist =["Jiho", "Adam", "Sonny", "Alisha"]
#removing Alisha and adding alex
garden_waitlist [-1]="Alex"
garden_waitlist [1]= "Calla"
print (garden_waitlist)

#removing the Flatbread from the list would be line 11 and after you would print.  on line 12
order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
#You must have something in the list in order to remove it or it will be a syntax error. 
order_list.remove("Flatbread")
print(order_list)

##Accessing 2D Lists
#Your code below:
class_name_test=[["Jenny", 90],["Alexus", 85.5],["Sam", 83],["Ellie", 101.5]]
print(class_name_test)
#within the sqaure brackets
sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)

#adding and removing
incoming_class=[["Kenny", "American", 9],["Tanya", "Russian", 9],["Madison","Indian",7]]

incoming_class[2][2]=8
incoming_class[-3][-3]="Ken"
print(incoming_class)
