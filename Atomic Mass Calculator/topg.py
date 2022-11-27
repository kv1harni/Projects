import csv, sys, os


# Dictionary of all elements matched with their atomic masses.
elements_dict = {'H' : 1.008,'HE' : 4.003, 'LI' : 6.941, 'BE' : 9.012,\
                 'B' : 10.811, 'C' : 12.011, 'N' : 14.007, 'O' : 15.999,\
                 'F' : 18.998, 'NE' : 20.180, 'NA' : 22.990, 'MG' : 24.305,\
                 'AL' : 26.982, 'SI' : 28.086, 'P' : 30.974, 'S' : 32.066,\
                 'CL' : 35.453, 'AR' : 39.948, 'K' : 39.098, 'CA' : 40.078,\
                 'SC' : 44.956, 'TI' : 47.867, 'V' : 50.942, 'CR' : 51.996,\
                 'MN' : 54.938, 'FE' : 55.845, 'CO' : 58.933, 'NI' : 58.693,\
                 'CU' : 63.546, 'ZN' : 65.38, 'GA' : 69.723, 'GE' : 72.631,\
                 'AS' : 74.922, 'SE' : 78.971, 'BR' : 79.904, 'KR' : 84.798,\
                 'RB' : 84.468, 'SR' : 87.62, 'Y' : 88.906, 'ZR' : 91.224,\
                 'NB' : 92.906, 'MO' : 95.95, 'TC' : 98.907, 'RU' : 101.07,\
                 'RH' : 102.906, 'PD' : 106.42, 'AG' : 107.868, 'CD' : 112.414,\
                 'IN' : 114.818, 'SN' : 118.716, 'PR' : 140.908, 'ND' : 144.243,\
                 'PM' : 144.913, 'SM' : 150.36, 'EU' : 151.964, 'GD' : 157.25,\
                 'TB' : 158.925, 'DY': 162.5011, 'SB' : 121.760, 'TE' : 126.7,\
                 'I' : 126.904, 'XE' : 131.294, 'CS' : 132.905, 'BA' : 137.328,\
                 'LA' : 138.905, 'CE' : 140.10, 'HO' : 164.930, 'ER' : 167.259,\
                 'TM' : 168.934, 'YB' : 173.055, 'LU' : 174.967, 'HF' : 178.49,\
                 'TA' : 180.948, 'W' : 183.84, 'RE' : 186.207, 'OS' : 190.23,\
                 'IR' : 192.217, 'PT' : 195.085, 'AU' : 196.967, 'HG' : 200.592,\
                 'TL' : 204.383, 'PB' : 207.2, 'BI' : 208.980, 'PO' : 208.982,\
                 'AT' : 209.987, 'RN' : 222.081, 'FR' : 223.020, 'RA' : 226.025,\
                 'AC' : 227.028, 'TH' : 232.038, 'PA' : 231.036, 'U' : 238.029,\
                 'NP' : 237, 'PU' : 244, 'AM' : 243, 'CM' : 247, 'BK' : 247,\
                 'CT' : 251, 'ES' : 252, 'FM' : 257, 'MD' : 258, 'NO' : 259,\
                 'LR' : 262, 'RF' : 261, 'DB' : 262, 'SG' : 266, 'BH' : 264,\
                 'HS' : 269, 'MT' : 268, 'DS' : 271, 'RG' : 272, 'CN' : 285,\
                 'NH' : 284, 'FL' : 289, 'MC' : 288, 'LV' : 292, 'TS' : 294,\
                 'OG' : 294}





