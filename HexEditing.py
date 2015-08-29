import re
import Tkinter
import tkFileDialog
import csv
import xml.etree.ElementTree as ET

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

def getFileLocation():
    exten='.*'
    ftypes=[('all files', '.*')]
    idir='C:\\',
    title='Get File Location'
    
    root = Tkinter.Tk()
    file_opt = options = {}
    options['defaultextension'] = exten
    options['filetypes'] = ftypes
    options['initialdir'] = idir
    options['parent'] = root
    options['title'] = title
    root.withdraw()

    return tkFileDialog.askopenfilename(**file_opt)

def getFolderLocation():
    root = Tkinter.Tk()
    file_opt = options = {}
    options['parent'] = root
    root.withdraw()
    return tkFileDialog.askdirectory(parent=root, title='Path to Copy to', \
                                     initialdir='.')

def hex2byte(retCode):
    hexfile = openFile(ftypes=[('all files', '.*'), ('Intel Hex', '.hex'),
                       ('Memory Initialization File', '.mif')],
                       title='Open Hex File').read()
    hbytes = []
    bdata = []
    byteString = ''
    scale = 16
    byteSize = 8
    try:
        hdata = re.findall(r':[\w]{2}([\w]+)[\w]{2}', hexfile)
        if retCode == 0:
            return hdata
        
        for data in hdata:
            hbytes.append(re.findall(r'([\w]{2})', data))
        if retCode == 1:
            return hbytes
        
        for data in hbytes:
            for byte in data:
                bdata.append(bin(int(byte, scale))[2:].zfill(byteSize))
        if retCode == 2:
            return bdata
        
        bfile = saveFile(exten='.csv',ftypes=[('comma separated value', '.csv')],
                         ifilen='mybytefile.csv',title='Save Byte File')
        writer = csv.writer(bfile)
        writer.writerow(bdata)
        bfile.close()
        
    except:
        print "Invalid Hex File. . . sucks to suck!"

def compareHexFiles():
    try:
        hexfile1 = openFile(ftypes=[('all files', '.*'), ('Intel Hex', '.hex'),
                            ('Memory Initialization File', '.mif')],
                            title='Open Hex File').read().strip()
        hexfile2 = openFile(ftypes=[('all files', '.*'), ('Intel Hex', '.hex'),
                            ('Memory Initialization File', '.mif')],
                            title='Open Hex File').read().strip()
        if hexfile1 == hexfile2:
            print "\n========================="
            print "\nYay, the hex files match!"
            print "\n========================="
        else:
            print "\n================================"
            print "\nAww, the hex files do NOT match!"
            print "\n================================"
    except:
        print "\n============================================================="
        print "Something went wrong when trying to read your files, try again.\n"
        print "\n============================================================="
        
def hex2MIF():
    hbytes = hex2byte(1)
    for row in hbytes:
        hbytes[0] = hbytes[0] + row
    hbytes = hbytes[0]
    mifbuff = []
    mifbuff.append('WIDTH=8;')
    mifbuff.append('DEPTH={0};'.format(len(hbytes)))
    mifbuff.append('ADDRESS_RADIX=UNS;')
    mifbuff.append('DATA_RADIX=UNS;')
    mifbuff.append('CONTENT BEGIN')

    for j in xrange(len(hbytes)):
        mifbuff.append('\t{0}\t:\t{1};'.format(j,hex2dec(hbytes[j])))

    mifbuff.append('END;')

    try:
        miff = saveFile(exten='.mif',ftypes=[('Memory Initialization File', '.mif')],
                        ifilen='mymiffile.mif',title='Save MIF file')
        for row in mifbuff:
            miff.write(row+'\n')
        miff.close()
    except:
        pass
    
