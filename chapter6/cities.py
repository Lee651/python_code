cities = {
    "beijing" : {
        "attributes" : "China",
        "peoples" : "14yi",
        "central city" : "WuHan",
        },
    
    "paris" : {
        "attributes" : "France",
        "peoples" : "2yi",
        "central city" : "Marseille"
        },

    "washington" : {
        "attributes" : "USA",
        "peoples" : "3yi",
        "central city" : "New York"
        },
    }

for city,message in cities.items():
   print("\n" + city.title() + ":")
   for information,xinxi in message.items():
       print(information + ":" + " " + xinxi)
  
