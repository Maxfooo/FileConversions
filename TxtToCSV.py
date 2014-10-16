'''
Created on Oct 10, 2014

@author: Max A. Ruiz
'''

import re
from tkinter import *
from tkinter import filedialog


class TxtToCSV(Frame):

    file_opt = options = {}
    options['defaultextension'] = '.txt'
    options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
    options['initialdir'] = 'C:\\'
    options['initialfile'] = 'myfile.txt'
    options['title'] = 'This is a title'

    wfile_opt = woptions = {}
    woptions['defaultextension'] = '.csv'
    woptions['filetypes'] = [('all files', '.*'), ('csv files', '.csv')]
    woptions['initialdir'] = 'C:\\'
    woptions['initialfile'] = 'myfile.csv'
    woptions['title'] = 'This is a title'

    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.title('Text to CSV')
        self.pack()

        self.initGUI()

    def toCSV(self,file, csvFile):
        j = ''
        for line in file:
            words = line.split()
            words.append('\n')
            l = len(words)
            for i in range(l):
                if i < l and words[i] != '\n':
                    j = j + str(words[i]) + ','
                else:
                    j = j + str(words[i])

        file.close()
        csvFile.write(j)
        csvFile.close()


    def getPartList(self):
        pFileTxt = filedialog.askopenfile(mode='r', **self.file_opt)
        if pFileTxt != None:
            self.parseFileName(str(pFileTxt))
            pFileCsv = filedialog.asksaveasfile(mode='w', **self.wfile_opt)

            if pFileCsv != None:
                self.parseFileName(str(pFileCsv), fType='csv', mode=1)
                self.toCSV(pFileTxt, pFileCsv)


    def getPinList(self):
        pnFileTxt = filedialog.askopenfile(mode='r', **self.file_opt)
        if pnFileTxt != None:
            self.parseFileName(str(pnFileTxt))
            pnFileCsv = filedialog.asksaveasfile(mode='w', **self.wfile_opt)
            if pnFileCsv != None:
                self.parseFileName(str(pnFileCsv), fType='csv', mode=1)
                self.toCSV(pnFileTxt, pnFileCsv)


    def getNetList(self):
        nFileTxt = filedialog.askopenfile(mode='r', **self.file_opt)
        if nFileTxt != None:
            self.parseFileName(str(nFileTxt))
            nFileCsv = filedialog.asksaveasfile(mode='w', **self.wfile_opt)
            if nFileCsv != None:
                self.parseFileName(str(nFileCsv), fType='csv', mode=1)
                self.toCSV(nFileTxt, nFileCsv)

    def initGUI(self):

        bF = Frame(self)
        bF.pack()

        partFrame = LabelFrame(bF, text='Part List')
        partFrame.pack(side='left')
        b1 = Button(partFrame, text='Select Part File', command = self.getPartList)
        b1.pack(side='left')

        pinFrame = LabelFrame(bF, text='Pin List')
        pinFrame.pack(side='left')
        b2 = Button(pinFrame, text='Select Pin File', command = self.getPinList)
        b2.pack(side='left')

        netFrame = LabelFrame(bF, text='Net List')
        netFrame.pack(side='left')
        b3 = Button(netFrame, text='Select Net File', command=self.getNetList)
        b3.pack(side='left')

        self.logFrame = LabelFrame(self, text='Log')
        self.logFrame.pack()
        self.logVar = StringVar()
        self.log = Label(self.logFrame, textvariable=self.logVar, width=35)
        self.log.pack(side='bottom', anchor='s')

    def parseFileName(self, string, fType='txt', mode=0):
        wordArray = re.findall(r'(\w)', string)
        sz = len(wordArray)
        if sz > 35:
            self.log.pack_forget()
            self.log = Label(self.logFrame, textvariable=self.logVar, width=sz)
            self.log.pack(side='bottom', anchor='s')
        try:
            fName = re.findall(r'/([\w]+\.{0})'.format(fType), string)[0]
            fLoc = re.findall(r'\'([\w\W]+)/', string)[0]
            if mode == 0:
                self.logThis = 'Loaded: ' + fName + '\nFrom: ' + fLoc
            elif mode == 1:
                self.logThis = 'Saved: ' + fName + '\nTo: ' + fLoc
            else:
                self.logThis = 'Mode error'
        except:
            self.logThis = 'Failed to load/save file'

        self.logVar.set(self.logThis)

root = Tk()
app = TxtToCSV(master=root)
app.mainloop()
