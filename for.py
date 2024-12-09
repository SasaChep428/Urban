numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for flag_1 in numbers:
    if flag_1 != 1:
        for flag_2 in range(2, flag_1+1):
            if flag_1 - flag_2 == 0:
                print(flag_1, "true")
                primes.append(flag_1)
            elif flag_1 % flag_2 == 0:
                print(flag_1, "false")
                not_primes.append(flag_1)
                break
print(primes)
print(not_primes)