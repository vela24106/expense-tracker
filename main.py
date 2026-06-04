print("\tEXPENSES TRAKER")
expense = []

def add_expense():
    add = int(input("enter the number : "))
    expense.append(add)
    
def view_expense(expense):
    count =1
    for i in expense:
         print ("expense",count,":",i)

         count +=1

def total_expense(expense):
    total = 0

    for i in expense:
        total = total + i

    return total

def del_expense():
    dele = int(input("enter the delete expense : "))
    if dele in expense:
        expense.remove(dele)

    else:
       print ("NO EXPENSES")
    

while True:
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. exit")
    choice = int(input("enter the choice :"))
    match choice:
        case 1 :
            print ("ADD EXPENSES")
            print ("------------")
            add_expense()

        case 2:
           print("view_expense")
           print("------------")
           view_expense(expense)
        
        case 3:
             print("Total Expense =", total_expense(expense))
        case 4:
            print ("DELETE EXPENSES")
            print ("---------------")
            del_expense()
            
        case 5:
             break

        case _:
            print("-----invalid choice-----")
