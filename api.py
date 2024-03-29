class PIN:
    def __init__(self, PIN=695615):
        from datetime import date
        # import urllib3, certifi

        self.PIN = PIN
        self.DATE = self.GetDate(date)
        self.URL = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={self.PIN}&date={self.DATE}'
        # self.http = urllib3.PoolManager(ca_certs=certifi.where())

    def GetDate(self, date) : return date.today().strftime('%d-%m-%y').split('-21')[0] + '-2021'
    def GetWeek(self) : pass

    def Data(self):
        # import json
        import requests

        # sessions = self.http.request('GET', self.URL).data.decode('utf-8')
        sessions = requests.get(self.URL)
        return sessions.json()

class DIST:
    def __init__(self, PIN=695615):
        # import urllib3, certifi
        from datetime import date

        self.DIST = DIST
        self.DATE = self.GetDate(date)
        self.URL = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={self.PIN}&date={self.DATE}'
        # self.http = urllib3.PoolManager(ca_certs=certifi.where())

    def GetDate(self, date) : return date.today().strftime('%d-%m-%y').split('-21')[0] + '-2021'
    def GetWeek(self) : pass

    def Data(self):
        # import json
        import requests

        # sessions = self.http.request('GET', self.URL).data.decode('utf-8')
        sessions = requests.get(self.URL)
        return sessions.json()