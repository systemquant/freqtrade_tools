# Blacklist template, prefix
# Hardcoded, TODO: Maybe change later to make it easier to edit
string = '{\n\
  "exchange": {\n\
    "pair_blacklist": [\n\
      // Exchange Tokens\n\
      "(BNB|FTT|HT|KCS)/.*",\n\
      // Major Crypto\n\
      "(BTC|ETH)/.*",\n\
      // Leverage tokens\n\
      ".*(3|3L|3S)/.*",\n\
      ".*(BULL|BEAR|HALF|HEDGE|-PERP)/.*",\n\
      "(BVOL|IBVOL)/.*",\n\
      ".*(_PREMIUM|BEAR|BULL|DOWN|HALF|HEDGE|UP|[1235][SL])/.*",\n\
      // Fiat\n\
      "(AUD|BRZ|CAD|CHF|EUR|GBP|HKD|IDRT|JPY|NGN|RUB|SGD|TRY|UAH|USD|ZAR)/.*",\n\
      // Stable tokens\n\
      "(BUSD|CUSDT|DAI|PAXG|SUSD|TUSD|USDC|USDP|USDT|VAI)/.*",\n\
      // FAN Tokens\n\
      "(ACM|AFA|ALA|ALL|APL|ASR|ATM|BAR|CAI|CITY|FOR|GAL|GOZ|IBFK|JUV|LEG|LOCK-1|NAVI|NMR|NOV|OG|PFL|PSG|ROUSH|STV|TH|TRA|UCH|UFC|YBO)/.*",\n\
      // Other Coins\n\
      "('