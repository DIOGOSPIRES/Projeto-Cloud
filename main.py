import pandas as pd
from twilio.rest import Client

# Passo a Passo de solução

# Abrir os 6 arquivos em excel

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = Client.messages.create(
            to="+5527997299892",
            from_="+12693903331",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)

# Your Account SID from twilio.com/console
account_sid = "AC900a8aa1e13f5d8f326d3c9e7035da3e"
# Your Auth Token from twilio.com/console
auth_token = "a5fe4130a9f760942ee42205af5d2863"

client = Client(account_sid, auth_token)



# Para cada arquivo:

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior que 55.000 não quero fazer nada

