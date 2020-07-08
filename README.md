# python-pikudHaoref-api
A Python library for Pikud Haoref's unofficial rocket alert API.

# Getting rocket alerts data - in Real time
With the library you can listen to the new alerts.

The data comes from the library in the following format:
```json
[{
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
}]
```

With the library you can:
  - Listen to new rocket alerts, and get the Data into your `Alerts_Handler` function.
  - You can choose to receive only alerts from certain cities !
  - Get the latest alerts history, with time filtering and different languages.

tzevaadom is open source with a [public repository](https://github.com/itaiguli/python-pikudHaoref-api/) on GitHub.

### Installation

Install `tzevaadom` from PIP.

```sh
$ pip install tzevaadom
```

The library doesn't require installing any additional PIP package.

### Examples


```python
import tzevaadom

def handler(List_Alerts):
  for alert in List_Alerts:
    
    message = "New Alarm: " + alert["name_en"] + ". Zone: " + alert["zone_en"]
    print(message)

    
    
''' start monitor api '''
tzevaadom.alerts_listener(handler) # listening to alerts in background (Thread)
```


Filter and get alerts, only from certain cities.

```python
tzevaadom.alerts_listener(handler, ["אשקלון","נחל עוז"])  # You will receive alerts, only if it was in `אשקלון` or `נחל עוז`.
```
