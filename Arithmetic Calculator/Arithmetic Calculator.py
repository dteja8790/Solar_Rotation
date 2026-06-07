import sys
print("_" * 50)
print("\t\t\t\tArithmetic Calculation")
print("_" * 50)
print("\t\t\t\t\t 1.Addition")
print("\t\t\t\t\t 2.Substraction")
print("\t\t\t\t\t 3.Multiplication")
print("\t\t\t\t\t 4.Division")
print("\t\t\t\t\t 5.FloorDivision")
print("\t\t\t\t\t 6.ModuloDivision")
print("\t\t\t\t\t 7.Power")
print("\t\t\t\t\t 8.Reverse of a string")
print("\t\t\t\t\t 9.Exit")
print("_" * 50)
while (1):
        n = int(input("enter your choice:"))
        if (n <= 0):
            print("Invalid choice try Again")
        else:
            match (n):
                    case 1:
                        try:
                            a = float(input("\tenter A value:"))
                            b = float(input("\tenter B value:"))
                            c = a + b
                            print("\tSum({},{})={}".format(a, b, c))
                        except ValueError:
                            print("\t DON'T ENTER ALNUMS,STRS AND SPECIAL SYMBOLS INSTEAD OF NUMBERS")
                    case 2:
                        try:
                            a = float(input("\tenter A value:"))
                            b = float(input("\tenter B value:"))
                            c = a - b
                            print("\tSub({},{})={}".format(a, b, c))
                        except ValueError:
                            print("\t DON'T ENTER ALNUMS,STRS AND SPECIAL SYMBOLS INSTEAD OF NUMBERS")
                    case 3:
                        try:
                            a = float(input("\tenter A value:"))
                            b = float(input("\tenter B value:"))
                            c = a * b
                            print("\tMul({},{})={}".format(a, b, c))
                        except ValueError:
                            print("\t DON'T ENTER ALNUMS,STRS AND SPECIAL SYMBOLS INSTEAD OF NUMBERS")
                    case 4:
                        try:
                            a = float(input("\tenter A value:"))
                            b = float(input("\tenter B value:"))
                            c = a / b
                            print("\tDiv({},{})={}".format(a, b, c))
                        except ValueError:
                            print("\t DON'T ENTER ALNUMS,STRS AND SPECIAL SYMBOLS INSTEAD OF NUMBERS")
                    case 5:
                        try:
                            a = float(input("\tenter A value:"))
                            b = float(input("\tenter B value:"))
                            c = a // b
                            print("\tFloor({},{})={}".format(a, b, c))
                        except ValueError:
                            print("\t DON'T ENTER ALNUMS,STRS AND SPECIAL SYMBOLS INSTEAD OF NUMBERS")
                    case 6:
                        try:
                            a = float(input("\tenter A value:"))
                            b = float(input("\tenter B value:"))
                            c = a % b
                            print("\tModDiv({},{})={}".format(a, b, c))
                        except ValueError:
                            print("\t DON'T ENTER ALNUMS,STRS AND SPECIAL SYMBOLS INSTEAD OF NUMBERS")
                    case 7:
                        try:
                            a = float(input("\tenter A value:"))
                            b = float(input("\tenter B value:"))
                            c = a ** b
                            print("\tPow({},{})={}".format(a, b, c))
                        except ValueError:
                            print("\t DON'T ENTER ALNUMS,STRS AND SPECIAL SYMBOLS INSTEAD OF NUMBERS")
                    case 8:
                        print("\t Thanks for using this Arithmetic calculation")
                        sys.exit()
                    case _:
                        print("Your selection of Operation wrong try again")
            ch = input("\tenter your choice again you want to use (yes/no):")
            if (ch == "no"):
                break
