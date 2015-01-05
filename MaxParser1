'''
Created on Jan 4, 2015

@author: Max Ruiz
'''
import re

''' OBJECTIVE
Group:
all special characters
anything between parenthesis
all numbers
find the symbol "\m\"
track names and numbers - make dictionary key=name, value=number
'''

def checkExtension(fname):
    f_ext = '.txt' # file extension

    # token for recognizing file extension
    ext_token = r'[\{0}]+'.format(f_ext)

    # check if any part of the file extension was there
    check_fext = re.findall(ext_token, fname)

    # place correct file extension even if it was there
    if len(check_fext) > 0:
        fileName = fname.replace(check_fext[0], f_ext)
    else:
        fileName = fname + f_ext

    return fileName

def findThis(token, strng):
    return re.findall(token, strng)

def makeDict(lyst_2d):
    temp = {}
    for track in lyst_2d:
        temp[track[1]] = track[0]

    return temp

def prepForCSV(lyst_2d):
    st = ''
    for items in lyst_2d:
        st = st + str(items[0]) + ',' + str(items[1]) + '\n'
    return st

def findLine(token, strng):
    temp = re.findall(r'[\n]|{0}'.format(token), strng)
    cr = 0
    if len(temp) > 0:
        for item in temp:
            if item == '\n':
                cr = cr + 1
            else:
                break
        return cr + 1 # Assume lines in a file start at 1, lists start at 0
    else:
        return -1

# Start of Program
openable = True
while openable:
    fname =  input('Please input file name to open and parse:\n')
    fileName = checkExtension(fname)
    try:
        f = open(fileName)
        contents = f.read()
        f.close()
        openable = False
    except:
        pass


spec_token = r'[^ \s\w]'
inParen_token = r'\((.+)\)'
num_token = r'[\d]'
metal_token = r'\\m/'
track_token = r'\+([\d]+) ["]*([\w\s]*)["]*\n'


# count how many times respective icons/tokens appear
specialChars = len(findThis(spec_token, contents))
inParenthesis = len(findThis(inParen_token, contents))
numbers = len(findThis(num_token, contents))

metalHand = findLine(metal_token, contents)

tracks = findThis(track_token, contents)
trackDict = makeDict(tracks)





print(specialChars)
print(inParenthesis)
print(numbers)
print(metalHand)
print(tracks)

