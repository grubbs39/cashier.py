import random

total_dollar = random.randint(0, 101)
Total_cent = random.randint(0, 101)

#print("Our random dollars" + str(total_dollar))
#print("Our random cents" + str(Total_cent))

total = float(total_dollar) + float(Total_cent)/100
print("Our total is:" + "${:,.2f}".format(total))

payment = round(random.uniform(total, total+100), 2)
print("our payment was" + "${:,.2f}".format(payment))

change = payment - total
print("our change was" + "${:,.2f}".format(change))

remaining_change = change
#print("our remaining change was" + "${:,.2f}".format(remaining_change))

currency_values = {
    20: 0,
    10: 0,
    5: 0,
    1: 0,
    .25: 0,
    .10: 0,
    .05: 0,
    .01: 0
}

types_of_money = currency_values.keys()
for denomination in types_of_money:
    #print("Considering the denominatin is:" + str(denomination))
    while denomination <= remaining_change:
        remaining_change -= denomination
        currency_values[denomination] += 1
        print("Our remaining change is:" + "${:,.2f}".format(remaining_change))
    #print("We are going to give back:" + str(currency_values[denomination]) + "of" + .format(denomination))
    #print("Our remaining change is:" + .format(remaining change))

end_of_transaction_total = total_dollar
print("your total was:" + "${:,.2f}".format(end_of_transaction_total))
for denomination in reversed(types_of_money):
    end_of_transaction_total -= currency_values[denomination] * denomination
    print(str(currency_values[denomination]) + "of" + "${:,.2f}".format(denomination) + "makes" +\
     "${:,.2f}".format(end_of_transaction_total))

if(end_of_transaction_total > total):
    print("you are giving money away!")
elif(end_of_transaction_total == total):
    print("good job!")
else:
    print("you are a thief!")


sorted_keys = currency_values.keys()
for key in sorted_keys:
    print(str(key) + ": " + str(currency_values[key]))
