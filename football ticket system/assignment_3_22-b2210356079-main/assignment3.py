category = {}
column_dict = {}
row_dict = {}
import string
import sys
def create_category():
    category_name = line[15:26]
    row = int(line[27:29])
    column = int(line[30:])
    number_of_seats = row * column
    alphabet = string.ascii_uppercase[0:row]
    if category_name not in category:
        category[category_name] = {}
        column_dict[category_name] = column
        row_dict[category_name] = row
        for letter in alphabet:
            for j in range(column):
                str_j = str(j)
                category[category_name][letter+str_j] = "X"

        with open("output.txt", "a", encoding="utf-8") as o:
            o.write("The category {} having {} seats has been created.\n".format(category_name, number_of_seats))
        print("The category {} having {} seats has been created.".format(category_name, number_of_seats))
    else:
        with open("output.txt", "a", encoding="utf-8") as o:
            o.write("Warning: Cannot create the category for the second time. The stadium has already {}.\n".format(category_name))
        print("Warning: Cannot create the category for the second time. The stadium has already {}.".format(category_name))


def sell_ticket():
    sell_list = line[:-1].split(" ")
    if sell_list[3] in category:
        for i in range(len(sell_list)-4):
            if len(sell_list[4+i]) < 4:
                one_seat_name = sell_list[4 + i][0] + "0"
                number = sell_list[4 + i][1:]
                if one_seat_name not in category[sell_list[3]]:
                    if int(number) >= int(column_dict[sell_list[3]]):
                        with open("output.txt", "a", encoding="utf-8") as o:
                            o.write("Error: The category '{}' has less column and row than the specified index {}!\n".format(sell_list[3], sell_list[4 + i]))
                        print("Error: The category '{}' has less column and row than the specified index {}!".format(sell_list[3], sell_list[4 + i]))
                    else:
                        with open("output.txt", "a", encoding="utf-8") as o:
                            o.write("Error: The category '{}' has less column and row than the specified index {}!\n".format(sell_list[3], sell_list[4 + i]))
                        print("Error: The category '{}' has less column and row than the specified index {}!".format(sell_list[3], sell_list[4 + i]))
                elif int(number) >= int(column_dict[sell_list[3]]):
                    with open("output.txt", "a", encoding="utf-8") as o:
                        o.write("Error: The category '{}' has less column than the specified index {}!\n".format(sell_list[3],sell_list[4 + i]))
                    print("Error: The category '{}' has less column than the specified index {}!".format(sell_list[3],sell_list[4 + i]))
                else:
                    if sell_list[2] == "student":
                        category[sell_list[3]][sell_list[4 + i]] = "S"
                        with open("output.txt", "a", encoding="utf-8") as o:
                            o.write("Success: {} has bought {} at {}\n".format(sell_list[1],sell_list[4 + i],sell_list[3]))
                        print("Success: {} has bought {} at {}".format(sell_list[1],sell_list[4 + i],sell_list[3]))
                    elif sell_list[2] == "full":
                        category[sell_list[3]][sell_list[4 + i]] = "F"
                        with open("output.txt", "a", encoding="utf-8") as o:
                            o.write("Success: {} has bought {} at {}\n".format(sell_list[1], sell_list[4 + i], sell_list[3]))
                        print("Success: {} has bought {} at {}".format(sell_list[1], sell_list[4 + i], sell_list[3]))
                    elif sell_list[2] == "seasons":
                        category[sell_list[3]][sell_list[4 + i]] = "T"
                        with open("output.txt", "a", encoding="utf-8") as o:
                            o.write("Success: {} has bought {} at {}\n".format(sell_list[1], sell_list[4 + i], sell_list[3]))
                        print("Success: {} has bought {} at {}".format(sell_list[1], sell_list[4 + i], sell_list[3]))

            elif len(sell_list[4+i]) >= 4:
                check = sell_list[4+i].split("-")
                na = check[0][0]
                name = check[0][0] + "0"
                number = int(check[-1])
                if name not in category[sell_list[3]]:
                    if int(number) >= int(column_dict[sell_list[3]]):
                        with open("output.txt", "a", encoding="utf-8") as o:
                            o.write("Error: The category '{}' has less column and row than the specified index {}!\n".format(sell_list[3], sell_list[4 + i]))
                        print("Error: The category '{}' has less column and row than the specified index {}!".format(sell_list[3], sell_list[4 + i]))
                    else:
                        with open("output.txt", "a", encoding="utf-8") as o:
                            o.write("Error: The category '{}' has less row than the specified index {}!\n".format(sell_list[3], sell_list[4 + i]))
                        print("Error: The category '{}' has less row than the specified index {}!".format(sell_list[3], sell_list[4 + i]))
                elif int(number) >= int(column_dict[sell_list[3]]):
                    with open("output.txt", "a", encoding="utf-8") as o:
                        o.write("Error: The category '{}' has less column than the specified index {}!\n".format(sell_list[3], sell_list[4 + i]))
                    print("Error: The category '{}' has less column than the specified index {}!".format(sell_list[3], sell_list[4 + i]))
                else:
                    a = 1
                    for j in range(int(check[0][1:]),int(check[1])+1):
                        if not category[sell_list[3]][na + str(j)] == "X":
                            a = 0
                    if a == 1:
                        for j in range(int(check[0][1:]),int(check[1])+1):
                            if sell_list[2] == "student":
                                category[sell_list[3]][na + str(j)] = "S"
                            elif sell_list[2] == "full":
                                category[sell_list[3]][na + str(j)] = "F"
                            elif sell_list[2] == "seasons":
                                category[sell_list[3]][na + str(j)] = "T"
                        with open("output.txt", "a", encoding="utf-8") as o:
                            o.write("Success: {} has bought {} at {}\n".format(sell_list[1], sell_list[4 + i], sell_list[3]))
                        print("Success: {} has bought {} at {}".format(sell_list[1], sell_list[4 + i], sell_list[3]))
                    else:
                        with open("output.txt", "a", encoding="utf-8") as o:
                            o.write("Warning: The seats {} cannot be sold to {} due some of them have already been sold!\n".format(sell_list[4+i],sell_list[1]))
                        print("Warning: The seats {} cannot be sold to {} due some of them have already been sold!".format(sell_list[4+i],sell_list[1]))
    else:
        with open("output.txt", "a", encoding="utf-8") as o:
            o.write("Cannot be sold due to absence of asked {}\n".format(sell_list[3]))
        print("Cannot be sold due to absence of asked {}".format(sell_list[3]))


