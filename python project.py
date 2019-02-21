from Tkinter import *

root1=Tk()
z=PhotoImage(file='splasher.gif')
Label(root1,image=z).grid(row=0,column=1,columnspan=100,rowspan=100)
Label(root1,text="Python Project",relief='ridge',font="times 30 italic",bg='maroon2').grid(row=0,column=1)
Label(root1,text="Topic-Movie Database System",relief='ridge',font="times 25 italic",bg='mediumpurple1').grid(row=1,column=1)
Label(root1,text="Name-Sanyam Jain",relief='ridge',font="times 20 italic",bg='orange2',fg='white').grid(row=2,column=1)
Label(root1,text="Er. No.-161B196",relief='ridge',font="times 18 italic",bg='sienna2').grid(row=3,column=1)
Label(root1,text="Batch-B-7",relief='ridge',font="times 18 italic",bg='burlywood').grid(row=4,column=1)
root1.after(5000,root1.destroy)
root1.mainloop()

root=Tk()
root.title("Movie Database System")
root.configure(bg="purple")
x=PhotoImage(file='movie.gif')
Label(root,image=x).grid(row=0,column=1,columnspan=100,rowspan=100)
Label(root,text="Movie Database System",relief='ridge',font="times 40 italic",bg='SeaGreen1').grid(row=0,column=1,columnspan=20)

import sqlite3
con=sqlite3.Connection('12.db')
cur=con.cursor()
Label(root,text="Enter the movie name:",font="times 18 bold",bg='gold',fg='blue').grid(row=3,column=1)
e1=Entry(root,width=30,bd=15,font="times 20")
e1.grid(row=3,column=2,columnspan=13)

cur.execute("create table if not exists movie(no varchar(100),name varchar(50) primary key,runtime varchar(50),genre varchar(35),release date date,synopsis varchar(500),language varchar(30),budget varchar(30),rating number(5,5))")

