#!/usr/bin/python
import routeros_api

connection = routeros_api.RouterOsApiPool('IP', username='admin', password='superpassword' ,plaintext_login=True)
api = connection.get_api()
# Obtener información de la versión del router
system_resource = api.get_resource('/system/resource')
version = system_resource.get()[0]['version']
print(f"RouterOS version: {version}")

# Obtener información de la configuración de la interfaz
interfaces = api.get_resource('/interface')
print("\nInterfaces:")
for interface in interfaces.get():
    print(f"Name: {interface['name']}, Download: {round(int(interface['tx-byte'])/1024/1024)}MB , Upload: {round(int(interface['rx-byte'])/1024/1024)}MB")
    if 'mac-address' in interface:
        print(f"MAC address: {interface['mac-address']}")
    else:
        print("None")

# Obtener información de la configuración de la red
ip_addresses = api.get_resource('/ip/address')
print("\nIP addresses:")
for ip_address in ip_addresses.get():
    print(f"Address: {ip_address['address']}, Interface: {ip_address['interface']}")

# Obtener información de la tabla de rutas
routes = api.get_resource('/ip/route')
print("\nRoutes:")
for route in routes.get():
    if route['dst-address'] == '0.0.0.0/0': 
        print(f"Gateway: {route['gateway']}, Inactive:{route['inactive']}, Active:{route['active']}")#, Interface: {route['interface']}")
    elif 'via' in route:
        print(f"Destination: {route['dst-address']}, Gateway: {route['gateway']} , Inactive:{route['inactive']}, Active:{route['active']})#, Interface: {route['interface']}")
    elif 'connect' in route:
        print(f"Destination: {route['dst-address']}, Inactive:{route['inactive']}, Active:{route['active']} , Connect:{route['connect']}")  # , Interface: {route['interface']}")
    else:
        print(f"Destination: {route['dst-address']}, Inactive:{route['inactive']}, Active:{route['active']}")#, Interface: {route['interface']}")

# Obtener información de las reglas de firewall
firewall_rules = api.get_resource('/ip/firewall/filter')
if firewall_rules.get() == []:
    print("\nFirewall rules: None")
else:
    print("\nFirewall rules:")
    for rule in firewall_rules.get():
        print(f"Chain: {rule['chain']}, Protocol: {rule['protocol']}, Source address: {rule['src-address']}, Destination address: {rule['dst-address']}")

# Obtener información de las colas de tráfico
queues = api.get_resource('/queue/simple')
print("\nTraffic queues:")
for queue in queues.get():
    #print(queue)
    print(f"Name: {queue['name']}, Target address: {queue['target']}, Max limit: {queue['max-limit']}")

# Obtener información de los clientes PPPoE
pppoe_clients = api.get_resource('/ppp/active')
if pppoe_clients.get() == []:
    print("\nPPPoE clients: None")
else:
    print("\nPPPoE clients:")
    for client in pppoe_clients.get():
        print(client)
    #print(f"Name: {client['name']}, Address: {client['address']}, Uptime: {client['uptime']}")

# Obtener información de los usuarios y grupos de usuarios
users = api.get_resource('/user')
groups = api.get_resource('/user/group')
print("\nUsers:")
for user in users.get():
    groups_string = ""
    for group in groups.get():
        if group['name'] in user['group']:
            groups_string += f"{group['name']} "
    print(f"Name: {user['name']}, Groups: {groups_string.strip()}")

    
