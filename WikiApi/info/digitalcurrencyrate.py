import requests

class DigitalCurrencyRate:
    def DigitalCurrencyRate(symbol:str=None):
        """
        `symbol` Optional

        Receiving the digital exchange rate in rials IR

        His exit is Json
        """
        gets= requests.get("https://open.wiki-api.ir/apis-1/DigitalCurrencyRate").json()
        if symbol == None:
            return gets
        else:
            listarz = {"BTC": 0, "ETH": 1, "XRP": 2, "USDT": 3, "SOL": 4, "BNB": 5, "USDC": 6, "DOGE": 7, "ADA": 8, "TRX": 9, "LINK": 10, "AVAX": 11, "XLM": 12, "HBAR": 13, "TON": 14, "SUI": 15, "SHIB": 16, "DOT": 17, "LTC": 18, "LEO": 19, "BGB": 20, "BCH": 21, "HYPE": 22, "UNI": 23, "PEPE": 24, "USDE": 25, "NEAR": 26, "TRUMP": 27, "DAI": 28, "AAVE": 29, "APT": 30, "OM": 31, "ONDO": 32, "ICP": 33, "XMR": 34, "ETC": 35, "MNT": 36, "POL": 37, "VET": 38, "CRO": 39, "TAO": 40, "RENDER": 41, "KAS": 42, "ALGO": 43, "OKB": 44, "FIL": 45, "ARB": 46, "FET": 47, "ATOM": 48, "ENA": 49, "GT": 50, "TIA": 51, "RAY": 52, "OP": 53, "BONK": 54, "IMX": 55, "STX": 56, "INJ": 57, "THETA": 58, "WLD": 59, "LDO": 60, "FDUSD": 61, "GRT": 62, "DEXE": 63, "KCS": 64, "PENGU": 65, "MOVE": 66, "XDC": 67, "SEI": 68, "VIRTUAL": 69, "S": 71, "FLR": 72, "JASMY": 73, "SAND": 74, "FLOKI": 75, "QNT": 76, "$WIF": 77, "FARTCOIN": 78, "EOS": 79, "KAIA": 80, "ENS": 81, "GALA": 82, "XTZ": 83, "IOTA": 84, "PYTH": 85, "XCN": 86, "SPX": 87, "MKR": 88, "FLOW": 89, "AIOZ": 90, "BTT": 91, "BSV": 92, "CRV": 93, "NEO": 94, "AR": 95, "NEXO": 96, "MANA": 97, "AXS": 98, "RUNE": 99}
            if listarz[symbol] in None:
                return gets['results'][listarz[symbol]]