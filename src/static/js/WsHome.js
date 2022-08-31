const brsHomeWs = new WebSocket('ws://localhost:8000/home/bourse/ws/');
brsHomeWs.addEventListener("message", (e => {

    const payload = JSON.parse(e.data);
    const dict_brs = payload.price;

    let getBrsIndexElmt = document.getElementById('brs-index');
    getBrsIndexElmt.innerText = dict_brs['index'];

    let getBrsIndexHElmt = document.getElementById('brs-index-h');
    getBrsIndexHElmt.innerText = dict_brs['index_h'];

    let getMrktVluElmt = document.getElementById('brs-market-value');
    getMrktVluElmt.innerText = dict_brs['market_value'];

    let getTradeVluElmt = document.getElementById('brs-trade-value');
    getTradeVluElmt.innerText = dict_brs['trade_value'];

    let getTradeVlmElmt = document.getElementById('brs-trade-volume');
    getTradeVlmElmt.innerText = dict_brs['trade_volume']
}));

const cpHomeWs = new WebSocket('ws://localhost:8000/home/crypto/ws/');
cpHomeWs.addEventListener("message", (e => {
    const payload = JSON.parse(e.data);
    const dict_coins = payload.price;

    for (let item in dict_coins) {
        let data = dict_coins[item];
        let symbol = data['symbol'].toLowerCase();

        let getPriceCoinElmt = document.getElementById(
            symbol + '-price'
        );
        getPriceCoinElmt.innerText = "$" + data['price'];

        let getChange24hCoinElmt = document.getElementById(
            symbol + '-24h'
        );
        getChange24hCoinElmt.innerText = data['change_percent_24h'];

        if ("-" ===  data['change_percent_24h'][0]) {
            getChange24hCoinElmt.style.cssText = "color : red"
        } else {
            getChange24hCoinElmt.style.cssText = "color : green"
        }

        let chartAddrs = data['chart_24h'].replace("\/", "/");

        let getChartCoinElmt = document.getElementById(
            symbol + '-chart'
        );
        getChartCoinElmt.src = chartAddrs;
    }
}));