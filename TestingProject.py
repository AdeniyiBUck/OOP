'''
Name: Adeniyi Buckley
Email: Adeniyi.buckley@edu.sait.ca
Date: 2025-01-30
ID#: 000977441

Name: Binaya Lakhe 
Email: binaya.lakhe.edu.sait.ca
Date: 2025-01-30
ID#: 000998156


Group 6: Assignment: Programming Basics - Flowchart
'''
#Defininging constants
BAGS_PER_BOX = 20
TEA_PRICE_PER_BAG = 0.45
COFFEE_PRICE_PER_KG = 18.50

TEA_DISCOUNT_THRESHOLD_BOXES = 10
COFFEE_DISCOUNT_THRESHOLD_KG = 25

TEA_DISCOUNT_RATE = 0.15
COFFEE_DISCOUNT_RATE = 0.10
 
GST_DEFAULT_RATE = 0.15

# Setting up the dictrionary of compound GST rates based on province
GST_AB_BC = ("AB", "BC") # Provinces with 5% GST
GST_RATES = {
    "AB": 0.05,
    "BC": 0.05,
    "ON": 0.13
}

# Defining the variables to be used in the program
product_name = ("")
product_amount = 0.0 # quantity of product purchased
province_code = ("")    # For province identification for GST calculation
before_discount = 0.0 # price before discount. To be calculated based on product and quantity
discount_price = 0.0 # price after discount
gst_rate = GST_DEFAULT_RATE # default GST rate, to be updated based on province
gst_amount = 0.0 # amount of GST to be calculated based on price after discount and GST rate
final_price = 0.0 # final price to be calculated as price after discount + GST amount

#Printing Welcome Message and Product Menu
print("-" * 60)
print("**** Welcome to Beverage Wholesale Program! ****")
print("-" * 60)

print("Please select the type of purchase:")
print("C: Coffee Beans")
print("T: Tea Boxes")
product_choice = input(">>> ")

product_choice = product_choice.strip().upper() # convert input if lowercase to uppercase and remove whitespace infront and back of input

if product_choice != "C" and product_choice != "T": # Check if the product choice is valid (C or T)
    print("Invalid input, you should enter c/C or t/T")
    exit() # Exit the program if invalid product choice

#####Coffee Beans are selected as the product
if product_choice == "C":
    product_name = ("\tCoffee")

    kg_num = float(input("Enter the number of kilograms (kg) of coffee: "))
    if kg_num <= 0:
        print("Quantity of Coffee should be > 0") 
        exit() # Exit the program if invalid quantity

        # Asking the user for their province code for GST calculation and validating the input
    province_code = input("Please enter the 2-letter province abbreviation:")
    province_code = province_code.strip().upper() # convert input if lowercase to uppercase and remove whitespace infront and back of input



    before_discount = kg_num * COFFEE_PRICE_PER_KG
    if kg_num > COFFEE_DISCOUNT_THRESHOLD_KG:
        discount_price = before_discount * (1 - COFFEE_DISCOUNT_RATE)
    else:
        discount_price = float(before_discount)

    product_amount = float("{:.2f}".format(kg_num))

    #####Tea Boxes are selected as the product

elif product_choice == "T":
    product_name = ("\tTea")

    box_num = int(input("Enter the number of boxes of tea: "))

    if box_num <= 0:
        print("Number of tea boxes must be > than 0.")
        exit() # Exit the program if invalid quantity

        # Asking the user for their province code for GST calculation and validating the input

    province_code = input("Please enter the 2-letter province abbreviation:")
    province_code = province_code.strip().upper() # convert input if lowercase to uppercase and remove whitespace infront and back of input
        
    bags = box_num * BAGS_PER_BOX # tea is sold in boxes but the price is per bag, so we need to calculate the total number of bags based on the number of boxes purchased
    before_discount = bags * TEA_PRICE_PER_BAG

    #Disount is calculated based on the number of boxes bought not the number of bags
    if box_num > TEA_DISCOUNT_THRESHOLD_BOXES:
        discount_price = before_discount * (1 - TEA_DISCOUNT_RATE)
    else:
        discount_price = float(before_discount)
    product_amount = float("{:.2f}".format(bags))
    
# Calculate GST based on province (checking to see if the province code is in the GST_RATES dictionary, if not use the default GST rate)
done = False
while done == False:
    if province_code in GST_RATES:
        gst_rate = GST_RATES[province_code]
        done = True
    else:
        gst_rate = GST_DEFAULT_RATE
        done = True

## Finding the GST amount and the final pricee to be paid by the customer.
gst_amount = discount_price * gst_rate
final_price = discount_price + gst_amount


print("-" * 130)
print( "\tProduct", "Qty (Bags/kg)", "Price Before Disc", "Price After Disc", "GST", "Total Price", sep= " " *10)
print("{:<15} {:>9.2f} {:>25} {:>25} {:>19} {:>17}".format(
    product_name,
    product_amount,
    "${:,.2f}".format(before_discount),
    "${:,.2f}".format(discount_price),
    "${:,.2f}".format(gst_amount),
    "${:,.2f}".format(final_price),
     
))
print("-" * 130)
print("Thanks for your business, Good Bye")
