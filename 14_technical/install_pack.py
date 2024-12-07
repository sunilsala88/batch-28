#yahoo finance
#yfinance==0.2.37
import yfinance as yf
import pandas as pd
import pandas_ta as ta
import talib 
# #talib
# #pandasta
data=yf.download(tickers='^NSEI',period='1y')
print(data)

# col=[]
# for c in data.columns:
#     col.append(c[0])
# data.columns=col

# data.columns=[c[0] for c in data.columns]
# print(data)
print(ta.sma(data['Close']))

#installing talib
#windows
#https://github.com/cgohlke/talib-build/releases
#pip install "/Users/algotrading2024/batch 28/ta_lib-0.5.1-cp312-cp312-win_amd64.whl"




#mac os
#/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
#add path
#source ~/.zshrc
#source ~/.bash_profile
#brew --version
#brew install ta-lib
#pip3 install TA-Lib

#test if working
# import talib 
# print(talib.get_functions())


#pandas-ta
#pip install pandas-ta
# error pkg_resources
#  pip install setuptools
#pip install numpy==1.26.4 