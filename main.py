import requests
from datetime import date

def GetDate():  # Get Current Date
    day = date.today()
    day = day.strftime('%d-%m-%y')
    day = day.split('-21')
    day = day[0] + '-2021'

    return day

PINCODE = 301001
DATE = GetDate()
print(DATE)
URL = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={PINCODE}&date={DATE}'

def main():
    response = requests.get(URL)
    data = response.json()

    if len(data['centers']) == 0:
        print("No Vaccination Centres Found")
        return
    
    else:
        print("Found Vaccination Centre")

main()