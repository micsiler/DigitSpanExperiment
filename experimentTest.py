#Code Adapted from https://github.com/tadorfer/digit-span-test/blob/master/digitspantest_fw.py
#Addded sets instead of increasing digits
#Added name functionality
#Added database transfer

import tkinter as tk     
import random



def startTest(*args):
    nums = ['One','Two','Three','Four','Five','Six','Seven','Eight']
    wdw.unbind('<Return>')
    canvas.delete('all')
    while True:
    
        global TRIALS, DIGITS, SET
        SET += 1
        TRIALS += 1

        txt = '{0}-Digit Sequence'.format(nums[DIGITS - 1])
        seqtxt = canvas.create_text(Width/2, Height/3.5, fill='darkblue', 
                                                         font='calibre 32', 
                                                         text=txt, 
                                                         justify='c')
        canvas.after(1200, canvas.update())
        seq = random.sample(range(10), DIGITS)
        while consecutive(seq) == False:
            seq = random.sample(range(10), DIGITS)
      
        seq = str(seq)
        seq_digits = ''.join(c for c in seq if c.isdigit())
        length = len(seq_digits)
        for a in range(length):
            z = canvas.create_text(Width/2, Height/2, fill='darkblue', 
                                                      font='Times 160', 
                                                      text=seq_digits[a], 
                                                      justify='c')
            canvas.after(1000,canvas.update())
            canvas.delete(z)        
        
        label = canvas.create_text(Width/2, Height/2.3, fill='darkblue', 
                                                        font='calibre 26', 
                                                        text='Repeat the sequence here', 
                                                        justify='c')
        
        entry = tk.Text(wdw, width=length, height=1, font=('calibre', 32))
        e = canvas.create_window(Width/2, Height/2, window=entry)
        entry.focus()
        
        def delete():
            canvas.delete('all')
            startTest()
            
        def get_text(event=None):
            global userNumbers, generatedNumbers, FAILURES, DIGITS
            content = entry.get(1.0, "end-1c")

            userNumbers.append(content)
            generatedNumbers.append(seq_digits)

            canvas.delete(label, b, e, seqtxt)
            if content == seq_digits:
                canvas.create_text(Width/2, Height/2.3, fill='darkblue', 
                                                        font='calibre 26', 
                                                        text='Next', 
                                                        justify='c')
                canvas.after(1200, delete)
            else:
                FAILURES += 1
                canvas.create_text(Width/2, Height/2.3, fill='darkblue', 
                                                        font='calibre 26', 
                                                        text='Next', 
                                                        justify='c')
                canvas.after(1200, delete)

            if DIGITS == 9: #Change this to to go past the eight trials (not have to add more words in num)
                canvas.delete('all')
                canvas.create_text(Width/2, Height/2.3, fill='darkblue', font='calibre 26', text='Thank you for your participation!', justify='c')

                wdw.after(3000, lambda: wdw.destroy())

        if SET == 3: # number of trials given a specific digit length
                SET = 0
                DIGITS += 1
        
                
        button2 = tk.Button(wdw, height=2, width=10, text='Continue', 
                                                     font='calibre 20', 
                                                     fg='black', 
                                                     command=get_text, bd=0)
        button2.configure(bg='#4682B4', 
                          activebackground='#36648B', 
                          activeforeground='white')
        entry.bind('<Return>', get_text)  
        b = canvas.create_window(Width/2, Height/1.6, window=button2)
        break
    

def consecutive(sequence):
    l = len(sequence)
    res = []
    for x in range(l-1):
        if sequence[x] == sequence[x+1]+1 or sequence[x] == sequence[x+1]-1:
            res.append(1)
    if len(res) > 0:
        return False

def getName(*args):
    global name
    name = name_entry.get(1.0, "end-1c")
    if len(name) == 0:
        name = "Null"
    canvas.delete('all')
    



wdw = tk.Tk()
wdw.title('Digit Span Test')
Width = wdw.winfo_screenwidth()
Height = wdw.winfo_screenheight()
wdw.geometry("%dx%d" % (Width, Height))
canvas = tk.Canvas(wdw, bg='#FDF5E6')
canvas.pack(fill = 'both', expand = True)
wdw.state('zoomed')


startTestPrompt = '''\nThis is a Digit Span Test that evaluates working memory performance.
Try to remember the digits in the order that they are presented and repeat
them once the sequence has stopped. 
We will start out with 3 digits which will increase to 8 digits as the test progresses.
You will complete this experiment TWICE with and without your phone present
\nPlease Enter your name and then press 'Enter' if you are ready to start the test.'''

title = 'Digit Span Test for Working Memory Evaluation'

name = ""

canvas.create_text(Width/2, Height/4.5, fill='Black', 
                                        font='calibre 45', 
                                        text=title, 
                                        justify='c')

canvas.create_text(Width/2, Height/2.2, fill='darkblue', 
                                        font='calibre 30', 
                                        text=startTestPrompt, 
                                        justify='c')

name_entry = tk.Text(wdw, width=10, height=1, font=('calibre', 32))
e = canvas.create_window(Width/2, Height/1.4, window=name_entry)
name_entry.focus()

name_entry.bind('<Return>', getName)


seqL = 0
DIGITS = 3
FAILURES = 0
SET = 0
TRIALS = 0

wdw.bind('<Return>', lambda event: startTest())
userNumbers, generatedNumbers = [], []

wdw.mainloop()

score = 1 - (FAILURES/TRIALS)
score = round(score,2)

print('Name: ', name)
print('Generated: ', generatedNumbers)
print('Repeated:  ', userNumbers)
print('Score: ', score)

with open('score_data.txt', 'a') as f:
    f.write(name + " " + str(score) + '\n')

with open('input_data.txt', 'a') as f:
    f.write(name + "\n")
    f.write("Generated: " + " ".join(generatedNumbers) + "\n")
    f.write("Input: " + " ".join(userNumbers) + "\n")






