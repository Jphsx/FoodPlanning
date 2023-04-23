

#table references
#kendal cookbook ID Name Calories Carbs Fat Protein
#greg cookbook ID Name Calories Fat Carbs Fiber Protein
import sys
import csv
from operator import add

def getMacros(cookbook, itemlist):
	theseitems = []
	#print(itemlist)
	for ID in itemlist:

		for item in cookbook:
			#print(ID,float(item[0]))
			if ID == float(item[0]):
				theseitems.append(item)
	

	return theseitems

def parseMeal(meal):
	#if( meal[0] < 1 ): #this is my additions
	parsedmeal = []
	parsednutr = []	
	if( meal[0][-2] == '.' ): #this is greg
		#conver to standard format
		parsednutr.append(float(meal[-5]))
		parsednutr.append(float(meal[-3]))
		parsednutr.append(float(meal[-4]))
		parsednutr.append(float(meal[-1]))
		name = ' '.join(meal[:-5])
		parsedmeal.append(name)
		
	else:
		parsednutr.append(float(meal[-4]))
		parsednutr.append(float(meal[-3]))
		parsednutr.append(float(meal[-2]))
		parsednutr.append(float(meal[-1]))
		name = ' '.join(meal[:-4])
		parsedmeal.append(name)

	return parsedmeal, parsednutr
	

def printMealPlan(itemlist):
	Totals = [ 0.0, 0.0, 0.0, 0.0 ]
	for i, item in enumerate(itemlist):
		#print(item)
		name,nutr = parseMeal(item)
		print("Item "+str(i)+" "+ name[0] )
		print("Cal: "+str(nutr[0])+" Carbs: "+str(nutr[1])+" Fats: "+str(nutr[2])+" Prot: "+str(nutr[3]))
		print("\n")
		Totals = list( map(add, Totals, nutr) )

	print("Meal Totals Cal: "+str(Totals[0])+" Carbs: "+str(Totals[1])+" Fats: "+str(Totals[2])+" Prot: "+str(Totals[3]))


with open('foodlist.txt') as csvfile:
	
	csvRead = csv.reader(csvfile, delimiter=' ')
	cookbook = []
	for row in csvRead:
		cookbook.append(row)

	#itemlist = [ 0.01, 73, 15.1 ]
	#populate item list


	print 'Number of arguments:', len(sys.argv), 'arguments.'
	print 'Argument List:', str(sys.argv)
	itemlist = list(map(float, sys.argv[1:]))
	print("intput itemlist",itemlist)
	myMacros = getMacros(cookbook, itemlist)
	printMealPlan(myMacros)




