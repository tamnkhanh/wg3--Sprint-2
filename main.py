#this is a function that writes files
def write_file(filename, data):
	new_file = open(filename, "w")
	for sentence in data:
		for word in sentence:
			new_file.write(word + " ")
		new_file.write("\n")
	new_file.close()

"""
***1.  Create a function to add a shift to a letter.

2.  Create a function to subtract a shift from a letter.

***3.  Create a function to encrypt words using a shift

4.  Create a function to decrypt words using a shift

***5.  Create a function to encrypt a message using a shift.

6.  Create a function to decrypt a message using a shift.
"""

def encrypt_letter(letter, shift):
  #write the function to take a letter and a shift (from 1 to 25) and return the 
  #shifted character
  cipher = ord(letter) + shift  
  return chr(cipher)


def decrypt_letter(letter, shift):
  #write the function to take a letter and a shift (from 1 to 25) and return the 
  #shifted character
  cipher = ord(letter) - shift
  return chr(cipher)


def encrypt_word(word, shift):
  #write the function to take a word and a shift (from 1 to 25) and return the 
  #shifted

  #so we want to shift the letters in a word/words over by a certain shift amount 
  list_letters = []

  for eachletter in word:
    cipher = chr(ord(eachletter) + shift)
    list_letters.append(cipher)
  return list_letters
  

def decrypt_word(word, shift):
  #write the function to take a word and a shift (from 1 to 25) and return the 
  list_letters = []

  for eachletter in word:
    cipher = chr(ord(eachletter) - shift)
    list_letters.append(cipher)
  return list_letters

#>>>>>>>>>>message is the list of lists of words

def encrypt_message(message, shift):
  #write the function to take a message and a shift (from 1 to 25) and return the shifted message  
  #initialize empty massage list to later return 
  messageList = []
  for sentence in message:
    newLine = []
    for word in sentence:
      newWord = []
      for letter in word:
        newWord.append(chr(ord(letter) + shift))
      newLine.append(newWord)
    messageList.append(messageList)
  return messageList

def decrypt_message(message, shift):
  #write the function to take a message and a shift (from 1 to 25) and return the 
  #shifted message  
  messageList = []
  for sentence in message:
    newLine = []
    for word in sentence:
      newWord = []
      for letter in word:
        newWord.append(chr(ord(letter) - shift))
      newLine.append(newWord)
    messageList.append(messageList)
  return messageList

###############################################
#a is shifted over by 5, results to f
write_file('enChar', encrypt_letter('a', 5))
#f is shifted back by 5, results to original letter a
write_file('deChar', decrypt_letter('f', 5))
#the word table is shifted by 5, results to yfgqj
write_file('enWord', encrypt_word('table', 5))
#the shifted word yfgqj is decrypted by 5, results to orginal word table
write_file('deWord', decrypt_word('yfgqj', 5))


