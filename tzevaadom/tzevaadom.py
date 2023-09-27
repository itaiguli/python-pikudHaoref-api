import requests
import time
import json
import threading
import os

def alerts_listener(callback, alerts_only_for_cities=[]):
  return __main__(callback, alerts_only_for_cities)

folder = os.path.dirname(os.path.realpath(__file__))
with open(folder+'/cities.json', encoding='utf-8-sig') as cities_json:
    cities = cities_json.read()
    cities = json.loads(cities)

def alerts_history(language="he", get_from="today"):
  options_languages = ["he","en","ru","ar"]
  options_date = ["today", "week", "month"]

  if language not in options_languages:
    return SyntaxError(language+" option is not exists. only: he/en/ru/ar")
  
  if get_from not in options_date:
    return SyntaxError(get_from + " is not exists. only: today/week/month")

  return requests.get("https://www.oref.org.il/Shared/Ajax/GetAlarmsHistory.aspx?lang={}&mode={}".format(language, options_date.index(get_from)+1)).json()

def __format_alerts__(alert_areas):
  format_list = []
  for i in cities:
    if i["value"] in alert_areas:
      format_list.append(i)
      alert_areas.remove(i["value"])
  
  for area in alert_areas:
    format_list.append({"value":area,"name":area,"name_en":area,"name_ru":area,"name_ar":area,"zone":area,"zone_en":area,"zone_ru":area,"zone_ar":area,"countdown":0,"time":"","time_en":"","time_ru":"","time_ar":"","lat":0,"lng":0})
  return format_list

class __main__:
  def __init__(self, callback, alerts_only_for_cities):
    self.callback = callback
    self.filter = alerts_only_for_cities
    self.running = True
    self.last_data = []
    self.thread = threading.Thread(target=self.__listener__)
    self.thread.start()

  def stop(self):
    self.running = False

  def __listener__(self):
    while self.running:
      try:
        time.sleep(2) # important to not crash
        response = requests.get("https://www.oref.org.il/WarningMessages/alert/alerts.json", headers={"X-Requested-With":"XMLHttpRequest","Referer":"https://www.oref.org.il/"})
        if len(response.content) > 5 and response.status_code == 200:
          list_oref = json.loads((response.content).decode('utf8'))["data"]
          filtered_areas = list({area for (area) in (list_oref) if (area not in self.last_data) and (self.filter == [] or (area) in self.filter) or (list_oref.count(area) > 1 and self.last_data.count(area) == 1)})
          filtered_areas.sort()
          self.last_data = list(list_oref)
          if len(filtered_areas) == 0:
            continue
          threading.Thread(target=self.callback, args=(__format_alerts__(filtered_areas),)).start()
        elif response.content != "" and self.last_data != []:
          self.last_data = []
      except:
        pass
