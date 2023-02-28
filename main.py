#!/usr/bin/python
#from librouteros import connect
#from ros import Ros
import routeros_api

#ros = Ros("https://192.168.88.1/", "admin", "")
connection = routeros_api.RouterOsApiPool('152.206.118.189', username='admin', password='112233' ,plaintext_login=True)
api = connection.get_api()
# Obtener información de la versión del router
system_resource = api.get_resource('/system/resource')
version = system_resource.get()[0]['version']
print(f"RouterOS version: {version}")

# Obtener información de la configuración de la interfaz
interfaces = api.get_resource('/interface')
print("\nInterfaces:")
for interface in interfaces.get():
    print(f"Name: {interface['name']}")
    if 'mac-address' in interface:
        print(f"MAC address: {interface['mac-address']}")
    else:
        print("None")
    #, )#, IP address: {interface['address']}

# Obtener información de la configuración de la red
ip_addresses = api.get_resource('/ip/address')
print("\nIP addresses:")
for ip_address in ip_addresses.get():
    print(f"Address: {ip_address['address']}, Interface: {ip_address['interface']}")

# Obtener información de la tabla de rutas
routes = api.get_resource('/ip/route')
print("\nRoutes:")
for route in routes.get():
    print(route)
    '''
    if route['dst-address'] == '0.0.0.0/0':
        print(f"Gateway: {route['gateway']}, Interface: {route['interface']}")
    elif 'via' in route:
        print(f"Destination: {route['dst-address']}, Gateway: {route['gateway']}, Interface: {route['interface']}")
    else:
        print(f"Destination: {route['dst-address']}, Interface: {route['interface']}")
    '''

# Obtener información de las reglas de firewall
firewall_rules = api.get_resource('/ip/firewall/filter')
print("\nFirewall rules:")
for rule in firewall_rules.get():
    print(rule)
    #print(f"Chain: {rule['chain']}, Protocol: {rule['protocol']}, Source address: {rule['src-address']}, Destination address: {rule['dst-address']}")

# Obtener información de las colas de tráfico
queues = api.get_resource('/queue/simple')
print("\nTraffic queues:")
for queue in queues.get():
    print(queue)
    #print(f"Name: {queue['name']}, Target address: {queue['target-addresses']}, Max limit: {queue['max-limit']}")

# Obtener información de los clientes PPPoE
pppoe_clients = api.get_resource('/ppp/active')
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
#ping = api.get_binary_resource('/').call('ping', { 'address': 'google.com', 'count': '4' })
#route = api.get_resource('/ip/route')
#interface = api.get_resource('/interface')
#interfaceinfo = interface.get()
#print(interfaceinfo)
#routeinfo = route.get()
#print(routeinfo)
#for i in ping:
    #print(i)
    
