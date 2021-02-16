import sys
import re

def replace_str(file_name, stext, rtext):
    with open(file_name,"r") as file:
        lines = file.readlines()
    with open(file_name,"w") as file1:
        for l in lines:
            file1.write(l.replace(stext,rtext))
            
def add_semicolon(outfile):
    dont_replace = ["{","}","*/","/*"]
    with open(outfile, 'r') as meow:
        L = meow.read().splitlines()
        for line in L:
            if line[-1] not in dont_replace:
                line = line + ";"
                print(line)
                
#Makes sure keywords inside strings aren't touched
def no_touchy(ogfile):
    dont_touch_list = []
    dont_touch_str = ""
    quote = '"'
    whilecount = 0
    occurance = 0
    with open(ogfile,"r") as f:
        lines = f.readlines()
        for l in lines:
            for countt,char in enumerate(l):
                if char == quote and occurance == 0:
                    occurance = occurance + 1
                    char2 = l[countt+1]
                    whilecount = countt+1
                    while l[whilecount] != quote:
                        #print(l[whilecount])
                        whilecount = whilecount + 1
                    dont_touch_str = l[countt+1:whilecount]
                    dont_touch_list.append(dont_touch_str)
                    dont_touch_str = dont_touch_str.replace(dont_touch_str, "")
                else:
                    dont_touch_str = ""
    return dont_touch_list

def replace_no_touchy(outfile,item1,item2,lines):
    if item1 in lines:
        if item1 not in no_touchy(outfile)[0]:
            replace_str(outfile,item1,item2)
            print("Wrote ",item1)
        elif item1 in no_touchy(outfile)[0]:
            with open(ogfile,"r") as f:
                lines = f.readlines()
                for l in lines:
                    occurrences = [m.start() for m in re.finditer(item1, l)]
                    to_replace = l.find(item1,occurrences[1])
                    f1.write(l[to_replace].replace(item1,item2))
        
def conv(outfile):
    nj_keywords = ["BEGIN","END","PRINT","LN","REM","STOP","MAIN METHOD","CLASS","PRIVATE","IMPORT","NEW",
                   "IF","THEN","ELSE","PROTECTED","INT","VOID","DOUBLE","BOOL","BYTE","BREAK",
                   "FLOAT","SWITCH","CASE","LONG","CONST","CATCH","PUBLIC","SHORT","STATIC","TRY","THROW","THROWS","WHILE","DO","CHAR","ELSE IF","STRING"]
    
    j_keywords = ["{","}","System.out.print","ln","/*","*/","public static void main(String[] args)","public class","private","import",
                  "new","if","{","else","protected","int","void","double","boolean","byte","break",
                  "float","switch","case","long","final","catch","public","short","static","try","throw","throws","while","do","char","else if","String"]
    tempstr1 = ""
    repfor = ""
    numfors = 0
    with open(outfile,"r") as f:
            lines = f.readlines()
            for l in lines:
                for c,item in enumerate(nj_keywords):
                    replace_str(outfile,nj_keywords[c],j_keywords[c])
                    #replace_no_touchy(outfile,nj_keywords[c],j_keywords[c],lines)
            for q,w in enumerate(lines):
                    if "FOR" in w:
                        linenum = q
                        #print("theres a for")
                        numfors = numfors + 1
            for x,m in enumerate(lines):
                    for p in range(numfors):
                        if "FOR" in m:
                            for ind,ch in enumerate(m[:-1]):
                                if m[ind+1] != ",":
                                    tempstr1+= m[ind+1]
                                if m[ind+1] == ",":
                                    tempstr1 += ","
                                if m[ind+1] == ")":
                                    break
                            tempstr2 = tempstr1[5:]
                            tempstr2 = tempstr2[:-1]
                            strvars = tempstr2.split(',')
                            #print(strvars)
                            repfor = "for(int" + " " + str(strvars[0]) + "=" + str(strvars[1]) + ";" + " " + str(strvars[0]) + "<" + str(strvars[2]) + ";" + " " + str(strvars[0]) + "+=" + str(strvars[3]) + ")"
                            replace_str(outfile,tempstr1,repfor)
                            strvars = strvars.clear()
                            tempstr1 = ""
                            tempstr2 = ""
                            
    print("Ok! Done!")

def createfile(ogfile,outfile):
    with open(ogfile) as f:
        with open(outfile, "w") as f1:
            for line in f:
                f1.write(line)
    conv(outfile)
    #add_semicolon(outfile)
    
def main():
    ogfile = sys.argv[1]
    outfile_name = sys.argv[2]
    outfile = outfile_name
    createfile(ogfile,outfile)

    
main()



        
