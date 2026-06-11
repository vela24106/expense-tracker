import json
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
        else:
            print("Invalid expense number")

def save_expense():
    #save = view_expense(expense)
    try:
        with open("expense.json","w")as f:
            json.dump(expense,f,indent=4)
            print("saved")
    except FileNotFoundError:
        print("file not found")
        
def load_expense():
        try:
            with open("expense.json","r")as f:
                data = json.load(f)
                expense.clear()
                expense.extend(data)
                print("loaded !!!")
    
        except FileNotFoundError:
            print("No saved expenses found")

def edit_expense():
    view_expense(expense)
    num=int(input("enter the edit expense number :"))
    index = num - 1
    if 0 <= index < len(expense):
            print(expense[index])
            new_category = input("enter the new category :")
            new_amount = int(input("enter the new amount :"))
            expense[index]["catagory"] = new_category
            expense[index]["amount"] = new_amount

            print("edit sucessfully")
    else:
        print("expense not found")


def manage_expense():
    print("1.edit")
    print("2.delete")
    sub_choice = int(input("enter the choice :"))
    
    match sub_choice:
        case 1:
          edit_expense()
        case 2:
          print ("DELETE EXPENSES")
          print ("---------------")
          view_expense(expense)
          del_expense()  

while True:
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Total Expense")
        print("4. Manage Expense")
        print("5. Save Expense")
        print("6. Load_Expense")
        print("7. Exit")
        #print("8. Exit")
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
               manage_expense()
            case 5:
                save_expense()

            case 6:
                load_expense()
                #print("loed expense is on going process not completed come later !!")

            case 7:
                 break
            
            case _:
                print ("------invalid choice------")

           





