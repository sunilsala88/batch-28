hedge_fund_portfolio = {
    "fund_name": "Alpha Investments",
    "portfolio_value": 5_00_00_000,
    "investments": [

        {
            "type": "Equity",
            "holdings": [
                {"ticker": "AAPL", "quantity": 10000, "average_buy_price": 120},
                {"ticker": "TSLA", "quantity": 5000, "average_buy_price": 600}
            ]
        },

        {
            "type": "Fixed Income",
            "holdings": [
                {"bond_issue": "US Treasuries", "amount": 10000000, "yield": 1.5}
            ]
        },

        {
            "type": "Derivatives",
            "holdings": [
                {"instrument": "Options", "details": {"underlying": "GOOGL", "type": "Call", "strike_price": 1500}}
            ]
        }

    ],
    "performance_metrics": {
        "year_to_date_return": 5.2,
        "five_year_annualized_return": 7.1
    }
}

# ans=hedge_fund_portfolio.get('investments')[2].get('holdings')[0].get('details').get('strike_price')
# print(ans)
# print(type(ans))

# a=hedge_fund_portfolio.get('investments', 'Not Found')[2].get('holdings', 'Not Found')[0].get('details', 'Not Found').get('strike_price', 'Not Found')
# print(a)

ans=hedge_fund_portfolio.get('investments')[0].get('holdings')[1].get('quantity')
print(ans)
print(type(ans))

hedge_fund_portfolio.get('investments')[0].get('holdings')[1].update({'quantity':6000})
print(hedge_fund_portfolio.get('investments')[0].get('holdings')[1])

print(hedge_fund_portfolio.get('investments'),'\n')
hedge_fund_portfolio.get('investments').pop(2)
print(hedge_fund_portfolio.get('investments'),'\n')


print(hedge_fund_portfolio.get('investments')[0].get('holdings')[1])




hedge_fund_portfolio.get('investments')[0].get('holdings')[0].update({'average_buy_price':125})
print(hedge_fund_portfolio.get('investments')[0].get('holdings')[0])

a={"ticker": "AMZN", "quantity": 3000, "average_buy_price": 3100}


print(hedge_fund_portfolio.get('investments')[0].get('holdings'))
hedge_fund_portfolio.get('investments')[0].get('holdings').append(a)
print(hedge_fund_portfolio.get('investments')[0].get('holdings'))
