import re
import Tkinter
import tkFileDialog
import csv

def openFile(exten='.hex', ftypes=[('all files', '.*')], idir='C:\\',
             ifilen='myhexfile.hex', title='Open File'):
    root = Tkinter.Tk()
    file_opt = options = {}
    options['defaultextension'] = exten
    options['filetypes'] = ftypes
    options['initialdir'] = idir
    options['initialfile'] = ifilen
    options['parent'] = root
    options['title'] = title
    root.withdraw()
    return tkFileDialog.askopenfile(mode='r', **file_opt)

def saveFile(exten='.hex', ftypes=[('all files', '.*')], idir='C:\\',
             ifilen='myhexfile.hex', title='Open File'):
    root = Tkinter.Tk()
    file_opt = options = {}
    options['defaultextension'] = exten
    options['filetypes'] = ftypes
    options['initialdir'] = idir
    options['initialfile'] = ifilen
    options['parent'] = root
    options['title'] = title
    root.withdraw()
    return tkFileDialog.asksaveasfile(mode='w', **file_opt)

    
def hex2byte(hfile):
    hexfile = hfile.read()
    hbytes = []
    bdata = []
    byteString = ''
    scale = 16
    byteSize = 8
    try:
        hdata = re.findall(r':[\w]{2}([\w]+)[\w]{2}', hexfile)
        for data in hdata:
            hbytes.append(re.findall(r'([\w]{2})', data))
        for data in hbytes:
            for byte in data:
                bdata.append(bin(int(byte, scale))[2:].zfill(byteSize))
        bfile = saveFile(exten='.csv',ftypes=[('comma separated value', '.csv')],
                         ifilen='mybytefile.csv',title='Save Byte File')
        writer = csv.writer(bfile)
        writer.writerow(bdata)
        bfile.close()
        
    except:
        print "Invalid Hex File. . . sucks to suck!"

exitProgram = False
while(not exitProgram):
    print "\nHex editing options\n"
    print " 1) Intel hex to byte format (save as .csv)\n"
    print " e) exit\n"
    choice = raw_input("Choice: ")

    if (re.match(r'[\d]+', choice)): #any number will work for now
        hfile = openFile(ftypes=[('all files', '.*'), ('Intel Hex', '.hex'),
                                 ('Memory Initialization File', '.mif')], title='Open Hex File')
        try:
            hex2byte(hfile)
        except AttributeError:
            del fopen
    else:
        exitProgram = True
        
        
