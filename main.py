from tkinter import *
from tkinter import ttk
import csv
import tkinter as tk
import webbrowser
from tkinter import messagebox as mb
global register_photo
global login_photo
global signin_photo
global a,b,c,d
global username

general_txt=str("""Identity Card is compulsory for getting access to the library
Silence to be maintained
No discussion permitted inside the library
Registration should be done to become a library member prior to using the library resources
No personal belongings allowed inside the library
Textbooks, printed materials and issued books are not allowed to be taken inside the library
Using Mobile phones and audio instruments with or without speaker or headphone is strictly prohibited in the library premises.
Enter your name and Sign in the register kept at the entrance counter before entering library
Show the books and other materials which are being taken out of the library to the staff at the entrance counter.
The librarian may recall any book from any member at any time and the member shall return the same immediately.
Library borrower cards are not transferable. The borrower is responsible for the books borrowed on his/her card.
Refreshment of any kind shall not be taken any where in the library premises""")
admission_txt=str("""Students are allowed to library only on production of their authorized/valid Identity Cards""")
circulation_txt=str("""Books will be issued on presentation of the library card along with the ID card.
 Students are instructed to check the books while borrowing and they will be responsible for any type of
  damage or mutilation noticed at the time of return.""")
overdue_txt=str("""Materials borrowed should be returned on or before the due date stamped, if returned late 
overdue fine will be charged for the delayed period.""")

class ScrolledFrame(tk.Frame):

    def __init__(self, parent, vertical=True, horizontal=False,bg_color='white'):
        super().__init__(parent)

        self.columnconfigure(0, weight=1) # changed
        self.rowconfigure(0, weight=1) # changed

        self._canvas = tk.Canvas(self,bg=bg_color)
        self._canvas.grid(row=0, column=0, sticky="news") # changed

        self._vertical_bar = tk.Scrollbar(self, orient="vertical", command=self._canvas.yview)
        if vertical:
            self._vertical_bar.grid(row=0, column=1, sticky="ns")
        self._canvas.configure(yscrollcommand=self._vertical_bar.set)

        self._horizontal_bar = tk.Scrollbar(self, orient="horizontal", command=self._canvas.xview)
        if horizontal:
            self._horizontal_bar.grid(row=1, column=0, sticky="we")
        self._canvas.configure(xscrollcommand=self._horizontal_bar.set)

        self.frame = tk.Frame(self._canvas,bg=bg_color)
        self._canvas.create_window((0, 0), window=self.frame, anchor="center")

        self.frame.bind("<Configure>", self.resize)

    def resize(self, event=None):
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))

class add_module():
    def __init__(self):
        self.update = Tk()
        self.update.config(bg="#FFF9C4")
        self.update.title("My Library App")
        self.update.geometry("{0}x{1}+0+0".format(self.update.winfo_screenwidth()-5, self.update.winfo_screenheight()-5))
        f2 = Frame(self.update, bg="#455A64")
        f2.grid(padx=50, pady=50)

        l1 = Label(f2, text="ADD BOOKS", bg="#455A64", fg='pink', font=("Courier", 50, "bold"))
        l1.grid(row=0, column=0, columnspan=4)

        self.n1 = Label(f2, text="Enter book name :", bg="#455A64", fg='#EEE9E9', font=("Candara", 30))
        self.n1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.n2 = Label(f2, text="Select branch :", bg="#455A64", fg='#EEE9E9', font=("Candara", 30))
        self.n2.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.n3 = Label(f2, text="Enter topic :", bg="#455A64", fg='#EEE9E9', font=("Candara", 30))
        self.n3.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.e2 = Entry(f2)
        self.e2.grid(row=3, column=3, padx=10, pady=10)

        self.e1 = Entry(f2)
        self.e1.grid(row=1, column=3, padx=10, pady=10)

        self.explore_branch_box = ttk.Combobox(f2)
        self.explore_branch_box.set('None')
        self.explore_branch_box['values'] = ('None', 'Computer', 'Electronics', 'Mechanical')
        self.explore_branch_box.grid(row=2, column=3, sticky=NSEW, padx=10, pady=20)

        global register_photo
        register_photo = PhotoImage(file="submit.png")
        c1 = Button(f2, text="submit", command=self.add_book, image=register_photo, height=50, width=180)
        c1.grid(row=4, column=2, columnspan=3, sticky=NSEW, padx=10, pady=10)

        self.update.grid_columnconfigure(0, weight=1)
        self.update.grid_rowconfigure(0, weight=1)
        back_button = Button(self.update, text = 'Menu',bg='#1c84c6',fg='black',command=self.back_search,width=self.update.winfo_reqwidth(),font=("Candara", 20),anchor='w')
        back_button.grid(row=0, column=0 ,sticky='NW')

    def back_search(self):
        self.update.destroy()
        admin_menu()

    def add_book(self):
        book_add = self.e1.get().upper()
        branch_add = self.explore_branch_box.get()
        topic_add = self.e2.get().upper()
        with open("books.txt", "a") as file:
            file.write('\n' + book_add + ',' + branch_add + ',' + topic_add)
            self.e1.delete(0, 'end')
            self.e2.delete(0, 'end')

