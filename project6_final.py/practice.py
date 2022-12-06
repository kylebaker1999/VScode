from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random


window = Tk()
window.title('Review Vocab Hangman Game')
semester_vocab= ['PROJECT','COMPUTER','SCIENCE','DICTIONARY','BRACKETS','FORLOOP','WHILELOOP','PARENTHESES','PYTESTPROGRAM','TKINTERPACKAGE','VARIABLE','PYTHON','CURLYBRACE',
            'IMPORTFILE','LENGTH','LAMBDA','LIST','MOLARMASSCALCULATOR','SHOPPINGLIST','VOLUME','TEAMACTIVITIES','WEEKLYPROOVE','ASSERT','PARAMETERS','NOPAPER','ERROR','CODECHALLENGES',
            'CREATESENTENCES']
            
photos = [PhotoImage(file="project6_final.py/hang4.png"), PhotoImage(file="project6_final.py/hang5.png"),PhotoImage(file="project6_final.py/hang6.png"), PhotoImage(file="project6_final.py/hang7.png"), PhotoImage(file="project6_final.py/hang8.png"),PhotoImage(file="project6_final.py/hang9.png"), PhotoImage(file="project6_final.py/hang10.png"), PhotoImage(file="project6_final.py/hang11.png")]
def start_game():
    global word
    global guess_count
    guess_count =0
    
    selected_word=random.choice(semester_vocab)
    word = " ".join(selected_word)
    word_lable.set(' '.join("_" * len(selected_word)))

def guess(letter_selcetion):
	global guess_count
	if guess_count < 11:	
		text = list(word)
		guessed = list(word_lable.get())
		if word.count(letter_selcetion)>0:
			for c in range(len(text)):
				if text[c]==letter_selcetion:
					guessed[c]=letter_selcetion
				word_lable.set("".join(guessed))
				if word_lable.get()==word:
					messagebox.showinfo("Final Project","TOO EASY, GOOD JOB REMEMBERING THE SEMESTER")
		else:
			guess_count += 1
			imgLabel.config(image=photos[guess_count])
			if guess_count==7:
					messagebox.showwarning("Final Project","Should have paid more attention")


imgLabel=Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

word_lable = StringVar()
Label(window, textvariable  =word_lable,font=('calibri 24 bold')).grid(row=0, column=3 ,columnspan=6,padx=10)

n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=('ariel 18'), width=4).grid(row=1+n//9,column=n%9)
    n+=1

Button(window, text="Start Over", command=lambda:start_game(), font=("calibri 10 bold")).grid(row=3, column=8)
start_game()
window.mainloop()



from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random


window = Tk()
window.title('Review Vocab Hangman Game')
semester_vocab= ['PROJECT','COMPUTER','SCIENCE','DICTIONARY','BRACKETS','FORLOOP','WHILELOOP','PARENTHESES','PYTESTPROGRAM','TKINTERPACKAGE','VARIABLE','PYTHON','CURLYBRACE',
            'IMPORTFILE','LENGTH','LAMBDA','LIST','MOLARMASSCALCULATOR','SHOPPINGLIST','VOLUME','TEAMACTIVITIES','WEEKLYPROOVE','ASSERT','PARAMETERS','NOPAPER','ERROR','CODECHALLENGES',
            'CREATESENTENCES']
            
photos = [PhotoImage(file="project6_final.py/hang0.png"), PhotoImage(file="project6_final.py/hang1.png"), PhotoImage(file="project6_final.py/hang2.png"),PhotoImage(file="project6_final.py/hang3.png"), PhotoImage(file="project6_final.py/hang4.png"), PhotoImage(file="project6_final.py/hang5.png"),PhotoImage(file="project6_final.py/hang6.png"), PhotoImage(file="project6_final.py/hang7.png"), PhotoImage(file="project6_final.py/hang8.png"),PhotoImage(file="project6_final.py/hang9.png"), PhotoImage(file="project6_final.py/hang10.png"), PhotoImage(file="project6_final.py/hang11.png")]
def start_game():
    global word
    global guess_count
    guess_count =0
    
    selected_word=random.choice(semester_vocab)
    word = " ".join(selected_word)
    word_lable.set(' '.join("_" * len(selected_word)))

def guess(letter_selcetion):
	global guess_count
	if guess_count < 11:	
		text = list(word)
		guessed = list(word_lable.get())
		if word.count(letter_selcetion)>0:
			for c in range(len(text)):
				if text[c]==letter_selcetion:
					guessed[c]=letter_selcetion
				word_lable.set("".join(guessed))
				if word_lable.get()==word:
					messagebox.showinfo("Final Project","TOO EASY, GOOD JOB REMEMBERING THE SEMESTER")
		else:
			guess_count += 1
			imgLabel.config(image=photos[guess_count])
			if guess_count==11:
					messagebox.showwarning("Final Project","Should have paid more attention")


imgLabel=Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

word_lable = StringVar()
Label(window, textvariable  =word_lable,font=('calibri 24 bold')).grid(row=0, column=3 ,columnspan=6,padx=10)

n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=('ariel 18'), width=4).grid(row=1+n//9,column=n%9)
    n+=1

Button(window, text="Start Over", command=lambda:start_game(), font=("calibri 10 bold")).grid(row=3, column=8)
start_game()
window.mainloop()