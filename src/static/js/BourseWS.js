const brsWs = new WebSocket('ws://localhost:8000/market-bourse/ws/');
brsWs.addEventListener("message", (e => {

    const payload = JSON.parse(e.data);
    const dict_brs = payload.price;

    let getBrsIndexElmt = document.getElementById('brs-index');
    let getBrsIndex2Elmt = document.getElementById('brs-index2');
    getBrsIndexElmt.innerText = dict_brs['index'];
    getBrsIndex2Elmt.innerText = dict_brs['index'];

    let getBrsIndexHElmt = document.getElementById('brs-index-h');
    let getBrsIndexH2Elmt = document.getElementById('brs-index-h2');
    getBrsIndexHElmt.innerText = dict_brs['index_h'];
    getBrsIndexH2Elmt.innerText = dict_brs['index_h'];

    let getMrktVluElmt = document.getElementById('brs-market-value');
    let getMrktVlu2Elmt = document.getElementById('brs-market-value2');
    getMrktVluElmt.innerText = dict_brs['market_value'];
    getMrktVlu2Elmt.innerText = dict_brs['market_value'];

    let getTradeNumElmt = document.getElementById('brs-trade-number');
    let getTradeNum2Elmt = document.getElementById('brs-trade-number2');
    getTradeNumElmt.innerText = dict_brs['trade_number'];
    getTradeNum2Elmt.innerText = dict_brs['trade_number'];

    let getTradeVluElmt = document.getElementById('brs-trade-value');
    let getTradeVlu2Elmt = document.getElementById('brs-trade-value2');
    getTradeVluElmt.innerText = dict_brs['trade_value'];
    getTradeVlu2Elmt.innerText = dict_brs['trade_value'];

    let getTradeVlmElmt = document.getElementById('brs-trade-volume');
    let getTradeVlm2Elmt = document.getElementById('brs-trade-volume2');
    getTradeVlmElmt.innerText = dict_brs['trade_volume']
    getTradeVlm2Elmt.innerText = dict_brs['trade_volume']
}));

const favBrsWs = new WebSocket('ws://localhost:8000/fav-named-bourse/ws/');
favBrsWs.addEventListener("message", (e => {

    const payload = JSON.parse(e.data);
    const list_brs = payload.price;
    for (let item in list_brs) {

        let data = list_brs[item];
        item ++;
        console.log(item)
        let brsNameElmt = document.getElementById('brs-name' + item)
        brsNameElmt.innerText = data['name']

        let brsFinalPriceElmt = document.getElementById('brs-final-price' + item)
        brsFinalPriceElmt.innerText = data['final_price']

        let brsFinalPriceChangeElmt = document.getElementById('brs-final-price-change' + item)
        brsFinalPriceChangeElmt.innerText = data['final_price_change']

        let brsClosePriceElmt = document.getElementById('brs-close-price' + item)
        brsClosePriceElmt.innerText = data['close_price']

        let brsClosePriceChangeElmt = document.getElementById('brs-close-price-change' + item)
        brsClosePriceChangeElmt.innerText = data['close_price_change']

        let brsLowerPriceElmt = document.getElementById('brs-lowest-price' + item)
        brsLowerPriceElmt.innerText = data['lowest_price']

        let brsHighestPriceElmt = document.getElementById('brs-highest-price' + item)
        brsHighestPriceElmt.innerText = data['highest_price']

        let brsNElmt = document.getElementById('brs-n' + item)
        brsNElmt.innerText = data['n']

        let brsVolumeElmt = document.getElementById('brs-volume' + item)
        brsVolumeElmt.innerText = data['volume']

        let brsValueElmt = document.getElementById('brs-value' + item)
        brsValueElmt.innerText = data['value']

    }

}));