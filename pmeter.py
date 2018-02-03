# Files: pmeter.py
# Sprint 3: Python-O-Meter
# Author: Maddy Fox
# Partner: Maddy Kulke

import os

def count_lines(dirPath):
  """function to count number of lines in file except for comments and blank lines"""
  
  allFiles = os.listdir(dirPath)
  pyFiles = [file for file in allFiles if ".py" in file]

  for file in pyFiles:
    numLines = sum(1 for line in open(file, "r") if line.strip() != "" and line[0] != "#")
    print("file: "+file+"    lines: "+str(numLines))

def main():
  dirPath = input("Enter the path for your directory: ")
  count_lines(dirPath)

main()
