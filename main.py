""" import streamlit as st
import pandas as pd
import time

st.title('Ralfs Comeback')

st.write('This is a simple example of a Streamlit app.')

st.write('You can easily add interactivity to your app by using Streamlit widgets.')

countdown_days = 20

st.write(f"Countdown: {countdown_days} days")

if st.button("Another day started"):
    countdown_days -= 1
    st.write(f"Countdown: {countdown_days} days") """


import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

# Titel der App
st.title("Ralfs Comeback")

# Benutzer wählt ein Ziel-Datum
target_date = datetime.strptime("18.12.2025", "%d.%m.%Y").date()
#st.date_input("Wähle das Ziel-Datum:", value=datetime.now().date())

# Zielzeit auf Mitternacht setzen
target_datetime = datetime.combine(target_date, datetime.min.time())
current_time = datetime.now()

# Berechnung der verbleibenden Zeit
remaining_time = target_datetime - current_time


# Zeitanzeige
while remaining_time.total_seconds() > 0:
    # Aktuelles Datum und Zeit
    current_time = datetime.now()
    # Berechnung der verbleibenden Zeit
    remaining_time = target_datetime - current_time
    
    # Zeitanzeige
    st.header("Verbleibende Zeit:")
    days = remaining_time.days
    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    st.subheader(f"{days} Tage, {hours} Stunden, {minutes} Minuten, {seconds} Sekunden")
    
    time.sleep(1)


st.subheader("Das war's! 🎉")



# # Optional: Benutzerdefinierte Nachricht
# message = st.text_input("Gib eine Nachricht ein, die bei Ablauf des Countdowns angezeigt werden soll:", "🎉 Countdown abgeschlossen!")
# if remaining_time.total_seconds() <= 0:
#     st.write(message)