class admin_menu():
    def goto_add(self):
        self.user_win.destroy()
        add_module()

    def goto_out(self):
        self.user_win.destroy()
        start_module()

    def __init__(self):
        self.user_win=Tk()
        self.user_win.title("My Library App")
        self.user_win.config(bg="#FFF9C4")
        self.user_win.geometry("{0}x{1}+0+0".format(self.user_win.winfo_screenwidth()-5, self.user_win.winfo_screenheight()-5))

        head_frame_user = Frame(self.user_win ,bg='#455A64')
        head_frame_user.grid(padx=50, pady=50)

        user_frame=Frame(head_frame_user,bg="#49A")
        user_frame.grid(row=1,column=0,padx=50, pady=50)

        heading_label=Label(head_frame_user,text='ADMIN MENU',bg='#455A64',fg='pink', font=("Courier", 50))
        heading_label.grid(row=0,column=0,columnspan=6, padx=10, pady=20)

        user_search=Button(user_frame,text='Add Books',command=self.goto_add,height = 1, width = 15,font=("Candara", 30))
        user_search.grid(row=0, sticky=NSEW, padx=10, pady=10)

        user_explore=Button(user_frame,text='Log Out',command=self.goto_out,height = 1, width =15,font=("Candara", 30))
        user_explore.grid(row=1, sticky=NSEW, padx=10, pady=10)

        self.user_win.grid_columnconfigure(0, weight=1)
        self.user_win.grid_rowconfigure(0, weight=1)
        self.user_win.mainloop()

class admin():
    def __init__(self):
        self.admin_log = Tk()
        self.admin_log.config(bg="#FFF9C4")
        self.admin_log.title("My Library App")
        self.admin_log.geometry("{0}x{1}+0+0".format(self.admin_log.winfo_screenwidth()-5, self.admin_log.winfo_screenheight()-5))

        self.f1 = Frame(self.admin_log,bg="#455A64")
        self.f1.grid(padx=50, pady=50)

        h1 = Label(self.f1, text=" Admin Login ",bg="#455A64", fg='pink', font=("Courier", 50,"bold"))
        h1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        user = Label(self.f1, text="User name : ",bg="#455A64", fg='#EEE9E9',font=("Candara", 30))
        user.grid(row=2, column=0, sticky=NSEW, padx=10, pady=10)

        passw = Label(self.f1, text="Password : ",bg="#455A64", fg='#EEE9E9',font=("Candara", 30))
        passw.grid(row=3, column=0, sticky=NSEW, padx=10, pady=10)

        self.u1 = Entry(self.f1,font=("Candara", 30))
        self.u1.grid(row=2, column=1, sticky=NSEW, padx=10, pady=10)

        self.p1 = Entry(self.f1,font=("Candara", 30))
        self.p1.grid(row=3, column=1, sticky=NSEW, padx=10, pady=10)
        #login_photo = PhotoImage(file="login.png")


        global login_photo
        login_photo = PhotoImage(file="login.png")
        log = Button(self.f1, text="Login", command=self.check, image=login_photo, height=90, width=215)
        log.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

        #back_button = Button(self.admin_log, text = 'Back',bg='#7CB9E8',fg='black',command=self.back_admin,width=self.admin_log.winfo_reqwidth(),font=("Candara", 30),anchor='w')
        #back_button.grid(row=0, column=0 ,sticky='NW')
#screen size winfo_screenwidth()

        self.admin_log.grid_columnconfigure(0, weight=1)
        self.admin_log.grid_rowconfigure(0, weight=1)

    def goto_adminmenu(self):
        self.admin_log.destroy()
        admin_menu()

    def check(self):
        if self.u1.get() == "admin" and self.p1.get() == "vit":
            self.admin_log.destroy()
            admin_menu()
        else:
            i3 = Label(self.f1, text="Invalid username or password", fg='red', font=("Courier", 15))
            i3.grid(row=5, columnspan=4,padx=10,pady=10)

