# Expense Tracker Project

expenses = [] #list of expenses in form of dictionary
print("Welcome to Expense Tracker : Kharcha kam kiya karo ")

while True: 
print("====MENU====")
print("1. Add Expense")
print("2. View All Expenses")
print("3. View Total Kharcha")
print("4. Exit")

choice= input("Please Enter Your Choice : ")

#ADD Expense
if(choice ==1):
if(choice ==2):
if(choice ==3):
    date= input("Kis date par kharcha kiya tha?")
    category= input("Kis type ka kharcha kiya? (Food, Travel, Makeup, Books): ")
    description= input("Aur detail dedo: ")
    amount= float(input("Enter the amount: "))

    expense={
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    print(" \n DONE bro. Expense is added succesfully")

# 2. VIEW ALL Expenses
    if(choice == 2):
        if( len(expenses) ==0 ):
            print("No Expenses Added. Jao pehle kharcha karo. ")   
        else:
           print("===== Ye y apka sara expense =====")  
           coun= 1
           for eachKharcha in expenses:
                print(f"Kharcha Number {count} -> {eachKharcha["date"]}, {eachKharcha["category"]}, {eachKharcha["description"], {eachKharcha["amount"]}} ")    
                count= count+1
# 3. View Total Spending
     if(choice == 3):
         total=0
         for eachKharch in expensesList:
             total = toal + eachKharch["amount"] 

             print("\n TOTAL KHARCHA = ", total)             
#4. Exit
    elif(choice == 4):
     print("Dhanyawad aapne humara system use kiya") 
     break

else:
    print("INVALID CHOICE. TRY AGAIN") 

