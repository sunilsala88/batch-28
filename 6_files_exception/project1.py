
def write_to_file(port):
    f=open('port.txt','a')
    total=0
    for i,j in port.items():
        string1=f"{i}:{j}\n"
        f.write(string1)
        if type(j)==int:
            total=total+int(j)
    f.write(f"total:{total}\n")
    f.write('\n\n')
    f.close()


def input_stocks()->dict:
    portfolio={}
    name=input('enter the name')
    portfolio.update({'name':name})
    while True:
        name=input('enter the stock name(q to quit)')
        if name.upper()=='Q':
            break
        exist=stock_prices.get(name)
        if exist:
            portfolio.update({name:exist})
        else:
            print('invalid name')
    return portfolio

stock_prices={'goog':400,'tsla':800,'amzn':870}
port=input_stocks()
print(port)
write_to_file(port)
print(port)