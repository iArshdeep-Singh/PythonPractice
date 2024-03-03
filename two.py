# Initialize lists to store salesperson data, sales table, and commission table
salespeople_data = []
sales_table = []
commission_table = []

# Function to calculate commission based on sales amount


def calculate_commission(sales_amount):
    if sales_amount <= 1000:
        return 20
    elif 1000 < sales_amount <= 2000:
        return 30
    elif 2000 < sales_amount <= 3000:
        return 40
    else:
        return 50


# Main loop for inputting salesperson data
while True:
    # Input salesperson's ID
    salesperson_id = input("Enter Salesperson's ID: ")

    # Input and validate sales amounts
    sales_amounts = []
    sales_labels = ['telephone', 'tablet', 'computer']
    for label in sales_labels:
        while True:
            amount = int(input(f"Enter {label} sales: "))
            if amount < 0:
                print(f"Invalid: Enter valid {label} sales.")
            else:
                sales_amounts.append(amount)
                break

    # Calculate commission for each sales category
    commissions = [calculate_commission(amount) for amount in sales_amounts]

    # Append salesperson data to lists
    salespeople_data.append((salesperson_id, *sales_amounts))
    sales_table.append((salesperson_id, *sales_amounts))
    commission_table.append((salesperson_id, *commissions))

    # Check if user wants to process another salesperson
    another_salesperson = input(
        "Do you want to process another Salesperson? (yes/no): ")
    if another_salesperson.lower() != 'yes':
        break

# Print sales table
print("\nSales Table:")
print("ID\tTelephone Sales\tTablet Sales\tComputer Sales")
totals = [0] * (len(sales_labels) + 1)
for data in sales_table:
    print("\t".join(str(x) for x in data))
    totals = [sum(x) for x in zip(totals, data[1:])]
print("Total\t" + "\t".join(str(x) for x in totals))

# Print commission table
print("\nCommission Table:")
print("ID\tTelephone Commission\tTablet Commission\tComputer Commission")
total_commissions = [0] * (len(sales_labels))
for data in commission_table:
    print("\t".join(str(x) for x in data))
    total_commissions = [sum(x) for x in zip(total_commissions, data[1:])]
print("Total\t" + "\t".join(str(x) for x in total_commissions))
