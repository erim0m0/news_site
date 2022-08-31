data = {
    'success': True,
    'timestamp': 1661614264,
    'source': 'GBP',
    'quotes': {'GBPUSD': 1.17495}
}

a = data.get('quotes')

b = [k for i,k in data.items()]

print(b)