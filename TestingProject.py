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

#Compound GST rates based on province
GST_AB_BC = ("AB", "BC") # Provinces with 5% GST
GST_RATE = {
    "AB": 0.05,
    "BC": 0.05,
    "ON": 0.13
}


#Printing Welcome Message and Product Menu
print("-" * 60)
print("**** Welcome to Beverage Wholesale Program! ****")
print("-" * 60)

print("Please select the type of purchase:")
print("C: Coffee Beans")
print("T: Tea Boxes")
product_choice = input(">>> ")
product_name = ("")
product_amount = ("") # quantity of product purchased
province_code = ("")    # For province identification for GST calculation
btotal = 0.0 # price before discount. To be calculated based on product and quantity
discount_price = 0.0 # price after discount

other_provinces = ["SK", "MB", "QC", "NB", "NS", "PE", "NL", "YT", "NT", "NU", "OTHER", "sk", "mb", "qc", "nb", "ns", "pe", "nl", "yt", "nt", "nu", "other"]
# Product Selection and Input
if product_choice != "c" and product_choice != "C" and product_choice != "t" and product_choice !="T":
    print("Invalid Input has been entered. Please restart the program and enter a valid product choice.")
    exit() # Exit the program if invalid product choice
if product_choice == "c" or product_choice == "C":
    product_name = "Coffee Beans"
    kg_num = float(input("Enter desired number of coffee beans in kilograms: "))
    if kg_num <= 0:
        print("Invalid quantity: coffee kilograms must be greater than 0") 
        exit() # Exit the program if invalid quantity
    province_code = input("Enter your province: ")
    if province_code != "AB" and province_code != "ab" and province_code != "BC" and province_code != "bc" and province_code != "ON" and province_code != "on" and province_code not in other_provinces:
        print("Province choice is invalid. Please restart the program and enter a valid province code.")
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
    if province_code != "AB" and province_code != "ab" and province_code != "BC" and province_code != "bc" and province_code != "ON" and province_code != "on" and province_code not in other_provinces:
        print("Province choice is invalid. Please restart the program and enter a valid province code.")
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
else:
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
