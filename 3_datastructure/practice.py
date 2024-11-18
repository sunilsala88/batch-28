# #split and join

# l1=['abc','askjd','asdkfj']
# ans1=' '.join(l1)
# print(ans1)

# s1='als,jdfl,kajs'
# l2=s1.split(',')
# print(l2)

# #truthy and falsy value
# #falsy values 0,False,[],{},"",()
# a='hello'
# print(a)
# if a:
#     print('inside if')
# else:
#     print('inside else')



# stock_prices={'amzn':500,'tsla':900,'goog':900,99:100}
# print(stock_prices)

# v=stock_prices.get('nifty')

# if v:
#     print(v)
# else:
#     print('key doesnt exist')


# list1=[[4,5,6], [6,7,8,[99,88,77]], [88,99,66]]
# print(list1[1][3][2])
# list1[1][3][2]=0
# print(list1)

# stocks={
#     'bank':['kotak','hdfc','icici'],
#     'it':['tcs','wipro','infy'],
#     'energy':['ntpc','ongc']
# }

# print(stocks.get('it')[1])


data= [

    {
        "name": "Company A",
        "symbol": "CMPA",
        "sector": "Technology",
        "current_price": 100.0,
        "historical_data": [
            {
                "date": "2024-01-10",
                "prices": {
                    "open": 98.0,
                    "close": 100.0,
                    "high": 101.0,
                    "low": 97.0
                },
                "volume": 12000
            },

            {
                "date": "2024-01-09",
                "prices": {
                    "open": 97.0,
                    "close": 98.0,
                    "high": 99.0,
                    "low": 96.0
                },
                "volume": 15000
            }

        ],
        "locations": ["New York", "London"]
    },

    {
        "name": "Company B",
        "symbol": "CMPB",
        "sector": "Finance",
        "current_price": 200.0,
        "historical_data": [
            {
                "date": "2024-01-10",
                "prices": {
                    "open": 198.0,
                    "close": 200.0,
                    "high": 202.0,
                    "low": 196.0
                },
                "volume": 18000
            },
            {
                "date": "2024-01-09",
                "prices": {
                    "open": 196.0,
                    "close": 198.0,
                    "high": 199.0,
                    "low": 195.0
                },
                "volume": 17000
            }
        ],
        "locations": ["Tokyo", "Singapore"]
    },

    {
        "name": "Company C",
        "symbol": "CMPC",
        "sector": "Healthcare",
        "current_price": 300.0,
        "historical_data": [
            {
                "date": "2024-01-10",
                "prices": {
                    "open": 295.0,
                    "close": 300.0,
                    "high": 302.0,
                    "low": 294.0
                },
                "volume": 22000
            },
            {
                "date": "2024-01-09",
                "prices": {
                    "open": 294.0,
                    "close": 295.0,
                    "high": 296.0,
                    "low": 293.0
                },
                "volume": 21000
            }
        ],
        "locations": ["Berlin", "Paris"]
    }

]

print(data[1].get('current_price'))
data[2].update({'current_price':310.0})
print(data[2])
data[0].get('historical_data').pop(1)
print(data[0])