"""
-> Three braces: [, {, (
-> [ cannot match with a non-]. Specifically, [}, [) is not allowed. same applies for other braces
-> stack works, and also pre-writing the mapping between each open and closing braces.
-> example: input: "[()]", stack: [ -> [( -> ) is a match to top of the stack, then pop -> [
- -> ] is a match to the top of the stack -> stack=[]. stack empty -> True. Otherwise, false. 
- input SHOULD strictly has characters (){}[], and no whitespace, based on given examples.
"""

def matching_parentheses(input: str) -> bool:
    parentheses = {"[": "]", "{": "}", "(": ")"}
    pStack = []
    for c in input: # iter through character
        if c == " ": # just incase, since it's not specified if whitespace can appear.
            continue
        if c not in parentheses: # c is a closing paren
            if pStack and parentheses[pStack[-1]] == c: # match
                pStack.pop()
            else: # no match, cancel early. 
                return False
        else:
            pStack.append(c)
    return len(pStack) == 0 # empty stack -> True

if __name__ == "__main__":
    cases = [
        "([])", # -> T
        "((([[{}]])))",# -> T
        "(){}([])",# -> T
        "{", # -> F
        "{)", # -> F
        "({{]})", # -> F
        "( [ { } ])" # -> T
    ]
    for case in cases:
        print(matching_parentheses(case))
