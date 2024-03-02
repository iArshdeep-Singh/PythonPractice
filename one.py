# declare list variables
id = []
telephoneSales = []
tabletSales = []
computerSales = []
totalSales = []


# get input
while True:

    id.append(int(input("\n-> Enter Salesperson's ID: ")))
    print("\n")

    labels = ["telephone", "tablet", "computer"]

    for label in labels:

        while True:

            amount = int(input(f"Enter {label} sales: "))

            if amount < 0:
                print("INVALID: Enter Valid Input\n")
            else:
                if label == "telephone":
                    telephoneSales.append(amount)
                    break
                elif label == "tablet":
                    tabletSales.append(amount)
                    break
                elif label == "computer":
                    computerSales.append(amount)
                    break
                else:
                    break

    proceed = input(
        "\nDo you want to process another Salesperson?\nPress 1 to continue and press any key to terminate: ")
    if proceed == '1':
        continue
    else:
        break


# calculate sales
labels = ["telephone", "tablet", "computer"]

for label in labels:

    while True:
        if label == 'telephone':
            tel = 0
            for i in telephoneSales:
                tel += i
            totalSales.append(tel)
            break

        elif label == 'tablet':
            tab = 0
            for i in tabletSales:
                tab += i
            totalSales.append(tab)
            break

        elif label == 'computer':
            com = 0
            for i in computerSales:
                com += i
            totalSales.append(com)
            break
        else:
            break

# calculate commission


# print sales table
print("\nSales Table-\n| Id  \t| Telephones \t| Tablets \t| Computers")

x = 0

while x < len(id):
    print(f"| {id[x]}  \t| {telephoneSales[x]} \t\t| {tabletSales[x]} \t\t| {computerSales[x]}")
    x += 1

print(f"| Total | {totalSales[0]} \t\t| {totalSales[1]} \t\t| {totalSales[2]}")


# print commission table
print("\n\nCommission Table-\n| Id  \t| Telephones \t| Tablets \t| Computers")