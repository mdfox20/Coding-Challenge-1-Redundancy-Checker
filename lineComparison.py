
# File: lineComparison.py
# Challenge 1, Redundancy Checker
# Authors: Logan Swanson, Maddy Fox, Maddy Kulke

import os

#CHANGE PATH HERE
path=".."

def compare_files(f1, f2):
    '''takes two filenames, and prints a report of the identical lines'''
    file1=open(f1,'r')
    file2=open(f2,'r')
    
    lines1=[line for line in file1]
    lines2=[line for line in file2]
    
    numIdentical=0
    results=""
    
    #check each line in file1 for a match
    for index, line in enumerate(lines1):
        #we dont count blank lines
        if line.isspace(): continue
    
        elif line in lines2:
            results+="*** "+str(index+1)+" "+str(lines2.index(line)+1)+" "+line
            #we also only want to match lines on a 1-1 basis
            #so this ensures that same line from file2 wont be paired again
            lines2[lines2.index(line)]=""
            numIdentical+=1
            
    if not results=="":
        print("---------------------------------")
        print("File1: "+os.path.basename(f1))
        print("File2: "+os.path.basename(f2))
        print("Number of Identical Lines: ", numIdentical)
        print("---------------------------------")
        print(results)

    file1.close()
    file2.close()

    return numIdentical
    
def main():
    #grab all .txt, .csv, & .py files from the specified file path
    files=[f for f in os.listdir(path) if os.path.isfile(path+"/"+f)]
    files=[f for f in files if f.endswith(".py") or f.endswith(".csv") or f.endswith(".txt")]

    if files:
      matches=0
      
      for file1 in files:
          for file2 in files[files.index(file1)+1:]:
              matches += compare_files(path+"/"+file1, path+"/"+file2)
              
      if matches==0:
          print("No matches found in files")
      
    else:
        print("No files found in directory")
    
main()