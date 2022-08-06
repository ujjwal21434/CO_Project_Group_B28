from pickle import FALSE, TRUE
import sys
import matplotlib
class memory:
    list=[]
    def __init__(self,value):
        self.value=value
        memory.list.append(self)
    def dump():
        for i in range(256):
            print(memory.list[i].value)

class registers:
    def __init__(self,num,value):
        self.num=num
        self.value=value
    
class flags:
    num="111"
    def __init__(self):
        self.v='0'
        self.l='0'
        self.g='0'
        self.e='0'
        self.val="000000000000"+self.v+self.l+self.g+self.e
    def setv(self):
        self.v='1'
    def setl(self):
        self.l='1'
    def setg(self):
        self.g='1'

    def sete(self):
        self.e='1'
    def reset(self):
        self.e='0'
        self.g='0'
        self.e='0'
        self.l='0'

class Progcount:
    value=0
pc=Progcount()
for i in range(256):
    m=memory('0000000000000000')


R0=registers("000","0000000000000000")
R1=registers("001","0000000000000000")
R2=registers("010","0000000000000000")
R3=registers("011","0000000000000000")
R4=registers("100","0000000000000000") 
R5=registers("101","0000000000000000")
R6=registers("110","0000000000000000")
FLAGS=flags()
# pc=Progcount()
 
def dum():
    print(R0.value,end=' ')
    print(R1.value,end=' ')
    print(R2.value,end=' ')
    print(R3.value,end=' ')
    print(R4.value,end=' ')
    print(R5.value,end=' ')
    print(R6.value,end=' ')
    FLAGS.val="000000000000"+FLAGS.v+FLAGS.l+FLAGS.g+FLAGS.e
    print(FLAGS.val)