class user():
    def __init__(self):
        self.username=str()

    class register():
        def __init__(self):
            self.reg = Tk()  # Constructing the register window
            self.reg.title("My Library App")
            self.reg.config(bg="#FFF9C4")
            self.reg.geometry("{0}x{1}+0+0".format(self.reg.winfo_screenwidth()-5, self.reg.winfo_screenheight()-5))
            regiframe = Frame(self.reg, bg="#455A64")
            regiframe.grid(padx=50, pady=50)

            h1 = Label(regiframe, text=" Register ", bg="#455A64", fg='pink', font=("Courier", 50, "bold"))
            h1.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

            self.n1 = Label(regiframe, text="Enter your username :", bg="#455A64", fg='#EEE9E9', font=("Candara", 30))
            self.n1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

            self.n2 = Label(regiframe, text="Enter your password :", bg="#455A64", fg='#EEE9E9', font=("Candara", 30))
            self.n2.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

            self.e1 = Entry(regiframe)
            self.e1.grid(row=1, column=3, padx=10, pady=10)

            self.e2 = Entry(regiframe)
            self.e2.grid(row=2, column=3, padx=10, pady=10)

            global register_photo
            register_photo = PhotoImage(file="submit.png")
            self.r1 = Button(regiframe, text="Register user", command=self.store, image=register_photo, height=50,
                             width=180)
            self.r1.grid(padx=10, pady=10, columnspan=4)

            self.reg.grid_columnconfigure(0, weight=1)
            self.reg.grid_rowconfigure(0, weight=1)

        def store(self):
            user1 = self.e1.get()
            pass1 = self.e2.get()
            fh = open("newuser.txt", "a")
            fh.write(user1 + "," + pass1 + "\n")
            fh.close()
            self.reg.destroy()
            user.login()

    class search_module():
        def __init__(self):
            self.start = Tk()  # Constructing after login window
            self.start.title("My Library App")
            self.start.config(bg="#FFF9C4")
            self.start.geometry("{0}x{1}+0+0".format(self.start.winfo_screenwidth()-5, self.start.winfo_screenheight()-5))
            self.start.grid_columnconfigure(0, weight=1)
            self.start.grid_rowconfigure(0, weight=1)

            # head_frame_user = Frame(self.start, bg='#455A64')
            # head_frame_user.grid(padx=50, pady=50)

            self.search_frame = ScrolledFrame(self.start, horizontal=True, bg_color="#455A64")
            self.search_frame.pack(fill='both', expand=True, side=TOP,anchor=N)  # grid(row=1,column=0,padx=50, pady=50)

            # heading_label=Label(self.start,text='Search Book',bg='#455A64',fg='pink', font=("Courier", 50))
            # heading_label.grid(row=0,column=0,columnspan=6, padx=10, pady=20)

            name_text=Label(self.search_frame.frame,text='Enter book name :',bg="#455A64",fg="white", font=("Candara", 30))
            name_text.grid(row=2, column=6, columnspan=4, padx=10, pady=10, sticky=N)

            self.name_box = Entry(self.search_frame.frame, font=("Candara", 30))
            self.name_box.grid(row=2, column=10, columnspan=3,padx=10, pady=10, sticky=N)

            find_button = Button(self.search_frame.frame, text='Search', fg='#f52b42', bg='#fccf4f',command=self.search, height=1, width=15, font=("Candara", 30))
            find_button.grid(row=3, column=8, columnspan=4, padx=10, pady=10, sticky=N)

            clear_button = Button(self.search_frame.frame, text='Clear', bg='#0052cc', fg='#ffffff', command=self.clear_books, height=1, width=15, font=("Candara", 30))
            clear_button.grid(row=4, column=8, columnspan=4, padx=10, pady=10, sticky=N)

            back_button = Button(self.search_frame.frame, text='Menu', bg='#1c84c6', fg='black',command=self.back_search, width=126, font=("Candara", 20), anchor="w")
            back_button.grid(row=0, column=0, columnspan=20, sticky=NW)

        def search(self):
            s1 = self.name_box.get()#.upper()
            flag = 0
            var = 1
            with open("books.txt", "r") as file:
                fh = csv.reader(file, delimiter=",", lineterminator="\n")
                for lines in fh:
                    if s1 in lines[0]:
                        res = Label(self.search_frame.frame, text='   Given book(s) is/are available', bg="#455A64",fg="pink",font=("Candara",30), anchor="w")
                        res.grid(row=6, column=0, sticky=N, padx=10, pady=10, columnspan=4)
                        # txt+=str(var) + '. ' + row[0]+'\n'
                        bk = Label(self.search_frame.frame, text='  '+str(var) + '. ' + lines[0], bg="#455A64", fg="white",font=("Candara", 15), anchor="w")
                        bk.grid(row=var + 6, column=0, sticky=W, padx=10, pady=10, columnspan=4)
                        if lines[3] == "TRUE":
                            eb = Button(self.search_frame.frame, text="Read ",
                                        command=lambda ebook_website=lines[4]: self.download_ebook(ebook_website),
                                        bg="white", font=("Candara", 15), anchor="w")
                            eb.grid(row=var + 6, column=13, padx=10, pady=10, sticky=W)
                        var += 1
                        flag = 1
            if flag == 0:
                res2 = Label(self.search_frame.frame, text='Book is not available',bg="#455A64",fg="pink", font=("Candara",30))
                res2.grid(row=6, column=8, columnspan=4,sticky=N, padx=10, pady=10)

        def clear_books(self):
            self.start.destroy()
            user.search_module()

        def back_search(self):
            self.start.destroy()
            user.user_menu()

        def download_ebook(self, ebook_website):
            webbrowser.open(ebook_website)

    class explore_module():
        def __init__(self):
            self.explore_win = Tk()
            self.explore_win.title('My Library App')
            self.explore_win.config(bg="#455A64")
            self.explore_win.geometry("{0}x{1}+0+0".format(self.explore_win.winfo_screenwidth()-5, self.explore_win.winfo_screenheight()-5))
            self.explore_win.grid_columnconfigure(0, weight=1)
            self.explore_win.grid_rowconfigure(0, weight=1)

            # head_frame_user = Frame(self.explore_win, bg='#455A64')
            # head_frame_user.grid(padx=50, pady=50)

            self.explore_frame = ScrolledFrame(self.explore_win, bg_color="#455A64")
            self.explore_frame.pack(fill='both', expand=True, side=TOP,
                                    anchor=N)  # grid(row=1,column=0,padx=50, pady=50,columnspan=8)

            # heading_label=Label(head_frame_user,text='Explore Library',bg='#455A64',fg='pink', font=("Courier", 50))
            # heading_label.grid(row=0,column=0,columnspan=6, padx=10, pady=20)

            explore_filt = Label(self.explore_frame.frame, text=' View available books', bg="#455A64", fg='#EEE9E9',
                                 font=("Candara", 30))
            explore_filt.grid(row=1, column=6, columnspan=8, sticky=NSEW, padx=10, pady=10)

            explore_branch = Label(self.explore_frame.frame, text='Branch  :', bg="#455A64", fg='#EEE9E9',
                                   font=("Candara", 20))
            explore_branch.grid(row=2, column=6, columnspan=4, sticky=NSEW, padx=10, pady=10)

            self.explore_branch_box = ttk.Combobox(self.explore_frame.frame)
            self.explore_branch_box.set('None')
            self.explore_branch_box['values'] = ('None', 'Computer Engineering', 'Aerospace Engineering', 'Mechanical Engineering')
            self.explore_branch_box.grid(row=2, column=10, columnspan=3, sticky=NSEW, padx=10, pady=10)

            def change_combobox(*args):
                branch = self.explore_branch_box.get()
                if branch == 'Computer Engineering':
                    b = ('Machine Learning', 'MySQL', 'Python')
                elif branch == 'Aerospace Engineering':
                    b = ('Vibration', 'Aerodynamics', 'Engine Design')
                elif branch == 'Mechanical Engineering':
                    b = ('Combustion', 'Thermodynamics', 'Boilers')
                self.explore_topic_box.config(values=b)

            self.explore_branch_box.bind("<<ComboboxSelected>>", change_combobox)

            explore_topic = Label(self.explore_frame.frame, text='Topic :', bg="#455A64", fg='#EEE9E9',
                                  font=("Candara", 20))
            explore_topic.grid(row=3, column=6, columnspan=4, sticky=NSEW, padx=10, pady=10)

            self.explore_topic_box = ttk.Combobox(self.explore_frame.frame)
            self.explore_topic_box.set('None')
            self.explore_topic_box['values'] = ('None')
            self.explore_topic_box.grid(row=3, column=10, columnspan=3, sticky=NSEW, padx=10, pady=10)

            explore_show = Button(self.explore_frame.frame, text='Show', bg="#0052cc", fg='#EEE9E9',
                                  command=self.show_books, height=1, width=18, font=("Candara", 20))
            explore_show.grid(row=5, column=8, columnspan=4, sticky=NSEW, padx=10, pady=10)

            back_button = Button(self.explore_frame.frame, text='Menu', bg='#1c84c6', fg='black',
                                 command=self.back_explore, width=126, font=("Candara", 20), anchor="w")
            back_button.grid(row=0, column=0, sticky='NW', columnspan=20)

        def show_books(self):
            branch = self.explore_branch_box.get()
            topic = self.explore_topic_box.get()
            var = 1
            with open("books.txt", "r") as file:
                fh = csv.reader(file, delimiter=",", lineterminator="\n")
                for row in fh:
                    if branch in row[1]:
                        if topic in row[2]:
                            res = Label(self.explore_frame.frame, text='List of books available', bg="#455A64",fg="pink",
                                        font=("Courier", 30))
                            res.grid(row=7, column=0, sticky=N, padx=10, pady=10, columnspan=4)
                            bk = Label(self.explore_frame.frame, text=str(var) + '. ' + row[0], bg="#455A64", fg="white",
                                       font=("Candara", 15), anchor="w")
                            bk.grid(row=var + 7, column=0, sticky=W, padx=10, pady=10, columnspan=4)
                            if row[3] == "TRUE":
                                eb = Button(self.explore_frame.frame, text="Read ",
                                            command=lambda ebook_website=row[4]: self.download_ebook(ebook_website),
                                            bg="white", font=("Candara", 15), anchor="w")
                                eb.grid(row=var + 7, column=13, padx=10, pady=10, sticky=W)
                            var += 1

        def download_ebook(self, ebook_website):
            webbrowser.open(ebook_website)

        def back_explore(self):
            self.explore_win.destroy()
            user.user_menu()

    class contact_module():
        def __init__(self):
            self.contact_win = Tk()
            self.contact_win.title('My Library App')
            self.contact_win.config(bg="#FFF9C4")
            self.contact_win.geometry("{0}x{1}+0+0".format(self.contact_win.winfo_screenwidth()-5, self.contact_win.winfo_screenheight()-5))
            self.contact_win.grid_columnconfigure(0, weight=1)
            self.contact_win.grid_rowconfigure(0, weight=1)

            head_frame_user = Frame(self.contact_win, bg='#455A64')
            head_frame_user.grid(padx=50, pady=50)

            contact_frame = Frame(head_frame_user, bg="#455A64")
            contact_frame.grid(row=1, column=0, padx=50, pady=50, columnspan=8)

            heading_label = Label(head_frame_user, text='Contact Us', bg='#455A64', fg='pink', font=("Courier", 50))
            heading_label.grid(row=0, column=1, columnspan=6, padx=10, pady=20)

            email_label = Label(contact_frame, text="Email :", bg='#455A64', fg='#EEE9E9', font=("Candara", 30))
            email_label.grid(row=2, column=0, columnspan=2, sticky=NSEW, padx=10, pady=10)

            email_label2 = Label(contact_frame, text="xyz@gmail.com", bg='#455A64', fg='#EEE9E9', font=("font14", 30))
            email_label2.grid(row=2, column=2, columnspan=2, sticky=NSEW, padx=10, pady=10)

            no_label = Label(contact_frame, text="Phone Number :", bg='#455A64', fg='#EEE9E9', font=("Candara", 30))
            no_label.grid(row=4, column=0, columnspan=2, sticky=NSEW, padx=10, pady=10)

            no_label2 = Label(contact_frame, text="9876543210", bg='#455A64', fg='#EEE9E9', font=("font14", 30))
            no_label2.grid(row=4, column=2, columnspan=2, sticky=NSEW, padx=10, pady=10)

            back_button = Button(self.contact_win, text='Menu', bg='#1c84c6', fg='black', command=self.back_contact,
                                 width=self.contact_win.winfo_reqwidth(), font=("Candara", 20), anchor='w')
            back_button.grid(row=0, column=0, sticky='NW')

            def callback(event):
                webbrowser.open("http://www.vit.edu/index.php/institute/bajrangdas-lohiya-central-library")

            web_label = Label(contact_frame, text="Visit the website", cursor="hand2", bg='#455A64', fg='lightblue',
                              font=("Candara", 30, 'underline'))
            web_label.grid(row=5, column=0, columnspan=4, sticky=NSEW, padx=10, pady=10)
            web_label.bind("<Button-1>", callback)

        def back_contact(self):
            self.contact_win.destroy()
            user.user_menu()

    class rules_module():
        def __init__(self):
            self.rules_win = Tk()
            self.rules_win.title('My Library App')
            self.rules_win.config(bg="#FFF9C4")
            self.rules_win.geometry("{0}x{1}+0+0".format(self.rules_win.winfo_screenwidth()-5, self.rules_win.winfo_screenheight()-5))
            self.rules_win.grid_columnconfigure(0, weight=1)
            self.rules_win.grid_rowconfigure(0, weight=1)

            # head_frame_user = Frame(self.rules_win, bg='#455A64')
            # head_frame_user.grid(padx=50, pady=50)

            sf = ScrolledFrame(self.rules_win, True, bg_color='#455A64')
            sf.pack(fill='both', expand=True, side='top')

            heading_label = Label(sf.frame, text='Library Rules And Regulations', bg='#455A64', fg='pink',
                                  font=("Courier", 50))
            heading_label.grid(row=1, column=0, columnspan=23, padx=10, pady=20, sticky=NSEW)

            general_label = Label(sf.frame, text="General Rules", bg='#455A64', fg='yellow', font=("Candara", 30),
                                  justify=LEFT, anchor="w")
            general_label.grid(row=3, column=0, columnspan=2, sticky=NSEW, padx=10, pady=10)

            gen_rules = Label(sf.frame, text=general_txt, bg='#455A64', fg='#EEE9E9', font=("Candara", 18),
                              justify=LEFT, anchor="w")
            gen_rules.grid(row=4, column=0, columnspan=2, sticky=NSEW, padx=10, pady=10)

            adm_label = Label(sf.frame, text="Admission to Library ", bg='#455A64', fg='yellow', font=("Candara", 30),
                              justify=LEFT, anchor="w")
            adm_label.grid(row=5, column=0, columnspan=2, sticky=NSEW, padx=10, pady=10)

            adm_rules = Label(sf.frame, text=admission_txt, bg='#455A64', fg='#EEE9E9', font=("Candara", 18),
                              justify=LEFT, anchor="w")
            adm_rules.grid(row=6, column=0, columnspan=2, sticky=NSEW, padx=10, pady=10)

            circulation_label = Label(sf.frame, text="Circulation", bg='#455A64', fg='yellow', font=("Candara", 30),
                                      justify=LEFT, anchor="w")
            circulation_label.grid(row=7, column=0, columnspan=2, sticky=NSEW, padx=10, pady=10)

            circulation_rules = Label(sf.frame, text=circulation_txt, bg='#455A64', fg='#EEE9E9', font=("Candara", 18),
                                      justify=LEFT, anchor="w")
            circulation_rules.grid(row=8, column=0, columnspan=2, sticky=NSEW, padx=10, pady=10)

            overdue_label = Label(sf.frame, text="Overdue Charges", bg='#455A64', fg='yellow', font=("Candara", 30),
                                  justify=LEFT, anchor="w")
            overdue_label.grid(row=9, column=0, columnspan=2, sticky=NSEW, padx=10, pady=10)

            overdue_rules = Label(sf.frame, text=overdue_txt, bg='#455A64', fg='#EEE9E9', font=("Candara", 18),
                                  justify=LEFT, anchor="w")
            overdue_rules.grid(row=10, column=0, columnspan=2, sticky=NSEW, padx=10, pady=10)

            back_button = Button(sf.frame, text='Menu', bg='#1c84c6', fg='black', command=self.back_rules, width=126,
                                 font=("Candara", 20), anchor="w")
            back_button.grid(row=0, column=0, sticky=NW)

        def back_rules(self):
            self.rules_win.destroy()
            user.user_menu()

    class edit_profile_module():
        def __init__(self):
            self.edit = Tk()
            self.edit.config(bg="#455A64")
            self.edit.title("My Library App")
            self.edit.geometry("{0}x{1}+0+0".format(self.edit.winfo_screenwidth()-5, self.edit.winfo_screenheight()-5))
            f2 = Frame(self.edit, bg="#455A64")
            f2.grid(padx=50, pady=50)

            self.n1 = Label(f2, text="Edit username", bg="#455A64", fg='white', font=("Candara", 30))
            self.n1.grid(row=1, column=0, columnspan=4, padx=10, pady=70)

            self.new = Entry(f2,font=("Candara", 30))
            self.new.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

            change_name=Button(f2, text="Change username", bg="#0052cc", fg='#EEE9E9',command=self.change_username, font=("Candara", 30))
            change_name.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

            self.edit.grid_columnconfigure(0, weight=1)
            self.edit.grid_rowconfigure(0, weight=1)

            back_button = Button(self.edit, text='Back', bg='#1c84c6', fg='black', command=self.back_profile,width=self.edit.winfo_reqwidth(), font=("Candara", 20), anchor='w')
            back_button.grid(row=0, column=0, sticky='NW')

        def change_username(self):
            txt=str()
            with open("newuser.txt", "r") as file:
                    for lines in file.readlines():
                        txt+=lines
            new_txt=txt.replace(user.username,self.new.get(),1)
            user.username=self.new.get()
            file=open("newuser.txt", "w")
            file.write(new_txt)
            file.close()
            self.back_profile()

        def back_profile(self):
            self.edit.destroy()
            user.profile_module()

    class edit_password_module():
        def __init__(self):
            self.edit = Tk()
            self.edit.config(bg="#455A64")
            self.edit.title("My Library App")
            self.edit.geometry("{0}x{1}+0+0".format(self.edit.winfo_screenwidth()-5, self.edit.winfo_screenheight()-5))
            f2 = Frame(self.edit, bg="#455A64")
            f2.grid(padx=50, pady=50)

            self.n1 = Label(f2, text="Edit password", bg="#455A64", fg='white', font=("Candara", 40))
            self.n1.grid(row=1, column=0, columnspan=4, padx=10, pady=70)

            old_pass=Label(f2, text="Current password", bg="#455A64", fg='white', font=("Candara", 25))
            old_pass.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

            new_pass=Label(f2, text="New password", bg="#455A64", fg='white', font=("Candara", 25))
            new_pass.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

            self.old= Entry(f2,font=("Candara", 25))
            self.old.grid(row=3, column=3, columnspan=2, padx=10, pady=10)

            self.new = Entry(f2,font=("Candara", 25))
            self.new.grid(row=4, column=3, columnspan=2, padx=10, pady=10)

            change_name=Button(f2, text="Change password", bg="#0052cc", fg='#EEE9E9',command=self.change_password, font=("Candara", 25))
            change_name.grid(row=5, column=2, columnspan=6, padx=10, pady=10)

            self.edit.grid_columnconfigure(0, weight=1)
            self.edit.grid_rowconfigure(0, weight=1)

            back_button = Button(self.edit, text='Back', bg='#1c84c6', fg='black', command=self.back_password,width=self.edit.winfo_reqwidth(), font=("Candara", 20), anchor='w')
            back_button.grid(row=0, column=0, sticky='NW')

        def change_password(self):
            txt=str()
            with open("newuser.txt", "r") as file:
                    for lines in file.readlines():
                        txt+=lines
            if user.username+","+self.old.get() in txt:
                new_txt=txt.replace(self.old.get(),self.new.get(),1)
                file=open("newuser.txt", "w")
                file.write(new_txt)
                file.close()
                self.back_password()
            else:
                mb.showwarning("Error","Entered password is incorrect")

        def back_password(self):
            self.edit.destroy()
            user.profile_module()

    class profile_module():
        def __init__(self):
            self.update = Tk()
            self.update.config(bg="#455A64")
            self.update.title("My Library App")
            self.update.geometry("{0}x{1}+0+0".format(self.update.winfo_screenwidth()-5, self.update.winfo_screenheight()-5))

            f2 = Frame(self.update, bg="#455A64")
            f2.grid(padx=50, pady=50)

            l1 = Label(f2, text="Profile", bg="#455A64", fg='pink', font=("Courier", 50, "bold"))
            l1.grid(row=0, column=0, columnspan=4,padx=40,pady=40)

            curr_username=user.username
            l1 = Label(f2, text="Username : " + curr_username , bg="#455A64", fg='#EEE9E9', font=("Candara", 30, "bold"))
            l1.grid(row=5, column=0, columnspan=4)

            self.n1 = Button(f2, text="Change username", bg="#0052cc", fg='#EEE9E9',command=self.goto_edit_profile, font=("Candara", 30))
            self.n1.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

            change_pass=Button(f2, text="Reset password", bg="#0052cc", fg='#EEE9E9',command=self.goto_edit_password, font=("Candara", 30))
            change_pass.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

            self.n2 = Button(f2, text="Log Out", bg="brown", fg='#EEE9E9',command=self.goto_logout,font=("Candara", 30))
            self.n2.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

            self.update.grid_columnconfigure(0, weight=1)
            self.update.grid_rowconfigure(0, weight=1)

            back_button = Button(self.update, text='Menu', bg='#1c84c6', fg='black', command=self.back_profile,width=self.update.winfo_reqwidth(), font=("Candara", 20), anchor='w')
            back_button.grid(row=0, column=0, sticky='NW')

        def back_profile(self):
            self.update.destroy()
            user.user_menu()

        def goto_edit_profile(self):
            self.update.destroy()
            user.edit_profile_module()

        def goto_edit_password(self):
            self.update.destroy()
            user.edit_password_module()

        def goto_logout(self):
            self.update.destroy()
            start_module()

    class user_menu():
        def goto_search(self):
            self.user_win.destroy()
            user.search_module()

        def goto_explore(self):
            self.user_win.destroy()
            user.explore_module()

        def goto_contact(self):
            self.user_win.destroy()
            user.contact_module()

        def goto_rules(self):
            self.user_win.destroy()
            user.rules_module()

        def goto_profile(self):
            self.user_win.destroy()
            user.profile_module()

        def __init__(self):
            self.user_win = Tk()
            self.user_win.title("My Library App")
            self.user_win.config(bg="#FFF9C4")
            self.user_win.geometry("{0}x{1}+0+0".format(self.user_win.winfo_screenwidth()-5, self.user_win.winfo_screenheight()-5))

            head_frame_user = Frame(self.user_win, bg='#455A64')
            head_frame_user.grid(padx=50, pady=50)

            user_frame = Frame(head_frame_user, bg="#49A")
            user_frame.grid(row=1, column=0, padx=50, pady=50)

            heading_label = Label(head_frame_user, text='USER MENU', bg='#455A64', fg='pink', font=("Courier", 50))
            heading_label.grid(row=0, column=0, columnspan=6, padx=10, pady=20)

            user_search = Button(user_frame, text='Search Books', command=self.goto_search, height=1, width=15,
                                 font=("Candara", 30))
            user_search.grid(row=0, sticky=NSEW, padx=10, pady=10)

            user_explore = Button(user_frame, text='Explore library', command=self.goto_explore, height=1, width=15,
                                  font=("Candara", 30))
            user_explore.grid(row=1, sticky=NSEW, padx=10, pady=10)

            user_rules = Button(user_frame, text='Library Rules ', command=self.goto_rules, height=1, width=15,
                                font=("Candara", 30))
            user_rules.grid(row=2, sticky=NSEW, padx=10, pady=10)

            user_contact = Button(user_frame, text='Contact Us', command=self.goto_contact, height=1, width=15,
                                  font=("Candara", 30))
            user_contact.grid(row=3, sticky=NSEW, padx=10, pady=10)

            log_out = Button(user_frame, text='Profile', command=self.goto_profile, height=1, width=15,
                             font=("Candara", 30))
            log_out.grid(row=4, sticky=NSEW, padx=10, pady=10)

            self.user_win.grid_columnconfigure(0, weight=1)
            self.user_win.grid_rowconfigure(0, weight=1)
            self.user_win.mainloop()

    class login():
        def __init__(self):
            self.root = Tk()  # Constructing the login window
            self.root.title("My Library App")
            self.root.config(bg="#FFF9C4")
            self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth()-5, self.root.winfo_screenheight()-5))

            self.lf = Frame(self.root, bg='#455A64')
            self.lf.grid(padx=50, pady=50)

            h1 = Label(self.lf, text=" USER LOGIN ", bg='#455A64', fg='pink', font=("Courier", 50))
            h1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

            user = Label(self.lf, text="User name : ", bg='#455A64', fg='#EEE9E9', font=("Candara", 30))
            user.grid(row=2, column=0, sticky=NSEW, padx=10, pady=10)

            passw = Label(self.lf, text="Password : ", bg='#455A64', fg='#EEE9E9', font=("Candara", 30))
            passw.grid(row=3, column=0, sticky=NSEW, padx=10, pady=10)

            self.u1 = Entry(self.lf)
            self.u1.grid(row=2, column=1, sticky=NSEW, padx=10, pady=10)

            self.p1 = Entry(self.lf)
            self.p1.grid(row=3, column=1, sticky=NSEW, padx=10, pady=10)

            login_photo = PhotoImage(file="login.png")
            log = Button(self.lf, command=self.check, image=login_photo, height=90, width=215)
            log.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

            self.root.grid_columnconfigure(0, weight=1)
            self.root.grid_rowconfigure(0, weight=1)
            self.root.mainloop()

        def login_check(self):
            user.username=self.u1.get()
            self.root.destroy()
            user.user_menu()

        def check(self):
            x1 = self.u1.get()
            x2 = self.p1.get()

            with open("newuser.txt", "r") as file:
                fh = csv.reader(file, delimiter=",", lineterminator="\n")
                for row in fh:
                    if row[0] == x1:
                        if row[1] == x2:
                            file.close()
                            user.login.login_check(self)
                            break
                else:
                    mb.showwarning("Error", "Invalid username/password")
                    #i3 = Label(self.lf, text="Invalid username or password", fg='red', font=("Courier", 15))
                    #i3.grid(row=5, columnspan=2, padx=10, pady=10)

        def user_edit(self):
            return self.u1.get()

