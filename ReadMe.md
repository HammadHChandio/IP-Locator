# IP Location Lookup 🔍

This program allows you to look up the location (country and city) of an IP address using the GeoLite2 City database from MaxMind.

## Installation

To install the required dependencies, run the following command:

```
pip install geoip2
```

You will also need to download the GeoLite2 City database from MaxMind (https://www.maxmind.com/en/geolite2/signup) and save it as `GeoLite2-City.mmdb` in the same directory as the Python script.

## Usage

To use the program, run the following command and pass it an IP address as an argument:

```
python ip_location.py 8.8.8.8
```


The program will print the country and city associated with the IP address to the console.

## Class Reference

The program contains a single class, `IPLocation`, with the following methods:

### `__init__(self, database_path)`

Initializes the `IPLocation` object with the path to the GeoLite2 City database.

### `get_location(self, ip_address)`

Looks up the location (country and city) of the specified IP address.

## License

This program is licensed under the MIT License.
