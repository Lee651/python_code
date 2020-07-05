def make_albue(singer_name, albue_name, sings_num=" "):
    message = {"singer" : singer_name.title(), "albue" : albue_name.title(), "num" : sings_num}
    return message

singers_information = {"zhou jielun" : "Qi Li Xiang",
    "lin junjie" : "Jiang Nan",
    "xu song" : "Hui Se Tou Xiang",
    }

for name,song in singers_information.items():
    full_information = make_albue(name,song)
    print(full_information)
#full_information = make_albue("zhou jielun", "qi li xiang",)

#print(full_information)

 