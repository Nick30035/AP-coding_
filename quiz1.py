# Create a new document called quiz1.py copy/ paste the following questions
# on your document and answer the following questions.

# quiz rules:
# - There is no talking during the quiz
# - You may only use your classnotes and w3schools.com for reference
# - If you have a question about a quiz question, please raise your hand
# - Once finished, submit your code to your repository using the source control 
# button. Your commit should be "completed quiz 1."

'note: all written responses should be written/ formatted as strings.'

# 1. In your own words, describe the differences between a linear search and a 
# binary search. Please write your response using complete sentences.
'The difference between a binary and linear seach is that binary searches split the list in two,'
'continuing this process until the desired number in the middle is found. Whereas, linear search'
'goes searching individually and in order.'
# 2. How many steps would it take to get to the desired number of 98 using linear search?
# Please write your response using complete sentences.
'It would take six total steps to get to the desired number, 98'
listA = [10,24,34,35,67,98,101]

# 3. How many steps would it take to get to the desired number of 150 using a binary search?
# Please write your response using complete sentences.
listB = [1,40, 44, 55, 70, 93, 99, 134, 145, 150, 200, 244]
'It would take three total steps to get to the desired number of 150'
# 4. In your own words describe what an algorithm is. 
# Please write your response using complete sentences.
'An algorithm is a method that follows instructions'
# 5. A person and their family is visiting a medical building. the medical building has
# 10 floors. The patient that the person and their family is visiting is on the 7th floor 
# of the building. The family also knows what room they need to go to to visit the
# patient on the 7th floor. which big-O time complexity would best describe the steps it
# would for them to get to the desired room and why? 
# Please write your response using complete sentences.
'The big-O time complexity being used here is an upper bound C.'

# 6. You and your friends are headed out to a party, as you're preparing to walk out the door to meet with
# your pals, your realize you forgot your phone. you you can't remember exactly where you misplaced it 
# but you know it is in one of your pairs of pants. You have 10 pairs of paints. which big-O time complexity
# would best describe the steps it would take to find your phone?
# Please write your response using complete sentences.
'The big-O time complexity that would need to be used here is upper bound C.'

# 7. Create a class that will represent and create game console objects. 
# Your class should have 4 attributes and 3 methods. 
# Once you've created your class, create 2 unique video game consoles.
class consoleObjects:
    def __intit__ (self,headset,microphone,controller,ps5,pc):
        self.headset= headset
        self.microphone = microphone
        self.controller = controller
        self.ps5 = ps5
        self.pc = pc

        def myfunc(self):
            print("Headset is connected "+ self.headset)
            p1 =consoleObjects("Headset",microphone)
            p1 = myfunc()


            def myfunc(self):
                print("Microphone is working"+self.microphone)
                p1 = consoleObjects("microphone",controller)
                p1 = myfunc()


                def myfunc(self):
                    print("Controller is connected"+self.controller)
                    p1 = consoleObjects("controller",ps5)
                    p1 = myfunc()



# 8. Create a class that will represent a video game for your console.
# Your class should have 4 attributes and 3 methods objects.
# ONCE You've created your class, create 2 unique video games objects.. 
