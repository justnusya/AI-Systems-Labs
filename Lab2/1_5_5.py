groups_data = {
    "Group1": {
        "students_count": 25,
        "head": "Johnsonyuk John Johnsovych"
    },
    "Group2": {
        "students_count": 30,
        "head": "Gupalo Mykhaylo Panasovych"
    },
    "Group3": {
        "students_count": 22,
        "head": "Perepletypole Maria Ivanivna"
    }
}

def get_students_count(group_name):
    if group_name not in groups_data:
        print(f"Group '{group_name}' does not exist")
        return None
    return groups_data[group_name]["students_count"]

def get_head_info(group_name):
    if group_name not in groups_data:
        print(f"Group '{group_name}' does not exist")
        return None
    return groups_data[group_name]["head"]

def create_tuple_list(groups, condition, number):
    if condition == "less_equal":
        result = [(name, groups_data[name]["students_count"]) 
                  for name in groups 
                  if groups_data[name]["students_count"] <= number]
        
    elif condition == "greater_equal":
        result = [(name, groups_data[name]["students_count"]) 
                  for name in groups 
                  if groups_data[name]["students_count"] >= number]
    else:
        return "Invalid condition"

    if not result:
        return "No such group exists"

    print("Created successfully.")
    return result

def change_students_count(group_name, new_count):
    if group_name not in groups_data:
        print(f"Group '{group_name}' does not exist.\n")
        return False
    if new_count < 0:
        print("Student count cannot be negative.\n")
        return False

    groups_data[group_name]["students_count"] = new_count
    return True

def change_head_data(group_name, new_data):
    if group_name not in groups_data:
        print(f"Group '{group_name}' does not exist.\n")
        return False

    groups_data[group_name]["head"] = new_data
    return True

def add_new_group(group_name, count, head_data):
    if group_name in groups_data:
        print("Group already exists.\n")
        return
    
    if count < 0:
        print("Student count cannot be negative.\n")
        return

    if not head_data.strip():
        print("Head data cannot be empty.\n")
        return

    groups_data[group_name] = {
        "students_count": count,
        "head": head_data
    }
    print("Group added successfully.\n")
    
def delete_group(group_name):
    if group_name not in groups_data:
        print(f"Group '{group_name}' does not exist.\n")
        return

    del groups_data[group_name]
    print("Deleted successfully.\n")

def get_heads_of_groups(group_names):
    result = []
    for group_name in group_names:
        group_name = group_name.strip()
        if group_name not in groups_data:
            print(f"Group '{group_name}' does not exist.")
            continue
        result.append(groups_data[group_name]["head"])
    return result

def list_all_groups():
    print("Here are all groups: ")
    return print(groups_data)

def commands_print():
    print("\nIn this program you can perfom the following operations: ")
    print("0 - Exit")
    print("1 - List all operations")
    print("2 - Get student amount in the [group_name]")
    print("3 - Get info about head of the [group_name]")
    print("4 - Create tuple list of all groups whose amount is <= [number]")
    print("5 - Create tuple list of all groups whose amount is >= [number]")
    print("6 - Change student amount in the [group_name] to [number]")
    print("7 - Change head data in the [group_name] to [data]")
    print("8 - Add new group with [group_name], [student_amount] and [head_data]")
    print("9 - Delete group with [group_name]")
    print("10 - Get heads of groups [<group_names>]")
    print("11 - List all groups \n")

isFirstMessage = True

while True:
    if isFirstMessage: 
        commands_print()
        isFirstMessage = False

    match input("Enter the number of operation: "):
        case "0": exit()
        case "1": commands_print()
        case "2": 
            group = input("Enter group name: ")
            students_count = get_students_count(group)
            if students_count is not None:
                print(students_count)
        case "3":
            group = input("Enter group name: ")
            head_info = get_head_info(group)
            if head_info is not None:
                print(head_info)
        case "4":
            number = int(input("Enter number: "))
            print(create_tuple_list(groups_data.keys(), "less_equal", number), "\n")
        case "5":
            number = int(input("Enter number: "))
            print(create_tuple_list(groups_data.keys(), "greater_equal", number), "\n")
        case "6":
            group = input("Enter group name: ")
            new_count = int(input("Enter new student amount:"))
            if change_students_count(group, new_count):
                print("Changes have been made successfully.")
                print("Student count for", group, "is now:", get_students_count(group), "\n")
        case "7":
            group = input("Enter group name: ")
            new_data = input("Enter new head data: ")
            if change_head_data(group, new_data):
                print("Changes have been made successfully.")
                print("Head of", group, "is now:", get_head_info(group), "\n")
        case "8":
            group_name = input("Enter new group name: ")
            count = int(input("Enter student amount: "))
            head_data = input("Enter head data: ")
            add_new_group(group_name, count, head_data)
        case "9":
            group = input("Enter group name: ")
            delete_group(group)
        case "10": 
            group_names = input("Enter group names (comma-separated): ").split(",")
            print(get_heads_of_groups(group_names), "\n")
        case "11": list_all_groups()
        case _: print("Wrong input, try again \n")