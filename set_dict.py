# Set and dictionary

my_favourite_song = {}

keys = [Artist,FullName,Genre,Title,DurationInSeconds,Viewers,
,YearReleased,Occupation,Height,Awards,Age,Labels,website,Instrument)
       ]
values = ["Burna boy","Damini Ebunoluwa","Afri hip hop","Gbona",4.95,33000000,
"sept. 27, 2018","Singer, Songwriter","1.85m","Best international Act"
,"28years","Spaceship bad habit","onaspaceship.com","Vocals"]

# Dictionaries and Sets

# Refactor code so all the variables are held as dictionary keys and value. 

keys = ["Artist","FullName","Genre","Title","DurationInSeconds","Viewers","YearReleased",
"Occupation","Height","Awards","Age","Labels","website","Instrument"]

values = ["Burna boy","Damini Ebunoluwa","Afri hip hop","Gbona",4.95,33000000,
"sept. 27, 2018","Singer & Songwriter","1.85m","Best international Act",
"28years","Spaceship bad habit","onaspaceship.com","Vocals"]

# my keys and values should be changed to tuples.

my_favourite_song = {}

my_favourite_song = {k: v for k, v in zip(keys, values)}
print(my_favourite_song)

# the syntax for this excercise
my_dictionary = {}
my_dictionary = {k: v for k, v in zip(keys, values)}
print(my_dictionary)


# Refactor print statement so that it's a single loop that passes through each item in the dictionary 

my_favourite_song = { "Artist": "Burna boy","FullName": "Damini Ebunoluwa","Genre": "Afri hip hop","Title": "Gbona", 
                      "DurationInSeconds": 4.95,"Viewers": 33000000,"YearReleased": "sept. 27, 2018",
                       "Occupation": "Singer & Songwriter","Height": "1.85m","Awards": "Best international Act","Age": "28years",
                       "Labels": "Spaceship bad habit","website": "onaspaceship.com","Instrument": "Vocals"}

for key in my_favourite_song:
 	print(keys, '->', my_favourite_song[keys])