# List of all elements to allow for easy inclusion testing.
elements_list = ['H', 'HE', 'LI', 'BE', 'B', 'C', 'N', 'O', 'F', 'NE', 'NA',\
                 'MG', 'AL', 'SI', 'P', 'S', 'CL', 'AR', 'K', 'CA', 'SC', 'TI',\
                 'V', 'CR', 'MN', 'FE', 'CO', 'NI', 'CU', 'ZN', 'GA', 'GE',\
                 'AS', 'SE', 'BR', 'KR', 'RB', 'SR', 'Y', 'ZR', 'NB', 'MO',\
                 'TC', 'RU', 'RH', 'PD', 'AG', 'CD', 'IN', 'SN', 'SB', 'TE',\
                 'I', 'XE', 'CS', 'BA', 'LA', 'CE', 'PR', 'ND', 'PM', 'SM',\
                 'EU', 'GD', 'TB', 'DY', 'HO', 'ER', 'TM', 'YB', 'LU', 'HF',\
                 'TA', 'W', 'RE', 'OS', 'IR', 'PT', 'AU', 'HG', 'TL', 'PB',\
                 'BI', 'PO', 'AT', 'RN', 'FR', 'RA', 'AC', 'TH', 'PA', 'U',\
                 'NP', 'PU', 'AM', 'CM', 'BK', 'CT', 'ES', 'FM', 'MD', 'NO',\
                 'LR', 'RF', 'DB', 'SG', 'BH', 'HS', 'MT', 'DS', 'RG', 'CN',\
                 'NH', 'FL', 'MC', 'LV', 'TS', 'OG']






def atomicMassCalculator():
    print('************************************************************************************************************************')
    print('                                   KENDRIYA VIDYALAYA No.1,VADODARA     ')
    print('************************************************************************************************************************')
    print('                                         ATOMIC MASS CALCULATOR            ')                                        
    print('                                 Developed by: Milind and Vikramaditya   ')
    print('                                             YEAR: 2022-2023                ')
    print('************************************************************************************************************************')
    print("     Enter the formula for the substance by seperating the atomic symbols\
    from their subscripts. ie. C 6 H 12 O 6.")
    print('************************************************************************************************************************')



    # Get the substance's formula from user.
    formula = input("                         Enter a formula or type 'q' to quit:").upper().split()
    print()

    # Continue to ask for a new formula until the user inputs a "q" for quit.
    # while formula != ["Q"]:
    while True:
        if formula != ["Q"]:
            # Set the conditons for a new loop.
            atomic_mass_float = 0.0
            invalid_input = False
            coefficient = 1
            
            # Loop through each index in the formula.
            for i, ch in enumerate(formula):
                # If the character is an element, check if the next character in the
                # formula is an integer.
                if ch in elements_list:
                    element_mass = elements_dict.get(ch)
                    # If the next character is an integer, multiply the element's mass 
                    # by that integer and add it to the running sum.
                    if formula[i + 1].isdigit() == True:
                        atomic_mass_float += element_mass * int(formula[i + 1])
                    # If not, just add that element's mass to the sum.
                    else:
                        atomic_mass_float += element_mass
                # If the charcter is an integer
                elif ch.isdigit() == True:
                    # If the first index is an integer, assume that that is a
                    # coefficient for the formula and multiply the formula by that
                    # number
                    if i == 0:
                        coefficient = int(ch)
                    # Make sure the previous index wasn't an integer as well
                    # (the integer needs an element to multiply), if it was, let the
                    # program know that there is an error.
                    elif formula[i - 1].isalpha() == False:
                        invalid_input = True
                    else:
                        pass
                # If the only character in the formula is an integer, let the program
                # know that there is an error.
                elif ch.isdigit() == True and len(formula) == 1:
                    invalid_input = True
                # If a character is not an element or an integer, let the program know
                # that there is an error.
                else:
                    invalid_input = True
            
            # Muliply the entire atomic mass by the coefficient.
            atomic_mass_float *= coefficient
            
            # If there was an error in the program, display the appropriate error.
            if invalid_input == True:
                # Error for if there is only an integer entered.
                if ch.isdigit() == True and len(formula) == 1:
                    print("You must enter at least one element for every integer\
        subscript.")
                    print()
                # Error for if there is a float or non-elemnt entered.
                else:
                    print("Please enter only the atomic symbols of elements or an integer\
        subscript.")
                    print()
            
            # If there was no error, then print the claculated atomic mass
            else:
                print("Atomic Mass: ", round(atomic_mass_float, 3))
                print()
            
            # Ask for another formula.
            formula = input("Enter a formula or type 'q' to quit: ").upper().split()
            print()

        elif formula == ["Q"]:
            menu()







