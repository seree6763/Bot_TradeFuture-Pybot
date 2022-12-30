import os

# BINANCE_API_KEY = "xxxxxxxxxxxxxxxx"
# BINANCE_API_SECRET = "xxxxxxxxxxxxxxxx"

# LINE_NOTIFY_API = "xxxxxxxxxxxxxxxx"

BINANCE_FUTURE_API_KEY = "D95sR8S2nbd0xjEZyYArQ4FUmAFRqdhaA0DaDlTfioTEX0ITWxRsgyUwFgYbp7C2"
BINANCE_FUTURE_API_SECRET = "ZNTTF929R4G9rPvdQEvKLWSLEiQwp2d8xa4myYoPgRPFTzLPTp8JmL0Ed844qfKL"

# แก้ไขเวลา Deploy ขึ้น heroku ใช้ ENV variable เพื่อปกป้อง api key
# heroku config:set BINANCE_API_KEY=xxx
# heroku config:set BINANCE_API_SECRET=xxx
# heroku config:set LINE_NOTIFY_API=xxx
# heroku config:set BINANCE_FUTURE_API_KEY=xxx
# heroku config:set BINANCE_FUTURE_API_SECRET=xxx
# heroku config:set HTTP_PROXY=xxx
# heroku config:set HTTPS_PROXY=xxx

# git add .
# git commit -m "add"
# git push heroku master

# BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
# BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
BINANCE_FUTURE_API_KEY = os.getenv("BINANCE_FUTURE_API_KEY")
BINANCE_FUTURE_API_SECRET = os.getenv("BINANCE_FUTURE_API_SECRET")
# LINE_NOTIFY_API = os.getenv("LINE_NOTIFY_API")