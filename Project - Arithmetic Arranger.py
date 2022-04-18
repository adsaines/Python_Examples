# receive an array of mathematical equations and return them in a vertical format
def arithmetic_arranger(problems,displayAnswers=False):
    processedEquations = dict()
    counter = 0
    # Error Reason: too many problems, max of 5
    if len(problems) > 5 :
        return "Error: Too many problems."

    while counter < len(problems) :
        problemParts = processEquation(problems[counter])
        # https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
        # Error Reason: any operations that are not addition or subtraction
        if problemParts['operand'] != '+' and problemParts['operand'] != '-' :
            return "Error: Operator must be '+' or '-'."
        # Error Reason: numbers can only contain digits, no decimals / variables
        if problemParts['firstNum'].isdigit() is False or problemParts['secondNum'].isdigit() is False :
            return "Error: Numbers must only contain digits."
        # Error Reason: any number more than four digits, Note: width is always 2+ the largest number's characters
        if problemParts['width'] > 6 :
            return "Error: Numbers cannot be more than four digits."
        # if no errors are triggered by the equation in question then add it to the process object/dictionary
        processedEquations[counter] = problemParts
        counter += 1
    
    return formatAnswer(processedEquations,displayAnswers)

# take the equation in question and extract the numbers
def processEquation(strEquation):
    parts = strEquation.split(' ')
    equationParts = dict()
    # find first number
    equationParts['firstNum'] = parts[0]
    # find operand
    equationParts['operand'] = parts[1]
    # find second number
    equationParts['secondNum'] = parts[2]
    # define width of equation as 2 + the widest number
    if len(equationParts['firstNum']) > len(equationParts['secondNum']) :
        equationParts['width'] = len(equationParts['firstNum']) + 2
    else :
        equationParts['width'] = len(equationParts['secondNum']) + 2
    return equationParts

# take the split apart equations and join them into a formatted output
def formatAnswer(processedEquations,displayAnswers) :
    firstLine = ""
    secondLine = ""
    thirdLine = ""
    fourthLine = ""
    firstEquation = True
    leadingSpace = ""

    # loop object/dictionary once
    for value in processedEquations :
        # add in spaces between equations, excluding the first
        if firstEquation == False and leadingSpace == "" :
            leadingSpace = giveMeCharacters(4, " ")

        equation = processedEquations[value]
        # once to lay down the first line with the "firstNum" values
        spacesToAdd = giveMeCharacters(equation['width'] - len(equation['firstNum']), " ")
        firstLine += f"{leadingSpace}{spacesToAdd}{equation['firstNum']}"
        # again to lay down the second line with the "secondNUm" and "operand" values
        spacesToAdd = giveMeCharacters(equation['width'] - len(str(int(equation['secondNum'])))-1, " ")
        secondLine += f"{leadingSpace}{equation['operand']}{spacesToAdd}{equation['secondNum']}"
        # third add the dashes
        dashSeparator = giveMeCharacters(equation['width'], "-")
        thirdLine += f"{leadingSpace}{dashSeparator}"
        # fourth get the results
        result = eval(f"{equation['firstNum']}{equation['operand']}{equation['secondNum']}")
        spacesToAdd = giveMeCharacters(equation['width'] - len(str(result)), " ")
        fourthLine += f"{leadingSpace}{spacesToAdd}{result}"

        firstEquation = False


    if displayAnswers :
        return f"{firstLine}\n{secondLine}\n{thirdLine}\n{fourthLine}"
    else :
        return f"{firstLine}\n{secondLine}\n{thirdLine}"

# get a number of the specified character
def giveMeCharacters(charNum,char) :
    charStr = ""
    # just make sure that charNum is actually a usable integer
    charNum = int(charNum)
    # make a string of characters
    while charNum > 0 :
        charStr += char
        charNum -= 1
    return charStr