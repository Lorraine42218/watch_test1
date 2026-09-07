import requests # 請求工具
from bs4 import BeautifulSoup # 解析工具
import time # 用來暫停程式

import requests # 請求工具
from bs4 import BeautifulSoup # 解析工具
import time # 用來暫停程式 (Although already imported in uK4v4er0dxNO, re-importing here ensures self-containment for troubleshooting)

stock = ["1215","7736","1216"]
for i in range(len(stock)): # 迴圈依序爬股價

    # 現在處理的股票

    stockid = stock[i]

    # 網址塞入股票編號

    url = "https://tw.stock.yahoo.com/quote/"+stockid+".TW"

    # 發送請求

    r = requests.get(url)

    # 解析回應的 HTML

    soup = BeautifulSoup(r.text, 'html.parser')

    # 定位股價

    # Add a delay to avoid overwhelming the server
    time.sleep(3)

    price_element = soup.find('span',class_=[ "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)","Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)","Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)"])

    if price_element: # Check if the element was found
        price = price_element.getText()
    else:
        price = 'N/A' # Assign a default value if not found
        print(f"Warning: Price not found for stock ID {stockid}")
    
    print(f"Stock ID: {stockid}, Price: {price}")

message = "7736"+stockid+" 即時股價為 "+price
# 用 telegram bot 回報股價

# bot token

token = "Lorraine_monitor_bot"

# 使用者 id

chat_id="L930817"

# bot 送訊息

url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"

requests.get(url)

# 每次都停 3 秒

time.sleep(3)
