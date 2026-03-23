def main():
    list1 = input("Enter 1st list elements separated by spaces: ").split()
    list2 = input("Enter 2nd list elements separated by spaces: ").split()

    #Remove duplicates
    set1 = set(list1)
    set2 = set(list2)

    common_elements = sorted(list(set1 & set2))
    different_elements = sorted(list(set1 ^ set2))

    print("\nResults:")
    print(f"Same: {common_elements}")
    print(f"Different: {different_elements}")

if __name__ == "__main__":
    main()