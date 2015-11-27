import string
import math


# Ten points per personally-described character whose fate we know by the end of the story
def characters(story):
	return 0


#ln(87) points per different Oscar-winning movie title included, up to a limit of five. (You can change punctuation, capitalisation and spell numbers out)
def oscar(story):
	return 0


#10 *SQRT(n) points for the longest run of n consecutive lines of iambic pentameter (you don't have to put line breaks in)
def pentameter(story):
	return 0


#Sqrt(n) points where n i sthe sum of the squares of the lengths of your sentences which are acrostics of valid words
def acrostic(story):
	return 0

#pi * sqrt(n) points for the longest run of n words in a row whose lengthhs (mod 10 make up the first n digits of pi)
def pi(story):
    pi = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091"
    piindex = 0
    storyindex = 0
    currentrun=0
    maxrun=0
    storywords= story.split()
    for word in storywords:
        if len(word)%10==int(pi[piindex]):
            currentrun+=1
            piindex+=1
            if currentrun > maxrun:
                maxrun=currentrun
        else:
            currentrun=0
            piindex=0
    return float(pi)*1e-250 * math.sqrt(maxrun)

#ln(118) * SQRT(n) points for the longest run of n words in a row that can be made of chemical element symbols (ingoring spaces and punctuation and capitalisation)
def elements(story):
	return 0

#3 *sqrt(n) points for the longest run of n words in a row that are in alphabetical order
def alphabetical(story):
	return 0

#1.52 * sqrt(n) points if a string of consecutive words in your story anagrams to the names of two stations on the same London Underground line, the shortest route between which on that line has n stops. Scored up to a limit of three times on different lines.
def underground(story):
	return 0

#n points where n! is the greatest factorial dividing the product of the lengths of all sentences in the story.
def factorial(story):
	return 0

#n words for the greatest n such that you use exactly n different n-letter words
def nDifferentNLetter(story):
	return 0

#15 exp(-ln(n/9)^2) points if you don't use any words that score n in scrabble, for the n which makes this biggest
def scrabble(story):
	return 0


#(n-13)^2/13 points if you use exactly n of the letters of the alphabet an odd number of times
def alphabet(story):
	return 0

story = ""
story = story.translate(string.maketrans("",""), string.punctuation) #Remove punctuation

print characters(story) + oscar(story) + pentameter(story) + acrostic(story) + pi(story) + elements(story) + alphabetical(story) + underground(story) + factorial(story) + nDifferentNLetter(story) + scrabble(story) + alphabet(story)