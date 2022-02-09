if __name__ == '__main__':
    s = input()
    for c in s:
        val = False
        if c.isalnum():
            val=True
            break
    print(val)
    for c in s:
        val = False
        if c.isalpha():
            val=True
            break
    print(val)
        
    for c in s:
        val = False
        if c.isdigit():
            val=True
            break
    print(val)
        
    for c in s:
        val = False
        if c.islower():
            val=True
            break
    print(val)
        
    for c in s:
        val = False
        if c.isupper():
            val=True
            break
    print(val)
