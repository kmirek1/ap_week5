def joining_splitting1():
    # String Joining and Splitting:
    # Given the list 
    motto = ["Make", "haste", "slowly."]
    # a. Convert the list into a single string.
    single_string =''.join(motto)
    print(single_string)
    # b. Now, split the string at every occurrence of the letter 'a'.
    split_motto =single_string.split('a')
    print(split_motto)
