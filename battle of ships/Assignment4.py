# I imported two libraries to take argument from user and to have the alphabet to use it later.
import string
import sys
places1 = []
places2 = []
shot1 = []
shot2 = []
move1_list = []
move2_list = []
check1_list = []
check2_list = []
b = 1
# I created a nested dict to use it later for showing the grids and keeping the info in one place.
player_dict = {}
copied_dict = {}
output_dict = {}
letters = string.ascii_uppercase[:10]
player_dict["Player1"] = {}
player_dict["Player2"] = {}
# This loop gives the names of the every cell of the grid.
for number in range(1, 11):
    for letter in letters:
        player_dict["Player1"][str(number) + letter] = "-"
        player_dict["Player2"][str(number) + letter] = "-"
for names in player_dict:
    output_dict[names] = {}
    for keys in player_dict[names]:
        output_dict[names][keys] = player_dict[names][keys]


def ship_replace():
    """This function converts the input file to a list then checks the elements of the list.
    If element is empty than it does nothing. Otherwise it changes the dict value as the element in the list.
    It does it for both players."""
    a = 0
    a_2 = 0
    places1 = plyr1_1_line.split(";")
    for i in range(len(places1)):
        if places1[i] != "":
            a += 1
            player_dict["Player1"][str(b) + letters[a-1]] = places1[i]
        else:
            a += 1
            player_dict["Player1"][str(b) + letters[a-1]] = "-"
    plyr2_1_line = g.readline()
    plyr2_1_line = plyr2_1_line.strip()
    places2 = plyr2_1_line.split(";")
    for j in range(len(places2)):
        if places2[j] != "":
            a_2 += 1
            player_dict["Player2"][str(b) + letters[a_2 - 1]] = places2[j]
        else:
            a_2 += 1
            player_dict["Player2"][str(b) + letters[a_2 - 1]] = "-"
    for each_name in player_dict:
        copied_dict[each_name] = {}
        for each_key in player_dict[each_name]:
            copied_dict[each_name][each_key] = player_dict[each_name][each_key]


def shots():
    plyr1_2_line = p.readline()
    shot1 = plyr1_2_line[:-1].split(";")
    for i in shot1:
        try:
            if len(i) == 3:
                row, column = str(int(i[0])), i[-1]
                move1 = row + column
                move1_list.append(move1)
            elif len(i) == 4:
                row, column = str(int(i[:2])), i[-1]
                move1 = row + column
                move1_list.append(move1)
            else:
                raise IndexError
        except ValueError:
            write_output("ValueError")
        except IndexError:
            write_output("It is not in the right format.")
    plyr2_2_line = s.readline()
    shot2 = plyr2_2_line[:-1].split(";")
    for i in shot2:
        try:
            if len(i) == 3:
                row, column = str(int(i[0])), i[-1]
                move2 = row + column
                move2_list.append(move2)
            elif len(i) == 4:
                row, column = str(int(i[:2])), i[-1]
                move2 = row + column
                move2_list.append(move2)
            else:
                raise IndexError
        except ValueError:
            write_output("ValueError")
        except IndexError:
            write_output("It is not in the right format.")
    moves = zip(move1_list, move2_list)
    return moves


