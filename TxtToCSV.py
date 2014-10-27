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

    def toCSV(self, file, csvFile, mode=0):
        def commaVals(arr, mode = 0):
            l = len(arr)
            c = 0
            a = ''
            for i in range(len(arr)):
                if re.match(r'[\w]+,', arr[i], re.I) != None: #need to fix for res and caps
                    c = c + 1
            for i in range(c+1):
                if i<(c+1):
                    a = a + arr[i] + '/'
                else:
                    a = a + arr[i]
            if mode == 0:
                return a
            elif mode == 1:
                newStrt = c+2
                b = ''
                if l > newStrt:
                    for i in range(l-newStrt-1):
                        cma = re.match(r'[\w],')
            
            
            
            
        if mode == 0:
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
        elif mode == 1:
            j = ''
            k = []
            p = []
            while len(k) == 0 and len(p) == 0:
                t0 = file.readline()
                k = re.findall(r'(Part[\s]+Value)',t0)
                p = re.findall(r'(Qty Value[\s]+Device)',t0)
                
            
            if len(k) > len(p):
                for line in file:
                    words = line.split()
                    l = len(words)
                    m = ''
                    words1 = []
                    for i in range(l):
                        pinhd = re.findall(r'(PINHD-[\w]+)', words[i])
                        if len(pinhd) > 0:
                            pin = True
                            break
                        else:
                            pin = False
                    if pin:
                        words1.append(words[0])
                        words1.append('N/A')
                        for i in range(1,l):
                            words1.append(words[i])
                        words1[len(words1)-2] = words1[len(words1)-2] + words1[len(words1)-1]
                        words1.pop()
                        words.append('\n')
                        words = words1
                        
                    if len(words) > 5:
                        
                        for n in range(4,l):
                            m = m + words[n] + ' '
                        for n in range(4,l):
                            del words[4]

                        if m.count(',') > 0:
                            m1 = re.findall(r'(\w+),', m)
                            m2 = re.findall(r',[\s]+([\w\s]+)', m)
                            m = m1[0] + ' ' + m2[0]

                        words.append(m)
                        
                    words.append('\n')
                    l = len(words)
                    
                    for i in range(l):
                        if words[i] != '\n':
                            j = j + str(words[i]) + ','
                        else:
                            j = j + str(words[i])
                            
                file.close()
                csvFile.write(j)
                csvFile.close()                
                            
            elif len(p) > len(k):
                j = ''
                for line in file:
                    pinhd = re.findall(r'(PINHD-[\w]+)', str(line))
                    words = line.split()
                    l = len(words)
                    if len(pinhd) == 0:
                        
                    else:
                        a = [str(words[0]), str(words[1]), str(words[2]), str(words[3])]
                        
                pass
            else:
                pass
        else:
            pass
        


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
                
    def getBOMList(self):
        bFileTxt = filedialog.askopenfile(mode='r', **self.file_opt)
        if bFileTxt != None:
            self.parseFileName(str(bFileTxt))
            bFileCsv = filedialog.asksaveasfile(mode='w', **self.wfile_opt)
            if bFileCsv != None:
                self.parseFileName(str(bFileCsv), fType='csv', mode=1)
                self.toCSV(bFileTxt, bFileCsv, mode=1)

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
        
        bomFrame = LabelFrame(bF, text='BOM List')
        bomFrame.pack(side='left')
        b4 = Button(bomFrame, text='Select BOM File', command=self.getBOMList)
        b4.pack(side='left')

        self.logFrame = LabelFrame(self, text='Log')
        self.logFrame.pack()
        self.logVar = StringVar()
        self.log = Label(self.logFrame, textvariable=self.logVar, width=50)
        self.log.pack(side='bottom', anchor='s')

    def parseFileName(self, string, fType='txt', mode=0):
        wordArray = re.findall(r'(\w)', string)
        sz = len(wordArray)
        if sz > 100:
            sz = sz/2 + (sz/2-50)
            self.log.pack_forget()
            self.log = Label(self.logFrame, textvariable=self.logVar, width=int(sz))
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
