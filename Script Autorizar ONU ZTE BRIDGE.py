#!/usr/bin/env python3

from netmiko import ConnectHandler
from datetime import datetime

# Parametros da OLT
zte = {
    'device_type': 'alcatel_aos',
    'host': 'X.X.X.X',  # IP OLT
    'username': 'XXXXXXX',  # Usuário OLT
    'password': 'XXXXXXX',  # Senha OLT
}


def configurar_onu(net_connect, slot, pon, posicao, serial, nome, vlan):
    # Entrando no modo de configuração
    comandos = [
        'conf t',
        f'interface gpon_olt-1/{slot}/{pon}',
        f'onu {posicao} type F601 sn {serial}',
        f'interface gpon_onu-1/{slot}/{pon}:{posicao}',
        f'name "{nome}"',
        'tcont 1 profile 1G',
        'gemport 1 tcont 1',
        'exit',
        f'pon-onu-mng gpon_onu-1/{slot}/{pon}:{posicao}',
        f'service 1 gemport 1 vlan {vlan}',
        f'vlan port eth_0/1 mode tag vlan {vlan}',
        'exit',
        f'interface vport-1/{slot}/{pon}.{posicao}:1',
        f'service-port 1 user-vlan {vlan} vlan {vlan}',
        'exit'
    ]

    # Enviar comandos
    net_connect.send_config_set(comandos)

def main():
    # Conectar à OLT
    net_connect = ConnectHandler(**zte)

    print('\n///-///-///-///-///-///-///-///-///-///-///-///-\n')
    print('SCRIPT DESENVOLVIDO POR: GUILHERME GUIMARÃES\n')
    print('///-///-///-///-///-///-///-///-///-///-///-///-\n')

    # Entradas do usuário
    serial = input("Informe o serial da ONU completo: ")
    nome = input("Informe o nome do Cliente: ")
    slot = input("Informe o SLOT: ")
    pon = input("Informe a pon: ")
    posicao = input("Informe a posição: ")
    vlan = input("Informe a Vlan desejada: ")

    # Configurar ONU
    configurar_onu(net_connect, slot, pon, posicao, serial, nome, vlan)

    print('ONU AUTORIZADA.')

    # Fechar conexão
    net_connect.disconnect()


if __name__ == '__main__':
    main()
