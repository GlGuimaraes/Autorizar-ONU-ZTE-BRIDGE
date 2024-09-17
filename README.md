# AutorizaONU - Script Python para Autorização de ONU em BRIDGE da ZTE
Este é um script Python desenvolvido para automatizar a autorização de ONUs (Optical Network Units) em BRIDGE da marca ZTE. Utilizando as bibliotecas Netmiko e datetime, o script simplifica o processo de configuração e autorização ao solicitar apenas algumas informações do usuário.

## Funcionalidades
- Autorização Automática: Autoriza ONUs em BRIDGE da ZTE com base nas informações fornecidas.
- Informações Requeridas: Apenas o serial completo da ONU, o nome do cliente, o slot, PON, posição e a VLAN desejada são necessários.
## Pré-requisitos
Antes de executar o script, certifique-se de ter as seguintes bibliotecas instaladas:

- Netmiko
- datetime

## Cofigure o Script

Abra o arquivo do script e ajuste os parâmetros conforme necessário. Você precisará fornecer o seguinte:

- Serial da ONU: O serial completo da ONU que você deseja autorizar.
- Nome do Cliente: Nome do cliente para identificação.
- Slot: Slot onde a ONU será alocada.
- PON: Porta PON onde a ONU será conectada.
- Posição: Posição da ONU no slot.
- VLAN: VLAN desejada para a ONU.
- Execute o Script

## Contribuição
Se você deseja contribuir com melhorias ou correções para o projeto, fique à vontade para abrir um pull request. Verifique as issues abertas e sinta-se livre para relatar bugs ou sugerir novos recursos.

## Contato
Para dúvidas ou mais informações, entre em contato com: https://www.linkedin.com/in/glguimaraes23/

Email:  Glguimaraes@yahoo.com
GitHub: https://github.com/glguimaraes
