from fileinput import filename
import csv
import sys 
print ("Група 9мб")
filename = "C:\Users\image\.vscode\Група 9мб.txt"
text_file = open("C:\Users\image\.vscode\Група 9мб.txt","r")
reader = csv.reader(text_file,delimiter = "t")
def sortByAlphabet(inputStr):
        return inputStr[0]
for str in reader:
 print (str)
text_file.close()
