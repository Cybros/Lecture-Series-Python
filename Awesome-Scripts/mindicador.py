''''
This is an helper class to the Chilean economic indicator http://mindicador.cl/
using the awesome requests library you can get uf, ivp, dolar, etc.

a simple example:

>> m = Mindicador()
>> m = m.get_uf()
>> uf
{'fecha': '2017-07-23T04:00:00.000Z', 'nombre': 'Unidad de fomento (UF)', 'codigo': 'uf',
'unidad_medida': 'Pesos', 'valor': 26624.85}

The above response is returned as a json ready object; you can use the object the following way:

>> for ufs in uf:
      print(ufs, ':', uf.get(ufs))

fecha : 2017-07-23T04:00:00.000Z
nombre : Unidad de fomento (UF)
codigo : uf
unidad_medida : Pesos
valor : 26624.85

Note: Some if not most of the words in the responses are in Spanish(Chilean).
'''


import requests


class Mindicador():

    def __init__(self):
        if requests.get('http://mindicador.cl/api').status_code == requests.codes.ok:
            self.api_url = requests.get('http://mindicador.cl/api')
        else:
            self.bad_r = requests.get('http://mindicador.cl/api')
            return self.bad_r.raise_for_status()

    def get_uf(self):
        api_url = self.api_url.json()
        return api_url.get('uf')

    def get_ivp(self):
        self.api_url = self.api_url.json()
        return self.api_url.get('ivp')

    def get_dolar(self):
        self.api_url = self.api_url.json()
        return self.api_url.get('dolar')

    def get_dolar_intercambio(self):
        self.api_url = self.api_url.json()
        return self.api_url.get('dolar_intercambio')

    def get_euro(self):
        self.api_url = self.api_url.json()
        return self.api_url.get('euro')

    def get_ipc(self):
        self.api_url = self.api_url.json()
        return self.api_url.get('ipc')

    def get_utm(self):
        self.api_url = self.api_url.json()
        return self.api_url.get('utm')

    def get_imacec(self):
        self.api_url = self.api_url.json()
        return self.api_url.get('imacec')

    def get_tpm(self):
        self.api_url = self.api_url.json()
        return self.api_url.get('tpm')

    def get_libra_cobre(self):
        self.api_url = self.api_url.json()
        return self.api_url.get('libra_cobre')

    def get_tasa_desempleo(self):
        self.api_url = self.api_url.json()
        return self.api_url.get('tasa_desempleo')


