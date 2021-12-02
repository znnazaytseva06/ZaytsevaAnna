from fileinput import filename
import csv
import sys 
print ("Група 9мб")
filename = "C:\Users\image\.vscode\Група 9мб.txt"
text_file = open("C:\Users\image\.vscode\Група 9мб.txt","r")
reader = csv.reader(text_file,delimiter = "t")
for row in reader:
    print(row)
text_file.close()



import csv
import sys
print("Група 8")
filename = "C:\Users\image\.vscode\Група 8.txt"
text_file = open("C:\Users\image\.vscode\Група 8.txt","r")
reader = csv.reader(text_file,delimiter = "t")
for row in reader:
    print(row)
text_file.close()



import csv
import sys
print("Група 7")
filename = "C:\Users\image\.vscode\Група 7.txt"
text_file = open("C:\Users\image\.vscode\Група 7.txt","r") 
reader = csv.reader(text_file,delimiter = "t")
for row in reader:
    print(row)
text_file.close()           
