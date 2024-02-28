import requests
SHEETY_PRICES_ENDPOINT= "https://api.sheety.co/ab29cbf168dedc0b5e71751848bb462b/flightDealsEvelyn/prices"
SHEETY_CUSTOMERS_ENDPOINT= "https://api.sheety.co/ab29cbf168dedc0b5e71751848bb462b/flightDealsEvelyn/users"
TOKEN = "jhkhjkluhjj989hjghjxj"
headers = {"Authorization":f"Bearer {TOKEN}"}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data= {}

    def get_data(self):
        response= requests.get(SHEETY_PRICES_ENDPOINT, headers=headers)
        self.destination_data= response.json()['prices']
        return self.destination_data

    def put_data(self, id, new_data):
        response= requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{id}", json=new_data, headers=headers)

    def get_emails(self):
        response = requests.get(SHEETY_CUSTOMERS_ENDPOINT, headers=headers)
        response.raise_for_status()
        data = response.json()['users']
        emails = [user['email'] for user in data]
        return emails

