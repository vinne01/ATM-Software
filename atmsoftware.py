'''
/*******************************************************************************
/*  AUTHORS:         vinay kumar maurya                                              *
/*  DATE:            January 5, 2024                                           *
/*  VER:             3.10.11                                                     *
/*  DESCRIPTION:     GUI ATM project                                           *
/*******************************************************************************
'''
# https://pythonprogramming.altervista.org/tkinter-open-a-new-window-and-just-one/?doing_wp_cron=1641247623.1099369525909423828125
# https://stackoverflow.com/questions/47378715/tkinter-how-to-get-the-value-of-an-entry-widget
# https://realpython.com/python-keyerror/
# https://pretagteam.com/question/python-unboundlocalerror-local-variable-count-referenced-before-assignment

bank = {'215321701332': ['vinay kumar maurya', 1783, 3500166],
        '203659302214': ['Abhishek patel', 1390, 520001],
        '126355700193': ['Archita sahani', 1214, 111000], '201455998011': ['Rachina Mishra', 2001, 1200],
        '201122369851': ['Rajlaxmi', 8935, 178933]
    , '201356788002': ['Adarsh kumar', 3420, 55000], '203366789564': ['Vivek Rai', 1179, 18000],
        '201236787812': ['Pankaj Maurya', 1430, 180350]}
#account:[account holder,pin code,balance]

import tkinter
from tkinter import *
from tkinter.messagebox import showinfo

count = 0
flag = 0

# WINDOW0
win = tkinter.Tk()
win.geometry("500x500+200+100")
win.title("ATM System")
win.resizable(False, False)

accountnum = tkinter.StringVar()
entry = tkinter.Entry(win, width=25, textvariable=accountnum)
entry.place(relx=0.70, rely=0.15, anchor='ne')
label = tkinter.Label(win, text="Enter Account Number", width=20)
label.place(relx=0.30, rely=0.15, anchor='ne')


# GUI windows
def new_window1():
    global win1, entry1, password
    win1 = tkinter.Toplevel()
    win1.geometry("500x500+200+100")
    win1.title("ATM System")
    win1.resizable(False, False)
    label1 = tkinter.Label(win1, text="Enter Password", width=15)
    label1.place(relx=0.30, rely=0.15, anchor='ne')
    password = tkinter.StringVar()
    entry1 = tkinter.Entry(win1, width=25, show='*', textvariable=password)
    entry1.place(relx=0.70, rely=0.15, anchor='ne')
    button1 = tkinter.Button(win1, text="Enter", width=5, height=1)
    button1['command'] = check_entered_pass
    button1.place(relx=0.50, rely=0.22, anchor='ne')
    account_nums = bank.keys()
    if flag == 1:
        showinfo(title="ATM System", message=("Your account is locked , Please go to the branch"))
    else:
        if accountnum.get() in account_nums:
            win1.focus()
        elif accountnum.get() not in account_nums:
            showinfo(title="ATM System", message=("account number is not identified!"))
            win1.withdraw()


# WINDOW 0
button = tkinter.Button(win, text="Enter", width=5, height=1)
button['command'] = new_window1
button.place(relx=0.50, rely=0.22, anchor='ne')

#W
def new_window2():
    win1.withdraw()
    global win2
    win2 = tkinter.Toplevel()
    win2.geometry("500x500+200+100")
    win2.title("ATM System")
    win2.resizable(False, False)
    button21 = tkinter.Button(win2, text="Cash Withdraw", width=15, height=1)
    button21['command'] = new_window31
    button21.place(relx=0.60, rely=0.10, anchor='ne')

    button22 = tkinter.Button(win2, text="Balance Inquiry", width=15, height=1)
    button22['command'] = new_window32
    button22.place(relx=0.60, rely=0.20, anchor='ne')

    button23 = tkinter.Button(win2, text="Password Change", width=15, height=1)
    button23['command'] = new_window33
    button23.place(relx=0.60, rely=0.30, anchor='ne')

    button24 = tkinter.Button(win2, text="Fawry Service", width=15, height=1)
    button24['command'] = new_window34
    button24.place(relx=0.60, rely=0.40, anchor='ne')

    button25 = tkinter.Button(win2, text="Exit", width=5, height=1)
    button25['command'] = exit
    button25.place(relx=0.55, rely=0.50, anchor='ne')


