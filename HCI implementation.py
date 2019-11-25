import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from tkinter import *
from random import choice
import xlrd
import time

ask = ["hi", "hello"]
general=['ok','thank you','thanks']
genaral_ans=['ok','thats great','its ok']
hi = ["hi", "hello", "Hello too"]
error = ["sorry, i don't know", "what u said?",'Can you ask again?','sorry i dont have answer for your question']

def wish(user_msg_tokens):
    msg_list.insert(END, 'BOT :' + choice(hi))
    del user_msg_tokens

def both_result(user_msg_tokens):
    wb = xlrd.open_workbook(r'C:\Users\saikrishna\Downloads\Book1.xlsx')
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    a = sheet.nrows
    if a % 2 == 0:
        value = sheet.cell_value((a - 1), 0)
        value1 = sheet.cell_value((a - 2), 0)
        value2 = value.__str__() + '   and   ' + value1.__str__()
        msg_list.insert(END, 'BOT :' + value2.__str__())
        del user_msg_tokens
    else:
        value = sheet.cell_value((a - 2), 0)
        value1 = sheet.cell_value((a - 1), 0)
        value2 = value.__str__() + '  and  ' + value1.__str__()
        msg_list.insert(END, 'BOT :' + value2.__str__())
        del user_msg_tokens

def only_temperture(user_msg_tokens):
    wb = xlrd.open_workbook(r'C:\Users\saikrishna\Downloads\Book1.xlsx')
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    a = sheet.nrows
    if a % 2 == 0:
        value = sheet.cell_value((a - 1), 0)
        msg_list.insert(END, 'BOT :' + value.__str__())
        del user_msg_tokens
    else:
        value = sheet.cell_value((a - 2), 0)
        msg_list.insert(END, 'BOT :' + value.__str__())
        del user_msg_tokens

def only_humidity(user_msg_tokens):
    wb = xlrd.open_workbook(r'C:\Users\saikrishna\Downloads\Book1.xlsx')
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    a = sheet.nrows
    if a % 2 == 0:
        value = sheet.cell_value((a - 2), 0)
        msg_list.insert(END, 'BOT :' + value.__str__())
        del user_msg_tokens
    else:
        value = sheet.cell_value((a - 1), 0)
        msg_list.insert(END, 'BOT :' + value.__str__())
        del user_msg_tokens
def gen_questions(user_msg_tokens):
    msg_list.insert(END, 'BOT :' + choice(genaral_ans))
    del user_msg_tokens
def error_questions(user_msg_tokens):
    msg_list.insert(END, 'BOT :' + choice(error))
    del user_msg_tokens
def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    if msg == "{quit}":
        top.quit()
    else:
        msg_list.insert(END,'YOU :'+ msg)
        user_msg_tokens=word_tokenize(msg)
        if any(elem in user_msg_tokens for elem in hi):
            top.after(2000,wish,user_msg_tokens)
        elif 'both' in user_msg_tokens or 'temperature' in user_msg_tokens and 'humidity' in user_msg_tokens:
            top.after(2000,both_result,user_msg_tokens)
        elif 'temperature' in user_msg_tokens:
            top.after(2000,only_temperture,user_msg_tokens)
        elif 'humidity' in user_msg_tokens:
            top.after(2000,only_humidity,user_msg_tokens)
        elif any(elem in user_msg_tokens  for elem in general):
            top.after(2000,gen_questions,user_msg_tokens)
        else:
            top.after(2000, error_questions, user_msg_tokens)

        def on_closing(event=None):

            my_msg.set("{quit}")
            send()

        top = Tk()
        top.title("TEMPERATURE AND HUMIDITY")
        messages_frame = Frame(top, highlightbackground="green", highlightcolor="green", highlightthickness=5,
                               width=100, height=100, bd=0)
        my_msg = StringVar()
        my_msg.set("Enter here")
        scrollbar = Scrollbar(messages_frame)  # To navigate through past messages.
        # Following will contain the messages.
        msg_list = Listbox(messages_frame, height=15, width=100, yscrollcommand=scrollbar.set,
                           highlightbackground="green", highlightcolor="green", highlightthickness=5)
        scrollbar.pack(side=RIGHT, fill=Y)
        msg_list.pack(side=LEFT, fill=BOTH)
        msg_list.pack()
        messages_frame.pack()
        msg_list.configure(background='black', foreground='white')
        entry_field = Entry(top, textvariable=my_msg)
        entry_field.bind("<Return>", send)
        entry_field.pack()
        msg_list.insert(END, 'BOT :Hi,i am temperature and humidity bot. How can i help you? ')
        send_button = Button(top, text="Send", command=send)
        send_button.pack()

        top.protocol("WM_DELETE_WINDOW", on_closing)
        mainloop()
