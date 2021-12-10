from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk
from pathlib import Path
from urllib import request
import gitupdate
import webbrowser
import platform


class librarygui(Tk):

    def __init__(self):
        super().__init__()
        self.title("Online Library")
        self.c = 1
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.resizable(FALSE, FALSE)
        self.user = ""
        self.booklist = {}
        self.path = str(Path(__file__).absolute())
        if platform.platform()[:platform.platform().index("-")] == "Windows":
            self.req = self.path[:self.path.rindex("\\gui.py") + 1] + "\\requests.txt"
            b= Image.open(self.path[:self.path.rindex("\\gui.py") + 1] + "\\bg.jpg")
            self.bg = ImageTk.PhotoImage(b)
        elif platform.platform()[:platform.platform().index("-")] == "Linux":
            self.req = self.path[:self.path.rindex("/gui.py") + 1] + "/requests.txt"
            b = Image.open(self.path[:self.path.rindex("\\gui.py") + 1] + "\\bg.jpg")
            self.bg = ImageTk.PhotoImage(b)
        label1 = Label(image=self.bg)
        label1.image = self.bg
        label1.place(x=0, y=0)
        self.path = str(Path(__file__).absolute())
        if platform.platform()[:platform.platform().index("-")] == "Windows":
            self.path = self.path[:self.path.rindex("\\gui.py") + 1] + "\\books.txt"
        elif platform.platform()[:platform.platform().index("-")] == "Linux":
            self.path = self.path[:self.path.rindex("/gui.py") + 1] + "/books.txt"
        data = request.urlopen(
            request.Request("https://raw.githubusercontent.com/Aryan-Lohia/OnlineLibrary/main/root/books.txt"))
        with open(self.path, "w") as books:
            books.write("")
            for line in data:
                if len(line) == 0:
                    break
                line = str(line)[2:-3]
                books.write(line + "\n")
                book = line[0:line.rindex(" ")]
                link = line.split()[-1]
                self.booklist[book.upper()] = link
        self.list1 = list(self.booklist.keys()).copy()

        data = request.urlopen(
            request.Request("https://raw.githubusercontent.com/Aryan-Lohia/OnlineLibrary/main/root/requests.txt"))
        with open(self.req, "w") as books:
            books.write("")
            for line in data:
                if len(line) == 0:
                    break
                line = str(line)[2:-3]
                books.write(line + "\n")

    def home(self):
        self.homeframe = Frame(self)

        label1 = Label(self.homeframe, image=self.bg)
        label1.image = self.bg
        label1.place(x=0, y=0)
        frame1 = Frame(self.homeframe)
        label1 = Label(frame1, image=self.bg)
        label1.image = self.bg
        label1.place(x=0, y=0)
        txt = Label(frame1, text=" : ONLINE LIBRARY : ", bd=10, relief=SUNKEN, bg="cyan", font="arialbold 35 bold")
        txt.pack(padx=10, pady=85)
        txt = Label(frame1, text="ENTER YOUR NAME : ", bd=5, relief=SUNKEN, bg="cyan", fg="black",
                    font="arialbold 18 bold")
        txt.pack(padx=10, ipadx=10, side=LEFT, pady=20)
        self.name = Entry(frame1, bg="cyan", fg="black", bd=5, font="arialbold 18 bold")
        self.name.pack(side=LEFT, padx=20, pady=20)
        self.name.focus()
        frame1.pack(padx=350)
        frame2 = Frame(self.homeframe)
        sbmt = Button(frame2, text="Submit", bg="pink", command=self.submit, font="arialbold 13", bd=10, relief=RIDGE)
        sbmt.pack(ipadx=50)
        self.bind('<Return>', self.func)
        frame2.pack(pady=20, padx=100)
        self.homeframe.pack(pady=180)

    def func(self, event):
        self.submit()

    def submit(self):
        self.user = self.name.get().upper()
        if self.user == "" or self.user.isalpha() == FALSE:
            txt = Label(self.homeframe, text="Please Enter a valid Name", fg="red", font="lucida 18", bg="grey", bd=10,
                        relief=SUNKEN)
            txt.pack(pady=10, padx=10)
            if self.c >= 2:
                txt.destroy()
            self.c += 1
            return
        self.homeframe.destroy()
        self.library()

    def library(self):

        self.libraryframe = Frame(self)
        self.c = 1

        label1 = Label(self.libraryframe, image=self.bg)
        label1.image = self.bg
        label1.place(x=0, y=0)
        txt = Label(self.libraryframe, text=f" WELCOME \n {self.user} ", bd=10, relief=SUNKEN, bg="cyan",
                    font="arialbold 35 bold")
        txt.pack(padx=50, pady=50, expand=TRUE)
        frame1 = Frame(self.libraryframe)
        button = Button(frame1, text="BOOKLIST", command=self.display, bg="cyan", bd=10, relief=RIDGE,
                        font="arialbold 13")
        button.pack(ipadx=50, side=LEFT, ipady=10)
        frame1.pack(side=TOP)
        frame2 = Frame(self.libraryframe)
        button = Button(frame2, text="REQUEST A BOOK", command=self.request_book, bg="cyan", bd=10, relief=RIDGE,
                        font="arialbold 13")
        button.pack(ipadx=20, side=LEFT, ipady=10)
        button = Button(frame2, text="ADD A BOOK", command=self.add_book, bg="cyan", bd=10, relief=RIDGE,
                        font="arialbold 13")
        button.pack(ipadx=20, side=LEFT, ipady=10)
        frame2.pack(side=BOTTOM)
        self.libraryframe.pack(side=LEFT, padx=450, ipady=20, fill=X, expand=TRUE)

    def display(self):
        self.libraryframe.destroy()
        self.displayframe = Frame(self, bg="black")
        framex = Frame(self.displayframe, bg="black")
        self.back = Button(framex, text="Goback")
        self.back.pack(anchor="w", side=LEFT)
        self.back.bind('<Button-1>', self.goto)
        Label(framex, text="Double Click any book to Open", bg="black", fg="white").pack(side=LEFT, padx=15)
        self.entry = Entry(framex)
        self.entry.pack(anchor="e", side=RIGHT)
        self.entry.bind('<KeyRelease>', self.search_book)
        label1 = Label(framex, text="Search : ", bg="black", fg="white")
        label1.pack(anchor="e", padx=5, side=RIGHT)
        framex.pack(fill=X)
        sc = Scrollbar(self.displayframe)
        sc.pack(fill=Y, side=RIGHT)
        self.mylist = Listbox(self.displayframe, yscrollcommand=sc.set, width=70, height=100,
                              font="timesnewroman 15 bold italic", bg="grey")
        self.mylist.pack(side=LEFT, fill=Y, ipady=30)
        self.mylist.bind('<Double-1>', self.openbook)
        sc.config(command=self.mylist.yview)
        self.update_list()
        self.displayframe.pack(pady=30, side=LEFT, padx=450)

    def openbook(self, event):
        cs = self.mylist.curselection()[0]
        ch = askyesnocancel(title="Open Book", message=f"Would you like to open {self.list1[cs]}?")
        if ch == True:
            webbrowser.open(self.booklist[self.list1[cs]])

    def goto(self, event):
        self.displayframe.destroy()
        self.library()

    def update_list(self):
        self.mylist.delete(0, END)
        i = 1
        for book in self.list1:
            self.mylist.insert(END, f"{i}. {book}")
            i += 1

    def search_book(self, event):
        searchobj = self.entry.get().upper()
        self.list1 = []
        if searchobj == "":
            self.list1 = list(self.booklist.keys()).copy()
        else:
            for book in list(self.booklist.keys()):
                if searchobj in book:
                    self.list1.append(book)
        self.update_list()

    def request_book(self):
        self.libraryframe.destroy()
        self.displayframe = Frame(self)
        label1 = Label(self.displayframe, image=self.bg)
        label1.image = self.bg
        label1.place(x=0, y=0)
        framex = Frame(self.displayframe, bg="black")
        self.back = Button(framex, text="Goback")
        self.back.pack(anchor="w")
        self.back.bind('<Button-1>', self.goto)
        framex.pack(side=TOP, anchor="w")
        Label(self.displayframe, text="ENTER NAME OF BOOK(s)", bg="cyan", font="arialbold 35 bold", bd=10,
              relief=SUNKEN).pack()
        self.req = Entry(self.displayframe, bg="cyan", fg="black", bd=5, font="arialbold 18 bold")
        self.req.pack(fill=X, pady=20)
        self.req.focus()
        sbmt = Button(self.displayframe, text="Submit", bg="pink", command=self.submitrequest, font="arialbold 13",
                      bd=10, relief=RIDGE)
        sbmt.pack(ipadx=50, pady=10)
        self.bind('<Return>', self.func1)
        self.displayframe.pack(pady=200)

    def func1(self, event):
        self.submitrequest()

    def func2(self, event):
        self.submitbook()

    def submitrequest(self):
        print(self.req.get())
        request1 = self.req.get().upper()
        if request1 == "" or request1.isalpha() == FALSE:
            frame1 = Frame(self.displayframe)
            txt = Label(frame1, text="Please Enter a valid Request", fg="red", font="lucida 18", bg="grey", bd=10,
                        relief=SUNKEN)
            txt.pack()
            frame1.pack()
            if self.c >= 2:
                frame1.destroy()
            self.c += 1
            return
        with open("requests.txt", "a") as r:
            r.write(request1 + "\n")
        gitupdate.update_list(self.user, "requests")
        showinfo("Request Submitted", "Your request has been submitted.")
        self.goto(event=None)

    def add_book(self):
        self.libraryframe.destroy()
        self.displayframe = Frame(self)
        label1 = Label(self.displayframe, image=self.bg)
        label1.image = self.bg
        label1.place(x=0, y=0)
        framex = Frame(self.displayframe, bg="black")
        self.back = Button(framex, text="Goback")
        self.back.pack(anchor="w")
        self.back.bind('<Button-1>', self.goto)
        framex.pack(side=TOP, anchor="w")
        Label(self.displayframe, text="ENTER NAME OF BOOK", bg="cyan", font="arialbold 35 bold", bd=10,
              relief=SUNKEN).pack()
        self.bookname = Entry(self.displayframe, bg="grey", fg="black", bd=5, font="arialbold 18 bold")
        self.bookname.pack(fill=X, pady=20)
        self.bookname.focus()
        Label(self.displayframe, text="ENTER LINK OF BOOK", bg="cyan", font="arialbold 35 bold", bd=10,
              relief=SUNKEN).pack()
        self.booklink = Entry(self.displayframe, bg="grey", fg="black", bd=5, font="arialbold 18 bold")
        self.booklink.pack(fill=X, pady=20)
        sbmt = Button(self.displayframe, text="Submit", bg="pink", command=self.submitbook, font="arialbold 13",
                      bd=10, relief=RIDGE)
        sbmt.pack(ipadx=50, pady=10)
        self.bind('<Return>', self.func2)
        self.displayframe.pack(pady=200)

    def submitbook(self):
        book = self.bookname.get().upper()
        link = self.booklink.get()
        if book == "" or link == "" or link.startswith("http") == False:
            frame1 = Frame(self.displayframe)
            txt = Label(frame1, text="Please Enter a valid Book/Link", fg="red", font="lucida 18", bg="grey", bd=10,
                        relief=SUNKEN)
            txt.pack()
            frame1.pack()
            if self.c >= 2:
                txt.destroy()
            self.c += 1
            return

        with open("books.txt", "a") as r:
            r.write(book + " " + link)
        gitupdate.update_list(self.user, "books")
        showinfo("Request Submitted", "Your book has been submitted for review.")
        self.goto(event=None)


master = librarygui()
master.home()
master.mainloop()
