if __name__ == '__main__':
    s = input()
    for methods in ['isalnum','isalpha','isdigit','islower','isupper']:
        print(any(eval('c.'+methods+'()') for c in s))