# WINDOW for CashWithdraw
def new_window31():
    win2.withdraw()
    global win31, withdraw
    win31 = tkinter.Toplevel()
    win31.geometry("500x500+200+100")
    win31.title("ATM System ,Cash Withdraw")
    win31.resizable(False, False)
    withdraw = tkinter.IntVar()
    entry311 = tkinter.Entry(win31, width=25, textvariable=withdraw)
    entry311.place(relx=0.65, rely=0.25, anchor='ne')
    button311 = tkinter.Button(win31, text="Cash withdraw", width=15, height=1)
    button311['command'] = withdraw_Operation
    button311.place(relx=0.60, rely=0.40, anchor='ne')


# WINDOW for BalanceInquiry
def new_window32():
    win2.withdraw()
    global win32
    win32 = tkinter.Toplevel()
    win32.geometry("500x500+200+100")
    win32.title("ATM System ,Balance Inquiry   ")
    win32.resizable(False, False)
    id = accountnum.get()
    lb321 = bank[id][0]
    lb322 = str(bank[id][2])
    label321 = tkinter.Label(win32, text=lb321, width=30)
    label321.place(relx=0.65, rely=0.30, anchor='ne')
    label322 = tkinter.Label(win32, text=lb322, width=30)
    label322.place(relx=0.65, rely=0.40, anchor='ne')
    button321 = tkinter.Button(win32, text="OK", width=5, height=1)
    button321['command'] = exit_to_win
    button321.place(relx=0.50, rely=0.50, anchor='ne')


# WINDOW for PasswordChange
# ...

# WINDOW for PasswordChange
# ...

def check_Pass():
    pass1 = entry331.get()
    pass2 = entry332.get()
    if len(pass1) == 4 and len(pass2) == 4 and pass1 == pass2:
        update_password(pass1)
        showinfo(title="ATM System", message=("Password Saved!"))
        win33.destroy()
    else:
        showinfo(title="ATM System", message=("Enter Password Again"))

def update_password(new_password):
    # Update the password in the bank dictionary
    id2 = accountnum.get()
    bank[id2][1] = int(new_password)

# ...

# WINDOW for PasswordChange
def new_window33():
    win2.withdraw()
    global win33, entry331, entry332
    win33 = tkinter.Toplevel()
    win33.geometry("500x500+200+100")
    win33.title("ATM System , Password Change")
    win33.resizable(False, False)
    entry331 = tkinter.Entry(win33, width=25)
    entry331.place(relx=0.70, rely=0.15, anchor='ne')
    entry332 = tkinter.Entry(win33, width=25)
    entry332.place(relx=0.70, rely=0.25, anchor='ne')
    button331 = tkinter.Button(win33, text="OK", width=5, height=1)
    button331['command'] = check_Pass
    button331.place(relx=0.50, rely=0.50, anchor='ne')
    label331 = tkinter.Label(win33, text='New password', width=25)
    label331.place(relx=0.30, rely=0.15, anchor='ne')
    label332 = tkinter.Label(win33, text='New password again', width=25)
    label332.place(relx=0.30, rely=0.25, anchor='ne')

# ...





# ...



