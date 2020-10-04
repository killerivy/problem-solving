def count_substring(string, sub_string):
    a = len(string)
    b = len(sub_string)
    counter = 0
    for i in range(0,a):
        counter += string.count(sub_string,i,i+b)
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)