# declare list variables
id = [] 

telephoneSales = []
tabletSales = []
computerSales = []
totalSales = []

telephoneCommission = []
tabletCommission = []
computerCommission = []
totalCommission = []


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
                    if amount < 1000:
                        telephoneCommission.append(20)
                    elif 1000 < amount <= 2000:
                        telephoneCommission.append(30)
                    elif 2000 < amount <= 3000:
                        telephoneCommission.append(40)
                    elif amount >= 3000:
                        telephoneCommission.append(50)
                    break

                elif label == "tablet":
                    tabletSales.append(amount)
                    if amount < 1000:
                        tabletCommission.append(30)
                    elif 1000 < amount <= 2000:
                        tabletCommission.append(40)
                    elif 2000 < amount <= 3000:
                        tabletCommission.append(50)
                    elif amount >= 3000:
                        tabletCommission.append(60)
                    break
                
                elif label == "computer":
                    computerSales.append(amount)
                    if amount < 1000:
                        computerCommission.append(40)
                    elif 1000 < amount <= 2000:
                        computerCommission.append(50)
                    elif 2000 < amount <= 3000:
                        computerCommission.append(60)
                    elif amount >= 3000:
                        computerCommission.append(70)
                    break
                    
                else:
                    break

    proceed = input("\nDo you want to process another Salesperson?\nPress 1 to continue and press any key to terminate: ")
    if proceed == '1':
        continue
    else:
        break



# calculate sales
totalSales = [sum(telephoneSales), sum(tabletSales), sum(computerSales)]

# calculate commission
totalCommission = [sum(telephoneCommission), sum(tabletCommission), sum(computerCommission)]


# print sales table
print("\nSales Table-\n| Id  \t| Telephones \t| Tablets \t| Computers")

x = 0

while x < len(id):
    print(f"| {id[x]}  \t| {telephoneSales[x]} \t\t| {tabletSales[x]} \t\t| {computerSales[x]}")
    x += 1

print(f"| Total | {totalSales[0]} \t\t| {totalSales[1]} \t\t| {totalSales[2]}")


# print commission table
print("\n\nCommission Table-\n| Id  \t| Telephones \t| Tablets \t| Computers")

y = 0

while y < len(id):
    print(f"| {id[y]}  \t| {telephoneCommission[y]} \t\t| {tabletCommission[y]} \t\t| {computerCommission[y]}")
    y += 1

print(f"| Total | {totalCommission[0]} \t\t| {totalCommission[1]} \t\t| {totalCommission[2]}")
