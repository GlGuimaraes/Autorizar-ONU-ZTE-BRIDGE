#!/usr/bin/env python3


# Importando Bibliotecas
from netmiko import ConnectHandler
from datetime import datetime

# Parametros da OLT
zte = {
	'device_type': 'alcatel_aos',
	'host': 'X.X.X.X', #IP OLT
	'username': 'XXXXXXX',  #Usuário OLT
	'password': 'XXXXXXX', #Senha OLT
	}

# Connect to OLT
net_connect = ConnectHandler(**zte)

# show terminal to prove connection
net_connect.find_prompt()
print('\n///-///-///-///-///-///-///-///-///-///-///-///-\n')
print('SCRIPT DESENVOLVIDO POR : GUILHERME GUIMARÃES \n')
print('///-///-///-///-///-///-///-///-///-///-///-///- \n')


#Serial
serial = input("Informe o serial da ONU completo: ")

#Nome
nome = input("Informe o nome do Cliente: ")

#Slot
slot = input("Informe o SLOT: ")

#Pon
pon = input("Informe a pon: ")

#Posição
posicao = input("Informe a posição: ")

#Vlan
vlan = input("Informe a Vlan desejada: ")

#Configurando a interface na OLT
conf = net_connect.send_config_set('conf t')
InterfaceOlt = net_connect.send_config_set(f'interface gpon_olt-1/{slot}/{pon}')
Autorizando = net_connect.send_config_set(f'onu {posicao} type F601 sn {serial}')
back = net_connect.send_config_set('exit')

#Configurando a interface na posição da ONU
InterfaceOnu = net_connect.send_config_set(f'interface gpon_onu-1/{slot}/{pon}:{posicao}')
name = net_connect.send_config_set(f'name "{nome}"')
Profile = net_connect.send_config_set('tcont 1 profile 1G')
Tcont = net_connect.send_config_set('gemport 1 tcont 1')
back = net_connect.send_config_set('exit')

#Configurando mng
OnuMng = net_connect.send_config_set(f'pon-onu-mng gpon_onu-1/{slot}/{pon}:{posicao}')
Service = net_connect.send_config_set(f'service 1 gemport 1 vlan {vlan}')
PortEth = net_connect.send_config_set(f'vlan port eth_0/1 mode tag vlan {vlan}')
back = net_connect.send_config_set('exit')

#Configurando a interface Vport
Vport = net_connect.send_config_set(f'interface vport-1/{slot}/{pon}.{posicao}:1')
ServicePort = net_connect.send_config_set(f'service-port 1 user-vlan {vlan} vlan {vlan}')
back = net_connect.send_config_set('exit')

print('ONU AUTORIZADA.')

# disconect ssh connection
net_connect.disconnect()
