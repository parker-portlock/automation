
#host = input("Hostname/IP: ")
#username = input("Username: ")
#password = input("Password: ")

from napalm import get_network_driver
driver = get_network_driver("asa")
device = driver(hostname="10.78.50.7", username="net_pportlock", password="[p3anutbutt3r!]", optional_args = {'port': 443})
device.open()
facts = device.get_facts()
print (facts)
device.close()