def write_table():
    global table
    round = 1
    carrier1 = ["-"]
    battleship1 = ["-", "-"]
    destroyer1 = ["-"]
    submarine1 = ["-"]
    patrol1 = ["-", "-", "-", "-"]
    carrier2 = ["-"]
    battleship2 = ["-", "-"]
    destroyer2 = ["-"]
    submarine2 = ["-"]
    patrol2 = ["-", "-", "-", "-"]
    write_output("Battle of Ships Game\n\n")
    for x, y in shots():
        table = ""
        table += "Player1’s Move\n\n"
        table += f"Round : {round}\t\t\t\t\tGrid Size: 10x10\n\n"
        table += "Player1’s Hidden Board\t\tPlayer2’s Hidden Board\n"
        table += "  A B C D E F G H I J\t\t  A B C D E F G H I J"
        for i in range(1, 11):
            table += "\n"
            table += f"{i:<2}"
            for j in range(10):
                added_line = f" {output_dict['Player1'][str(i) + letters[j]]}"
                table += added_line
            table += " \t\t"
            table += f"{i:<2}"
            for k in range(10):
                added_line = f" {output_dict['Player2'][str(i) + letters[k]]}"
                table += added_line
        table += "\n\n"
        patrol_1 = patrol1[0] + ' ' + patrol1[1] + ' ' + patrol1[2] + ' ' + patrol1[3]
        patrol_2 = patrol2[0] + ' ' + patrol2[1] + ' ' + patrol2[2] + ' ' + patrol2[3]
        table +=  f"Carrier:\t\t{carrier1[0]}\t\t\t\tCarrier:\t\t{carrier2[0]}\nBattleship:\t{battleship1[0]+' '+battleship1[1]}\t\t\t\tBattleship:\t{battleship2[0]+' '+battleship2[1]}\n" \
                  f"Destroyer:\t{destroyer1[0]}\t\t\t\tDestroyer:\t{destroyer2[0]}\nSubmarine:\t{submarine1[0]}\t\t\t\tSubmarine:\t{submarine2[0]}\nPatrol Boat:\t{patrol_1}\t\t\tPatrol Boat:\t{patrol_2}\n\n"
        if round % 2 == 1:
            table += f"Enter your move: {x}\n"
        else:
            table += f"Enter your move: {y}\n"
        if player_dict["Player2"][x] == "-":
            output_dict["Player2"][x] = "O"
            copied_dict["Player2"][y] = "O"
        else:
            output_dict["Player2"][x] = "X"
            player_dict["Player2"][x] = "X"
            copied_dict["Player2"][y] = "X"
            values2 = player_dict["Player2"].values()
            if "C" not in values2:
                carrier2[0] = "X"
            if "B1" not in values2:
                battleship2[0] = "X"
            if "B2" not in values2:
                battleship2[1] = "X"
            if "D" not in values2:
                destroyer2[0] = "X"
            if "S" not in values2:
                submarine2[0] = "X"
            if "P1" not in values2:
                patrol2[0] = "X"
            if "P2" not in values2:
                patrol2[1] = "X"
            if "P3" not in values2:
                patrol2[2] = "X"
            if "P4" not in values2:
                patrol2[3] = "X"
        table += "Player2’s Move\n\n"
        table += f"Round : {round}\t\t\t\t\tGrid Size: 10x10\n\n"
        table += "Player1’s Hidden Board\t\tPlayer2’s Hidden Board\n"
        table += "  A B C D E F G H I J\t\t  A B C D E F G H I J"
        for i in range(1, 11):
            table += "\n"
            table += f"{i:<2}"
            for j in range(10):
                added_line = f" {output_dict['Player1'][str(i) + letters[j]]}"
                table += added_line
            table += " \t\t"
            table += f"{i:<2}"
            for k in range(10):
                added_line = f" {output_dict['Player2'][str(i) + letters[k]]}"
                table += added_line
        table += "\n\n"
        table += f"Carrier:\t\t{carrier1[0]}\t\t\t\tCarrier:\t\t{carrier2[0]}\nBattleship:\t{battleship1[0]+' '+battleship1[1]}\t\t\t\tBattleship:\t{battleship2[0]+' '+battleship2[1]}\n" \
                  f"Destroyer:\t{destroyer1[0]}\t\t\t\tDestroyer:\t{destroyer2[0]}\nSubmarine:\t{submarine1[0]}\t\t\t\tSubmarine:\t{submarine2[0]}\nPatrol Boat:\t{patrol_1}\t\t\tPatrol Boat:\t{patrol_2}\n\n"
        round += 1
        if round % 2 == 1:
            table += f"Enter your move: {x}\n"
        else:
            table += f"Enter your move: {y}\n"
        if player_dict["Player1"][y] == "-":
            output_dict["Player1"][y] = "O"
            copied_dict["Player1"][y] = "O"
        else:
            output_dict["Player1"][y] = "X"
            player_dict["Player1"][y] = "X"
            copied_dict["Player1"][y] = "X"
            values1 = player_dict["Player1"].values()
            if "C" not in values1:
                carrier1[0] = "X"
            if "B1" not in values1:
                battleship1[0] = "X"
            if "B2" not in values1:
                battleship1[1] = "X"
            if "D" not in values1:
                destroyer1[0] = "X"
            if "S" not in values1:
                submarine1[0] = "X"
            if "P1" not in values1:
                patrol1[0] = "X"
            if "P2" not in values1:
                patrol1[1] = "X"
            if "P3" not in values1:
                patrol1[2] = "X"
            if "P4" not in values1:
                patrol1[3] = "X"
        total1 = carrier1 + battleship1 + destroyer1 + submarine1 + patrol1
        total2 = carrier2 + battleship2 + destroyer2 + submarine2 + patrol2
        write_output(table)
        f_table = ""
        if "-" not in total1 or "-" not in total2:
            f_table += "Player1’s Board\t\tPlayer2’s Board\n"
            f_table += "  A B C D E F G H I J\t\t  A B C D E F G H I J"
            for i in range(1, 11):
                f_table += "\n"
                f_table += f"{i:<2}"
                for j in range(10):
                    added_line = f" {copied_dict['Player1'][str(i) + letters[j]]}"
                    f_table += added_line
                f_table += " \t\t"
                f_table += f"{i:<2}"
                for k in range(10):
                    added_line = f" {copied_dict['Player2'][str(i) + letters[k]]}"
                    f_table += added_line
            f_table += "\n\n"
            f_table += f"Carrier:\t\t{carrier1[0]}\t\t\t\tCarrier:\t\t{carrier2[0]}\nBattleship:\t{battleship1[0] + ' ' + battleship1[1]}\t\t\t\tBattleship:\t{battleship2[0] + ' ' + battleship2[1]}\n" \
                     f"Destroyer:\t{destroyer1[0]}\t\t\t\tDestroyer:\t{destroyer2[0]}\nSubmarine:\t{submarine1[0]}\t\t\t\tSubmarine:\t{submarine2[0]}\nPatrol Boat:\t{patrol_1}\t\t\tPatrol Boat:\t{patrol_2}\n\n"
        if "-" not in total1 and "-" in total2:
            write_output("Player1 Wins!\n")
            write_output(f_table)
            break
        elif "-" in total1 and "-" not in total2:
            write_output("Player2 Wins!\n")
            write_output(f_table)
            break
        elif "-" not in total1 and "-" not in total2:
            write_output("It is a Draw!\n")
            write_output(f_table)


