from twilio.rest import Client
from datetime import datetime, timedelta
import os
import json

# Twilio Credentials (Replace with your actual credentials)
account_sid = os.getenv("TWILIO_ACCOUNT_SID") # Get this from Twilio Dashboard
auth_token = os.getenv("TWILIO_AUTH_TOKEN")   # Get this from Twilio Dashboard
harish = os.getenv("HARISH_NUMBER")   # your whatsapp number
sachin = os.getenv("SACHIN_NUMBER")   # Your whatsapp Number
client = Client(account_sid, auth_token)
twilio_whatsapp = os.getenv("TWILIO_PHONE_NUMBER")   # Twilio Sandbox Number
# Birthday List

birthdays_json = os.getenv("BIRTHDAYS")
anniversaries_json = os.getenv("ANNIVERASARIES")
anniversaries = json.loads(anniversaries_json)
birthdays = json.loads(birthdays_json)
#print(birthdays)
# Your WhatsApp number and Twilio sandbox number
      # E.g., whatsapp:+1234567890
  # Twilio Sandbox Number

# Get today's date

today = datetime.now()
today_str = today.strftime("%m-%d")
tomorrow_str = (today + timedelta(days=1)).strftime("%m-%d")

# # Check for birthdays and send reminder
for name, bday in birthdays.items():
    # reminder = datetime.strptime(bday, "%m-%d")
    if today_str == bday:
        message = client.messages.create(
            body=f"🎉 Reminder: It's {name}'s birthday today! Don't forget to wish them! 🎂",
            from_=twilio_whatsapp,
            to=sachin
        )
        message = client.messages.create(
        body=f"🎉 Reminder: It's {name}'s birthday today! Don't forget to wish them! 🎂",
        from_=twilio_whatsapp,
        to=harish
        )
        print(f"Reminder sent for {name}'s birthday!")
    elif tomorrow_str == bday:
        # Send Reminder for Upcoming Birthday
        message = client.messages.create(
            body=f"⏰ Reminder: {name}'s birthday is tomorrow! 🎉 Don't forget to prepare your wishes or a surprise! 🎁",
            from_=twilio_whatsapp,
            to=harish)
        message = client.messages.create(
            body=f"⏰ Reminder: {name}'s birthday is tomorrow! 🎉 Don't forget to prepare your wishes or a surprise! 🎁",
            from_=twilio_whatsapp,
            to=sachin)
    else:
        print(f"No birthday or anniversary today or tomorrow!")

for name, anni_date in anniversaries.items():
    if today_str == anni_date:
        message = client.messages.create(
            body=f"🎉 Reminder: It's {name}'s anniversary today! Don't forget to wish them! 🎂",
            from_=twilio_whatsapp,
            to=harish
        )
        message = client.messages.create(
            body=f"🎉 Reminder: It's {name}'s anniversary today! Don't forget to wish them! 🎂",
            from_=twilio_whatsapp,
            to=sachin
        )
        print(f"Reminder sent for {name}'s Anniversary!")

    elif tomorrow_str == anni_date:
        # Send Reminder for Upcoming Anniversary
        message = client.messages.create(
            body=f"⏰ Reminder: {name}'s Anniversary is tomorrow! 🎉 Don't forget to prepare your wishes or a surprise! 🎁",
            from_=twilio_whatsapp,
            to=harish
        )
        print(f"Reminder message sent for {name}'s Anniversary!")
        message = client.messages.create(
            body=f"⏰ Reminder: {name}'s Anniversary is tomorrow! 🎉 Don't forget to prepare your wishes or a surprise! 🎁",
            from_=twilio_whatsapp,
            to=sachin
        )
        print(f"Reminder message sent for {name}'s Anniversary!")
    else:
        print(f"No birthday or anniversary today or tomorrow!")

