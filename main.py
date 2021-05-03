import requests
from pprint import pprint
import datetime, time
import json

print("Welcome to my bot!\nTakes care of reporting data from coinmarketcap")
print("-Write 'info' for info bot\n-Write 'start' to start the bot\n-Write 'exit' to access the next area")
activated = True
while activated:
        answer = input('Write: ')
        if answer == 'start':

                class Bot:
                    def __init__(self):
                        #NUMERO DI CRYPTO INTERESSATE
                        self.crypto_analized = int(input('Write number of crypto to analize: '))
                        #VALUTA FIAT CON IL QUALE EFFETTUARE LA CONVERSIONE
                        self.moneta_fiat = input('Choose a fiat coin who you are interesting in '
                                                 'converting: ')
                        #URL_SITO
                        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
                        #CRIPTO_CON_MAGGIOR_VOLUME_NELLE_ULTIME_24_ORE
                        self.params_volume_24h = {'start': '1', 'limit': '1', 'convert': self.moneta_fiat,
                                                  'sort': 'volume_24h'}
                        #MIGLIORI_10_CRIPTOVALUTE_PER_INCREMENTO_IN_PERCENTUALE
                        if self.crypto_analized < 10:
                            self.params_best_currencies = {'start': '1', 'limit': self.crypto_analized,
                                                           'convert': self.moneta_fiat,
                                                           'sort': 'percent_change_24h'}
                        else:
                           self.params_best_currencies = {'start': '1', 'limit': '10', 'convert': self.moneta_fiat,
                                                          'sort': 'percent_change_24h'}
                        #PEGGIORI_10_CRIPTOVALUTE_PER_DECREMENTO_IN_PERCENTUALE
                        if self.crypto_analized < 10:
                            self.params_wrost_currencies = {'start': '1', 'limit': self.crypto_analized,
                                                            'convert': self.moneta_fiat,
                                                            'sort': 'percent_change_24h',
                                                            'sort_dir': 'asc'}
                        else:
                           self.params_wrost_currencies = {'start': '1', 'limit': '10',
                                                           'convert': self.moneta_fiat,
                                                           'sort': 'percent_change_24h', 'sort_dir': 'asc'}
                        #PRIME_20(O MENO)_CRIPTOVALUTE_PER_CMC,PARAMETRO_USATO_ANCHE_PER_DECRETARE_UN_GUADAGNO_O_UNA_PERDITA
                        if self.crypto_analized < 20:
                            self.params_top_20 = {'start': '1', 'limit': self.crypto_analized, 'convert': self.moneta_fiat}
                        else:
                            self.params_top_20 = {'start': '1', 'limit': '20', 'convert': self.moneta_fiat}
                        #CRIPTO_IN_GENERALE
                        self.all_crypto = {'start': '1', 'limit': self.crypto_analized, 'convert': self.moneta_fiat}
                        #DATI_CHE_MI_SERVONO_PER_API
                        self.headers = {
                                    'Accepts': 'application/json',
                                    'X-CMC_PRO_API_KEY': 'afbeab28-c95d-4df6-85c6-3c5e32fe6500'
                        }
                        #QUESTA DOMANDA SERVE PER INDICARE SE TI INTERESSA ATTIVARE ORA O DOPO IL BOT
                        domanda_tempo = input('You want me to active now? Say me yes or no: ')
                        #IN QUESTO CASO SI ATTIVA SUBITO
                        if domanda_tempo == 'yes':
                            print('active now')
                        #SCRIVI TU UN ORARIO PRECISO,IL BOT SI ATTIVERA' A QUELL'ORA
                        elif domanda_tempo == 'no':
                            ora = input('Write hour: ')
                            minuti = input('Write minutes: ')
                            secondi = input('Write seconds: ')
                            print(f"I activate at the hours: {ora}:{minuti}:{secondi}")
                            while f"{ora}:{minuti}:{secondi}" != time.strftime('%X'):
                                                    time.sleep(1)
                    #NUMERO CRYPTO ANALIZZATE
                    def n_crypto(self):
                        limite_crypto = self.crypto_analized
                        return f"crypto analized: {limite_crypto}"
                        #METODO_DELLA_CLASSE_INERENTE_ALLA_CRYPTO_CON_MAGGIOR_VOLUME
                    def volume_24_order(self):
                        first_crypto_volume_24h = requests.get(url=self.url, headers=self.headers,
                                                               params=self.params_volume_24h).json()
                        first_crypto_volume_24h_value = \
                            first_crypto_volume_24h['data'][0]['quote'][self.moneta_fiat]['volume_24h']
                        volume_24h_name = first_crypto_volume_24h['data'][0]['name']
                        return f"Cryptocurrency with greater volume in the last 24 hours: {volume_24h_name} " \
                               f"with {first_crypto_volume_24h_value} {self.moneta_fiat}"
                    #METODO_INERENTE_ALLA_TOP_10_ED_ALLA_FLOP_10
                    def top_10_flop_10(self):
                        top_10 = requests.get(url=self.url, headers=self.headers,
                                              params=self.params_best_currencies).json()
                        flop_10 = requests.get(url=self.url, headers=self.headers,
                                               params=self.params_wrost_currencies).json()
                        best_currencies = []
                        flop_currencies = []
                        for i in top_10['data']:
                            best_currencies.append(i['name'])
                            best_currencies.append(i['quote'][self.moneta_fiat]['percent_change_24h'])
                        for x in flop_10['data']:
                            flop_currencies.append(x['name'])
                            flop_currencies.append(x['quote'][self.moneta_fiat]['percent_change_24h'])
                        return f"Best cryptocurrencies,with next to their %,for increment in the last 24 hours are:" \
                               f" {best_currencies}, while worst are: {flop_currencies}"
                    #METODO_TOP_PREZZO_CRIPTOVALUTE
                    def top_20_price(self):
                        top_price = requests.get(url=self.url, headers=self.headers, params=self.params_top_20).json()
                        top_price_20 = []
                        prezzo_totale = 0
                        for currency in top_price['data']:
                            top_price_20.append(currency['name'])
                            top_price_20.append(currency['quote'][self.moneta_fiat]['price'])
                            prezzo_totale += currency['quote'][self.moneta_fiat]['price']
                        return f"Price top 20 (or less) crypto in CMC in {self.moneta_fiat}: {top_price_20} , " \
                               f"total cost to buy one coin of each crypto within the list: {prezzo_totale} " \
                               f"{self.moneta_fiat}"
                    #METODO_INERENTE_ALLE_CRIPTOVALUTE_CHE_HANNO_UN_VOLUME_MAGGIORE_DI_76000000
                    def crypto_volume_76000000(self):
                        volume_76000000 = requests.get(url=self.url, headers=self.headers,
                                                       params=self.all_crypto).json()
                        crypto = []
                        prezzo_totale = 0
                        for currency in volume_76000000['data']:
                            if currency['quote'][self.moneta_fiat]['volume_24h'] > 76000000:
                                crypto.append(currency['name'])
                                crypto.append(currency['quote'][self.moneta_fiat]['volume_24h'])
                                prezzo_totale += currency['quote'][self.moneta_fiat]['volume_24h']
                        return f"Crypto with higher volume than 76000000 {self.moneta_fiat}, in {self.moneta_fiat}: {crypto}, " \
                               f"total cost to buy one coin of each crypto within the list: {prezzo_totale}"
                    #METODO_CHE_INDICA_UN_GUADAGNO_O_UNA_PERDITA_SE_AVESSIMO_INVESTITO_24_ORE_PRIMA_NELLA_TOP_20_DI_CRYPTO
                    def profit_loss(self):
                        profit_or_loss = requests.get(url=self.url, headers=self.headers,
                                                      params=self.params_top_20).json()
                        profit__loss_price = []
                        percentage_change_crypto = []
                        percentage = []
                        for currency in profit_or_loss['data']:
                            profit__loss_price.append(currency['quote'][self.moneta_fiat]['price'])
                            percentage_change_crypto.append(currency['quote'][self.moneta_fiat]['percent_change_24h'])
                        for i, x in zip(profit__loss_price, percentage_change_crypto):
                                percentage.append((i*x)/100)
                        sum_price_top_20_crypto = sum(profit__loss_price)
                        return_investiment = sum(percentage)
                        price_yesterday = sum_price_top_20_crypto-return_investiment
                        percentage_change_asset = (return_investiment*100)/price_yesterday
                        if percentage_change_asset > 0:
                            Final_comment = f"Price with which you bought yesterday the top 20 crypto in CMC is:" \
                                            f" {price_yesterday} {self.moneta_fiat}, " \
                                            f"today is {sum_price_top_20_crypto} {self.moneta_fiat}." \
                                            f"Your assets have varied of {percentage_change_asset}%.Great!" \
                                            f" Your asset are increasing."
                        elif percentage_change_asset == 0:
                            Final_comment = f"Price with which you bought yesterday the top 20 crypto in CMC is: " \
                                            f"{price_yesterday} {self.moneta_fiat}, " \
                                            f"today is {sum_price_top_20_crypto} {self.moneta_fiat}." \
                                            f"Your assets have varied of {percentage_change_asset}%." \
                                            f"Your asset has not changed."
                        else:
                            Final_comment = f"Price with which you bought yesterday the top 20 crypto in CMC is:" \
                                            f" {price_yesterday} {self.moneta_fiat},today is {sum_price_top_20_crypto} {self.moneta_fiat}." \
                                            f"Your assets have varied of {percentage_change_asset}%.Be quiet."
                        return Final_comment
                   # METODO_PER_INSERIRE_LA_DATA_ALL'INTERNO_DEL_FILE_JSON
                    def default(self, obj):
                        if isinstance(obj, (datetime.datetime, datetime.datetime)):
                            return obj.isoformat()
                #SISTEMAZIONE DELLO SCRIPT
                impact_Bot = Bot()
                File_json = {}
                File_json['date'] = []
                File_json['Request'] = []
                File_json['date'].append({'date': impact_Bot.default(datetime.datetime.now())})
                File_json['Request'].append({
                    'Request0': impact_Bot.n_crypto(),
                    'Request1': impact_Bot.volume_24_order(),
                    'Request2': impact_Bot.top_10_flop_10(),
                    'Request3': impact_Bot.top_20_price(),
                    'Request4': impact_Bot.crypto_volume_76000000(),
                    'Request5': impact_Bot.profit_loss()
                })
                file = open('Project.json', 'w')
                json.dump(File_json, file, indent=6)
                file.close()
                pprint(File_json)
        elif answer == 'info':
            print("You choose the number of crypto to analize.\n"
                  "I print this parameters:\n"
                  "-Cryptocurrency with greater volume in the last 24 hours\n-Best cryptocurrencies,"
                  "with next to their %,for increment in the last 24 hours\n"
                  "-Worst cryptocurrencies,with next to their %,for increment in the last 24 hours \n"
                  "-Price top 20 crypto in CMC in $,total cost to buy one coin of each crypto within the list\n"
                  "-Crypto with higher volume than 76000000$ in $,total cost to buy one coin of each crypto within "
                  "the list \n"
                  "-Any gain or loss if i had invested 24 hours earlier in the top 20 (or less) coinmarketcap")

        elif answer == 'exit':
            break
        else:
            print('You misspelled')


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
while activated:
    '''CON QUESTA DOMANDA APRIAMO UN'ALTRA AREA DEL BOT,QUI IL BOT CHIEDE SE L'UTENTE E' INTERESSATO AD UN CRYPTO IN
    PARTICOLARE'''
    Answer_particular_crypto = input('Are you interesting in a particular crypto? : ')
    #L'UTENTE DIGITA IL SIMBOLO DELLA CRYPTO,SE RISPONDE YES
    if Answer_particular_crypto == 'yes':
            name_crypto = input('Write symbol of crypto interesting: ')
            moneta_fiat = input('Write a symbol of a fiat coin who you are interesting in '
                                'converting: ')
            url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
            parameters = {
              'symbol': name_crypto, 'convert': moneta_fiat
            }
            headers = {
              'Accepts': 'application/json',
              'X-CMC_PRO_API_KEY': 'afbeab28-c95d-4df6-85c6-3c5e32fe6500',
            }

            session = Session()
            session.headers.update(headers)

            try:
              response = session.get(url, params=parameters)
              data = json.loads(response.text)
              parseData = json.dumps(response.json())
              quote_obj = json.loads(parseData)
              #NOME CRYPTO
              print(f"Name of crypto interesting: {quote_obj['data'][name_crypto]['name']}")
              #PREZZO
              print(f"price: {quote_obj['data'][name_crypto]['quote'][moneta_fiat]['price']} {moneta_fiat}")
              #VOLUME
              print(f"volume 24h: {quote_obj['data'][name_crypto]['quote'][moneta_fiat]['volume_24h']} {moneta_fiat}")
              #VARIAZIONI DI 1H, 24H, 7D, 30D
              print(f"Percent change 1h: "
                    f"{quote_obj['data'][name_crypto]['quote'][moneta_fiat]['percent_change_1h']} %")
              print(f"Percent change 24h: "
                    f"{quote_obj['data'][name_crypto]['quote'][moneta_fiat]['percent_change_24h']} %")
              print(f"Percent change 7d: "
                    f"{quote_obj['data'][name_crypto]['quote'][moneta_fiat]['percent_change_7d']} %")
              if quote_obj['data'][name_crypto]['quote'][moneta_fiat]['percent_change_7d'] > 200:
                  print("It's probably a shitcoin")
              print(f"Percent change 30d: "
                    f"{quote_obj['data'][name_crypto]['quote'][moneta_fiat]['percent_change_30d']} %")
              #CAPITALIZZAZIONE DI MERCATO
              print(f"market cap: "
                    f"{quote_obj['data'][name_crypto]['quote'][moneta_fiat]['market_cap']} {moneta_fiat}")
            except (ConnectionError, Timeout, TooManyRedirects) as e:
              print(e)
    #SE L'UTENTE SCRIVE NO,IL BOT SI SPEGNE
    elif Answer_particular_crypto == 'no':
        print('Goodbye')
        break
    else:
        print('Tell me yes or no')



