
def instructions():
    print()
    print("+---------------------------------------------------------------------+")
    print("+-                     WELCOME TO INTERGRATE AUTO!                   -+")
    print("+- for seperate terms in an expression use spaces in between terms   -+")
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
    print(" > for any 1/x please use this syntax: 1/(x^1)                       -+")
    print("+---------------------------------------------------------------------+")
    print()


# checking that the variable is a valid maths variable
def check(variable):
    check = (any(char.isalpha() for char in variable))
    if check:
        return True
    else: return False



def maths(eq):
    result = []

    reciprocal = False
    sqr = False
    for element in eq:

        # any lone terms (DOESNT WORK)  
        if element.isdigit():
            result.append(f"{element}x")

        for index in range(0, len(element)-1):
            text = ""

            # raised to the power
            if element[index] == "^" and reciprocal == False and sqr == False:
                # power rule: integral of x^2 = (x^2+1)/3
                exponent = int(element[index+1])
                variable = element[index-1]
                
                # checking for a single and double digit base
                if len(element[index]) == 4:
                    base = int(element[index-2])
                    text = base
                if len(element[index]) > 4:
                    base = int(element[index-2], element[index-3])
                    exponent = int(str(element[index+1], element[index+2]))
                    text = base

                if check(variable):
                    new_exponent = exponent + 1
                    text += f"({variable}^{new_exponent})/{new_exponent}"

                result.append(text)

            # square root function: the integral of the square root of x == x^1/2
            elif element[index] == "/":
                if element[index+1] == "/":
                    sqr = True
                    root = element[index+2]
                    variable = element[index-3]
                    exponent = element[index-1]

                    text = f"{variable} ^ ({exponent}/{root})"
                    result.append(text)

            # reciprocal function
            elif element[index] == "1":
                if element[index+1] == "/" and element[index+2] != "/":
                    reciprocal = True
                    text = "ln "
                    for term in range(3, len(element)-1):
                        if element[term] != "^" or element[term] != "(" or element[term] != ")":
                            text += element[term]
                        if element[term] == "^":
                            term += 1
                    result.append(text)


    result.append("+ C")
    return result
                    


def main():
    instructions()
    app = True
    question = 1

    while app:
        #try:
            command = input("Please enter a Expression or 'quit': ")
            file = open("equation.txt", "+a")
            command = command.lower()
            if command == "quit":
                app = False
                print("Thank you for using Integrate Auto!")
                print("Bye.....")
            else:
                equation = command.split(" ")
                print(equation)
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
                file.write(" ")

                question += 1
                file.close()

        #except Exception:
           #print("Try again, error in integrating your expression!")

main()

