#Write A Program In Python In 2 Different Method even(),odd() And Print The Even Odd Numbers With A Specific range->range() Function

# Method 1
def even():
    list_1=[]
    n=int(input("Enter No. Of List Element"))
    for x in range(0,n):
        element=int(input("Enter Element"))
        list_1.append(element)
    print("The List->",list_1)
    y= tuple(list_1)
    x=list(y)
even()

# Method 2
# def odd():
#     list_1=[]
#     n=int(input("Enter No. Of List Element"))
#     for x in range(0,n):
#         element=int(input("Enter Element"))
#         list_1.append(element)
#     print("The List->",list_1)
#     y= tuple(list_1)
# odd()