cur.execute("insert into movie values('22','The Shawshank Redemption','2h 22min','Crime,Thriller','14-Oct-1994','Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.','English','$25,000,000','9.3')")
cur.execute("insert into movie values('22','The Godfather','2h 55min','Crime,Horror','24-Mar-1972','The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',' English,Italian,Latin','$6,000,000','9.2')")
cur.execute("insert into movie values('22','The Dark Knight','2h 32min',' Action, Crime,History','18-Jul-2008','Eight years after the Jokers reign of anarchy, the Dark Knight, with the help of the enigmatic Catwoman, is forced from his exile to save Gotham City, now on the edge of total annihilation, from the brutal guerrilla terrorist Bane','English,Mandarin','$185,000,000','9.0')")
cur.execute("insert into movie values('22','12 Angry Men','1h 36min','Crime,Adventure','1-Apr-1957','A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence.','english','$350,000','8.9')") 
cur.execute("insert into movie values('22','Schindlers List','3h 15min','Biography,Mystery, History','4-Feb-1994','In German-occupied Poland during World War II, Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazi Germans.','English,Hebrew,German,Polish','$22,000,000','8.9')")
cur.execute("insert into movie values('22','Pulp Fiction','2h 34min','Crime,Mystery','14-Oct-1994','The lives of two mob hit men, a boxer, a gangster wife, and a pair of diner bandits intertwine in four tales of violence and redemption.','English,Spanish,French','$8,000,000','8.9')") 
cur.execute("insert into movie values('22','The Lord of the Rings: The Return of the King','3h 21min','Adventure,Mystery,Horror','17-Dec-2003','Gandalf and Aragorn lead the World of Men against Saurons army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.','English,Quenya,Old English,Sindarin','$94,000,000','8.9')")
cur.execute("insert into movie values('22','The Good, the Bad and the Ugly','2h 58min','Sci-Fi,Horror','29-Dec-1967','A bounty hunting scam joins two men in an uneasy alliance against a third in a race to find a fortune in gold buried in a remote cemetery.','Italian,English','$1,200,000','8.9')")  
cur.execute("insert into movie values('22','Fight Club','2h 19min','Drama','15-Oct-1999','An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more.','English','$63,000,000','8.8')")
cur.execute("insert into movie values('22','Forrest Gump','2h 22min','Mystery,Thriller','6-Jul-1994','JFK, LBJ, Vietnam, Watergate, and other history unfold through the perspectivStar Wars: Episode V - The Empire Strikes Back','English','$18,000,000','8.8')") 
cur.execute("insert into movie values('22','Inception','2h 28min','Action, Adventure,Sci-Fi','16-Jul-2010','A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.','English,Japanese,French','$160,000,000','8.8')") 
cur.execute("insert into movie values('22','The Lord of the Rings: The Two Towers','2h 59min','Adventure, Drama, Fantasy','18-Dec-2002','While Frodo and Sam edge closer to Mordor with the help of the shifty Gollum, the divided fellowship makes a stand against Saurons new ally, Saruman, and his hordes of Isengard.',' English,Sindarin,Old English','$94,000,000','8.7')") 
cur.execute("insert into movie values('22','Goodfellas','2h 26min','Biography,Crime,Mystery','21-Sep-1990','The story of Henry Hill and his life through the teen years into the years of mafia, covering his relationship with his wife Karen Hill and his Mob partners Jimmy Conway and Tommy DeVito in the Italian-American crime syndicate.',' English,Italian','$25,000,000','8.7')")
cur.execute("insert into movie values('22','The Matrix','2h 16min','Action, Sci-Fi','31-Mar-1999','A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.',' English','$63,000,000 ','8.7')")
cur.execute("insert into movie values('1','Seven Samurai','3h 27min','Adventure,Drama','19-Nov-1956','A poor village under attack by bandits recruits seven unemployed samurai to help them defend themselves.',' Japanese','$2,000,000','8.7')")
cur.execute("insert into movie values('1','City of God','2h 10min','Crime,Drama','13-Feb-2004','Two boys growing up in a violent neighborhood of Rio de Janeiro take different paths: one becomes a photographer, the other a drug dealer.','Portuguese','$3,300,000','8.6')")
cur.execute("insert into movie values('1','Se7en','2h 7min','Crime,Drama,Mystery','22-Sep-1995','Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his motives.',' English','$33,000,000','8.6')")
cur.execute("insert into movie values('1','Interstellar','2h 49min','Adventure, Drama,Comedy,Sci-Fi','7-Nov-2014','A team of explorers travel through a wormhole in space in an attempt to ensure humanitys survival.',' English',' $165,000,000','8.6')")
cur.execute("insert into movie values('1','Psycho','1h 49min','Horror, Mystery,Action, Thriller','8-Sep-1960','A Phoenix secretary embezzles $40,000 from her employers client, goes on the run, and checks into a remote motel run by a young man under the domination of his mother.',' English','$806,947','8.5')")
cur.execute("insert into movie values('1','City Lights','1h 27min','Comedy, Drama, Romance','7-Mar-1931','With the aid of a wealthy erratic tippler, a dewy-eyed tramp who has fallen in love with a sightless flower girl accumulates money to be able to help her medically.','English','$1,500,000','8.6')")
cur.execute("insert into movie values('1','The Departed','2h 31min','Crime, Drama, Thriller','6-Oct-2006','An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.',' English,Cantonese','$90,000,000','8.5')")
cur.execute("insert into movie values('1','Rear Window','1h 52min','Mystery, Thriller','Sep-1954','A wheelchair-bound photographer spies on his neighbours from his apartment window and becomes convinced one of them has committed murder.','English','$1,000,000','8.5')")
cur.execute("insert into movie values('1','Terminator 2','2h 17min','Action, Sci-Fi, Thriller','3-Jul-1991','A cyborg, identical to the one who failed to kill Sarah Connor, must now protect her ten year old son, John Connor, from a more advanced cyborg.','English,Spanish','$102,000,000','8.2')")
cur.execute("insert into movie values('1','The Prestige','2h 10min','Drama,Mystery,Sci-Fi','20-Oct-2006','After a tragic accident two stage magicians engage in a battle to create the ultimate illusion whilst sacrificing everything they have to outwit the other.','English','$40,000,000','8.4')")
cur.execute("insert into movie values('1','Dangal','2h 41min','Action, Biography, Drama,History','21-Dec-2016','Former wrestler Mahavir Singh Phogat and his two wrestler daughters struggle towards glory at the Commonwealth Games in the face of societal oppression.','Hindi','INR 700,000,000','8.6')")
cur.execute("insert into movie values('1','Braveheart','2h 58min','Biography,Drama,History','24-May-1995','When his secret bride is executed for assaulting an English soldier who tried to rape her, Sir William Wallace begins a revolt against King Edward I of England.','English,French,Latin,Scottish Gaelic','$72,000,000','8.4')")
cur.execute("insert into movie values('1','Taare Zameen Par','2h 45min','Drama,Sci-Fi','21-Dec-2007','An eight-year-old boy is thought to be a lazy trouble-maker, until the new art teacher has the patience and compassion to discover the real problem behind his struggles in school.','Hindi,English','$1,204,660','8.5')")
cur.execute("insert into movie values('1','3 Idiots','2h 50min','Comedy,Drama','25-Dec-2009','Two friends are searching for their long lost companion. They revisit their college days and recall the memories of their friend who inspired them to think differently, even as the rest of the world called them idiots.','Hindi,English','INR 550,000,000','8.4')")
cur.execute("insert into movie values('1','Dunkirk','1h 46min','Action,Drama,History','21-Jul-2017','Allied soldiers from Belgium, the British Empire and France are surrounded by the German Army, and evacuated during a fierce battle in World War II.','English,French,German','$100,000,000','8.3')")
cur.execute("insert into movie values('1','A Separation','2h 3min','Drama,History, Mystery','29-Oct-2012','A married couple are faced with a difficult decision - to improve the life of their child by moving to another country or to stay in Iran and look after a deteriorating parent who has Alzheimers disease.','Persian','$500,000','8.4')")
cur.execute("insert into movie values('22','Stan Helsing','1h 48min','Comedy, Horror','25-Mar-2010','Its Halloween night, and slacker video clerk Stan Helsing along with his insanely sexy ex-girlfriend , best buddy and an exotic dancer massage therapist - detours into a town cursed by the biggest monsters in movie history Freddy, Jason , Pinhead , Leatherface , Chucky , & Michael Myers. Written by Anonymous.','English','8000','3.6')")
cur.execute("insert into movie values('22','Nightmare','1h 37min','Crime,Horror,Thriller','29-Jul-2000','Seven friends will die one by one for protecting a terrible secret. Can a vengeful spirit be stopped',' Korean','90000','5.3')")
cur.execute("insert into movie values('22','Bean','1h 29min','Adventure,Comedy,Horror','7-Nov-1997','The bumbling Mr. Bean travels to America when he is given the responsibility of bringing a highly valuable painting to a Los Angeles museum.','English','$22,000,000','6.4')")
cur.execute("insert into movie values('22','The Onion Movie','1h 20min','Comedy,History','7-Jan-2008','Satirical interpretations of world events and curious human behavior.','English,Russian,Spanish','9999900','6.3')")
cur.execute("insert into movie values('22','The Comedians of Comedy','1h 43min','Comedy','12-Mar-2005','Follow four comedians as they tour the States.',' English','$500,000','7.4')")
            
   
def Search():
    showall=Tk()
    showall.configure(bg="peru")
    
    def back():
        showall.destroy()
    Button(showall,text="Back",bd=8,command=back,relief='ridge',font="times  15",bg='Firebrick',fg='white').grid(row=10,column=2)
    Label(showall,text="Movie Database System",relief='ridge',font="times 40 italic",bg='pink').grid(row=0,column=0,columnspan=5,pady=5)
    
    
    cur.execute("select name from movie where name=?",(e1.get(),))
    a=cur.fetchall()
    Label(showall,text="NAME",relief='ridge',bg='sky blue').grid(row=1,column=0,pady=5)
    Label(showall,text=a,relief='ridge',bg='Pale Green').grid(row=1,column=1)

    cur.execute("select runtime from movie where name=?",(e1.get(),))
    b=cur.fetchall()
    Label(showall,text="RUNTIME",relief='ridge',bg='sky blue').grid(row=2,column=0,pady=5)
    Label(showall,text=b,relief='ridge',bg='Pale Green').grid(row=2,column=1)

    cur.execute("select genre from movie where name=?",(e1.get(),))
    c=cur.fetchall()
    Label(showall,text="GENRE",relief='ridge',bg='sky blue').grid(row=3,column=0,pady=5)
    Label(showall,text=c,relief='ridge',bg='Pale Green').grid(row=3,column=1)

    cur.execute("select release date from movie where name=?",(e1.get(),))
    d=cur.fetchall()
    Label(showall,text="RELEASE DATE",relief='ridge',bg='sky blue').grid(row=4,column=0,pady=5)
    Label(showall,text=d,relief='ridge',bg='Pale Green').grid(row=4,column=1)

    cur.execute("select synopsis from movie where name=?",(e1.get(),))
    e=cur.fetchall()
    Label(showall,text="SYNOPSIS",relief='ridge',bg='sky blue').grid(row=5,column=0,padx=20,pady=5)
    Label(showall,text=e,relief='ridge',bg='Pale Green').grid(row=5,column=1)

    cur.execute("select language from movie where name=?",(e1.get(),))
    f=cur.fetchall()
    Label(showall,text="LANGUAGE",relief='ridge',bg='sky blue').grid(row=6,column=0,pady=5)
    Label(showall,text=f,relief='ridge',bg='Pale Green').grid(row=6,column=1)
    
    cur.execute("select budget from movie where name=?",(e1.get(),))
    g=cur.fetchall()
    Label(showall,text="BUDGET",relief='ridge',bg='sky blue').grid(row=7,column=0,pady=5)
    Label(showall,text=g,relief='ridge',bg='Pale Green').grid(row=7,column=1)

    cur.execute("select rating from movie where name=?",(e1.get(),))
    h=cur.fetchall()
    Label(showall,text="RATING",relief='ridge',bg='sky blue').grid(row=8,column=0,pady=5)
    Label(showall,text=h,relief='ridge',bg='Pale Green').grid(row=8,column=1)
    
    showall.mainloop()

