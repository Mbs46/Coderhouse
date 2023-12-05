#!/usr/bin/env python
# coding: utf-8

# In[20]:


from plyer import notification
from datetime import datetime

def alerta(nivel, base, etapa):
    if nivel == 1:
        titulo = 'Alerta Baixo'
    elif nivel == 2:
        titulo = 'Alerta Médio'
    elif nivel == 3:
        titulo = 'Alerta Alto'
    else:
        titulo = 'Alerta'

    mensagem = f'Falha no carregamento da base {base} na etapa {etapa}\nData: {datetime.now()}'

    notification.notify(
        title=titulo,
        message=mensagem,
        app_name='Nome do aplicativo',
        timeout=10)

alerta(2, 'Clientes', 'Processamento Inicial')


# In[ ]:




