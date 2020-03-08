import urllib.request
from urllib.parse import urlencode
import json



def getStockData(symbol): 
    
    url="https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=%s&apikey=9J1RZLTW23BXC0KX"%(symbol)
    connection = urllib.request.urlopen(url)
    responseString = connection.read().decode()
    
    return responseString

def main():

    file = open("japi.out", "w")
    symbol = input("Type the stock symbol, or type 'QUIT' to exit ")
    while symbol.upper() != 'QUIT':
        responseString = getStockData(symbol)
        print(responseString)
        responseDict = json.loads(responseString)
        price = responseDict["Global Quote"]['price']
        printPrice= "The current price of "+ symbol + " is: " +price
        print(printPrice)
        symbol = input("Type the stock symbol, or type 'QUIT' to exit ")
        file.write(responseString)
        file.write(printPrice)
        
    file.close()
    print('Stock Quotes retrieved successfully!')
        
        
if __name__ == '__main__':
    main()
        
