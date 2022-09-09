import requests

from threading import Thread

class Enumerator():
    def __init__(self) -> None:
        self.threads = []
        self.codes = [200, 201, 202, 204, 301, 302, 303, 307, 308, 403]

    def enumerate(self, url, timeout):
        t = Thread(target=self.__enum, args=(url, timeout))
        t.start()
        t.join()

    def __enum(self, url, timeout):
        try:
            isValidCode = False

            r = requests.get(url, timeout=timeout)            
            
            for code in self.codes:
                if(r.status_code == code):
                    isValidCode = True
                    break

            if(isValidCode):
                print("Target: " + url + " - Code: " + str(r.status_code))
        except requests.ConnectionError:
            pass