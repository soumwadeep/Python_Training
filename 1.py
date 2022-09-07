def Sit():
    list_1=[]
    n=int(input("Enter No. Of List Element"))
    for x in range(0,n):
        element=int(input("Enter Element"))
        list_1.append(element)
    print("The List->",list_1)
    list_1.sort(reverse=True)
    print("Reverse->",list_1)
Sit()