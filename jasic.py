import sys

def replace_str(file_name, stext, rtext):
    with open(file_name,"r+") as file:
        lines = file.readlines()
    with open(file_name,"w") as file1:
        for l in lines:
            file1.write(l.replace(stext,rtext))
            
    
def conv(outfile):
    nj_keywords = ["BEGIN","END","PRINT"]
    j_keywords = ["{","}","System.out.println"]
    tempstr1 = ""
    repfor = ""
    with open(outfile,"r") as f:
        lines = f.readlines()
        for l in lines:
            for c,item in enumerate(nj_keywords):
                replace_str(outfile,nj_keywords[c],j_keywords[c])
        for x,m in enumerate(lines):
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
                    repfor = "for(int" + " " + str(strvars[0]) + "=" + str(strvars[1]) + ";" + " " + str(strvars[0]) + "<" + str(strvars[2]) + ";" + " " + str(strvars[0]) + "+=" + str(strvars[3]) + ")"
    replace_str(outfile,tempstr1,repfor)
    print("Ok! Done!")

def createfile(ogfile,outfile):
    with open(ogfile) as f:
        with open(outfile, "w") as f1:
            for line in f:
                f1.write(line)
    conv(outfile)
            
def main():
    ogfile = sys.argv[1]
    createfile(ogfile,ogfile+".java")

    
main()



        
