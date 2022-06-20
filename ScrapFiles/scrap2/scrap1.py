# Question 1
def serGen(series):
    cd = int((series[0] + series[-1])/4)
    return [{series[0]}, {(series[0] + cd)}, {series[0] + 2*cd}, {series[-1]}]


# Question 2
def units(n1, n2):
    if n1 % 10 > n2 % 10:
        return n2
    else:
        return n1


# Question 3
def hyphenAdd(sentence):
    return sentence.replace(' ', '-')


# Question 4
def removeDuplicates(dupl):
    newl = []
    [newl.append(x) for x in dupl if x not in newl]
    return newl


# Question 5
def insertList(list, newElement, position):
    list.insert(position, newElement)
    return list


# Question 6
def sameLen(str1, str2):
    return True if len(str1) == len(str2) else False


# Question 7
def strDigitSum(string):

    return sum([int(i) for i in string if i.isdigit()])


# Question 8
def valInDict(d, value):
    if value in list(d.values()):
        return list(d.keys())[list(d.values()).index(value)]


# Question 9
def merge(dict1, dict2):
    dict1.update(dict2)
    return dict1


# Question 10
def dictHighests(d):
    return sorted(list(d.values()))[-2:]


print(removeDuplicates([1, 1, 2, 3, 2, 1]))
