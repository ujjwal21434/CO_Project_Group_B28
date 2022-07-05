f = open("run", "r")
w = open("binary.txt", "w")
readlist = f.readlines()

writelist = []
hltlist=[]
varline=[]


readlist=[i for i in readlist if i!='\n']
length = len(readlist)

vardict = {}
labdict={}
k = 20


def checkregister(l):
    if((l[1] == "R0" or l[1] == "R1" or l[1] == "R2" or l[1] == "R3" or l[1] == "R4" or l[1] == "R5" or l[1] == "R6") and (l[2] == "R0" or l[2] == "R1" or l[2] == "R2" or l[2] == "R3" or l[2] == "R4" or l[2] == "R5" or l[2] == "R6") and (l[3] == "R0" or l[3] == "R1" or l[3] == "R2" or l[3] == "R3" or l[3] == "R4" or l[3] == "R5" or l[3] == "R6")):
        return 1
    else:
        return 0


def checkregisterB(s):
    if(s == "R0" or s == "R1" or s == "R2" or s == "R3" or s == "R4" or s == "R5" or s == "R6"):
        return 1
    else:
        return 0


def checkimmediate(l):
    num = int(l[2][1:])
    if(num >= 0 and num <= 255):
        return 1
    else:
        return 0


def writebinary(l, s):
    global writelist
    if(l[1] == "R0"):

        s = s+"000"
    elif(l[1] == "R1"):
        s = s+"001"
    elif(l[1] == "R2"):
        s = s+"010"
    elif(l[1] == "R3"):
        s = s+"011"
    elif(l[1] == "R4"):
        s = s+"100"
    elif(l[1] == "R5"):
        s = s+"101"
    elif(l[1] == "R6"):
        s = s+"110"
    if(l[2] == "R0"):
        s = s+"000"
    elif(l[2] == "R1"):
        s = s+"001"
    elif(l[2] == "R2"):
        s = s+"010"
    elif(l[2] == "R3"):
        s = s+"011"
    elif(l[2] == "R4"):
        s = s+"100"
    elif(l[2] == "R5"):
        s = s+"101"
    elif(l[2] == "R6"):
        s = s+"110"
    if(l[3] == "R0"):
        s = s+"000"
    elif(l[3] == "R1"):
        s = s+"001"
    elif(l[3] == "R2"):
        s = s+"010"
    elif(l[3] == "R3"):
        s = s+"011"
    elif(l[3] == "R4"):
        s = s+"100"
    elif(l[3] == "R5"):
        s = s+"101"
    elif(l[3] == "R6"):
        s = s+"110"
    s = s+"\n"

    writelist.append(s)


def writeB(l, s):
    global writelist

    if(l[1] == "R0"):

        s = s+"000"
    elif(l[1] == "R1"):
        s = s+"001"
    elif(l[1] == "R2"):
        s = s+"010"
    elif(l[1] == "R3"):
        s = s+"011"
    elif(l[1] == "R4"):
        s = s+"100"
    elif(l[1] == "R5"):
        s = s+"101"
    elif(l[1] == "R6"):
        s = s+"110"
    if(l[2] == "R0"):
        s = s+"000"
    elif(l[2] == "R1"):
        s = s+"001"
    elif(l[2] == "R2"):
        s = s+"010"
    elif(l[2] == "R3"):
        s = s+"011"
    elif(l[2] == "R4"):
        s = s+"100"
    elif(l[2] == "R5"):
        s = s+"101"
    elif(l[2] == "R6"):
        s = s+"110"
    s = s+"\n"
    writelist.append(s)


def writeC(s, s1):
    global writelist
    if(s1 == "R0"):

        s = s+"000"
    elif(s1 == "R1"):
        s = s+"001"
    elif(s1 == "R2"):
        s = s+"010"
    elif(s1 == "R3"):
        s = s+"011"
    elif(s1 == "R4"):
        s = s+"100"
    elif(s1 == "R5"):
        s = s+"101"
    elif(s1 == "R6"):
        s = s+"110"
    return s


s1=readlist[length-1]
l=s1.split()
num=len(l)
if(num!=1):
    print("missing hlt function")

