#sims4 randomizer
#updated aug 15 - add Cottage Living

#FUTURE UPDATES:
# add ability to check expansion/game packs
# smart kid/pet #s that don't exceed family size limit

from tkinter import *
import random

window=Tk()
window.title("Sims 4 Randomizer")
window.geometry('500x450')
window.configure(bg="palegreen")

#top
topLbl = Label(window, text="Sims 4 Randomizer          ", bg="palegreen",
               font=("Chalkboard SE", 30))
topLbl.grid(column=1, row=0, sticky=W)


#variables for checkbuttons
relChecked = IntVar()
relChecked.set(0)

kidChecked = IntVar()
kidChecked.set(0)

petChecked = IntVar()
petChecked.set(0)

carChecked = IntVar()
carChecked.set(0)

aspChecked = IntVar()
aspChecked.set(0)

t1Checked = IntVar()
t1Checked.set(0)

t2Checked = IntVar()
t2Checked.set(0)

t3Checked = IntVar()
t3Checked.set(0)

chalChecked = IntVar()
chalChecked.set(0)

#checkbuttons for each category

relCB = Checkbutton(window, text="Relationship", bg="palegreen", variable=relChecked)
relCB.grid(column=0, row=1, sticky=W)

kidCB = Checkbutton(window, text="Children", bg="palegreen", variable=kidChecked)
kidCB.grid(column=0, row=2, sticky=W)

petCB = Checkbutton(window, text="Pets", bg="palegreen", variable=petChecked)
petCB.grid(column=0, row=3, sticky=W)

carCB = Checkbutton(window, text="Career", bg="palegreen", variable=carChecked)
carCB.grid(column=0, row=4, sticky=W)

aspCB = Checkbutton(window, text="Aspiration", bg="palegreen", variable=aspChecked)
aspCB.grid(column=0, row=5, sticky=W)

t1CB = Checkbutton(window, text="Trait #1", bg="palegreen", variable=t1Checked)
t1CB.grid(column=0, row=6, sticky=W)

t2CB = Checkbutton(window, text="Trait #2", bg="palegreen", variable=t2Checked)
t2CB.grid(column=0, row=7, sticky=W)

t3CB = Checkbutton(window, text="Trait #3", bg="palegreen", variable=t3Checked)
t3CB.grid(column=0, row=8, sticky=W)

chalCB = Checkbutton(window, text="Challenge", bg="palegreen", variable=chalChecked)
chalCB.grid(column=0, row=9, sticky=W)

#category result labels
relRes = Label(window, text="", bg="palegreen")
relRes.grid(column=1, row=1, sticky=W)

kidRes = Label(window, text="", bg="palegreen")
kidRes.grid(column=1, row=2, sticky=W)

petRes = Label(window, text="", bg="palegreen")
petRes.grid(column=1, row=3, sticky=W)

carRes = Label(window, text="", bg="palegreen")
carRes.grid(column=1, row=4, sticky=W)

aspRes = Label(window, text="", bg="palegreen")
aspRes.grid(column=1, row=5, sticky=W)

t1Res = Label(window, text="", bg="palegreen")
t1Res.grid(column=1, row=6, sticky=W)

t2Res = Label(window, text="", bg="palegreen")
t2Res.grid(column=1, row=7, sticky=W)

t3Res = Label(window, text="", bg="palegreen")
t3Res.grid(column=1, row=8, sticky=W)

chalRes = Label(window, text="",
                bg="palegreen")
chalRes.grid(column=1, row=9, sticky=W)


#result lists for each category

relList = ["Single", "Married", "Divorced", "Single with help",
           "Divorced and remarried", "Multi-generation household"]
kidList = ["1 child", "2 children", "3 children", "4 children", "5 children"]
petList = ["No pets", "1 dog", "1 cat", "1 cat and 1 dog", "Adopt a stray",
           "Small pet", "2+ dogs", "2+ cats", "As many as possible!"]
carList = ["Detective", "Doctor", "Scientist", "Astronaut", "Athlete",
           "Business", "Critic", "Culinary", "Entertainer", "Freelance Writer",
           "Freelance Artist", "Freelance Collector", "Freelance Gardener",
           "Freelance Programmer", "Gardener", "Painter", "Politician", "Secret Agent",
           "Social Media", "Style Influencer", "Tech Guru", "Writer", "Veterinarian",
           "Business Owner", "Conservationist", "Education", "Engineer", "Law",
           "Interior Decorator","Odd Jobs", "Beekeeper", "Plopsy Seller",
           "Crafter/Woodworker", "Fishersim", "Animal Trainer"]
aspList = ["Friend of the Animal", "Body Builder", "Musical Genius",
           "Painter Extraordinaire", "Bestselling Author", "Lord of the Knits",
           "Master Maker", "Chief of Mischief", "Public Enemy",
           "Successful Lineage", "Big Happy Family", "Super Parent",
           "Master Chef", "Master Mixologist", "Fabulously Wealthy",
           "Mansion Baron", "Renaissance Sim", "Nerd Brain", "Academic",
           "Computer Whiz", "Spellcraft & Sorcery", "City Native",
           "Beach Life", "Serial Romantic", "Soulmate", "Curator",
           "Outdoor Enthusiast", "Angling Ace", "Freelance Botanist",
           "Purveryor of Potions", "Eco Innovator", "Country Caretake", "Leader of the Pack",
           "Friend of the World", "Party Animal", "Joke Star"]
