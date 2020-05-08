from tkinter import *
from tkinter import messagebox
import json
from difflib import get_close_matches

# Load the json file
data = json.load(open('data.json', 'r'))


window = Tk()
window.title('Dictionary')
window.geometry('450x500')

def word_meaning():
    # user enters a word
    word_meaning_entry.delete('1.0', END)
    word = my_word.get()
    # break the loop

    # checks if the word is in the data.keys()
    if word in data.keys():
        result = data[word]
        if len(result) > 1:
            for res in result:
                word_meaning_entry.insert(END,res)
                word_meaning_entry.insert(END,'\n')
        else:
            word_meaning_entry.insert(END,result[0])
            word_meaning_entry.insert(END,'\n')
    # lower case words
    elif word.lower() in data.keys():
        result = data[word.lower()]
        if len(result) > 1:
            for res in result:
                word_meaning_entry.insert(END,res)
                word_meaning_entry.insert(END,'\n')
        else:
            word_meaning_entry.insert(END,result[0])
            word_meaning_entry.insert(END,'\n')
    # if uppercase word
    elif word.upper() in data.keys():
        result = data[word.upper()]
        if len(result) > 1:
            for res in result:
                word_meaning_entry.insert(END,res)
                word_meaning_entry.insert(END,'\n')
        else:
            word_meaning_entry.insert(END,result[0])
            word_meaning_entry.insert(END,'\n')
    
    # If title word
    elif word.title() in data.keys():
        result = data[word.title()]
        if len(result) > 1:
            for res in result:
                word_meaning_entry.insert(END,res)
                word_meaning_entry.insert(END,'\n')

        else:
            word_meaning_entry.insert(END,result[0])
            word_meaning_entry.insert(END,'\n')


    # if no match we predict the nearest match
    else:
        # checks if there is a match - returns a list
        match = get_close_matches(word, data.keys(), cutoff=0.8)
        # check if one or more words are a match
        if len(match) >= 1:
            predicted_match = match[0]
            messagebox.showinfo('Word',f'Did you mean {predicted_match}?')
            meant_word = data[predicted_match]
            # if more than one result
            for m in meant_word:
                word_meaning_entry.insert(END,m)
                word_meaning_entry.insert(END,'\n')

        else:
            # if no matches is found
            messagebox.showerror('No matches found','Check the word')



title = Label(window, text="Enter word to get it's meaning")
title.grid(row=0, column=0, columnspan=3)

word_label = Label(window, text='Word:')
word_label.grid(row=1,column=0)

my_word = StringVar()
word_entry = Entry(window, textvariable=my_word)
word_entry.grid(row=1, column=1)

word_search = Button(window, text='Meaning', command=word_meaning)
word_search.grid(row=1, column=2)

word_meaning_entry = Text(window, width=55)
word_meaning_entry.grid(row=2, column=0, columnspan=3)

window.mainloop()