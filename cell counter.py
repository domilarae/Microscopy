#main
#welcome message
#counter
#closing

def main():
    print ("Hematology Cell Counter")
    welcome()
    cell_count_by_user_input()
    count_again()


def welcome():
    print("Welcome to my hematology cell counter app. You may use this tool to assist with manual white cell differentials.")
    
def cell_count_by_user_input():
    sum = 0
    cells_seen = True

    c_1 = 0
    c_2 = 0
    c_3 = 0
    c_4 = 0
    c_5 = 0

    while cells_seen and sum <= 24 :
        user_input = (int(input("Enter the cell you see. (1 = neut, 2=lymph, 3=mono, 4=eos, 5=baso)")))

        if user_input == 1:
            c_1 = c_1 + 1
            sum = sum + 1
        elif user_input == 2:
            c_2 = c_2 + 1
            sum = sum + 1
        elif user_input == 3:
            c_3 = c_3 + 1
            sum = sum + 1
        elif user_input == 4:
            c_4 = c_4 + 1
            sum = sum + 1
        elif user_input == 5:
            c_5 = c_5 + 1
            sum = sum + 1
        else :
            print ("Your input is invalid, please try again.")


    print ("You have completed a manual cell count for ", sum, "white blood cells.")
    print ("Neutrophils =", c_1)
    print ("Lymphocyte =", c_2)
    print ("Monocytes =", c_3)
    print ("eosinophils =", c_4)
    print ("Basophils =", c_5)


def count_again():

    answer = True
    while answer :
        choice = (input("Would you like to perform another manual differential?(y or n)"))
        if choice == "y":
            print ("Okay. Let's count again!")
            answer = False
            cell_count_by_user_input()
        elif choice == "n":
            print ("Okay. Thanks for using my cell counter.")
        else :
            print ("I'm sorry, I don't understand your answer.")



main()

    
