def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

name = {"xiangfei" : "ai",
   "zhangwei" : "li",
    "yawen" : "shu",
    }

for F,L in name.items():
    musician = get_formatted_name(F,L)
    print(musician)