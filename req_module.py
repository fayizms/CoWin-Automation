import requests
from datetime import date

def GetDate():  # Get Current Date
    day = date.today()
    day = day.strftime('%d-%m-%y')
    day = day.split('-21')
    day = day[0] + '-2021'

    return day

PIN = 30100
DATE = GetDate()

def main(pin, date):
    URL = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pin}&date={date}'
    
    response = requests.get(URL)
    data = response.json()

    if len(data['centers']) == 0:
        return None
    
    else:
        return data

main()