# WINDOW for Fawry Service
def new_window34():
    win2.withdraw()
    global win34
    win34 = tkinter.Toplevel()
    win34.geometry("500x500+200+100")
    win34.resizable(False, False)
    win34.title("ATM System")
    button341 = tkinter.Button(win34, text="Orange Recharge", width=20, height=1)
    button341['command'] = new_window344
    button341.place(relx=0.60, rely=0.20, anchor='ne')
    button342 = tkinter.Button(win34, text="Etisalat Recharge", width=20, height=1)
    button342['command'] = new_window344
    button342.place(relx=0.60, rely=0.30, anchor='ne')
    button343 = tkinter.Button(win34, text="Vodafone Recharge", width=20, height=1)
    button343['command'] = new_window344
    button343.place(relx=0.60, rely=0.40, anchor='ne')
    button344 = tkinter.Button(win34, text="Recharge", width=20, height=1)
    button344['command'] = new_window344
    button344.place(relx=0.60, rely=0.50, anchor='ne')


# WINDOW for Fawry Service Recharging (Orange,Vodafone,Etisalat,We)
def new_window344():
    win34.withdraw()
    global win344, entry3442, charge
    win344 = tkinter.Toplevel()
    win344.geometry("500x500+200+100")
    win344.title("ATM System , Fawry Service Recharging")
    win344.resizable(False, False)
    entry3441 = tkinter.Entry(win344, width=25)
    entry3441.place(relx=0.70, rely=0.15, anchor='ne')
    charge = tkinter.IntVar()
    entry3442 = tkinter.Entry(win344, width=25, textvariable=charge)
    entry3442.place(relx=0.70, rely=0.25, anchor='ne')
    button3441 = tkinter.Button(win344, text="Recharge", width=15, height=1)
    button3441['command'] = recharge_Operation
    button3441.place(relx=0.60, rely=0.55, anchor='ne')
    labe3441 = tkinter.Label(win344, text='Phone Number', width=20)
    labe3441.place(relx=0.30, rely=0.15, anchor='ne')
    labe3442 = tkinter.Label(win344, text='Amount of charge', width=20)
    labe3442.place(relx=0.30, rely=0.25, anchor='ne')


def withdraw_Operation():
    id1 = accountnum.get()
    withdrawal_amount = withdraw.get()

    if 10 <= withdrawal_amount <= 50000000:
        if bank[id1][2] >= withdrawal_amount:
            # Update the account balance
            bank[id1][2] -= withdrawal_amount
            showinfo(title="ATM System", message=f"Thank You, Withdrawal of {withdrawal_amount} done!")
            win31.destroy()
        else:
            showinfo(title="ATM System", message="No Sufficient Balance!")
            win31.destroy()
    else:
        showinfo(title="ATM System", message="Invalid withdrawal amount. Please enter an amount between 100 and 5000.")



# WINDOW for checking the customer's password
def check_entered_pass():
    global flag, count
    id0 = accountnum.get()
    password0 = int(password.get())
    if count < 3:
        if password0 == bank[id0][1]:
            new_window2()
        else:
            count += 1
            showinfo(title="ATM System", message=("Enter your password again!"))

    else:
        showinfo(title="ATM System", message=("Your account is locked!"))
        flag = 1
        win1.destroy()


def exit():
    win.destroy()


def exit_to_win():
    win1.destroy()
    win2.destroy()
    win32.destroy()


# WINDOW for checking passwords similarity while changing
def check_Pass():
    pass1 = entry331.get()
    pass2 = entry332.get()
    if len(pass1) == 4 and len(pass2) == 4 and pass1 == pass2:
        showinfo(title="ATM System", message=("Password Saved!"))
    else:
        showinfo(title="ATM System", message=("Enter Password Again"))


def recharge_Operation():
    id2 = accountnum.get()
    if bank[id2][2] >= charge.get():
        bank[id2][2]-= charge.get()
        showinfo(title="ATM System", message=("Operation Done , Balance Updated!"))
    else:
        showinfo(title="ATM System", message=("No Sufficient Balance!"))
        win1.destroy()
        win2.destroy()
        win34.destroy()
        win344.destroy()


win.mainloop()




