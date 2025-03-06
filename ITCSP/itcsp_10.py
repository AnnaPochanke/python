# country = "PL"
# money = 500
# luggage_weight = 20
# output = False
#
# country = "USA"
# money = 500
# luggage_weight = 20
# # output = True
#
# country = "EU"
# money = 2000
# luggage_weight = 20
# # output = False
#
# country = "EU"
# money = 500
# luggage_weight = 30
# # output = False
#
country = input("Enter your country: \n")
money = int(input("Enter the amount of dollars you have with you: \n"))
luggage_weight = float(
    input("How many kilograms does your luggage weight: \n"))

##################################

# condition = False
condition = (country == "USA" or country == "EU") and (
    money < 1000 and money > 100) and luggage_weight <= 20

##################################
# OUTPUT
print(condition)
