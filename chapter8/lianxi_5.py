def show_magicians(magicians_name):
    for magicians in magicians_name:
        print(magicians)


def make_great(magician_names, new_magician_names):
    for magician_name in magician_names:
        new_magician_names.append(magician_name + " the Great")

names = ["A", "B", "C", "D"]
show_magicians(names)

new_names = []
make_great(names[:], new_names[:])
show_magicians(new_magician_names)