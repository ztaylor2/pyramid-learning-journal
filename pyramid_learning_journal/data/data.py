ENTRIES = [
    {
        "id": 12,
        "title": "Day 12",
        "creation_date": "this.date", 
        "body": "Today we learned about a binary heap. I thought that it was pretty cool trying to implement it with a list. Mapping the parent and child nodes together by their index was pretty cool. It would be interesting to compare that way with just creating nodes for each. We also learned about .jenja2 files which allow us to put variables into our html. I can see how this will come in very handy for templating.",
    },
    {
        "id": 11,
        "title": "Day 11",
        "creation_date": "this.date", 
        "body": "Yesterday we built out a pyramid app and then deployed it to heroku. It was a full day accomplishing all of this. The power of cookiecutter is pretty amazing. I would love to learn how to write software that writes software. The intricacies that went into all of the setup files for heroku was pretty astounding. There were a lot of nitty gritty details all over the place, and if you screw up one of them you'll be in a world of hurt. I definitely think that I need to solidify my knowledge and understanding on those details in the coming days. I'm not sure how I would have been able to do that without the codefellows notes, which makes me a little nervous.",
    },
    {
        "id": 10,
        "title": "Day 10",
        "creation_date": "this.date", 
        "body": "Today we learned about the pyramid python framework.  It feels like there is a lot going on with this framework, but it's also just the first day.  It's pretty awesome how a framwork will just build out an entire server for you.  I guess that makes the backend engineer's job a lot easier.  Routing is pretty cool, very interesting how you can load different html files in different places.",
    },
    {
        "id": 9,
        "title": "Day 9",
        "creation_date": "this.date", 
        "body": "Today we learned about queues which are a simple first in first out data structure. You can add a value to the front of the queue with an 'enqueue' method. You can get a value off of the back of the queue with a dequeue method. It is very reminiscent of people standing in line at a supermarket, things come in the front then leave out the back. We also learned about concurrency, which is when more than one process occurs at a single time. Basically, blocking operations stop the program at some point, and we don't want that to happen so we have ways of avoiding blocking by using various concurrent methods.",
    },
    {
        "id": 8,
        "title": "Day 8",
        "creation_date": "this.date", 
        "body": "Today we learned more about decoding and encoding and the difference between python2 and 3. Python2 has byte strings as default while python3 has unicode strings as default. Unicode strings are important because many people, especially outside of the US have unicode letters in their names and languages, so python3 implemented it into the language. It's important to us because to send strings between servers/sockets they have to be byte strings. This makes it important to encode the strings to byte strings before you send them, then decode them into unicode strings when you receive them. We also learned about doubly linked lists which are linked lists with pointers going both ways and a tail node. Lastly we learned about superclasses and how to give objects properties from other objects.",
    },
    {
        "id": 7,
        "title": "Day 7",
        "creation_date": "this.date", 
        "body": "Today I learned about HTTP methods such as GET, POST, PUT and REQUEST. The only safe method, or method that doesn't modify anything server side, is the GET method. We also learned about status codes that return when an HTTP request is made to a server. We even built our own status code during project work. Things that I could use a better understanding of include unicode and byte strings, and anscii characters.",
    },
    {
        "id": 6,
        "title": "Day 6",
        "creation_date": "this.date", 
        "body": "Today I learned about sockets, and how to build a basic server. We moved pretty quickly through the lesson and I'll have to do some more reading about it. Right now my basic understanding is that sockets are things that send and receive data between programs. They sound like an essential part of server development and I look forward to learning more about them.",
    },
    {
        "id": 5,
        "title": "Day 5",
        "creation_date": "this.date", 
        "body": "Today I learned about a few things that work in python 3 but not 3. For example import statistics does not work in python 2. I also got better at systematically thinking through problems because of all of the katas that were required. Lastly, I learned that I have a lot to learn in the coming weeks.",
    },
    {
        "id": 4,
        "title": "Day 4",
        "creation_date": "this.date", 
        "body": "Today I learned about how to use tox, a tool that allows us to run a python program in both py 2.7 and 3.6. I thought that it was an awesome extremely powerful tool. Today I also wrote my first test before writing software which was a pretty interesting experience. It'll definitely take some getting used to but I can see how TDD could be a great way to write software.",
    },
    {
        "id": 3,
        "title": "Day 3",
        "creation_date": "this.date", 
        "body": "Today I learned a lot of python. One of the most interesting things I learned today was that a dictionary was a hash map. I was wondering what it was. I look forward to finding out what kind of list a list is. I'd guess an array-list (doubles in length if filled). Today I also used the open and read commands for the first time. It was cool seeing how you can open a file in python then manipulate its contents. It definitely sheds some light on how parsing tools work. Look forward to doing more parsing.",
    },
    {
        "id": 2,
        "title": "Day 2",
        "creation_date": "this.date", 
        "body": "Today I learned about test driven development. It'll be an interesting philosophy to adopt because everything I've done so far has involved zero testing. I can definitely see how it will facilitate better software development and I'm interested to see how I like it in the future. Another thing I tried to learn today was how to use a requirements.txt file. I could use some more practice with that.",
    },
    {
        "id": 1,
        "title": "Day 1",
        "creation_date": "this.date", 
        "body": "Today I learned about python environments. Environments are a way to separate which python packages you should use for a project. This way if you happen to update some global package but don't want that to break a project of yours your project should be protected by the env. Additionally you only have to install the packages that the project requires. It took me a second to wrap my head around this but I understand it now.",
    },
]