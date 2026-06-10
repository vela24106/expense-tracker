expense = []

def add_expense():
    item={"date":"","catagory":"","amount":""}
    try:
        item["date"] = input("enter the date YYYY-MM-DD:" )
        item["catagory"] = input("enter the catagory :" )
        item["amount"] = int(input("enter the amount :" ))
    except Exception as e:
        print("something worng !!",e)
    else:
        expense.append(item)
    
def view_expense(expense):
    count =1
    for i in expense:
         print("expense",count,":\n","date : " + i["date"])
         print(" catagory : " + i["catagory"])
         print(" amount : " + str(i["amount"]))
         count +=1

def total_expense(expense):
    total = 0

    for i in expense:
        total = total + i["amount"]

    return total

def del_expense():
    if not expense:
        print ("NO EXPENSES")
    else:
        dele = int(input("enter the delete expense number : "))    
        if 1 <= dele <= len(expense):
            expense.pop(dele - 1)
            print("successfully deleted")

def save_expense():
    # try:
     with open("expense.txt","w")as f:
         for i in expense:
            #f.write(str(view_expense(expense)))
            f.write("date : " + str(i["date"]) + "\n")
            f.write("catagory : " + str(i["catagory"]) + "\n")
            f.write("amount : " + str(i["amount"]) + "\n")
    #except 
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
        try:
            choice = int(input("enter the choice :"))
        except ValueError:
            print("please enter the valied menu number")
            continue
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
                view_expense(expense)
                del_expense()
            
            case 5:
                save_expense()

            case 6:
                load_expense()
            case 7:
                break
            case _:
                print ("------invalid choice------")

           