tList = ["Creative", "Active", "Cheerful", "Genius", "Gloomy", "Goofball",
         "Hot Headed", "Romantic", "Self-Assured", "Unflirty", "Art Lover",
         "Book Worm", "Foodie", "Geek", "Music Lover", "Perfectionist",
         "Ambitious", "Animal Enthusiast", "Cat Lover", "Childish", "Clumsy", "Dance Machine",
         "Dog Lover", "Erratic", "Glutton", "Kleptomaniac", "Lactose Intolerant", "Lazy",
         "Loves the Outdoors", "Materialistic", "Neat", "Slob", "Snob",
         "Squeamish", "Vegetarian", "Bro", "Evil", "Family Oriented",
         "Good", "Hates Children", "Insider", "Jealous", "Loner", "Mean",
         "Noncommittal", "Outgoing", "Child of the Islands", "Child of the Ocean",
         "Maker", "Freegan", "Green Fiend", "Recycle Disciple", ]
chalList = ["Complete a collection", "Children must complete aspirations",
            "Finish 2 Aspirations", "Short Lifespan", "Long Lifespan",
            "Tiny House", "All children must be adopted", "Live in an apartment",
            "Remodel a cheap house or apartment", "Children inherit at least 1 trait from parent",
            "Camping trip every summer", "Move at least once",
            "Grandparents get custody of first grandchild", "Big garden",
            "Move in with NPC", "Throw every kind of party", "Alien family member",
            "Spellcasters", "Mermaid family member"]


#define buttons

def reset():
    relRes.configure(text="")
    kidRes.configure(text="")
    petRes.configure(text="")
    carRes.configure(text="")
    aspRes.configure(text="")
    t1Res.configure(text="")
    t2Res.configure(text="")
    t3Res.configure(text="")
    chalRes.configure(text="")
    relChecked.set(0)
    kidChecked.set(0)
    petChecked.set(0)
    carChecked.set(0)
    aspChecked.set(0)
    t1Checked.set(0)
    t2Checked.set(0)
    t3Checked.set(0)
    chalChecked.set(0)
    
def clickall():
    result=random.choice(relList)
    relRes.configure(text=result)
    result=random.choice(kidList)
    kidRes.configure(text=result)
    result=random.choice(petList)
    petRes.configure(text=result)
    result=random.choice(carList)
    carRes.configure(text=result)
    result=random.choice(aspList)
    aspRes.configure(text=result)
    result=random.choice(tList)
    t1Res.configure(text=result)
    result=random.choice(tList)
    t2Res.configure(text=result)
    result=random.choice(tList)
    t3Res.configure(text=result)
    result=random.choice(chalList)
    chalRes.configure(text=result)

def clickslct():
    if relChecked.get() == 1:
       result=random.choice(relList)
       relRes.configure(text=result)
    if kidChecked.get() == 1:
        result=random.choice(kidList)
        kidRes.configure(text=result)
    if petChecked.get() == 1:
        result=random.choice(petList)
        petRes.configure(text=result)
    if carChecked.get() == 1:
        result=random.choice(carList)
        carRes.configure(text=result)
    if aspChecked.get() == 1:
        result=random.choice(aspList)
        aspRes.configure(text=result)
    if t1Checked.get() == 1: 
        result=random.choice(tList)
        t1Res.configure(text=result)
    if t2Checked.get() == 1: 
        result=random.choice(tList)
        t2Res.configure(text=result)
    if t3Checked.get() == 1: 
        result=random.choice(tList)
        t3Res.configure(text=result)
    if chalChecked.get() == 1:
        result=random.choice(chalList)
        chalRes.configure(text=result)


def save():
    print("sims.txt has been saved")
    with open("sims.txt", "a") as f:
        f.write("\n" + "Relationship: " + str(relRes.cget("text")) + "\n" +
                "Children: " + str(kidRes.cget("text")) + "\n" +
                "Pets: " + str(petRes.cget("text")) + "\n" +
                "Career: " + str(carRes.cget("text")) + "\n" +
                "Aspiration: " + str(aspRes.cget("text")) + "\n" +
                "Trait 1: " + str(t1Res.cget("text")) + "\n" +
                "Trait 2: " + str(t2Res.cget("text")) + "\n" +
                "Trait 3: " + str(t3Res.cget("text")) + "\n" +
                "Challenge: " + str(chalRes.cget("text")) + "\n")
    
#buttons
                
blankLbl = Label(window, text="", bg="palegreen")
blankLbl.grid(column=0, row=10)

rollallBtn = Button(window, text="Roll All", font=("Arial", 14), bg="white",
                       fg="green",  command=clickall)
rollallBtn.grid(column=1, row=11, sticky=W)

rollslctBtn = Button(window, text="Roll Selected", font=("Arial", 14), bg="white",
                     fg="green", command=clickslct)
rollslctBtn.grid(column=0, row=11, stick=W)

saveBtn = Button(window, text="Save", font=("Arial", 14), bg="white",
                       fg="green", command=save)
saveBtn.grid(column=0, row=12, sticky=W)

resetBtn = Button(window, text="Reset", font=("Arial", 14), bg="white",
                       fg="green", command=reset)
resetBtn.grid(column=0, row=13, sticky=W)



window.mainloop()

