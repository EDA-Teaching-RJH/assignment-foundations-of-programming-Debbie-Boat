

def init_database():
    n = ["Picard", "Riker", "Data", "Worf", "Spock"]
    r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lt. Commander"]
    d = ["Command", "Command", "Operations", "Security", "Command", "Operations"]
    i = ["1", "2", "3", "4", "5"]

    return n, r, d, i

def display_menu():
    print("")
    print("--- MENU ---")
    print("1) Display Roster")
    print("2) Add Crew Member")
    print("3) Remove Crew Member")
    print("4) Update Crew Rank")
    print("5) Update Crew Name")
    print("6) Filter By Division")
    print("7) Calculate Crew Payroll")
    print("8) Count Officers")

    option = input("Select Option: ")

    return option

def add_member(n, r, d, i):
    new_name = input("Enter Name: ")
    n.append(new_name)

    new_rank = input("Enter Rank: ")
    if new_rank == "Captain" or new_rank == "Commander" or new_rank == "Lt. Commander" or new_rank == "Lieutenant":
        r.append(new_rank)

    else:
        print("Invalid. ")
        add_member(n, r, d, i)

    new_division = input("Enter Division: ")
    d.append(new_division)

    new_id = input("Enter ID: ")
    for ii in range(len(i)):
        if new_id == i[ii]:
            print("Invalid. ")
            add_member(n, r, d, i)

        else:
            i.append(new_id)

    return n, r, d, i

def remove_member(n, r, d, i):
    option = input("Enter ID of record to remove: ")

    idx = i.index(option)
    n.pop(idx)
    r.pop(idx)
    d.pop(idx)
    i.pop(idx)

    return n, r, d, i

def update_rank(n, r, i):
    idToChange = input("Enter the ID for rank changes: ")
    new_rank = input("Enter new rank: ")

    for ii in range(len(i)):
        if i[ii] == idToChange:
            r[ii] = new_rank

def display_roster(n, r, d, i):
    print(f"{'Name':<10} {'Rank' :<10} {'Division':>10} {'ID':>5}")

    for ii in range(len(n)):
        print(f"{n[ii]:<10} {r[ii]:<10} {d[ii]:>10} {i[ii]:>5}")

        