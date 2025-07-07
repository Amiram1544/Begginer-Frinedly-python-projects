#we want to read a file and count how many capital words it got



with open("File name with format", "r") as file:

    count = 0
    
    for word in file:
        if word.isupper():
            count += 1

    print(count)