#For using the  simple function
a=17
b=21
#making function of average of two number
def average(a,b):
    average=(a+b)/2
    print(average) 
#call the function of average
print("The average of a and b is:" )
average(a,b)
c=7
d=9
#again call the same function with different arguments
print("The average of c and d is:" )
average(c,d)
#FOR DEFAULT ARGUMENTS FUNCTION
def name(firstname ="MuHAMMAD", lastname ="ABEER"):
    print("Aslamualaikum My name is", firstname,lastname)
#Calling the name funtion
name("Talha","Younis") #Talha younis replace Muhammad Abeer
name("Talha",) #Talha  replace Muhammad And last name is taken from funtion argument And output is Talha Abeer

#FOR LIST
marks=[4,9,6,7,9,0,5] #its always in square bracket
print(type(marks))        #check the type
print(marks)               #print the whole list
print(marks [1:4])          #for printing the index between 2 and 4
#FOR DIFFERNT METHOD OF LIST
marks.append(8)  #for ending the list with number 8
marks.reverse()     #for reversing the the list 
marks.insert(1,45) # for insert the number 45 into 9 is first index
print(marks)
#FOR tuple
tup=(3,4,8,6,5) #tuple is same as list but cannot be directly change and it always be in round brackets
print(tup)
