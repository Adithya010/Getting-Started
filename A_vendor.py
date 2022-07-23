
# if else to select which is more
# bring in discount through total=amt-discount

def compute_discount():
    print("1. Battery Based. ")
    print("2. Key Based. ")
    print("3. Electrical Based. ")
    opt = int(input("Select an option from 1,2 or 3 from the list:- "))
    amt = float(input("Enter the amount:- "))
    if opt == 1:
        if amt >= 1000:
            dis = amt*0.1
        else:
            dis = 0
    elif opt == 2:
        if amt >= 100:
            dis = amt*0.05
        else:
            dis = 0
    elif opt == 3:
        if amt >= 500:
            dis = amt*0.1
        else:
            dis = 0
    else:
        print("The selected product is not available! ")

    bill_would_be = amt-dis
    print("The bill amount would be", bill_would_be)


compute_discount()