def Exit():
    root.destroy()
    
def name():
    name=Tk()    
    name.configure(bg="tomato")
    Label(name,text="Movie Database System",relief='ridge',font="times 40 italic",bg='blue').pack()
    Label(name,text="",bg='tomato').pack()
    Label(name,text="Name Of All Movies",bg='PaleGreen1',relief='ridge',font="times 20 italic").pack()
    Label(name,text="",bg='tomato').pack()
    cur.execute("select name from movie where no=22")
    a=cur.fetchall()
    for i in a:
        Label(name,text=i,relief='ridge').pack()
    def name1():
        name1=Tk()
        name1.configure(bg="tomato")
        def back():
            name1.destroy()
        Button(name1,text="Back",bd=8,command=back,relief='ridge',font="times  15",bg='violet',fg='white').pack(side='bottom')
        Label(name1,text="Movie Database System",relief='ridge',font="times 40 italic",bg='blue').pack()
        Label(name1,text="",bg='tomato').pack()
        Label(name1,text="Name Of All Movies",bg='PaleGreen1',relief='ridge',font="times 20 italic").pack()
        Label(name1,text="",bg='tomato').pack()
        cur.execute("select name from movie where no=1")
        a=cur.fetchall()
        for i in a:
            Label(name1,text=i,relief='ridge').pack()
        name1.mainloop()
    Button(name,text="More Movies",command=name1,relief='ridge',font="times  15",bg='tan2',bd=10,fg='white').pack()

        
    name.mainloop()

    
