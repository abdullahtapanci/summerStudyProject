import requests
import time
import schedule
import pandas as pd

#api requirements
API_KEY = "97b8da01-f4b6-4f4c-b8c0-b0070d634cc0"
headers = {
    'X-CMC_PRO_API_KEY': API_KEY,
    'Accepts': 'application/json',
    'Accept-Encoding': 'deflate, gzip',
}
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
#id=1 is equal to symbol=BTC
params = {
    'id': '1'
}

bitcoinData=0

def get_data():
    global bitcoinData
    global lineNumber
    try: 
        response = requests.get(url, headers=headers, params=params)

        data = response.json()
        bitcoinData = data['data']['1']

        try:
            with open("./BTCData/btcData.csv", "a") as f:
                f.write(
                    pd.to_datetime( str(bitcoinData['last_updated']) ).strftime('%Y-%m-%d') + "," +
                    str(bitcoinData['quote']['USD']['price']) + "," +
                    str(bitcoinData['quote']['USD']['volume_24h']) + "\n"
                )
        except Exception as e:
            print(e)

    except Exception as e:
        print(e)


#OHLC open , high , low , close 
def calculateOHLC():
    # Read the CSV file
    df = pd.read_csv('./BTCData/btcData.csv',header=None, names=['date', 'price', 'volume'])
    # convert tp data frame
    df = pd.DataFrame(df)

    date = df['date'].iloc[-1]
    openValue = df['price'].iloc[1]
    high = df['price'][1:].max()
    low = df['price'][1:].min()
    close = df['price'].iloc[-1]
    volume = df['volume'].iloc[-1]

    openValue = str(openValue)
    high = str(high)
    low = str(low)
    close = str(close)
    volume = str(volume)

    try:
        with open("./BTCData/bitcoinData.csv", "a") as f:
            f.write(
                date + "," +
                openValue + "," +
                high + "," +
                low + "," +
                close + "," +
                volume + "," + "\n"
            )
    except Exception as e:
        print(e)

    # clear data
    with open("./BTCData/btcData.csv", 'w') as file:
        # Write the header
        file.write('date,price,volume\n')


#Schedule the task to run every 1 minutes
schedule.every(5).minutes.do(get_data)
schedule.every().day.at("23:56").do(calculateOHLC)

while True:
    schedule.run_pending()

