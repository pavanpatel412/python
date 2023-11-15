# Write a Python class to reverse a string word by word.
# assign some input to the word variable
word = input("enter somthing:")
# split that word 
word2 = word.split()
# now join split word by adding some reverseindex in it >
reverser = ' '.join(word2[::-1])
reverser2 = "".join(reverser[::-1])
print(reverser2)
# another example using class and object
class ReversedObj:
    def reverse_word(self, word):
        word2 = word.split()
        reversed_words = ' '.join(word2[::-1])
        reversed_words2 = "".join(reversed_words[::-1])
        
        return reversed_words2

obj1 = ReversedObj()
result = obj1.reverse_word("kumara swami is  the one and only tiger")
print(result)

