#Wrong Code
# if __name__ == '__main__':
#     s = raw_input()
#     if s.isalnum():
#         print("True")
#     else:
#         print("False")
    
#     if s.isalpha():
#         print("True")
#     else:
#         print("False")
        
#     if s.isdigit():
#         print("True")
#     else:
#         print("False")
        
#     if s.islower():
#         print("True")
#     else:
#         print("False")
        
#     if s.isupper():
#         print("True")
#     else:
#         print("False")

# Another Solution Still Wrong #
if __name__ == '__main__':
    s = input()
    for c in s:
        val = False
        if c.isalnum():
            val=True
    print(val)
    for c in s:
        val = False
        if c.isalpha():
            val=True
    print(val)
        
    for c in s:
        val = False
        if c.isdigit():
            val=True
    print(val)
        
    for c in s:
        val = False
        if c.islower():
            val=True
    print(val)
        
    for c in s:
        val = False
        if c.isupper():
            val=True
    print(val)
