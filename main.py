#1
from abc import ABC, abstractmethod

class WordCounter(ABC):
    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass
#2
class ListCount(WordCounter):
    def calculateFreqs(self):
        with open("C:\Users\kaana\OneDrive\Belgeler\Masaüstü\weirdwords.txt", 'r') as file:
            words = file.read().split()
        word_freqs = {}
        for word in words:
            word_freqs[word] = word_freqs.get(word, 0) + 1
        return word_freqs

class DictCount(WordCounter):
    def calculateFreqs(self):
        with open("C:\Users\kaana\OneDrive\Belgeler\Masaüstü\weirdwords.txt", 'r') as file:
            words = file.read().split()
        word_freqs = {}
        for word in words:
            if word in word_freqs:
                word_freqs[word] += 1
            else:
                word_freqs[word] = 1
        return word_freqs
#3
class ListCount(WordCounter):
    def calculateFreqs(self):
        with open("C:\Users\kaana\OneDrive\Belgeler\Masaüstü\weirdwords.txt", 'r') as file:
            content = file.read()
        letters = list(content)
        letter_freqs = []
        for letter in letters:
            freq = letters.count(letter)
            if letter not in letter_freqs:
                letter_freqs.append(letter)
                letter_freqs.append(freq)
        return letter_freqs
#4
class DictCount(WordCounter):
    def calculateFreqs(self):
        with open("C:\Users\kaana\OneDrive\Belgeler\Masaüstü\weirdwords.txt", 'r') as file:
            content = file.read()
        letters = list(content)
        letter_freqs = {}
        for letter in letters:
            if letter in letter_freqs:
                letter_freqs[letter] += 1
            else:
                letter_freqs[letter] = 1
        return letter_freqs
#5
# Create objects from the subclasses
list_counter = ListCount("weirdWords.txt")
dict_counter = DictCount("weirdWords.txt")

# Call the calculateFreqs() method and print the results
print("ListCount:")
list_freqs = list_counter.calculateFreqs()
print(list_freqs)

print("DictCount:")
dict_freqs = dict_counter.calculateFreqs()
print(dict_freqs)

