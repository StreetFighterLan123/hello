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
#makes it so that it shouldn't be more than 10 letters
r = 1
while r == 1:
	if len(answer) >= 10:
		answer = random.choice(lstwords).lower()
	elif len(answer) < 10:
			r = 0

#print answer
def makeitadash(x):
	x = '_ ' * len(x)
	return x
#ANSWER IS THE WORD YOU ARE GUESSING FOR
#Start game
rista = []
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
	counter_answer_original_for_dash_substituion = []
	amount_of_dashes = ['_ ' * len(answer)]
	for x in answer:
		counter_answer_original_for_dash_substituion.append(makeitadash(x))
	print amount_of_dashes
	print counter_answer_original_for_dash_substituion
	let_in_ans = 0
	#Length of answer
	let_in_ans = len(answer)
	counter = 0
	answer_list = []
	for x in answer:
		answer_list.append(x)
		x = answer_list[counter]
		counter += 1
	#make lower line a comment
	#print answer_list
	guess_counter = 0
	for x in guesses:
		guess_attempt = raw_input("Guess the first letter!")
		if guess_attempt.lower() in answer_list:
			print "Good"
			#removed = answer_list.remove(guess_attempt.lower())
			#difference = len(answer_list) - len(removed)
			#print difference
			answer_list.remove(guess_attempt.lower())
			#Now we have to find the one you said and make it show in the list.
			counter_answer_original_for_dash_substituion = ['_ ' * len(answer_list)]
			#amount_of_dashes = ['_ ' * len(counter_answer_original_for_dash_substituion)]
			#That would just make it one so our counter thing is now our amount.
			rista.append(guess_attempt.lower())
			#print guess_attempt.lower() + counter_answer_original_for_dash_substituion[0]
			for x in rista:
				print x
			print counter_answer_original_for_dash_substituion[0]
			#print answer_list
			print rista
			#make the print answer_list a comment later on
		else:
			print "Fail"


elif rdornot.lower() == "no":
	print "Okay. Have fun next time!"
	sys.exit()
else:
	print "That's not an option baka."
	sys.exit()
