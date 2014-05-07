import os
import time
import difflib
from itertools import zip_longest

def diffindex(string1, string2):
    for i, (char1, char2) in enumerate(zip_longest(string1, string2)):
        if char1 != char2:
            return i
    # return -1

# read in the exercise text as list of sentences
mywd = os.path.dirname(os.path.realpath(__file__))
myfile = os.path.join(mywd, "examplaryText.txt")
inputDataFile = open(myfile,'r')
lsInput = inputDataFile.readlines()	# readlines -> list of strings
inputData = ''.join(lsInput)		# join list of strings -> string (but on different lines because of imported \n)
inputDataFile.close()
lsRows = inputData.split('\n')		# split string -> list (empty string at end, because empty last line in file)

# print the exercise text
print(lsRows)

# set up the typing exercise
nrSentences = 0
nrSentencesCorrect = 0
nrCharacters = 0
nrTyped = 0
exString = 'Type this sentence'
input('Press Enter to Start Typing\n')
start = time.time()
for example in lsRows:
	myTyping = input(example+'\n')
	nrSentences += 1
	nrTyped += len(myTyping)
	nrCharacters += len(example)
	seq=difflib.SequenceMatcher(None,example,myTyping)
	if((1-seq.ratio())>0.0):
		print("errors: difference length ("+str(len(myTyping)-len(example)),") - first error ("+str(diffindex(myTyping,example))+") and % ("+str(round(1-seq.ratio(),2))+")")
		for block in seq.get_matching_blocks():
			print("a[%d] and b[%d] match for %d elements" % block)
		print("\n")
	else:
		nrSentencesCorrect += 1
		
end = time.time()
duration = end - start

# output results
print("\nthe results are as follows: ")
print("the process took "+str(round(duration,2))+" seconds")
print(str(nrSentencesCorrect)+" sentences were correct, which is "+str(round(nrSentencesCorrect/nrSentences,2))+"%")
print(str(nrCharacters)+" characters were offered in ",str(nrSentences)," sentences")
print("the number of typed characters is "+str(nrTyped))
print("the number of characters per second is "+str(round(nrCharacters/duration,2))," which is "+str(round(nrCharacters/duration*60,2))," characters per minute\n")