def cancel_ticket():
    cancel_list = line[:-1].split(" ")
    if cancel_list[1] in category:
        for cancel in range(len(cancel_list)-2):
            canceled_seat = cancel_list[2+cancel]
            letter = canceled_seat[0]
            letter_checked = letter + "0"
            ranged = canceled_seat[1:]
            if letter_checked not in category[cancel_list[1]]:
                if int(ranged) >= int(column_dict[cancel_list[1]]):
                    with open("output.txt", "a", encoding="utf-8") as o:
                        o.write("Error: The category '{}' has less column and row than the specified index {}!\n".format(cancel_list[1], cancel_list[2 + cancel]))
                    print("Error: The category '{}' has less column and row than the specified index {}!\n".format(cancel_list[1], cancel_list[2 + cancel]))
                else:
                    with open("output.txt", "a", encoding="utf-8") as o:
                        o.write("Error: The category '{}' has less row than the specified index {}!\n".format(cancel_list[1], cancel_list[2 + cancel]))
                    print("Error: The category '{}' has less row than the specified index {}!\n".format(cancel_list[1], cancel_list[2 + cancel]))
            elif int(ranged) >= int(column_dict[cancel_list[1]]):
                with open("output.txt", "a", encoding="utf-8") as o:
                    o.write("Error: The category '{}' has less column than the specified index {}!\n".format(cancel_list[1],cancel_list[2 + cancel]))
                print("Error: The category '{}' has less column than the specified index {}!\n".format(cancel_list[1],cancel_list[2 + cancel]))
            else:
                if category[cancel_list[1]][canceled_seat] != "X":
                    category[cancel_list[1]][canceled_seat] = "X"
                    with open("output.txt", "a", encoding="utf-8") as o:
                        o.write("Success: The seat {} at ’{}’ has been canceled and now ready to sell again\n".format(cancel_list[2 + cancel],cancel_list[1]))
                    print("Success: The seat {} at ’{}’ has been canceled and now ready to sell again\n".format(cancel_list[2 + cancel],cancel_list[1]))
                else:
                    with open("output.txt", "a", encoding="utf-8") as o:
                        o.write("Error: The seat {} at ’{}’ has already been free! Nothing to cancel\n".format(cancel_list[2 + cancel],cancel_list[1]))
                    print("Error: The seat {} at ’{}’ has already been free! Nothing to cancel\n".format(cancel_list[2 + cancel],cancel_list[1]))
    else:
        with open("output.txt", "a", encoding="utf-8") as o:
            o.write("Cannot be sold due to absence of asked {}\n".format(cancel_list[1]))
        print("Cannot be sold due to absence of asked {}\n".format(cancel_list[1]))


def balance():
    balance_list = line[:-1].split(" ")
    value_list = list(category[balance_list[1]].values())
    student = value_list.count("S")
    seasons = value_list.count("T")
    full = value_list.count("F")
    total = student*10 + seasons*250 + full*20
    empty =""
    first_line = f"Category report of {balance_list[1]}\n"
    empty += first_line
    second_line = f"{'--------------------------------'}\n"
    empty += second_line
    last_line = f"Sum of students = {student}, Sum of full pay = {full}, Sum of season ticket={seasons}, and\nRevenues = {total} Dollars\n"
    empty += last_line
    with open("output.txt", "a", encoding="utf-8") as o:
        o.write(empty+"\n")
    print(empty)


def show_category():
    show_list = line[:-1].split(" ")
    letters = string.ascii_uppercase[:column_dict[show_list[1]]]
    reversed_letters = letters[::-1]
    table = ""
    first_line = f"Printing category layout of {show_list[1]}"
    table += first_line
    for value in range(row_dict[show_list[1]]):
        table += f"\n"
        table += f"{reversed_letters[value]}"
        for number in range(column_dict[show_list[1]]):
            added_line = f"  {category[show_list[1]][reversed_letters[value]+str(number)]}"
            table += added_line
    table += "\n"
    table+= " "
    for i in range(column_dict[show_list[1]]):
        last_line = f" {i:<2}"
        table += last_line
    table += "\n"
    print(table)
    with open("output.txt", "a", encoding="utf-8") as o:
        o.write(table)

file = sys.argv[1]
with open("output.txt", "w", encoding="utf-8") as g:
    g.close()
with open(file, "a", encoding="utf-8") as f:
    f.write("\n")
with open(file, "r", encoding="utf-8") as f:
    line = f.readline()
    while True:
        if "CREATE" in line:
            create_category()
            line = f.readline()
        elif "SELLTICKET" in line:
            sell_ticket()
            line = f.readline()
        elif "CANCELTICKET" in line:
            cancel_ticket()
            line = f.readline()
        elif "BALANCE" in line:
            balance()
            line = f.readline()
        elif "SHOWCATEGORY" in line:
            show_category()
            line = f.readline()
        else:
            break