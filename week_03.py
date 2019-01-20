# Week 3: Homework

# A cipher is a secret code for a language. In this case study, we will explore
# a cipher that is reported by contemporary Greek historians to have been used
# by Julius Caesar to send secret messages to generals during times of war.
#
# The Caesar cipher shifts each letter of a message to another letter in the
# alphabet located a fixed distance from the original letter. If our encryption
# key were 1, we would shift h to the next letter i, i to the next letter j,
# and so on. If we reach the end of the alphabet, which for us is the space
# character, we simply loop back to a. To decode the message, we make a similar
# shift, except we move the same number of steps backwards in the alphabet.
#
# Over the next five exercises, we will create our own Caesar cipher, as well
# as a message decoder for this cipher. In this exercise, we will define the
# alphabet used in the cipher.

# Exercise 1
# The string library has been imported. Create a string called alphabet
# consisting of the lowercase letters of the space character space ' ',
# concatenated with string.ascii_lowercase at the end.
import string
alphabet = ' ' + string.ascii_lowercase

# Excercise 2
# alphabet has already defined from the last exercise. Create a dictionary
# with keys consisting of the characters in alphabet, and values consisting of
# the numbers from 0 to 26.
Store this as positions.
positions = {alphabet[i]:i for i in range(len(alphabet))}

# Excercise 3
# alphabet and positions have already been defined from previous exercises.
# Use positions to create an encoded message based on message where each
# character in message has been shifted forward by 1 position, as defined by
# positions. Note that you can ensure the result remains within 0-26 using
# result % 27
# Store this as encoded_message
message = "hi my name is caesar"

encoded_message = ''

for letter in message:
    encoded_message += alphabet[positions[letter] + 1 % 27]

# Excercise 4
# alphabet, position and message remain defined from previous exercises. In
# addition, sample code for the previous exercise is provided below. Modify
# this code to define a function encoding that takes a message as input as well
# as an int encryption key key to encode a message with the Caesar cipher by
# shifting each letter in message by key positions.
# Your function should return a string consisting of these encoded letters.
# Use encode to encode message using key = 3, and save the result as
# encoded_message.
# Print encoded_message
def encode(message, key):
    encoding_list = []
    for char in message:
        position = positions[char]
        encoded_position = (position + key) % 27
        encoding_list.append(alphabet[encoded_position])
    encoded_string = ''.join(encoding_list)
    return encoded_string

encoded_message = encode(message, key = 3)
print(encoded_message)

# Excercise 5
# Note that encoding and encoded_message are already loaded from the previous
# problem. Use encoding to decode encoded_message using key = -3.
# Store your decoded message as decoded_message.
# Print decoded_message. Does this recover your original message?
decoded_message = encoding(encoded_message, key = -3)

# print your decoded message here!
print(decoded_message)
