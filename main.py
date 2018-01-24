'''
Read a text file to get the total number of people present in the social network.
Append names of the people in a list.
'''

class SocialNetwork:
	
	def __init__(self):
		# List containing name of all the people in the social network.
		self.social_network = []
		self.names_list = []
		self.object_names_list = []
		self.dict_names_objects = {}
		
	
	# Read the file and parse it for ',' and new line
	def readFile(self, filename):
		
		'''
		The file contains name of all the people in the social network, separated by a ','. In this case
		each line contains 2 names showing the relationship between the two names
		'''

		# read the file
		file = open (filename, "r")
		
		# Read the names from the file and update the list
		self.names_list = file.readlines()
		
		# close the file
		file.close()
'''	
		# Parse the file for ',' 
			

			
		
		print self.social_network
'''
	#def getCountPeople(self):
		# Returns the total number of people present in the social Network
	#	return len(self.social_network)

class Vertex:

	def __init__(self, vertex):
		self.name = vertex;
		self.friends = []

	def add_friend(self, friend):
		if isinstance(friend, Vertex):

			# if friend is not already in the list:
			if friend.name not in self.friends:
				
				# add the new friend in the list
				self.friends.append(friend.name)

				# Since its a undirected graph, friend of a friend is also a friend.
				friend.friends.append(self.name)
		else:
			return False

if __name__ == '__main__':
	
	sc = SocialNetwork()
	sc.readFile("dummy_1.txt")
	
	# get the names from the name list
	#print(sc.names_list)

	object_names = ['0', '0']
	for names_line in sc.names_list:
		# strip the names_line of '\r' and '\n', else might result in multiple entries
		# For e.g. SAM_SWAIT and SAM_SWAIT\r\n
		names_line = names_line.strip()
			
		# parse the file on the delimiter ',' 
		names_line = names_line.split(',')

		# as per the use case scenario there are two names in a single line
		for idx in xrange(2):
			# check if the names are encountered for the first time
			#if names_line[idx] not in sc.social_network:
			if (sc.dict_names_objects.has_key(names_line[idx]) != True):
				#print("0:",names_line[0])
				#print("1:",names_line[1])
				print("name:",names_line[idx], "idx:",idx)
				sc.dict_names_objects.update({names_line[idx]: Vertex(names_line[idx])})	
			print(sc.dict_names_objects)
			print("\n")

			#print(sc.dict_names_objects.get('MYLES_JEFFCOAT'))

			# We have all the names and their objects in a pair now
			# Next task would be to create a tree for every pair
			
			#print len(sc.dict_names_objects)
			#object_names[0].add_friend(object_names[1])
			#sc.object_names_list.append(object_names[0])
			#sc.object_names_list.append(object_names[1])
		person_1_obj = sc.dict_names_objects[names_line[0]]
		person_2_obj = sc.dict_names_objects[names_line[1]]
		person_1_obj.add_friend(person_2_obj)
	#print (sc.dict_names_objects.keys())		
	#print (sc.dict_names_objects.values())		
	
	print(sc.dict_names_objects['MYLES_JEFFCOAT'].friends)	
	print(sc.dict_names_objects['LANNY_TIBURCIO'].friends)	
	print(sc.dict_names_objects['MARTIN_OMERSA'].friends)	
	#print len(sc.social_network)	
	#print (sc.social_network)	


	# if already present dont add in the list, else add them in the vertex and add in the list



#all the names have to be a vertex