# print(inputdata)
getbinary = lambda x, n: format(x, 'b').zfill(n)
def exec(inst):
    opcode=inst[0:5]
    
    if(opcode=="10000"):
        r1=eval("R"+str(int(inst[7:10],2)))
        r2=eval("R"+str(int(inst[10:13],2)))
        r3=eval("R"+str(int(inst[13:16],2)))
        value=int(r1.value,2)+int(r2.value,2)
        FLAGS.reset()
        if(value>65535):
            FLAGS.v='1'

        else:
            
            r3.value=getbinary(value,16)
        pc.value=pc.value+1
        return FALSE
    elif(opcode=="10001"):
        r1=eval("R"+str(int(inst[7:10],2)))
        r2=eval("R"+str(int(inst[10:13],2)))
        r3=eval("R"+str(int(inst[13:16],2)))
        value=int(r1.value,2)-int(r2.value,2)
        FLAGS.reset()
        if(value<0):
            r3.value=getbinary(0,16)
            FLAGS.v='1'
        else:
            r3.value=getbinary(value,16)
        pc.value=pc.value+1
        return FALSE

        
        #ask about overflow condition
    elif(opcode=="10110"):
        r1=eval("R"+str(int(inst[7:10],2)))
        r2=eval("R"+str(int(inst[10:13],2)))
        r3=eval("R"+str(int(inst[13:16],2)))
        value=int(r1.value,2)*int(r2.value,2)
        FLAGS.reset()
        if(value>65535):
            FLAGS.v='1'
        else:
            r3.value=getbinary(value,16)
        pc.value=pc.value+1
        return FALSE
    elif(opcode=="10111"):
        r1=eval("R"+str(int(inst[10:13],2)))
        r2=eval("R"+str(int(inst[13:16],2)))
        value=int(int(r1.value,2)/int(r2.value,2))
        R0.value=getbinary(value,16)
        R1.value=int(int(r1.value,2)%int(r2.value,2))
        FLAGS.reset()
        pc.value=pc.value+1
        return FALSE
    elif(opcode=="11010"):
        r1=eval("R"+str(int(inst[7:10],2)))
        r2=eval("R"+str(int(inst[10:13],2)))
        r3=eval("R"+str(int(inst[13:16],2)))
        value=int(r1.value,2)^int(r2.value,2)
        r3.value=getbinary(value,16)
        pc.value=pc.value+1
        FLAGS.reset()
        return FALSE
    elif(opcode=="11011"):
        r1=eval("R"+str(int(inst[7:10],2)))
        r2=eval("R"+str(int(inst[10:13],2)))
        r3=eval("R"+str(int(inst[13:16],2)))
        value=int(r1.value,2)|int(r2.value,2)
        r3.value=getbinary(value,16)
        pc.value=pc.value+1
        FLAGS.reset()
        return FALSE
    elif(opcode=="11100"):
        r1=eval("R"+str(int(inst[7:10],2)))
        r2=eval("R"+str(int(inst[10:13],2)))
        r3=eval("R"+str(int(inst[13:16],2)))
        value=int(r1.value,2)&int(r2.value,2)
        r3.value=getbinary(value,16)
        pc.value=pc.value+1
        FLAGS.reset()
        return FALSE
    elif(opcode=="10010"):
        r=eval("R"+str(int(inst[5:8],2)))
        r.value="00000000"+inst[8:16]
        FLAGS.reset()
        pc.value=pc.value+1
        return FALSE
    elif(opcode=="11001"):
        r=eval("R"+str(int(inst[5:8],2)))
        value=int(r.value,2)<<int(inst[8:16],2)
        print(value)
        r.value=getbinary(value,16)
        FLAGS.reset()
        pc.value=pc.value+1
        return FALSE
    elif(opcode=="11000"):
        r=eval("R"+str(int(inst[5:8],2)))
        value=int(r.value,2)>>int(inst[8:16],2)
        print(value)
        r.value=getbinary(value,16)
        FLAGS.reset()
        pc.value=pc.value+1
        return FALSE
    elif(opcode=="11101"):
        r1=eval("R"+str(int(inst[10:13],2)))
        r2=eval("R"+str(int(inst[13:16],2)))
        s=''
        for i in range(0,16):
            if(r1.value[i]=="0"):
                s=s+'1'
            elif(r1.value[i]=="1"):
                s=s+'0'
        r2.value=s
        pc.value=pc.value+1
        FLAGS.reset()
        return FALSE
    elif(opcode=="11110"):
        r1=eval("R"+str(int(inst[10:13],2)))
        r2=eval("R"+str(int(inst[13:16],2)))
        value1=int(r1.value,2)
        value2=int(r2.value,2)
        if(value1<value2):
            FLAGS.l='1'
        elif(value1>value2):
            FLAGS.g='1'
        elif(value1==value2):
            FLAGS.e='1'
        pc.value=pc.value+1
        
        return FALSE
    elif(opcode=="10011"):
        if(inst[10:13]=="111"):
            r1=FLAGS
            r2=eval("R"+str(int(inst[13:16],2)))
            r2.value=r1.val
            pc.value=pc.value+1
            
        else:

           r1=eval("R"+str(int(inst[10:13],2)))
           r2=eval("R"+str(int(inst[13:16],2)))
           r2.value=r1.value
           pc.value=pc.value+1
        FLAGS.reset()
        return FALSE
        
    elif(opcode=="10100"):
        r=eval("R"+str(int(inst[5:8],2)))
        ind=int(inst[8:16],2)
        r.value=memory.list[ind].value
        pc.value=pc.value+1
        FLAGS.reset()
        return FALSE
    elif(opcode=="10101"):
        r=eval("R"+str(int(inst[5:8],2)))
        ind=int(inst[8:16],2)
        memory.list[ind].value=r.value
        pc.value=pc.value+1
        FLAGS.reset()
        return FALSE
    elif(opcode=="11111"):
        label=int(inst[8:16],2)
        pc.value=label
        FLAGS.reset()
        return FALSE
    elif(opcode=="01100"):
        if(FLAGS.l=='1'):
            label=int(inst[8:16],2)
            pc.value=label
        else:
            pc.value=pc.value+1
        FLAGS.reset()
        return FALSE
    elif(opcode=="01101"):
        if(FLAGS.g=='1'):
            label=int(inst[8:16],2)
        
            pc.value=label
        else:
            pc.value=pc.value+1
        FLAGS.reset()
        return FALSE
    elif(opcode=="01111"):
        if(FLAGS.e=='1'):
            label=int(inst[8:16],2)
            pc.value=label
        else:
            pc.value=pc.value+1
        FLAGS.reset()
        return FALSE
    elif(opcode=="01010"):
        return TRUE
    


    

   


        
                
        

    

    

    

inputdata=sys.stdin.readlines()

for i in range(0,len(inputdata)):
    memory.list[i].value=inputdata[i][0:16]
hlt=FALSE
# pcstr=getbinary(pc.value,8)
# print(pcstr,end=' ')
# dum()
oldpc=pc.value
cycle=0
while(hlt==FALSE):
    inst=(memory.list[pc.value]).value
    hlt=exec(inst)
    
    pcstr=getbinary(oldpc,8)
    print(pcstr,end=' ')
    # print("after pcstr",end=' ')
    dum()
    oldpc=pc.value
memory.dump()


    # print(inst)
    
    

    
    
    # print(memory.list[i].value)       
