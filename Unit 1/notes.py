

#1 What is an array called in Python?
#Lists []

#2 What python would you use to add an element to python array? How would you write this?
#Append 
#Insert, takes the position in your list
categories =['action,''horror','drama,']
categories.append('fantasy')
print(categories)

categories =['action,''horror','drama,']
categories.insert(1,'fantasy')
print(categories)

# 3 In Python code how would you access an item in an array? You want to print horror from the lisit
print(categories[3])

# 4 Difference between binary and linear seach?
# Binary search - ordered search, splits list into two halves. Keep splitting until you get to
# desired middle number. list must be ordered

#Linear search - Goes in order in a  straight line,

# 5 Searching for a student in each classroom, you would use a Linear Search

# 6 What is an algorithm?
# A method that follows isntructions, looping 

# 7 What is a python class?
# a group of functions that follow instructions for creating an object

class tikTokProfile:
    def __init__(self,username,profile,followers,following,favVideos,saved):
        self.username = username
        self.profile = profile
        self.profile= followers
        self.profile= following
        self.favVideos= favVideos
        self.saved= saved

        def postVideo(self):
            input ("upload video...")
            if videoFormat == 'avi':
            elif videoFormat == 'mp4':
                
            



