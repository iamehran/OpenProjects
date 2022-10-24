import socket
from ip2geotools.databases.noncommercial import DbIpCity
url = input("Enter the Website URL: ")
ip = socket.gethostbyname(url)
response = DbIpCity.get(ip,api_key  = 'free')
print("IP:",ip)
print("City:",response.city)
print("Region:",response.region)
print("Country:",response.country)