def about():
    about=Tk()
    
    about.configure(bg="pink")
    
    def back():
        about.destroy()
    Button(about,text="Back",bd=8,command=back,relief='ridge',font="times  13",bg='forest green',fg='white').pack(side='bottom')
    Label(about,text="Movie Database System",relief='ridge',font="times 40 italic",bg='blue').pack()
    Label(about,text="",bg='pink').pack()
    Label(about,text="About Us",bg='red',relief='ridge',font="times 20 italic").pack()
    Label(about,text="",bg='pink').pack()
    Label(about,text="In the current scenario, a moviegoer has to visit more than one website to get the following basic movie information.",bg='orange',relief='ridge',font="times 15 italic").pack()
    Label(about,text="List of movies playing in theaters, upcoming movies, DVD/Blu-ray movies",bg='orange',relief='ridge',font="times 15 italic").pack()
    Label(about,text="MDB Rating; Rotten Tomatoes Rating",bg='orange',relief='ridge',font="times 15 italic").pack()
    Label(about,text="Simple Plot, Cast & Crew, Genre, Year Released, Runtime",bg='orange',relief='ridge',font="times 15 italic").pack()
    Label(about,text="MDB Rating; Rotten Tomatoes Rating",bg='orange',relief='ridge',font="times 15 italic").pack()
    Label(about,text="Show Times",bg='orange',relief='ridge',font="times 15 italic").pack()
    Label(about,text="Links to stream/rent the movie online, buy DVD/Blu-ray",bg='orange',relief='ridge',font="times 15 italic").pack()
    Label(about,text="There are websites like www.imdb.com and www.rottentomatoes.com with rich amount of the",bg='orange',relief='ridge',font="times 15 italic").pack()
    Label(about,text="aforementioned data but the user has to open at least 3-4 websites to view all the data. So, this project was ",bg='orange',relief='ridge',font="times 15 italic").pack()
    Label(about,text="started with the intention of developing a one-stop destination for the user to view all the data.",bg='orange',relief='ridge',font="times 15 italic").pack()
    Label(about,text="The data from these websites was fetched by calling the APIs and putting them together in a dynamic web ",bg='orange',relief='ridge',font="times 15 italic").pack()
    Label(about,text="application named as Movie Database Syatem. ",bg='orange',relief='ridge',font="times 15 italic").pack()
    Label(about,text="MDB (Movie Database) is one of the largest movie databases available in the web. It has detailed",bg='orange',relief='ridge',font="times 15 italic").pack()
    Label(about,text="information about all the movies including movie show times and trailers. But it doesnt provide the",bg='orange',relief='ridge',font="times 15 italic").pack()   
    Label(about,text="information about online streaming. Rotten Tomatoes is another website which primarily gives the",bg='orange',relief='ridge',font="times 15 italic").pack()
    Label(about,text="combined critic score of any movie. It provides the basic movie data, streaming links but not show times of",bg='orange',relief='ridge',font="times 15 italic").pack()
    Label(about,text="movies playing in theaters.",bg='orange',relief='ridge',font="times 15 italic").pack() 
    Label(about,text="",bg='pink').pack()    
    about.mainloop()


