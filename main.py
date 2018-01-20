'''
Read a text file to get the total number of people present in the social network.
Append names of the people in a list.
'''

class SocialNetwork:
	
	def __init__(self):
		# List containing name of all the people in the social network.
		self.social_network = []
	
	# Read the file and parse it for ',' and new line
	def readParseFile(self):
		
		'''
		The file contains name of all the people in the social network, separated by a ','. In this case
		each line contains 2 names showing the relationship between the two names
		'''

		# read the file
		file = open ("dummy.txt", "r")
		#file = open ("SocialNetwork.txt", "r")
		
		lines = file.readlines()
		file.close()
		
		# Parse the file for ',' 
		for line in lines:
			line = line.strip()
			line = line.split(',')
			#print(line[0])
			#print(line[1])
			
			# read the length of the line, will signify count of names in a single line. 
			length = len(line)
			for idx in xrange(length):
				# append the names in a list if the name is not already present in the list
				if line[idx] not in self.social_network:
					self.social_network.append(line[idx])
				
		print self.social_network

	def getCountPeople(self):
	# Returns the total number of people present in the social Network
		return len(self.social_network)

if __name__ == '__main__':
	
	sc = SocialNetwork()
	sc.readParseFile()
	print (sc.getCountPeople())
