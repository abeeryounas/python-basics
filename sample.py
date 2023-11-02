# # #For using the  simple function
# # a=17
# # b=21
# # #making function of average of two number
# # def average(a,b):
# #     average=(a+b)/2
# #     print(average) 
# # #call the function of average
# # print("The average of a and b is:" )
# # average(a,b)
# # c=7
# # d=9
# # #again call the same function with different arguments
# # print("The average of c and d is:" )
# # average(c,d)
# # #FOR DEFAULT ARGUMENTS FUNCTION
# # def name(firstname ="MuHAMMAD", lastname ="ABEER"):
# #     print("Aslamualaikum My name is", firstname,lastname)
# # #Calling the name funtion
# # name("Talha","Younis") #Talha younis replace Muhammad Abeer
# # name("Talha",) #Talha  replace Muhammad And last name is taken from funtion argument And output is Talha Abeer

# # #FOR LIST
# # marks=[4,9,6,7,9,0,5] #its always in square bracket
# # print(type(marks))        #check the type
# # print(marks)               #print the whole list
# # print(marks [1:4])          #for printing the index between 2 and 4
# # #FOR DIFFERNT METHOD OF LIST
# # marks.append(8)  #for ending the list with number 8
# # marks.reverse()     #for reversing the the list 
# # marks.insert(1,45) # for insert the number 45 into 9 is first index
# # print(marks)
# # #FOR tuple
# # tup=(3,4,8,6,5) #tuple is same as list but cannot be directly change and it always be in round brackets
# # print(tup)
# # Exercise given by harry to make a gaem kn bany ga crorepati
# question1=["Q.1 1992 World cup winning captain","Imran khan","waseem akram","inzamam"]#making a list of question
# print(question1)
# answer=str(input("enter the answer"))#input the answer from the user
# print(answer)
# if(answer=="imrankhan"):
#     print("Your answer is correct you won 1000 rupees")
# else:
#     print("your answer is wrong")
# question2=["Q.2 In which Odi world cup shahid afridi is the captain of pakistan",2007,2011,2015]
# print(question2)
# answer=int(input("enter the answer"))
# print(answer)
# if(answer==2011):
#     print("Your answer is correct you won 5000 rupees")
# else:
#     print("your answer is wrong")
# question3=["Q.3 Babar Azam odi ranking right now",1,3,5]
# print(question3)
# answer=int(input("enter the answer"))
# print(answer)
# if(answer==1):
#     print("Your answer is correct you won 10000 rupees")
# else:
#     print("your answer is wrong")
# print("why my code is not push on github")

#F STRING
naan=30
cutlus=30
price=(f"The price of naan is {naan} and price of cutlus is {cutlus}")#The price of naan and cutlus is stored 
print(price)
petrol=284.850
Gov=(f"The price of petrol is {petrol:.2f} rupees")
print(Gov)
#DOC STRING is always below the function and is written ass function.__doc__ and the display is inbetween the string
def add(n):
    '''The addition of the two number is'''
    print(n+n)
print(add.__doc__)#its means they show the the addtion of two number or in between the strinf in function
add(10)
#Zen of python
import this #Just write import this and the poem display in output
#RECURSION in python we use function in function
def fibonacci(n):
    if(n==0 ): #if the number is 0 then its return zero
        return 0
    if( n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))
#SET in python it is similer as list  but cannt maintain order and its is always in curly bracket
set={"abeer",1,17.69, False}
print(set)
for info in set:#we can use for loop to display sets
    print(info)