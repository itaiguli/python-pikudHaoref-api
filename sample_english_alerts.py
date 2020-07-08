import tzevaadom

def handler(List_Alerts):

  for alert in List_Alerts:
    message_english = "New Alarm: " + alert["name_en"] + ". Zone: " + alert["zone_en"]
    print(message_english) # New Alarm: {CityName_english}. Zone: {ZoneName_english}
    
''' start monitor api '''
tzevaadom.alerts_listener(handler) # listening to alerts in background (Thread)
