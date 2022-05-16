def solution(inputString):
    for i in range (len(inputString)):
        if inputString[i] == '(':
            start = i
        if inputString[i] == ')':
           end = i
           input_str = inputString[:start] + inputString[start+1:end][::-1] + inputString[end+1:]
           return solution(input_str)
    return inputString  