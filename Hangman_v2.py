import urllib2
import random
import time
import sys
word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-ty$
response = urllib2.urlopen(word_site)
txt = response.read()
#Words is a list with strings in it
lstwords = txt.splitlines()
answer = random.choice(lstwords).lower()

guesses = [1,2,3,4,5,6,7,8,9,10]


#print answer
def makeitadash(x):
        x = '_ ' * len(x)
        return x
#ANSWER IS THE WORD YOU ARE GUESSING FOR
#Start game
question = raw_input("Hello, welcome to hangman. What's your name?: ")
time.sleep(1)
print "Oh, hi %s" % (question)
time.sleep(1)
#Ready to start or not
rdornot = raw_input("Are you ready to start playing hangman?: ")
if rdornot.lower() == "yes":
        #while len(guesses) > 0:
                

