

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
	return 0

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

print characters(story) + oscar(story) + pentameter(story) + acrostic(story) + pi(story) + elements(story) + alphabetical(story) + underground(story) + factorial(story) + nDifferentNLetter(story) + scrabble(story) + alphabet(story)