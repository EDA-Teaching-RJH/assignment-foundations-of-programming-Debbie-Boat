

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