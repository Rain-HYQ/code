import requests

# 请求网页json数据
res = requests.get('https://api.live.bilibili.com/xlive/web-interface/v1/webMain/getMoreRecList?platform=web',headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})
print(res.text)  # 打印json字符串
data = res.json() # josn 转换成 字典
# 你需要写的代码并且打印出来.数据是字典格式的.