Button(root,text="Search",command=Search,relief='ridge',font="times  15",bg='SlateBlue1',bd=10,fg='white').grid(row=3,column=25)
Button(root,text="Exit",command=Exit,relief='ridge',font="times  15",bg='tan2',bd=10,fg='white').grid(row=14,column=25)
Button(root,text="Name of Movies",command=name,relief='ridge',font="times  15",bg='tomato1',bd=10,fg='white').grid(row=14,column=1)
Button(root,text="About Us",command=about,relief='ridge',font="times  15",bg='orchid1',bd=10,fg='white').grid(row=15,column=1,columnspan=45)

def horror():
    horror=Tk()    
    horror.configure(bg="orange")
    def back():
        horror.destroy()
    Button(horror,text="Back",bd=8,command=back,relief='ridge',font="times  10",bg='tomato1',fg='white').pack(side='bottom')
    Label(horror,text="Movie Database System",relief='ridge',font="times 40 italic",bg='violet').pack()
    Label(horror,text="",bg='orange').pack()
    Label(horror,text="Horror Movies",bg='blue',font="times 20 italic").pack()
    Label(horror,text="",bg='orange').pack()
    cur.execute("select name from movie where genre like '%Horror%'")
    b=cur.fetchall()
    for i in b:
        Button(horror,text=i).pack()    
    horror.mainloop()
    

