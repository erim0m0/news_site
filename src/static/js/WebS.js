const ws = new WebSocket('ws://localhost:8000/crypto/ws/');
ws.addEventListener("message", (e => {
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

        let getChange7dCoinElmt = document.getElementById(
            symbol + '-7d'
        );
        getChange7dCoinElmt.innerText = data['change_percent_7d'];

        if ("-" ===  data['change_percent_7d'][0]) {
            getChange7dCoinElmt.style.cssText = "color : red"
        } else {
            getChange7dCoinElmt.style.cssText = "color : green"
        }

        let getMrktCapCoinElmt = document.getElementById(
            symbol + '-market-cap'
        );
        getMrktCapCoinElmt.innerText = "$ " + data['market_cap'];
        let getVolumeCoinElmt = document.getElementById(
            symbol + '-volume'
        );
        getVolumeCoinElmt.innerText = "$ " + data['volume_24h'];
        let chartAddrs = data['chart_24h'].replace("\/", "/");
        let getChartCoinElmt = document.getElementById(
            symbol + '-chart'
        );
        getChartCoinElmt.src = chartAddrs;
    }
}));