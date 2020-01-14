import urllib2
import random
import time
import sys
word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = urllib2.urlopen(word_site)
txt = response.read()
#Words is a list with strings in it
lstwords = txt.splitlines()
answer = random.choice(lstwords).lower()


#print answer

#ANSWER IS THE WORD YOU ARE GUESSING FOR
#Start game
question = raw_input("Hello, welcome to hangman. What's your name?: ")
time.sleep(1)
print "Oh, hi %s" % (question)
time.sleep(1)
#Ready to start or not
rdornot = raw_input("Are you ready to start playing hangman?: ")
if rdornot.lower() == "yes":
	#Start hangman game
	print "Lets start!"
	#Starting guesses is going to be going down
	guesses = [1,2,3,4,5,6,7,8,9,10]
	#Dashes is the one it's going to print
	amount_of_dashes = '_ ' * len(answer)  
	print amount_of_dashes
	let_in_ans = 0
	#Length of answer
	let_in_ans = len(answer)
	counter = 0
	counter2 = 0
	answer_list = []
	for x in answer:
		answer_list.append(x)
		x = answer_list[counter]
		counter += 1
	#make lower line a comment
	print answer_list
	guess_counter = 0
	for x in guesses:
		guess_attempt = raw_input("Guess the first letter!")
		if guess_attempt.lower() in answer_list:
			print "Good"
		else:
			print "Fail"




elif rdornot.lower() == "no":
	print "Okay"
	sys.exit()
else:
	print "That's not an option baka"
	sys.exit()
