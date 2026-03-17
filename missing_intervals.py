def distinctIntegers(MAX_VALUE, VALUES): # return RESULT
    VALUES.sort()
    res = []
    prev = -1
    for i, val in enumerate(VALUES):
        if (val-prev) == 2:
            res.append(str(prev+1))
        elif (val-prev) > 2:
            range = str(prev+1) + "-" + str(val-1)
            res.append(range)
        prev = val
    if (MAX_VALUE-1 == prev):
        res.append(str(MAX_VALUE))
    elif (MAX_VALUE-prev) > 2:
        res.append(str(prev+1) + "-" + str(MAX_VALUE))
    return ','.join(res)

# case 1: val is the same as prev, no missing numbers
# ^ this case is not needed for checking, can just check c2 c3 and move on
# case 2: (val-prev) = 2, which means only 1 missing number
# case 3: (val-prev) > 2, range of more than 1 missing number

if __name__ == "__main__":
    sampleInputs = [
        [[0,1,2,50,52,75],1000],
        [[59,10,8],59],
        [[59,10,8],60]
    ]
    for values, maxVal in sampleInputs:
        print(distinctIntegers(maxVal, values))
