import sys
import csv

def ReadFile():
	lista = []
	with open('tour.csv', 'r') as f:
		reader = csv.reader(f)
		header = next(reader)
		for row in reader:
			lista.append(row)
		
		return header, lista
		
def WriteFile(header, lista):
	with open('insert.sql', 'w') as f:
		for elem in lista:
			f.write('INSERT INTO Tour \n')
			f.write('(')
			for item in header:
				f.write(item + ', ')

			f.write(')\n')
			f.write('VALUES\n')
			f.write('(')

			for field in elem:
				f.write(field + ', ')
			
			f.write(')\n')
			
			f.write('\n')
			

		
header, lista = ReadFile() 

WriteFile(header, lista)

