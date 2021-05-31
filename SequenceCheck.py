def main():
    print("Enter a sequence of non-decreasing numbers.")
    value = sequence_check()
    print("Thanks for playing!")
    print("Sequence length:", value)

def sequence_check():
    num1 = float(input("Enter num: "))
    count = 1
    num2 = float(input("Enter num: "))
    while num2 >= num1:
        count +=1
        num1 = num2
        num2 = float(input("Enter num: "))
    return count

if __name__ == "__main__":
    main()