def write_output(i):
    with open("Battleship.out", "a", encoding="utf-8") as z:
        z.write(i)
        print(i)


def check_ship():
    with open("OptionalPlayer1.txt", "r", encoding="utf-8") as o:
        check1 = o.readline()
        while True:
            if check1 == "" or check1 == "\n" or check1 == " ":
                break
            check1_list = check1.split(",")
            row = check1_list[0][3:]
            column = check1_list[1][0]
            in_letters = letters.index(column)
            if check1[0] == "B":
                for i in range(4):
                    if "down" in check1:
                        player_dict["Player1"][str(int(row)+i) + column] = check1[:2]
                    elif "right" in check1:
                        player_dict["Player1"][row + letters[in_letters + i]] = check1[:2]
            elif check1[0] == "P":
                for j in range(2):
                    if "right" in check1:
                        player_dict["Player1"][row + letters[in_letters + j]] = check1[:2]
                    elif "down" in check1:
                        player_dict["Player1"][str(int(row) + j) + column] = check1[:2]
            check1 = o.readline()
    with open("OptionalPlayer2.txt", "r", encoding="utf-8") as r:
        check2 = r.readline()
        while True:
            if check2 == "" or check2 == "\n" or check2 == " ":
                break
            check2_list = check2.split(",")
            row = check2_list[0][3:]
            column = check2_list[1][0]
            in_letters = letters.index(column)
            if check2[0] == "B":
                for k in range(4):
                    if "down" in check2:
                        player_dict["Player2"][str(int(row) + k) + column] = check2[:2]
                    elif "right" in check2:
                        player_dict["Player2"][row + letters[in_letters + k]] = check2[:2]
            elif check2[0] == "P":
                for l in range(2):
                    if "right" in check2:
                        player_dict["Player2"][row + letters[in_letters + l]] = check2[:2]
                    elif "down" in check2:
                        player_dict["Player2"][str(int(row) + l) + column] = check2[:2]
            check2 = r.readline()
