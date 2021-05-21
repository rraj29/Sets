#create a program that takes some text and
# returns all the unique characters in the text that are not vowels
#in the alphabetical order
#
#you can enter a text or initialize a string

sample_text = input("Please input a string: ")

vowel = frozenset("aeiou ")     # added a space at last, so we don't get the spaces in the output
#vowel = {'a','e','i','o','u',' '}     #it does the same work as line just above.
string = set()

final_text = set(sample_text).difference(vowel)
print(final_text)

print(sorted(final_text))
