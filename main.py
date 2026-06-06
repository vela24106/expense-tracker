expense = []

def add_expense():
    add = int(input("enter the number : "))
    expense.append(add)
    
def view_expense(expense):
    count =1
    for i in expense:
         print("expense",count,":",i)
         
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


def save_expense():
    
     with open("expense.txt","w")as f:
         for i in expense:
            f.write(str(i) + "\n")
     print("saved")

def load_expense():
    expense.clear()
    with open("expense.txt","r")as f:
        for line in f:
            value = int(line.strip())
            expense.append(value)

    print("loaded !!!")
           
while True:
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Save Expense")
    print("6. Load_Expense")
    print("7. Exit")
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
             save_expense()

        case 6:
            load_expense()
        case 7:
            break

        case _:
            print("-----invalid choice-----")





