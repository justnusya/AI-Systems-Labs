vals_list = [-2, 30, 8, -4, 0, 1, 5]
excludable = 8

def generator_filter_list(vals_list, excludable_num):
    new_list = [vals_list[i] for i in range(len(vals_list)) if vals_list[i]!=excludable_num]
    return new_list

def cycle_filter_list(vals_list, excludable_num):
    new_list = []
    for i in range(len(vals_list)):
        if vals_list[i]!=excludable_num: new_list.append(vals_list[i])
    return new_list

if __name__ == "__main__":
    print("Generator filter list:", generator_filter_list(vals_list, excludable))
    print("Cycle filter list:", cycle_filter_list
    (vals_list, excludable))