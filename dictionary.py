################## CODE WITH BENNY ############################

import json
from difflib import get_close_matches

# Load the json file
data = json.load(open('data.json', 'r'))


'''
This is a direct solution. Uncomment to test the code
'''
# for continuosly asking user input
# while True:
#     print()
#     print('Dictionary. Enter q to quit')
#     # user enters a word
#     word = input('Enter word: ').lower()
#     print()
#     # break the loop
#     if word.lower() == 'q':
#         break
#     # checks if the word is in the data.keys()
#     elif word in data.keys():
#         result = data[word]
#         if len(result) > 1:
#             for res in result:
#                 print(res)
#         else:
#             print(result[0])
#         # lower case words
#     elif word.lower() in data.keys():
#         result = data[word.lower()]
#         if len(result) > 1:
#             for res in result:
#                 print(res)
#         else:
#             print(result[0])
#     # if uppercase word
#     elif word.upper() in data.keys():
#         result = data[word.upper()]
#         if len(result) > 1:
#             for res in result:
#                 print(res)
#         else:
#             print(result[0])
#     # If title word
#     elif word.title() in data.keys():
#         result = data[word.title()]
#         if len(result) > 1:
#             for res in result:
#                 print(res)
#         else:
#             print(result[0])

#     # if no match we predict the nearest match
#     else:
#         # checks if there is a match - returns a list
#         match = get_close_matches(word, data.keys(), cutoff=0.8)
#         # check if one or more words are a match
#         if len(match) >= 1:
#             predicted_match = match[0]
#             ans = input(f'Did you mean {predicted_match}? (y/n)').lower()
#             if ans == 'y':
#                 meant_word = data[predicted_match]
#                 # if more than one result
#                 for m in meant_word:
#                     print(m)
#                 # print(data[predicted_match])
#             else:
#                 # if no matches is found
#                 print('Please double check the word.')
#                 continue
#         else:
#             print('Not a valid word. Please double check the word.')
# print('Thank You. See you soon')


# Functional approach
'''
This is a functional approach to the same thing.
'''


def word_meaning():
    while True:
        print()
        print('Dictionary. Enter q to quit')
        # user enters a word
        word = input('Enter word: ')
        print()
        # break the loop
        if word.lower() == 'q':
            break

        # checks if the word is in the data.keys()
        elif word in data.keys():
            result = data[word]
            if len(result) > 1:
                for res in result:
                    print(res)
            else:
                print(result[0])
            # lower case words
        elif word.lower() in data.keys():
            result = data[word.lower()]
            if len(result) > 1:
                for res in result:
                    print(res)
            else:
                print(result[0])
        # if uppercase word
        elif word.upper() in data.keys():
            result = data[word.upper()]
            if len(result) > 1:
                for res in result:
                    print(res)
            else:
                print(result[0])
        # If title word
        elif word.title() in data.keys():
            result = data[word.title()]
            if len(result) > 1:
                for res in result:
                    print(res)
            else:
                print(result[0])

        # if no match we predict the nearest match
        else:
            # checks if there is a match - returns a list
            match = get_close_matches(word, data.keys(), cutoff=0.8)
            # check if one or more words are a match
            if len(match) >= 1:
                predicted_match = match[0]
                ans = input(f'Did you mean {predicted_match}? (y/n)').lower()
                if ans == 'y':
                    meant_word = data[predicted_match]
                    # if more than one result
                    for m in meant_word:
                        print(m)

                else:
                    # if no matches is found
                    print('Please double check the word.')
                    continue
            else:
                print('Not a valid word. Please double check the word.')
    print('Thank You. See you soon')


word_meaning()
