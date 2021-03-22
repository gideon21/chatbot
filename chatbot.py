from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot import filters

 


chatbot = ChatBot(
    'Geo',
    filters=[filters.get_recent_repeated_responses],
    preprocessors=['chatterbot.preprocessors.clean_whitespace'],
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "I do not understand! please try again or try (Help)",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            'maximum_similarity_threshold': 0.90
        }
    ]
    
)

trainer = ListTrainer(chatbot)

# Courses
trainer.train([
	"Courses",
    "Search for courses here https://www.uclan.ac.uk/course",
])
trainer.train([
	"Courses at uclan",
    "Search for courses here https://www.uclan.ac.uk/courses",
])

# Booking equipments
trainer.train([
	"booking",
    "A number of facilities can be booked using the Student Web Room Booking page https://www.uclan.ac.uk/students/support/room_booking.php",
])
trainer.train([
	"Booking",
    "A number of facilities can be booked using the Student Web Room Booking page https://www.uclan.ac.uk/students/support/room_booking.php",
])
trainer.train([
	"What can i book",
    "Laboratories, Workshops, Studios and other Specialist Spaces at https://www.uclan.ac.uk/students/support/room_booking.php",
])

# Facilities
trainer.train([
	"Facilities",
    "3D Scanning, 3D Workshop, Advertising Studio, Aerospace Workshop, Animation Studios, Architectural Design studios, Civil Engineering Laborataties and more, please visit https://www.uclan.ac.uk/facilities",
])
trainer.train([
	"Available facilities at uclan",
    "3D Scanning, 3D Workshop, Advertising Studio, Aerospace Workshop, Animation Studios, Architectural Design studios, Civil Engineering Laborataties and more, please visit https://www.uclan.ac.uk/facilities",
])
trainer.train([
	"Available facilities",
    "3D Scanning, 3D Workshop, Advertising Studio, Aerospace Workshop, Animation Studios, Architectural Design studios, Civil Engineering Laborataties and more, please visit https://www.uclan.ac.uk/facilities",
])

# Gym
trainer.train([
	"Gym",
    "Sir Tom Finney Sports Centre, from Mon-Fri: 7-30am-10pm and Sat-Sun: 10am-5pm",
])
trainer.train([
	"Where is the gym located",
    "Sir Tom Finney Sports Centre at PR1 2HE",
])
trainer.train([
	"Where can i find the gym",
    "University of Central Lancashire, Preston PR1 2HE",
])
trainer.train([
	"What time is the gym opened at",
    "Term time Mon-Fri: 7-30am-10pm and Sat-Sun: 10am-5pm",
])


# Library
trainer.train([
	"Library",
    "52 St Peter's Square, Preston PR1 2HE, from Mon-Sun: 8am-8pm",
])
trainer.train([
	"Whats in the library",
    "Library Drop in Zone, Study Spaces, The i, Uclan print service, Computers, Printers and more",
])
trainer.train([
	"Whats available at the library",
    "Library Drop in Zone, Study Spaces, The i, Uclan print services, Computers and more",
])
trainer.train([
	"Where is the library",
    "52 St Peter's Square, Preston PR1 2HE",
])
trainer.train([
	"At what time is the library opened",
    "Mon-Sun: 8am-8pm",
])

# Student union
trainer.train([
	"Student union",
    "Fylde Rd, Preston PR1 2TQ, from Mon-Fri: 9am-5pm, sat-sun: closed",
])
trainer.train([
	"Where can i find the student union",
    "Student union is located at Fylde Rd, Preston PR1 2TQ",
])
trainer.train([
	"Where is the student union",
    "Fylde Rd, Preston PR1 2TQ",
])
trainer.train([
	"What can i do at the student union",
    "Check whats on at https://www.uclansu.co.uk/whatson/",
])
trainer.train([
	"Student union shop",
    "https://uclan.personalised.clothing/Myshop.aspx",
])
trainer.train([
	"What time does the student union open at",
    "Mon-Fri: 9am-5pm, sat-sun: closed",
])
trainer.train([
	"How to join Societies",
    "Join Societies at https://www.uclansu.co.uk/get_involved/societies/join/",
])

#Greetings
trainer.train([
	"Hi",
    "Nice to meet you",
])
trainer.train([
	"Hello",
    "Howdy!",
])

#Gestures
trainer.train([
	"Thank you",
    "Your welcome!",
])
trainer.train([
	"Thanks",
    "Your welcome!",
])
trainer.train([
	"Bye",
    "Bye! see you soon",
])

#Support
trainer.train([
	"Help",
    "Make sure your spelling is correct or type in single word mentioned above",
])
trainer.train([
	"Contact",
    "For general enquiries please conatct us here https://www.uclan.ac.uk/contact/general-enquiries",
])
