n = int(input('enter no.'))      # taking input from the user.
prime_lis = []                   # list to contain prime numbers.
for num in range(1, n+1):        #      range upto n+1 because we want to calculate upto n.
    flag = 0                     # flag used here to confirm if a number is prime or not.
    for div in range(2, n//2+1): #      we will divide upto half of the num and here is used floor division to get only +ve value.
        if num == div:           # if both are same then we will,
            continue             #      jump to the next num 
        if num%div == 0:         # checking if num is divisible by div,
            flag = 1             #      then flag = 1
    if flag == 0:                # after exiting div loop if flag value didn't change then,
        prime_lis.append(num)    #      append that num in list.
print(prime_lis)                 
