# Write your code below this line 👇
def prime_checker(num):
    if num < 2:
        print("It's not a prime number.")
        return False
    for div_num in range(2, int(num**0.5) + 1):
        if num % div_num == 0:
            print("It's not a prime number.")
            return False
    print("It's a prime number.")
    return True


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(num=n)