def comedy():
    comedy=Tk()
    comedy.configure(bg="orange")
    def back():
        comedy.destroy()
    Button(comedy,text="Back",bd=8,command=back,relief='ridge',font="times  10",bg='tomato1',fg='white').pack(side='bottom')
    Label(comedy,text="Movie Database System",relief='ridge',font="times 40 italic",bg='violet').pack()
    Label(comedy,text="",bg='orange').pack()
    Label(comedy,text="Comedy Movies",bg='blue',font="times 20 italic").pack()
    Label(comedy,text="",bg='orange').pack()
    cur.execute("select name from movie where genre like '%Comedy%'")
    b=cur.fetchall()
    for i in b:
        Button(comedy,text=i).pack()    
    comedy.mainloop()


def thriller():
    thriller=Tk()
    thriller.configure(bg="orange")
    def back():
        thriller.destroy()
    Button(thriller,text="Back",bd=8,command=back,relief='ridge',font="times  10",bg='tomato1',fg='white').pack(side='bottom')
    Label(thriller,text="Movie Database System",relief='ridge',font="times 40 italic",bg='violet').pack()
    Label(thriller,text="",bg='orange').pack()
    Label(thriller,text="Thriller Movies",bg='blue',font="times 20 italic").pack()
    Label(thriller,text="",bg='orange').pack()
    cur.execute("select name from movie where genre like '%Thriller%'")
    b=cur.fetchall()
    for i in b:
        Button(thriller,text=i).pack()    
    thriller.mainloop()
    

def action():
    action=Tk()
    action.configure(bg="orange")
    def back():
        action.destroy()
    Button(action,text="Back",bd=8,command=back,relief='ridge',font="times  10",bg='tomato1',fg='white').pack(side='bottom')
    Label(action,text="Movie Database System",relief='ridge',font="times 40 italic",bg='violet').pack()
    Label(action,text="",bg='orange').pack()
    Label(action,text="Action Movies",bg='blue',font="times 20 italic").pack()
    Label(action,text="",bg='orange').pack()
    cur.execute("select name from movie where genre like '%Action%'")
    b=cur.fetchall()
    for i in b:
        Button(action,text=i).pack()    
    action.mainloop()


def drama():
    drama=Tk()
    drama.configure(bg="orange")
    def back():
        drama.destroy()
    Button(drama,text="Back",bd=8,command=back,relief='ridge',font="times  10",bg='tomato1',fg='white').pack(side='bottom')
    Label(drama,text="Movie Database System",relief='ridge',font="times 40 italic",bg='violet').pack()
    Label(drama,text="",bg='orange').pack()
    Label(drama,text="Drama Movies",bg='blue',font="times 20 italic").pack()
    Label(drama,text="",bg='orange').pack()
    cur.execute("select name from movie where genre like '%Drama%'")
    b=cur.fetchall()
    for i in b:
        Button(drama,text=i).pack()    
    drama.mainloop()
    

def history():
    history=Tk()
    history.configure(bg="orange")
    def back():
        history.destroy()
    Button(history,text="Back",bd=8,command=back,relief='ridge',font="times  10",bg='tomato1',fg='white').pack(side='bottom')
    Label(history,text="Movie Database System",relief='ridge',font="times 40 italic",bg='violet').pack()
    Label(history,text="",bg='orange').pack()
    Label(history,text="History Movies",bg='blue',font="times 20 italic").pack()
    Label(history,text="",bg='orange').pack()
    cur.execute("select name from movie where genre like '%History%'")
    b=cur.fetchall()
    for i in b:
        Button(history,text=i).pack()    
    history.mainloop()
    