class start_module():
    def __init__(self):
        self.win = Tk()      #Constructing login and register window
        self.win.title("My Library App")
        self.win.config(bg="#FFF9C4")
        self.win.geometry("{0}x{1}+0+0".format(self.win.winfo_screenwidth()-5, self.win.winfo_screenheight()-5))

        head_fr=Frame(self.win,bg="#FFF9C4")
        head_fr.grid(padx=10,pady=10)

        fr=Frame(head_fr,bg='#455A64')
        fr.grid(row=1,column=0,columnspan=3,padx=10,pady=10)

        la=Label(head_fr,text='WELCOME TO MY LIBRARY APP',bg='#FFF9C4',fg='purple',font=("BankGothic Lt BT",60,"bold"))
        la.grid(row = 0,sticky = NSEW,column=0,columnspan = 3,padx=20,pady=40)

        s1=Label(fr,text="FOR STUDENT",font=("Courier",20,"bold"))
        s1.grid(row=1,column=1,padx=25,pady=25)

        signin_photo= PhotoImage(file = "signin.png")
        l1 = Button(fr,command=self.log1,image=signin_photo,height = 88, width = 185)
        l1.grid(row=2,column=1,padx=25,pady=25)

        s1=Label(fr,text="FOR EMPLOYEE",font=("Courier",20,"bold"))
        s1.grid(row=1,column=3)

        admin_photo = PhotoImage(file = "admin-login.jpg")
        adlog = Button(fr,text = 'Admin Login', cursor="hand2",command=self.admingo,image=admin_photo,height = 300, width = 280)
        adlog.grid(row=2,column=3,rowspan=3,padx=25,pady=25)

        register_photo = PhotoImage(file = "register2.png")
        r1 = Button(fr, text='Register', command=self.regiuser,image = register_photo,height = 88, width = 180)
        r1.grid(row=4,column=1,padx=25,pady=25)

        self.win.grid_columnconfigure(0,weight=1)
        self.win.grid_rowconfigure(0,weight = 1)
        self.win.mainloop()

    def log1(self):
        self.win.destroy()
        a = user.login()

    def regiuser(self):
        self.win.destroy()
        b = user.register()

    def admingo(self):
        self.win.destroy()
        c = admin()

start_module()
