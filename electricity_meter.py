# Ask user to enter the Past meter reading and current meter reading.

def elec_bill():

    pmr = float(input("Enter the past meter reading: "))
    cmr = float(input("Enter the current meter reading: "))
    Units_Consumed = cmr - pmr

    if Units_Consumed > 0 and Units_Consumed <= 100:
        charges = 0.50*Units_Consumed
    elif Units_Consumed > 100 and Units_Consumed <= 200:
        charges = 50 + 1*(Units_Consumed-100)
    elif Units_Consumed > 200 and Units_Consumed <= 300:
        charges = 150 + 1.50*(Units_Consumed-200)
    else:
        charges = 300 + 2*(Units_Consumed-300)
    print("The charges are as given", charges)


elec_bill()
