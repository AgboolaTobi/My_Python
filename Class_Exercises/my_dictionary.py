my_dictionary = {
    "model": "Toyota",
    "year": "2022",
    "Owner": "Mr Agboola Tobi Samuel"
}

# print(my_dictionary.update({"color": "black"}))
# print(my_dictionary)

this_dictionary = {
    "child1": {"names": "[Agboola, tobi, samuel]",
               "age": "35",
               "status": "married"},
    "child2": "agboola Oluwatoyin",
    "child3": {"name": "agboola Oyenike",
               "age": "33",
               "sex": "female",
               "status": "married"}

        }

# .items() is a dictionary method that gives a tuple of key and the value
this_dictionary.items()

for k, v in this_dictionary.items():
    print(this_dictionary)
# print(this_dictionary.items())
# print(this_dictionary["child1"]["names"])
this_dictionary.update({'L': 50, 'XL': 40})
this_dictionary.update(C=100, D=500)