else:
    if(l[0]=="hlt"):
        s="01010"
        s=s+"00000000000"
        s=s+"\n"
        hltlist.append(s)
    else:
        print("wrong syntax for hlt")



    

if(len(hltlist)==1):
    count=0

    for i in range(0, length-1):
        count=count+1

        s1 = readlist[i]
        l = s1.split()
        if(s1=="\n"):

            continue
        if(l[0][-1]==":"):
            
            labdict[l[0][0:-1]]=i+1
            l.pop(0)
        

        if(l[0] == "add"):
            num = len(l)

            if(num != 4):

                print("wrong number of registers", i+1)
                writelist=[]
                break
            else:
                if(checkregister(l) == 1):

                    s = "1000000"
                    writebinary(l, s)
                else:
                    print("wrong register", i+1)
                    writelist=[]
                    break
        elif(l[0] == "sub"):

            num = len(l)

            if(num != 4):

                print("wrong number of registers", i+1)
                writelist=[]
                break
            else:

                if(checkregister(l) == 1):

                    s = "1000100"
                    writebinary(l, s)

                else:
                    print("wrong register", i+1)
                    writelist=[]
                    break
        elif(l[0] == "mul"):
            num = len(l)

            if(num != 4):

                print("wrong number of registers", i+1)
                writelist=[]
                break

            else:
                if(checkregister(l) == 1):

                    s = "1011000"
                    writebinary(l, s)

                else:
                    print("wrong register", i+1)
                    writelist=[]
                    break

        elif(l[0] == "xor"):
            num = len(l)

            if(num != 4):

                print("wrong no. of register", i+1)
                writelist=[]
                break
            else:
                if(checkregister(l) == 1):

                    s = "1101000"
                    writebinary(l, s)

                else:
                    print("wrong register", i+1)
                    writelist=[]
                    break
        elif(l[0] == "or"):
            num = len(l)

            if(num != 4):

                print("wrong number of register", i+1)
                writelist=[]
                break
            else:
                if(checkregister(l) == 1):

                    s = "1101100"
                    writebinary(l, s)

                else:
                    print("wrong register", i+1)
                    writelist=[]
                    break
        elif(l[0] == "and"):
            num = len(l)

            if(num != 4):

                print("wrong number of register", i+1)
                writelist=[]
                break
            else:
                if(checkregister(l) == 1):

                    s = "1110000"
                    writebinary(l, s)

                else:
                    print("wrong register", i+1)
                    writelist=[]
                    break
        elif(l[0] == "mov"):
            num = len(l)
            if(num != 3):
                print("wrong number of register", i+1)
                writelist=[]
                break
            else:
                if(checkregisterB(l[1]) == 1):
                    if(l[2][0] == "$"):
                        if(checkimmediate(l) != 1):
                            print("invalid immediate")
                            writelist=[]
                            break
                        else:
                            imm = int(l[2][1:])
                            binarystr = bin(imm)
                            binarystr = binarystr[2:]
                            zerostr = ''
                            for i in range(8-len(binarystr)):
                                zerostr = zerostr+'0'

                            binarystr = zerostr+binarystr
                            s = "10010"
                            
                            s =writeC(s, l[1])

                            s = s+binarystr
                            s = s+"\n"
                            writelist.append(s)
                    elif(checkregisterB(l[2])==1 or l[2]=="FLAGS"):
                        s = "1001100000"
                        
                        s=writeC(s, l[1])
                        if(l[2]=="FLAGS"):
                            s=s+"111"
                            s=s+"\n"
                            writelist.append(s)
                        else:
                            s=writeC(s,l[2])
                            writelist.append(s)
                    else:
                        print("wrong register", i+1)
                        writelist=[]
                        break
                else:
                    print("wrong register", i+1)
                    writelist=[]
                    break

        elif(l[0] == "ls"):
            num = len(l)
            if(num != 3):
                print("wrong number of register", i+1)
                writelist=[]
                break
            else:

                if(checkregisterB(l[1]) == 1):

                    if(l[2][0] == "$"):

                        if(checkimmediate(l) != 1):

                            print("invalid immediate on line", i+1)
                            writelist=[]
                            break
                        else:
                            imm = int(l[2][1:])
                            binarystr = bin(imm)
                            binarystr = binarystr[2:]
                            zerostr = ''
                            for i in range(8-len(binarystr)):
                                zerostr = zerostr+'0'

                            binarystr = zerostr+binarystr
                        s = "11001"
                        s = writeC(s, l[1])
                        s = s+binarystr
                        s = s+"\n"
                        writelist.append(s)
                    else:
                        print("wrong syntax for immediate", i+1)
                        writelist=[]
                        break
                else:
                    print("wrong register")
                    writelist=[]
                    break

        elif(l[0] == "div"):
            num = len(l)
            if(num != 3):
                print("wrong no. of register", i+1)
                writelist=[]
                break
            else:

                if(checkregisterB(l[1]) == 1):

                    if(checkregisterB(l[2]) == 1):

                        s = "1011100000"
                        writeB(l, s)
                    else:
                        print("wrong register", i+1)
                        writelist=[]
                        break
                else:

                    print("wrong register", i+1)
                    writelist=[]
                    break
        elif(l[0] == "rs"):
            num = len(l)
            if(num != 3):
                print("wrong number of register", i+1)
                writelist=[]
                break
            else:

                if(checkregisterB(l[1]) == 1):

                    if(l[2][0] == "$"):

                        if(checkimmediate(l) != 1):

                            print("invalid immediate on line", i+1)
                        else:
                            imm = int(l[2][1:])
                            binarystr = bin(imm)
                            binarystr = binarystr[2:]
                            zerostr = ''
                            for i in range(8-len(binarystr)):
                                zerostr = zerostr+'0'

                            binarystr = zerostr+binarystr
                        s = "11000"
                        s = writeC(s, l[1])
                        s = s+binarystr
                        s = s+"\n"
                        writelist.append(s)
                    else:
                        print("wrong syntax for immediate", i+1)
                        writelist=[]
                        break
                else:
                    print("wrong register",i+1)
                    writelist=[]
                    break
        elif(l[0] == "cmp"):
            num = len(l)
            if(num != 3):
                print("wrong number of register", i+1)
                writelist=[]
                break
            else:
                if(checkregisterB(l[1]) == 1):
                    if(checkregisterB(l[2]) == 1):
                        s = "1111000000"
                        writeB(l, s)
                    else:
                        print("wrong register", i+1)
                        writelist=[]
                        break
                else:

                    print("wrong register", i+1)
                    writelist=[]
                    break
        elif(l[0] == "not"):
            num = len(l)
            if(num != 3):
                print("wrong number of register", i+1)
                writelist=[]
                break
            else:
                if(checkregisterB(l[1]) == 1):
                    if(checkregisterB(l[2]) == 1):
                        s = "1111000000"
                        writeB(l, s)
                    else:
                        print("wrong register", i+1)
                        writelist=[]
                        break
                else:

                    print("wrong register", i+1)
                    writelist=[]
                    break
        elif(l[0] == "var"):
            indicator=1
            varline.append(i+1)
            if(len(varline)==1):
                if(varline[0]!=1):

                    for j in range(varline[0]-2,-1,-1):
                        s2=readlist[j]
                        if(s2=="\n"):

                            continue
                        else:
                            indicator=0
                            break
                            
                    if(indicator==0):
                        print("variable declared at wrong place")
                        writelist=[]
                        break
                    else:
                        vardict[l[1]]=i+1
                    
                else:
                    vardict[l[1]]=i+1

            else:
                if(varline[-1]-varline[-2]==1):
                    vardict[l[1]]=i+1
                else:
                    for j in range(varline[-2],varline[-1]-1):
                        s=readlist[j]
                        if(s=="\n"):
                            continue
                        else:
                            indicator=0
                            break
                    if(indicator==0):
                        print("variable declared at wrong place")
                        writelist=[]
                        break
                    else:
                        vardict[l[1]]=i+1

        elif(l[0] == "ld"):
            num = len(l)
            if(num != 3):
                print("wrong no of operands", i+1)
                writelist=[]
                break
            else:
                if(checkregisterB(l[1]) == 1):


                    if(l[2] in vardict.keys()):

                        s = "10100"
                        s = writeC(s, l[1])
                        binarystr = bin(vardict[l[2]])
                        binarystr = binarystr[2:]
                        zerostr = ''
                        for i in range(8-len(binarystr)):
                            zerostr = zerostr+'0'

                        binarystr = zerostr+binarystr
                        s = s+binarystr
                        s=s+"\n"
                        writelist.append(s)
                    else:
                        print("wrong memory address", i+1)
                        writelist=[]
                        break
                else:
                    print("wrong register",i+1)
                    writelist=[]
                    break
        elif(l[0]=="st"):
            num = len(l)
            if(num != 3):
                print("wrong no of operands", i+1)
                writelist=[]
                break
            else:
                if(checkregisterB(l[1]) == 1):


                    if(l[2] in vardict.keys()):

                        s = "10101"
                        s = writeC(s, l[1])
                        binarystr = bin(vardict[l[2]])
                        binarystr = binarystr[2:]
                        zerostr = ''
                        for i in range(8-len(binarystr)):
                            zerostr = zerostr+'0'

                        binarystr = zerostr+binarystr
                        s = s+binarystr
                        s=s+"\n"
                        writelist.append(s)
                    else:
                        print("wrong memory address", i+1)
                        writelist=[]
                        break
                else:
                    print("wrong register",i+1)
                    writelist=[]
                    break
        elif(l[0]=="jmp"):
            num=len(l)
            if(num!=2):
                print("wrong no. of operands",i+1)
                writelist=[]
                break
            else:
                if(l[1] in labdict.keys()):
                    s="11111000"
                    binarystr=bin(labdict[l[1]])
                    binarystr = binarystr[2:]
                    zerostr = ''
                    for i in range(8-len(binarystr)):
                        zerostr = zerostr+'0'

                    binarystr = zerostr+binarystr
                    s=s+binarystr
                    s=s+"\n"
                    writelist.append(s)
                else:
                    print("wrong memory address",i+1)
                    writelist=[]
                    break
        elif(l[0]=="jlt"):
            num=len(l)
            if(num!=2):
                print("wrong no. of operands",i+1)
                writelist=[]
                break
            else:
                if(l[1] in labdict.keys()):
                    s="01100000"
                    binarystr=bin(labdict[l[1]])
                    binarystr = binarystr[2:]
                    zerostr = ''
                    for i in range(8-len(binarystr)):
                        zerostr = zerostr+'0'

                    binarystr = zerostr+binarystr
                    s=s+binarystr
                    s=s+"\n"
                    writelist.append(s)
                else:
                    print("wrong memory address",i+1)
                    writelist=[]
                    break
        elif(l[0]=="jgt"):
            num=len(l)
            if(num!=2):
                print("wrong no. of operands",i+1)
                writelist=[]
                break
            else:
                if(l[1] in labdict.keys()):
                    s="01101000"
                    binarystr=bin(labdict[l[1]])
                    binarystr = binarystr[2:]
                    zerostr = ''
                    for i in range(8-len(binarystr)):
                        zerostr = zerostr+'0'

                    binarystr = zerostr+binarystr
                    s=s+binarystr
                    s=s+"\n"
                    writelist.append(s)
                else:
                    print("wrong memory address",i+1)
                    writelist=[]
                    break
        elif(l[0]=="je"):
            num=len(l)
            if(num!=2):
                print("wrong no. of operands",i+1)
                writelist=[]
                break
            else:
                if(l[1] in labdict.keys()):
                    s="01111000"
                    binarystr=bin(labdict[l[1]])
                    binarystr = binarystr[2:]
                    zerostr = ''
                    for i in range(8-len(binarystr)):
                        zerostr = zerostr+'0'

                    binarystr = zerostr+binarystr
                    s=s+binarystr
                    s=s+"\n"
                    writelist.append(s)
                else:
                    print("wrong memory address",i+1)
                    writelist=[]
                    break
        elif(l[0]=="hlt"):
            print("hlt can not be used between code",i+1)
            writelist=[]
            break
        else:
            print("unsupported instruction",i+1)
            writelist=[]
            break
    if(count==length-1):
        writelist.append(hltlist[0])

for i in writelist:
    print(i,end="")
    
w.writelines(["%s" % item  for item in writelist])

f.close()
w.close()