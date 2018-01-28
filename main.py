import Util

'''
Read a text file to get the total number of people present in the social network.
Append names of the people in a list.
'''

class SocialNetwork:
	
	def __init__(self):
		# List containing name of all the people in the social network.
		self.list_names = []
		self.dict_names_objects = {}

	#
	# Reads the file, prepares the network list and assigns friends
	#
	def prepareNetworkList(self, filename):

		# get an instance of the Util helper class
		u = Util.util()

		# read the content of the social network file.
		self.list_names = u.readFile(filename)

		for names_line in self.list_names:
			# strip the names_line of '\r' and '\n', else might result in multiple entries
			# For e.g. SAM_SWAIT and SAM_SWAIT\r\n
			names_line = names_line.strip()
			
			# parse the file on the delimiter ',' 
			names_line = names_line.split(',')

			# as per the use case scenario there are two names in a single line
			for idx in xrange(2):
				# check if the names are encountered for the first time
				if (self.dict_names_objects.has_key(names_line[idx]) != True):
				#if (names_line[idx] in sc.dict_names_objects != True):
					self.dict_names_objects.update({names_line[idx]: Vertex(names_line[idx])})	

			# We have all the names and their objects in a pair now
			# Next task would be to create a tree for every pair	
			person_1_obj = self.dict_names_objects[names_line[0]]
			person_2_obj = self.dict_names_objects[names_line[1]]
			person_1_obj.addFriend(person_2_obj)
	
	#
	# returns the list of all the names in the network 
	#
	def getNameList(self):
		
		#
		return self.dict_names_objects.keys()

	#
	# Returns list of all the objects in the network 
	#
	def getVerticesList(self):
		
		# 
		return self.dict_names_objects.values()	

	#
	# Returns the count of people in the network
	#
	def getCountOfPeopleInNetwork(self):

		# Returns the total number of people present in the social Network
		return len(self.dict_names_objects.keys())


#
# Vertex Class, 
#
class Vertex:

	def __init__(self, vertex):
		self.name = vertex;
		self.friends = []

	#
	# Add a friend in the list 
	#
	def addFriend(self, friend):
		if isinstance(friend, Vertex):

			# if friend is not already in the list:
			if friend.name not in self.friends:
				
				# add the new friend in the list
				self.friends.append(friend.name)

				# Since its a undirected graph, friend of a friend is also a friend.
				friend.friends.append(self.name)
		else:
			return False

#
# Graph Class, contains varaibles and related to the graph 
#
class Graph:
    
    def __init__(self):
        self.vertices = {}

	#
	# Add the vertices in a graph
	#
    def addVertices(self, vertices):
        for vertex in vertices:
		    if isinstance(vertex, Vertex):
			    self.vertices[vertex.name] = vertex.friends

	#
	# Finds the shortest path between two nodes using bfs
	#
    def findShortestPath(self, start, goal):
	
		# maintain a list of all the explored nodes
	    explored_path = []
	
		# Maintain a queue to keep track of the paths to be checked
	    queue = [[start]]

	    if start == goal:
			# Start is same as the goal. Return the same.
		    return start

		# keep checking until all the paths have been checked.
	    while queue:
    
			# pop the first path from the queue
		    path = queue.pop(0)
		
			# get the last node from the path
		    node = path[-1]
		
		    if node not in explored_path:
			    friends_list = self.vertices[node]
			
				# go through all friend nodes, construct a new path and
				# push it into the queue
			    for friend in friends_list:
				    new_path = list(path)
				    new_path.append(friend)
				    queue.append(new_path)
				    
					# return path if neighbour is goal
				    if friend == goal:
					    return new_path
 
				# mark node as explored
			    explored_path.append(node)

		# if there is no path return none
	    return None
            
#
# Main function
#
def main():

	sc = SocialNetwork()
	g = Graph()

	sc.prepareNetworkList("SocialNetwork.txt")
	g.addVertices(sc.getVerticesList())
	print sc.getCountOfPeopleInNetwork()
	print (g.findShortestPath('STACEY_STRIMPLE', 'RICH_OMLI'))


if __name__ == '__main__':
	
	# Start the program
	main()

	
