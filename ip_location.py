import geoip2.database


class IPLocation:
    def __init__(self, database_path):
        self.reader = geoip2.database.Reader(database_path)

    def get_location(self, ip_address):
        response = self.reader.city(ip_address)
        print(f"Country: {response.country.name}")
        print(f"City: {response.city.name}")