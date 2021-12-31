import os
import platform

from categories import categories_list


def clear_console():
    system = platform.system()
    if system == "Linux" or system == "Darwin":
        os.system('clear')
    else:
        os.system('cls')


def invalid_input():
    clear_console()
    input("Invalid input\nPress enter")


def update_budget(total_budget, too_big):
    # saves the budget data into the budget file
    budget_file = open("budget.txt", 'w')
    budget_file.write(f"{total_budget}\n")
    if not too_big:
        for line in categories_list:
            budget_file.write(f"{line.money_allocated}\n")
    # resets the values for the budget data
    else:
        for i in range(len(categories_list)):
            budget_file.write(f"{0.0}\n")
    budget_file.close()


def get_budget():
    # checks for and creates the budget file
    if os.path.exists("budget.txt") is False:
        update_budget(0, False)

    # reads the budget values from the budget file into memory
    budget_file = open("budget.txt", 'r')
    budget_list = budget_file.readlines()
    budget_file.close()
    for i in range(len(budget_list)):
        temp = str(budget_list[i])
        temp = temp.rstrip()
        budget_list[i] = temp
    return budget_list


def sum_budget():
    # sums the individual budgets for each category
    sum = 0.0
    for item in range(len(categories_list)):
        sum += categories_list[item].money_allocated
    return sum


def category_budget(category_select, total_budget):
    clear_console()
    new_budget = float(
        input(f"Enter the amount of money you want to allocate to {categories_list[category_select].name}\n£"))
    # checks if the new category budget is less than the total budget
    if (sum_budget() - categories_list[category_select].money_allocated) + new_budget <= total_budget:
        # sets the new category budget to the inputted value
        clear_console()
        categories_list[category_select].money_allocated = new_budget
        print(
            f"{categories_list[category_select].name} budget is now £{new_budget}\nYour total unspent budget is £{total_budget - sum_budget()} ")
        update_budget(total_budget, False)
        input("Press enter")
        option_two(total_budget)

    else:
        clear_console()
        print(
            f"{categories_list[category_select].name} budget allocation failed\nThe budget you entered of £{new_budget} was £{((sum_budget() - categories_list[category_select].money_allocated) + new_budget) - total_budget} over your total budget of £{total_budget}")
        input("Press enter")
        option_two(total_budget)


def option_two(total_budget):
    while True:
        # displays the categories and their assigned budgets
        clear_console()
        print(f"Your current total budget is £{total_budget}\nYour current category budgets:")
        for item in range(len(categories_list)):
            print(f"{item + 1}: {categories_list[item].name}, £{categories_list[item].money_allocated}")
        print(f"Your total unspent budget is £{total_budget - sum_budget()}")

        # asks the user to select a category to re-budget
        try:
            category_select = (
                input("Enter the number of the category budget you want to modify\n(Enter n to go back)\n"))
            if category_select == 'n':
                main()
            else:
                category_budget(int(category_select) - 1, total_budget)
        except KeyboardInterrupt:
            exit()
        except:
            invalid_input()


def main():
    # allocates the budget values into memory
    budget_list = get_budget()
    for i in range(len(categories_list)):
        categories_list[i].money_allocated = round(float(budget_list[i + 1]), 2)
    total_budget = round(float(budget_list[0]), 2)

    while True:
        clear_console()
        print(f"Your current total budget is £{total_budget}")
        option = input("Press 1 to change your total budget/income\nPress 2 to manage your category budgets\n")
        if option == '1':
            # asks the user for a new budget
            while True:
                clear_console()
                print(f"Your current total budget is £{total_budget}")
                too_big = False
                print(f"If your new budget is less than £{sum_budget()} the category budgets will be reset to £0")
                # checks if the new budget is less than the sum of the category budgets
                try:
                    total_budget = float(input("Enter your total budget/income\n£"))
                    if total_budget < sum_budget():
                        too_big = True
                    update_budget(total_budget, too_big)
                    main()
                except KeyboardInterrupt:
                    exit()
                except:
                    invalid_input()

        elif option == '2':
            option_two(total_budget)
        else:
            invalid_input()


try:
    main()
except KeyboardInterrupt:
    exit()
