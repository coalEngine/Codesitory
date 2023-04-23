dict  = {"name": "Bob", "ref": "Python", "sys": "Win"}
print("Dictionary:", dict)
print("\nReferance:", dict["ref"])
print("\nKeys:", dict.keys())

del dict["name"]
dict['user'] = "Tom"
print('\nDictionary:', dict)
print("\nIs there a \"Name\" key?:", 'name' in dict)
