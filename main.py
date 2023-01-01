from ip_location import IPLocation


def main():
    user_input = input("Enter an IP address: ")
    ip_locator = IPLocation('GeoLite2-City.mmdb')
    ip_locator.get_location(user_input)


if __name__ == "__main__":
    main()
