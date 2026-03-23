def list_generator(vals_list):
    negative_vals = [vals_list[i] for i in range(len(vals_list)) if vals_list[i]<0]
    return negative_vals

def usual_cycle(vals_list):
    negative_vals = []
    for i in range (len(vals_list)):
        if vals_list[i]<0: negative_vals.append(vals_list[i])
    return negative_vals

vals_list = [-2,40,0,-5,3,-1,8]

if __name__ == "__main__":
    print("List generator:", list_generator(vals_list))
    print("Usual cycle:", usual_cycle(vals_list))