def elementInfo():
    print('************************************************************************************************************************')
    print('                                   KENDRIYA VIDYALAYA No.1,VADODARA     ')
    print('************************************************************************************************************************')
    print('                                          PERIODIC TABLE           ')                                        
    print('                                 Developed by: Milind and Vikramaditya   ')
    print('                                             YEAR: 2022-2023                ')
    print('************************************************************************************************************************')


    # Read in all the data from periodictable.csv.
    elementsFile = open('periodictable.csv', encoding='utf-8')
    elementsCsvReader = csv.reader(elementsFile)
    elements = list(elementsCsvReader)
    elementsFile.close()

    ALL_COLUMNS = ['Atomic Number', 'Symbol', 'Element', 
                'Group', 'Period', 'Atomic weight', 'Density',
                'Melting point', 'Boiling point',
                'Specific heat capacity', 'Electronegativity',
                'Abundance in earth\'s crust']

    # To justify the text, we need to find the longest string in ALL_COLUMNS.
    LONGEST_COLUMN = 0
    for key in ALL_COLUMNS:
        if len(key) > LONGEST_COLUMN:
            LONGEST_COLUMN = len(key)

    # Put all the elements data into a data structure:
    ELEMENTS = {}  # The data structure that stores all the element data.
    for line in elements:
        element = {'Atomic Number':  line[0],
                'Symbol':         line[1],
                'Element':        line[2],
                'Origin of name': line[3],
                'Group':          line[4],
                'Period':         line[5],
                'Atomic weight':  line[6] + ' u', # atomic mass unit
                'Density':        line[7] + ' g/cm^3', # grams/cubic cm
                'Melting point':  line[8] + ' K', # kelvin
                'Boiling point':  line[9] + ' K', # kelvin
                'Specific heat capacity':      line[10] + ' J/(g*K)',
                'Electronegativity':           line[11],
                'Abundance in earth\'s crust': line[12] + ' mg/kg'}

    

        ELEMENTS[line[0]] = element  # Map the atomic number to the element.
        ELEMENTS[line[1]] = element  # Map the symbol to the element.

    print('Periodic Table of Elements')

    print()

    

    while True:  # Main program loop.
        # Show table and let the user select an element:
        print('''            Periodic Table of Elements
        1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
        1 H                                                  He
        2 Li Be                               B  C  N  O  F  Ne
        3 Na Mg                               Al Si P  S  Cl Ar
        4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
        5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
        6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
        7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

                Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
                Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr''')
        print('Enter a symbol or atomic number to examine, or QUIT to quit.')
        response = input('> ').title()

        if response == 'Quit':
            sys.exit()

    # Display the selected element's data:
        if response in ELEMENTS:
            for key in ALL_COLUMNS:
                    keyJustified = key.rjust(LONGEST_COLUMN)
                    print(keyJustified + ': ' + ELEMENTS[response][key])
            input('Press Enter to continue...')






def menu():
    os.system("cls")
    print('************************************************************************************************************************')
    print('                                   KENDRIYA VIDYALAYA No.1,VADODARA     ')
    print('************************************************************************************************************************')
    print('                                          PERIODIC TABLE           ')                                        
    print('                                 Developed by: Milind and Vikramaditya   ')
    print('                                             YEAR: 2022-2023                ')
    print('************************************************************************************************************************')
    print("1. Atomic Mass Calculator")
    print("2. Periodic Table")
    print("3. Quit")
    userchoice = int(input("Enter your choice: "))

    if userchoice == 1:
        os.system("cls")
        atomicMassCalculator()
    elif userchoice == 2:
        os.system("cls")
        elementInfo() 
    elif userchoice ==3:
        os.system("cls")
        quit
    else:
        print("Enter a valid choice")
        os.system("cls")

menu()
