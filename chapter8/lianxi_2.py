def city_country(name, belong_to):
    information = '"' + name.title() + "," + " " + belong_to.title() + '"'
    return information

message = {"beijing" : "china", "tokyo" : "japan", "washington" : "usa"}

for name,belong_to in message.items():
    full_information = city_country(name, belong_to)
    print(full_information)