#Write your code below this line 👇



Divided_number = (number / 2)
Not_even_number = (number % 2)


Our attempt:

def prime_checker(number):
    numbers = list(range(0, number + 1))
    Chosen_number = numbers[number]
    excluded_numbers = [Chosen_number, 1, 0]

    for num in numbers:
        if num not in excluded_numbers:
            capture = int()
            capture += num
            calculation = number % capture
            listed_calc = [calculation]
            str_listed = str(listed_calc)
            capture_2 = ("")
            final_combination = capture_2 + str_listed
            
    print(final_combination)        
   

    # print(num)

    # if 0 in listed_calc:
    #     print("Its not a prime number")

    # elif 0 not in listed_calc:
    #     print("Its a prime number.")   


            # print(listed_calc)
            # str_listed = [str(int) for int in listed_calc]
            # print(str_listed)

 
             



# if not n == 1 or n == 2

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