# Firstly I checked whether there is enough argument or not.
output_doc = open("Battleship.out", "w", encoding="utf-8")
output_doc.close()


try:
    player1_txt = sys.argv[1]
    player2_txt = sys.argv[2]
    player1_in = sys.argv[3]
    player2_in = sys.argv[4]
    """ After I checked the files if there is a problem or not. If first file is opening then it checks the second and 
    the process goes like this."""
    try:
        with open(player1_txt, "r") as f:
            f.close()
        try:
            with open(player2_txt, "r") as g:
                g.close()
            try:
                with open(player1_in, "r") as p:
                    p.close()
                try:
                    with open(player2_in, "r") as s:
                        s.close()
                except IOError:
                    write_output(f"IOError: input file {player2_in} is not reachable.")
                #If all conditions are true the functions will be called.
                else:
                    with open(player1_txt, "r", encoding="utf-8") as f:
                        plyr1_1_line = f.readline()
                        plyr1_1_line = plyr1_1_line.strip()
                        g = open(player2_txt, "r", encoding="utf-8")
                        p = open(player1_in, "r", encoding="utf-8")
                        s = open(player2_in, "r", encoding="utf-8")
                        while True:
                            if plyr1_1_line == "" or plyr1_1_line == "\n" or plyr1_1_line == " ":
                                break
                            ship_replace()
                            b += 1
                            plyr1_1_line = f.readline()
                            plyr1_1_line = plyr1_1_line.strip()
                        check_ship()
                        shots()
                        write_table()
            except IOError:
                try:
                    with open(player2_in, "r") as s:
                        s.close()
                except IOError:
                    write_output(f"IOError: input files {player1_in} {player2_in} are not reachable. ")
                else:
                    write_output(f"IOError:input file {player1_in} is not reachable.")
        except IOError:
            try:
                with open(player1_in, "r") as p:
                    p.close()
                    try:
                        with open(player2_in, "r") as s:
                            s.close()
                        write_output(f"IOError: input file {player2_txt} is not reachable.")
                    except IOError:
                        write_output(f"IOError: input files {player2_txt} {player2_in} are not reachable.")
            except IOError:
                try:
                    with open(player2_in, "r") as s:
                        s.close()
                    write_output(f"IOError: input files {player2_txt} {player1_in} are not reachable.")
                except IOError:
                    write_output(f"IOError: input files {player2_txt} {player1_in} {player2_in} are not reachable.")
    #In this block only the first argument is wrong. It will control the others.
    except IOError:
        try:
            with open(player2_txt, "r") as g:
                g.close()
            try:
                with open(player1_in, "r") as p:
                    p.close()
                try:
                    with open(player2_in,"r") as s:
                        s.close()
                    write_output(f"IOError: input files {player1_txt} is not reachable.")
                except IOError:
                    write_output(f"IOError: input files {player1_txt} {player2_in} are not reachable.")
            except IOError:
                try:
                    with open(player2_in,"r") as s:
                        s.close()
                    write_output(f"IOError: input files {player1_txt} {player1_in} are not reachable.")
                except IOError:
                    write_output(f"IOError: input files {player1_txt} {player1_in} {player2_in} are not reachable.")
        # In this block two arguments are wrong it checks final two.
        except IOError:
            try:
                with open(player1_in, "r") as p:
                    p.close()
                try:
                    with open(player2_in,"r") as s:
                        s.close()
                    write_output(f"IOError: input files {player1_txt} {player2_txt} are not reachable.")
                except IOError:
                    write_output(f"IOError: input files {player1_txt} {player2_txt} {player2_in} are not reachable.")
            # It checks forth argument and first three arguments are wrong.
            except IOError:
                try:
                    with open(player2_in,"r") as s:
                        s.close()
                    write_output(f"IOError: input files {player1_txt} {player2_txt} {player1_in} are not reachable.")
                except IOError:
                    write_output(f"IOError: input files {player1_txt} {player2_txt} {player1_in} {player2_in} are not reachable.")
# If there is not enough argument it comes there.
except IndexError:
    write_output("IndexError: number of operands less than expected.")
except Exception:
    write_output("kaBOOM: run for your life!")
# Cansu ASLAN 2210356079
