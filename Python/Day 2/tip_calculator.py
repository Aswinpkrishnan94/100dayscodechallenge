#Welcome Message
print("Welcome to the tip calculator!")

# Asking the user to input values such as total bill, 
#the tip percentage wish to pay and the number of people to share it

bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give?\n"))
people = int(input("How many people to split the bill?\n"))

total_tip_amount = bill * tip/100                        # total amount to be paid as tip
total_bill = bill + total_tip_amount                     # total bill to be paid including tip
bill_per_person = total_bill / people                    # the amount each person has to share
final_amount = "{:.2f}".format(bill_per_person)          # to round the output to two places 

print(f"Each person should pay:{final_amount}")