# Simple script with plain text passwords stored in the script to connect to 
# cisco nexus device using netmiko


from netmiko import ConnectHandler
import json

username = ""
password = ""

nx_os = {
    'device_type': 'cisco_ios',
    'ip': 'sbx-nxos-mgmt.cisco.com',
    'username': username,
    'password': password,
    'port': 8181
}

connection = ConnectHandler(**nx_os)
output = connection.send_command('show ip int brief | json-pretty')
json_readable = json.loads(output)
number_of_ints = len(json_readable["TABLE_intf"]["ROW_intf"])

for x in range(number_of_ints):
    print(json_readable["TABLE_intf"]["ROW_intf"][0]["intf-name"])
    print(json_readable["TABLE_intf"]["ROW_intf"][0]["prefix"])
    print(json_readable["TABLE_intf"]["ROW_intf"][0]["proto-state"])
    print("")