def adventure():
    adventure=Tk()
    adventure.configure(bg="orange")
    def back():
        adventure.destroy()
    Button(adventure,text="Back",bd=8,command=back,relief='ridge',font="times  10",bg='tomato1',fg='white').pack(side='bottom')
    Label(adventure,text="Movie Database System",relief='ridge',font="times 40 italic",bg='violet').pack()
    Label(adventure,text="",bg='orange').pack()
    Label(adventure,text="Adventure Movies",bg='blue',font="times 20 italic").pack()
    Label(adventure,text="",bg='orange').pack()
    cur.execute("select name from movie where genre like '%Adventure%'")
    b=cur.fetchall()
    for i in b:
        Button(adventure,text=i).pack()    
    adventure.mainloop()
    

def crime():
    crime=Tk()
    crime.configure(bg="orange")
    def back():
        crime.destroy()
    Button(crime,text="Back",bd=8,command=back,relief='ridge',font="times  10",bg='tomato1',fg='white').pack(side='bottom')
    Label(crime,text="Movie Database System",relief='ridge',font="times 40 italic",bg='violet').pack()
    Label(crime,text="",bg='orange').pack()
    Label(crime,text="Crime Movies",bg='blue',font="times 20 italic").pack()
    Label(crime,text="",bg='orange').pack()
    cur.execute("select name from movie where genre like '%Crime%'")
    b=cur.fetchall()
    for i in b:
        Button(crime,text=i).pack()    
    crime.mainloop()
    

def mystery():
    mystery=Tk()
    mystery.configure(bg="orange")
    def back():
        mystery.destroy()
    Button(mystery,text="Back",bd=8,command=back,relief='ridge',font="times  10",bg='tomato1',fg='white').pack(side='bottom')
    Label(mystery,text="Movie Database System",relief='ridge',font="times 40 italic",bg='violet').pack()
    Label(mystery,text="",bg='orange').pack()
    Label(mystery,text="Mystery Movies",bg='blue',font="times 20 italic").pack()
    Label(mystery,text="",bg='orange').pack()
    cur.execute("select name from movie where genre like '%Mystery%'")
    b=cur.fetchall()
    for i in b:
        Button(mystery,text=i).pack()    
    mystery.mainloop()
    

def scifi():
    scifi=Tk()
    scifi.configure(bg="orange")
    def back():
        scifi.destroy()
    Button(scifi,text="Back",bd=8,command=back,relief='ridge',font="times  10",bg='tomato1',fg='white').pack(side='bottom')
    Label(scifi,text="Movie Database System",relief='ridge',font="times 40 italic",bg='violet').pack()
    Label(scifi,text="",bg='orange').pack()
    Label(scifi,text="Sci-fi Movies",bg='blue',font="times 20 italic").pack()
    Label(scifi,text="",bg='orange').pack()
    cur.execute("select name from movie where genre like '%Sci-fi%'")
    b=cur.fetchall()
    for i in b:
        Button(scifi,text=i).pack()    
    scifi.mainloop()
    

Button(root,text='Horror',command=horror,bg="violet").grid(row=5,column=3,sticky=W)
Button(root,text='Comedy',command=comedy,bg="chocolate").grid(row=5,column=6,sticky=W)
Button(root,text='Thriller',command=thriller,bg="gold").grid(row=6,column=3,sticky=W)
Button(root,text='Action',command=action,bg="silver").grid(row=6,column=6,sticky=W)
Button(root,text='Drama',command=drama,bg="LightBlue").grid(row=7,column=3,sticky=W)
Button(root,text='History',command=history,bg="Goldenrod").grid(row=7,column=6,sticky=W)
Button(root,text='Adventure',command=adventure,bg="light coral").grid(row=8,column=3,sticky=W)
Button(root,text='Crime',command=crime,bg="SlateBlue1").grid(row=8,column=6,sticky=W)
Button(root,text='Mystery',command=mystery,bg="forest green").grid(row=9,column=3,sticky=W)
Button(root,text='Sci-Fi',command=scifi,bg="red2").grid(row=9,column=6,sticky=W)


root.mainloop()
