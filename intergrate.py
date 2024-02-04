
def instructions():
    print()
    print("+---------------------------------------------------------------------+")
    print("+-                     WELCOME TO INTERGRATE AUTO!                   -+")
    print("+- for seperate expressions please use spaces in between             -+")
    print("+- To use type in your equations using these criteria:               -+")
    print(" > use the ^ character for raising to the power                      -+")
    print(" > use the // pair of characters for square root                     -+")
    print(" > e.g. the square root of 4; 4//2                                   -+")
    print(" > for each term put no spaces. e.g. 3x^2                            -+")
    print(" > for any number raised to the power of 1 please type it, e.g. 3x^1 -+")
    print(" > all equations typed and their answers are added to equations.txt  -+")
    print(" > please quit the program before accessing the text file            -+")
    print(" > two digits are not supported!                                     -+")
    print(" > to quit type in 'quit'                                            -+")
    print(" > all intergration equations must be in their simplist form         -+")
    print(" > do not put the dx at the end of the expression                    -+")
    print("+---------------------------------------------------------------------+")
    print()


def maths(eq):
    pass


def main():
    instructions()
    app = True
    question = 1

    while app:
        try:
            command = input("Please enter a Expression or 'quit': ")
            file = open("equation.txt", "+a")
            command = command.lower()
            if command == "quit":
                app = False
                print("Thank you for using Intergrate Auto!")
                print("Bye.....")
            else:
                equation = command.split(" ")
                result = maths(equation)
                quest = ""
                ans = ""
                print("f(x)dx = ", *result)

                text = str(question) + ". "
                file.write(text)
                for item in equation:
                    quest += item
                    quest += " "
                file.write(quest)
                file.write("\n")

                for item in result:
                    ans += item
                    ans += " "
                file.write(ans)
                file.write("\n")
                file.write("\n")

                question += 1
                file.close()

        except Exception:
            print("Try again, error in integrating your expression!")

main()

