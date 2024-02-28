import requests

SHEET_USERS_ENDPOINT= "https://api.sheety.co/ab29cbf168dedc0b5e71751848bb462b/flightDealsEvelyn/users"
TOKEN = "jhkhjkluhjj989hjghjxj"
headers = {"Authorization":f"Bearer {TOKEN}"}

print("Welcome to Bian's club!\nWe will find the best flight for you!")
first_name= input("What's your first name?\n")
last_name= input("What's your last name?\n")
email= input("What's your emial?\n")
email_1= input("Type your email agian.\n")

post_config= {
  "First Name": first_name,
  "Last Name":last_name,
  "Email":email
}
response= requests.post(url=SHEET_USERS_ENDPOINT, json=post_config, headers=headers)
response.raise_for_status()