'''
Created on Jan 5, 2015

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

# Start of Program
openable = True
while openable:
    fname =  input('Please input file name to open and parse:\n')
    fileName = checkExtension(fname)
    try:
        f = open(fileName)
        openable = False
    except:
        pass

spec_token = r'[^ \s\w]'
inParen_token = r'\((.+)\)'
num_token = r'[\d]'
metal_token = r'\\m/'
track_token = r'\+([\d]+) ["]*([\w\s]*)["]*\n'

specialChars = 0
inParenthesis = 0
numbers = 0

metalHand = 0
tracks = []

j = 0
for contents in f:
    # count how many times respective icons/tokens appear
    specialChars = specialChars + len(findThis(spec_token, contents))
    inParenthesis = inParenthesis + len(findThis(inParen_token, contents))
    numbers = numbers + len(findThis(num_token, contents))

    metalHand = findThis(metal_token, contents)
    if len(metalHand) > 0:
        metalHandLine = j + 1 # Assume lines in a file start at 1, lists start at 0
    else:
        j = j + 1

    # take care of tracks here

f.close()


print(specialChars)
print(inParenthesis)
print(numbers)
print(metalHandLine)
print(tracks)

