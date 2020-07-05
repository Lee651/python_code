favorite_language = {
    "jen":["python","ruby"],
    "sarah":"c",
    "bob":["java","c#"],
    "tom":["c++","php"],
    }

for name,languages in favorite_language.items():
    if len(languages) ==2:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print(language.title())
    else :
        print(name.title() + "'s favorite language is:")
        for language in languages:
            print(language.title())