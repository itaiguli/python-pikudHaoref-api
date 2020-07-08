import tzevaadom

def handler(List_Alerts):

  for alert in List_Alerts:
    
    ''' 
    data looks like this.. {
        "value":"אשקלון",
        "name":"אשקלון",
        "name_en":"Ashkelon",
        "name_ru":"Ашкелон",
        "name_ar":"أشكلون",
        "zone":"מערב לכיש",
        "zone_en":"Western Lakhish",
        "zone_ru":"запад Лахиш",
        "zone_ar":"الغربي لاخيش",
        "countdown":30,
        "time":"30 שניות",
        "time_en":"30 Seconds",
        "time_ru":"30 секунд",
        "time_ar":"30 ثانية",
        "lat":31.6688,
        "lng":34.5743
    }
   '''
    
    message_english = "New Alarm: " + alert["name_en"] + ". Zone: " + alert["zone_en"]
    print(message_english) # New Alarm: {CityName_english}. Zone: {ZoneName_english}

    
    
''' start monitor api '''
tzevaadom.alerts_listener(handler) # listening to alerts in background (Thread)
