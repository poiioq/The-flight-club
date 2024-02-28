#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint
import datetime

data_manager= DataManager()
sheet_data= data_manager.get_data()
search= FlightSearch()
notification_manager= NotificationManager()
# pprint(sheet_data)

for record in sheet_data:
    if record['iataCode'] == '':
        record['iataCode']= search.city_code(record['city'])
        new_data = {'price': {'iataCode': record['iataCode']}}
        data_manager.put_data(record['id'], new_data)

original_city_IATA= "LON"
from_date = datetime.datetime.now()
to_date = from_date + datetime.timedelta(days=180)

for record in sheet_data:
    flight= search.search_flight(
        original_city_IATA,
        record['iataCode'],
        from_date,
        to_date
    )
    if flight is None:
        continue
    if flight.price < record["lowestPrice"]:
        message = f"Low price alert! Only £{flight.price} to fly from " \
                  f"{flight.origin_city}-{flight.origin_airport} to " \
                  f"{flight.destination_city}-{flight.destination_airport}, " \
                  f"from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs != 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        emails = data_manager.get_emails()
        notification_manager.send_email(emails, message)








