isDLL = input("Are you current student of DLL ( yes / no ) :    ")

if isDLL.lower() == "yes":
        print("Welcome to the DLL BSIT Scholarship form")
        isGG = input("Are you from Brgy Gulang - Gulang ( yes / no ) :   ")

        if isGG.lower() == "yes" :
                print("Please fill up the second form ")
                isLevel = input("What is your cuurrent year level right now in DLL\nF-Freshmen\nS-Sophomore\nJ-Junior\nR-Senior\nPlease input your answer")
                if isLevel.lower() == 'f':
                        print("Hi Freshmen")
                elif isLevel.lower() == 's':
                        print("Hi Sophomore")
                elif isLevel.lower() == 'j':
                        print("Hi junior")
                elif isLevel.lower() == 'r':
                        print("Hi Senior")
                else:
                        print("")