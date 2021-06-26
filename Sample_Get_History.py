import tzevaadom

# history data in: Hebrew, English, Russian, Arabic.
# history from: today, week, month.

history_hebrew = tzevaadom.alerts_history(language="he", get_from="month")
print(history_hebrew)

history_russian = tzevaadom.alerts_history(language="ru", get_from="week")
print(history_russian)

history_english = tzevaadom.alerts_history(language="en", get_from="today")
print(history_english)

history_arabic = tzevaadom.alerts_history(language="ar", get_from="week")
print(history_arabic)

history_english_date_range = tzevaadom.alerts_history(language=lang, get_from="dates",date_from="10.05.2021", date_to="21.05.2021")
print(history_english_date_range)
