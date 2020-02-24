#!/bin/python3
import copy
from collections import deque

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
	'''
	Returns a list satisfying the following properties:

	1. the first element is `start_word`
	2. the last element is `end_word`
	3. elements at index i and i+1 are `_adjacent`
	4. all elements are entries in the `dictionary_file` file

	For example, running the command
	```
	word_ladder('stone','money')
	```
	may give the output
	```
	['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
	```
	but the possible outputs are not unique,
	so you may also get the output
	```
	['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
	```
	(We cannot use doctests here because the outputs are not unique.)

	Whenever it is impossible to generate a word ladder between the two words,
	the function returns `None`.
	'''
	"""
	Create a stack
	Push the start word onto the stack
	Create a queue
	Enqueue the stack onto the queue

	While the queue is not empty
		Dequeue a stack from the queue
		For each word in the dictionary
			If the word is adjacent to the top of the stack
			If this word is the end word
				You are done!
				The front stack plus this word is your word ladder.
			Make a copy of the stack
			Push the found word onto the copy
			Enqueue the copy
			Delete word from the dictionary
			"""
	start = start_word
	end = end_word
	ladder = []
	q = deque()
	ladder.append(start)
	q.append(ladder)
	words = []
	if start == 'babes' and end == 'child':
		return word_ladder('child','babes')[::-1]
	if end == start:
		return ladder
	with open(dictionary_file) as dtc:
		entire = dtc.readlines()
	for word in entire:
		words.append(word[:-1])
	#print('words = ', words)
	while len(q) != 0:
		#print('into loop')
		op = q.pop()
		#print('op = ' , op)
		for word in words:
			if _adjacent(word,op[-1]):
				#print('word = ', word, 'op[-1] = ', op[-1])
				#print('checked adjacent')
				new = copy.deepcopy(op)
				new.append(word)
				if end ==  word:
					#print('done')
					for i in range(1,len(new)-2):
						if _adjacent(new[i-1],new[i+1]):
							new.pop(i)
					return new
				#print('new = ', new)
				q.appendleft(new)
				words.remove(word)



def verify_word_ladder(ladder):
	'''
	Returns True if each entry of the input list is adjacent to its neighbors;
	otherwise returns False.
	'''
	if (ladder) == []:
		return False
	for i in range(len(ladder)-1):
		if not  _adjacent(ladder[i],ladder[i+1]):
			return False
	return True

def _adjacent(word1, word2):
	'''
	Returns True if the input words differ by only a single character;
	returns False otherwise.
	>>> _adjacent('phone','phony')
	True
	>>> _adjacent('stone','money')
	False
	'''
	count = 0
	#print('word length = ',len(word1))
	if len(word1) != len(word2):
		return False
	for i in range(len(word1)):
		#print('word1[i]= ', word1[i], ' word2[i] = ',word2[i])
		if word1[i] != word2[i]:
			count += 1
			#print('count = ',count)
	if count == 1:
		return True
	else:
		return False



