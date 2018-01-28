# Util.py
# Mentions some basic reusable utilities

class util:
	
	# Read the file and parse it for ',' and new line
	def readFile(self, filename):
		
		# declare an empty list to hold the contents of the file
		local_list = []

		# read the file
		file = open (filename, "r")
		
		# Read the names from the file and update the list
		local_list = file.readlines()
		
		# close the file
		file.close()

		return local_list
