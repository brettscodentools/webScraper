#! python3
#first use of a shebang line^ so that I don't have to run this from idle
"""
My first webscraper
lets see if we cannot get some info on local food trucks
""" 
import re, os, requests, bs4, pandas


#---------------------Functions-----------------------------

#the main function, take a webpage url as an argument 
def scrape(_webpage,):	
	dates = []
	Times = []
	locations = []

	#the request for the website searched
	res = requests.get('http://sf.lobstatruck.com/')
	#make sure we got it by raising for status
	res.raise_for_status()
	#make a beautiful soup object out of the requested page's text
	lobstaTruck = bs4.BeautifulSoup(res.text, 'html.parser')


	#make a reg expression for times
	findTime = re.compile(r'(\d\d|\d)(:)(\d\d)(\s)?(\w\w)(\s)?(s|-|\.)(\s)?(\d\d|\d)(:)(\d\d)(\s)?(\w\w)')

	#get the element of my specification in the arguement
	timeElems = lobstaTruck.select('table[class="schedule"] > tbody > tr > td > div[class="main4"] > p > strong')

	#getting an int value for the length of the array of the selected elements
	numOfTimeRes = int(len(timeElems))






	#need to start commenting out more
	#so this loop with check the number of results and print out the number of results + the results if there are any

	# so that i can stop getting the error spit back out for there not being any index in my code for the .gettext()

	print ("found" + str(numOfTimeRes) + " results")
	print ('                                  ')

	if numOfTimeRes > 0:
		#turn this into a enumerate so i can get the index of the array items
		for index, res in enumerate(timeElems):
			#get the text of the element I specified
			result = str(timeElems[index].getText())
		
			#take just the time out of the text in groups with regular expressions
			timeResult = (findTime.findall(result))
			
			for groups in timeResult:
				#join the regex groups together to form the information
				timeString = ''.join([groups[0],groups[1],groups[2],groups[4],groups[6],groups[8],groups[9],groups[10],groups[12]])
			
			
				#print('Between ' + timeString + ' lobsta truck will be at')
				print(timeString)
			
	else:
		print("found nothing/ Maybe an error")

scrape('http://sf.lobstatruck.com/')
