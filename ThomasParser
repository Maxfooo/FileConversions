'''
Created on Jan 5, 2015

@author: Thomas Forrest
'''
import re #Used for search
from _ast import List
from setuptools.tests.doctest import Tester
while True:
    filename=input("Enter your input")
    fExtension =".txt"
    if(filename.find(fExtension)==-1):  #checks if the file has .txt
        filename+=fExtension

    try:
        textFile=open(filename)         #in case filename is not found
    except IOError:
        print("Error invalid name")
        continue
    break
textlist=textFile.readlines()   #creates a list
textFile.close() # closes file
#print(textlist)
# variables
numcount=0
specialcount=0
Mline=0
paracount=0
numCh="\d"
whiteSpace="[\S]"
listlength=len(textlist)

def stringConverter(st):#used to make the list a string so parsing is done more easily

    stuff=""
    #searching=re.findall(str, textlist[num])
    for num in range(0,listlength): #range(len(textlist)) #a=re.findall(r'\((  ))\'),str)  [\w]*s  [\w\W\s]* *none to many +1 to many
        searching=re.findall(st, textlist[num])
        for match in searching:
            stuff=stuff+match
    return stuff
def counter(symbol,st):  # counts certain items in string
    count=0
    item=re.findall(symbol,st)
    for match in item:
        count=count+1
    return str(count)
def lineFinder(sym): # finds the line for a certain symbol
    count=0
    for num in range(0,listlength):
        searching=re.findall(sym, textlist[num])
        count=count+1
        for match in searching:
            return str(count)
stringOfTextList=(stringConverter(whiteSpace))
def findSymbols(str,data): #returns a string containing a certain regular express// accepts a string not a list
    items=""
    searching=re.findall(str, data)
    for match in searching:
        items=items+match
    return items
# variables used in final string writen to a new file
specialSymbols=(findSymbols("\W",stringOfTextList))
spSymCount=counter("\W", specialSymbols)
mLine=lineFinder("\m/")
nums=findSymbols(numCh,stringOfTextList)
numsCount=(counter(numCh,nums))
paraFinder='\((.*?)\)'
insidePara=(findSymbols(paraFinder,stringOfTextList ))  #a{4,}b
insideParaCount=(counter("\w",insidePara))


print(specialSymbols)


'''

# used for paring the song names
quotes='\"(.*?)\"'
quotesLW='\s\s(.*?)\"' #used for testing
quotesRW='\W*)'
quotefinder=stringConverter(quotes)
def songFinder(quotes,quotesLW,quotesRW): #def for parsing the names into a new list
    songcount=0
    songlist=[None]*12
    #searching=re.findall(str, textlist[num])
    for num in range(5,listlength+1): #range(len(textlist)) #a=re.findall(r'\((  ))\'),str)  [\w]*s  [\w\W\s]* *none to many +1 to many

        searching=re.findall(quotes, textlist[num])
        #searchingLW=re.findall(quotesLW, textlist[num])
        #searchingRW=re.findall(quotesRW,textlist[num])
        for match in searching:
            songlist[songcount]=match

        #for match in searchingLW:
          #  songlist[songcount]=match

        #for match in searchingRW:
          #  songlist[songcount]=match
        songcount=songcount+1
    return songlist
songlist=songFinder(quotes,quotesLW,quotesRW)
print(songlist)
songlist[4]=" " # For testing purposes
songlist[9]=" "
print(songlist) # for testing
#combines the first half of the file
writeFileHalf= "Special Characters"+","+specialSymbols+","+spSymCount+"\n"+"Chars between Parenthesis"+","+insidePara+","+insideParaCount+"\n"+"\m/ found on line"+","+mLine+"\n"
def otherHalfDef(p): #used to organize the list of songs into a string
    string="Animals are Leaders\n"
    l=list(p)
    l.reverse()
    for num in range(0,12):
        string=string+str((num+1))+","+l.pop()+"\n"


    return string
songNames=otherHalfDef(songlist)
#combines the two strings
fileToWrite=writeFileHalf+songNames
print(fileToWrite) #for testing
#asks for file name
fileName=input("Enter a file name(dont include file type)")
fileName=fileName+".csv"
#writes string to file
with open(fileName,"w") as f:
    f.write(fileToWrite)
f.close()

'''
