def is_prime(number):
    for i in range(2, number):
        if number%i == 0:
            return print('False')
        else:
            return print('True')
        
is_prime(int(input()))