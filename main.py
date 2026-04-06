from pyscript import document



class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return (
            "Hi! I am " + self.name +
            " from " + self.section +
            ". My favorite subject is " +
            self.favorite_subject + "."
        )



classmates = [
    Classmate("Vito De Guzman", "10 Sapphire", "Break time"),
    Classmate("Seth Ngo", "10 Sapphire", "Social Studies"),
    Classmate("Benigno Rivera", "10 Sapphire", "Science"),
    Classmate("Ishan Shrestha", "10 Sapphire", "Social Studies"),
    Classmate("Manuel Mergal", "10 Sapphire", "Mathematics"),
]



def show_list(event=None):
    output = document.getElementById("output")
    output.innerHTML = ""

    for cm in classmates:
        card = document.createElement("div")
        card.className = "classmate-card"
        card.innerHTML = cm.introduce()
        output.appendChild(card)



def add_classmate(event=None):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    if name == "" or section == "" or subject == "":
        document.getElementById("output").innerHTML = "<p>Please fill in all fields.</p>"
        return

    new_classmate = Classmate(name, section, subject)
    classmates.append(new_classmate)


    document.getElementById("name").value = ""
    document.getElementById("section").value = ""
    document.getElementById("subject").value = ""

    show_list()



import js
js.show_list = show_list
js.add_classmate = add_classmate



show_list()