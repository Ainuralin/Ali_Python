def main():
    print("Task 1: Number greater than 7")
    try:
        number = float(input("Enter a number: "))
        if number > 7:
            print("Hello")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

    print("\nTask 2: Name check")
    name = input("Enter a name: ")
    if name == "John":
        print("Hello, John")
    else:
        print("There is no such name")

    print("\nTask 3: Multiples of 3")
    try:
        arr_input = input("Enter numbers separated by spaces: ")
        numbers = [int(x) for x in arr_input.split()]
        multiples_of_3 = [x for x in numbers if x % 3 == 0]
        print("Array elements that are multiples of 3:", multiples_of_3)
    except ValueError:
        print("Invalid input. Please enter only integers separated by spaces.")

if __name__ == "__main__":
    main()