def mif2dec():
    miff = openFile(exten='.mif',ftypes=[('Memory Initialization File', '.mif')],
                        ifilen='mymiffile.mif',title='Open MIF file')
    hxbuff = []
    for row in miff:
        hxbuff.append(hex2dec(row))

    decString = ''
    for row in hxbuff:
        decString = decString + str(row) + '\n'
    decString.strip('\n')
    try:    
        decf = saveFile(exten='.txt',ftypes=[('text file', '.txt')],
                            ifilen='myhex2dectxtfile.txt',title='Save hex2dec txt file')
        decf.write(decString)
        decf.close()
    except:
        pass

def hex2dec(hx):
    return int(hx, 16)
    
def ISMatrix():
    #Instruction Set Matrix - read from csv file
    try:
        matf = openFile(ftypes=[('all files', '.*'), ('Comma Separated Values', '.csv')],
                       title='Open csv File')
        insmat = []
        for line in matf:
            insmat.append(line.split(','))
            
        return insmat

    except:
        pass

def initMulticopy():
    print "\nPlease select folder locations to copy to."
    print "\nThese folder locations will be saved/cached, which you can\n" \
            + "update later."
    print "\nWhen you are done loading in locations, simply\n" \
            + "press the cancel button in the file explorer.\n"

    try:
        tree = ET.parse('filecopylocations.xml')
        xroot = tree.getroot()
        for locs in xroot.findall('Location'):
            xroot.remove(locs)
    except:
        froot = ET.Element('Directories')
        tree = ET.ElementTree(froot)
        tree.write('filecopylocations.xml')
        tree = ET.parse('filecopylocations.xml')
        xroot = tree.getroot()

    locnum = 1
    floc = getFolderLocation()
    while(floc != ''):
        try:
            loc = ET.SubElement(xroot, 'Location'.format(locnum))
            loc.set('index', '{0}'.format(locnum))
            locnum = locnum + 1
            loc.text = floc
            floc = getFolderLocation()
        except:
            floc = ''
    
    tree.write('filecopylocations.xml')
    ET.dump(xroot)

def getFileNameFromFilePath(fpath):
    return fpath.split('/').pop()
    
def multicopy():    
    try:
        tree = ET.parse('filecopylocations.xml')
        xroot = tree.getroot()
        print "\nWould you like to edit the following copy desitinations?\n"
        ET.dump(xroot)
        edit = raw_input("\ny=yes : n=no\n")
        if edit == 'y':
            initMulticopy()
        else:
            pass
    except:
        initMulticopy()
        tree = ET.parse('filecopylocations.xml')
        xroot = tree.getroot()

    print "\nPlease select the file you wish to have copied."

    try:
        
        fcpyfrom = getFileLocation()
        fcpyname = getFileNameFromFilePath(fcpyfrom)
        fcpyfrom = open(fcpyfrom, 'r').read()
        for loc in xroot.findall('Location'):
            f = open(loc.text + '/' + fcpyname, 'w')
            f.write(fcpyfrom)
            f.close()
        print "\nFile was successfully copied!"
    except:
        print "\nCould not copy file!"
        pass
    
exitProgram = False
while(not exitProgram):
    print "\nHex editing options\n"
    print " 1) Intel hex to byte format (save as .csv)\n"
    print " 2) Compare two Hex files (or any two files)\n"
    print " 3) Display 8051 Instruction Set\n"
    print " 4) Convert Hex file to MIF file\n"
    print " 5) Convert MIF to decimal\n"
    print " 6) Multi-Copy => Copy one file to multiple locations\n"
    print " d) Debug methods/code...May or may not be available\n"
    print " e) exit\n"
    choice = raw_input("Choice: ")

    if (choice == '1'):
        try:
            hex2byte(-1)
        except AttributeError:
            del fopen
    elif (choice == '2'):
        compareHexFiles()

    elif (choice == '3'):
        print ISMatrix()

    elif (choice == '4'):
        hex2MIF()

    elif (choice == '5'):
        mif2dec()

    elif (choice == '6'):
        multicopy()

    elif (choice == 'd'):
        print getFolderLocation()
        
    elif (re.match(r'[\d]+', choice)):
          pass
    else:
        exitProgram = True
        
        
