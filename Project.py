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
bags_per_box = 20
tea_price_per_bag = 0.45
coffee_price_per_kg = 18.50

tea_discount_threshold_boxes = 10
coffee_discount_theshold_kg = 25

tea_discount = 0.15
coffee_discount = 0.10
 
gst_ab_bc = 0.05
gst_on = 0.13
gst_other = 0.15

#Printing Welcome Message and Product Menu
print("=" * 100)
print("                           **** Welcome to the Coffee and Tea Wholesale! ****")
print("=" * 100)

print("             Please Select Your Product from the Menu Below:")
print("Press 'C' or 'c' for Coffee Beans or 'T' or 't' for Tea Boxes")
print("C: Coffee Beans")
print("T: Tea Boxes")

product_choice = input("Enter your choice: ")
product_name = ("")
product_amount = ("") # quantity of product purchased
province_code = ("")    # For province identification for GST calculation
btotal = 0.0 # price before discount. To be calculated based on product and quantity
discount_price = 0.0 # price after discount

# Product Selection and Input
if product_choice == "c" or product_choice == "C":
    product_name = "Coffee Beans"
    kg_num = float(input("Enter desired number of coffee beans in kilograms: "))
    if kg_num <= 0:
        print("Invalid quantity: coffee kilograms must be greater than 0") 
        exit() # Exit the program if invalid quantity
    province_code = input("Enter your province: ")
    if province_code != "AB" and province_code != "ab" and province_code != "BC" and province_code != "bc" and province_code != "ON" and province_code != "on" and province_code != "Other" and province_code != "other":
        print("Province choice is invalid")
        exit() # Exit the program if invalid province code
        
    btotal = kg_num * coffee_price_per_kg
    if kg_num > coffee_discount_theshold_kg:
        discount_price = btotal * (1 - coffee_discount)
    else:
        discount_price = btotal
    product_amount = ("{:.2f}kg".format(kg_num))

elif product_choice == "t" or product_choice =="T":
    product_name = "Tea Boxes"
    box_num = int(input("Enter desired number of tea boxes: "))
    if box_num <= 0:
        print("Invalid quantity: tea boxes must be greater than 0")
        exit() # Exit the program if invalid quantity
    province_code = input("Enter your province: ")
    if province_code != "AB" and province_code != "ab" and province_code != "BC" and province_code != "bc" and province_code != "ON" and province_code != "on" and province_code != "Other" and province_code != "other":
        print("Province choice is invalid")
        exit() # Exit the program if invalid province code
        
    bags = box_num * bags_per_box
    btotal = bags * tea_price_per_bag
    if box_num > tea_discount_threshold_boxes:
        discount_price = btotal * (1 - tea_discount)
    else:
        discount_price = btotal
    product_amount = ("{} boxes".format(box_num))
    
# Calculate GST based on province
if province_code == "AB" or province_code == "ab" or province_code == "BC" or province_code == "bc":
    gst_rate = gst_ab_bc
elif province_code == "ON" or province_code == "on":
    gst_rate = gst_on
elif province_code == "Other" or province_code == "other":
    gst_rate = gst_other

gst_amount = discount_price * gst_rate
final_price = discount_price + gst_amount

print("\nReceipt:")
print("=" * 100)
print( "Product", "Quantity", "Before Disc", "After Disc", "GST", "Total", sep= " " *10)
print("{:<15} {:>9} {:>18} {:>18} {:>17} {:>15}".format(
    product_name,
    product_amount,
    "${:,.2f}".format(btotal),
    "${:,.2f}".format(discount_price),
    "${:,.2f}".format(gst_amount),
    "${:,.2f}".format(final_price)
))
print("=" * 100)
print("Thank you for shopping at Coffee and Tea Wholesale!")