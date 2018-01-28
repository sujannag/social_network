# social_network
Reads a text file containing names of people present in a social network, and deduces the shortest path between two people.

The file path can be changed by changing the global variable "file_name"
Name of two concerned persons can be modified by changing the global variable person_1 and person_2.

Total number of people in the network is deduced by counting the total number of nodes in the network.
The path search algorithm uses bfs to search for the goal node.

To run the code, simply type the following in the command terminal
python main.py

The following piece of code have been tested with python 2.7

For Example:
1. To open and read the file SocialNetwork.txt, file_name is set to "SocialNetwork.txt"
2. Path between STACEY_STRIMPLE and RICH_OMLI is given by:
['STACEY_STRIMPLE', 'KORY_NICKOLAS', 'LUCIANO_KEBA', 'RIGOBERTO_RACCA', 'FRITZ_RYBCZYK', 'RICH_OMLI']

Similarly path between RICH_OMLI and STACEY_STRIMPLE is given by:
['RICH_OMLI', 'FRITZ_RYBCZYK', 'RIGOBERTO_RACCA', 'LUCIANO_KEBA', 'KORY_NICKOLAS', 'STACEY_STRIMPLE']
