import random
import time
import requests

# 配置 Clash 的 API 地址和密钥
clash_url = "http://127.0.0.1:49893"  # 根据你的配置修改地址和端口
secret = "53cd8f5c-396c-49d6-b459-643c2873cb84"  # 替换为你的密钥

# 获取所有代理节点
def get_proxies():
    response = requests.get(f"{clash_url}/proxies", headers= {"Authorization": f"Bearer {secret}"})
    proxies = response.json()['proxies']
    return list(proxies.keys())

# 切换代理
def switch_proxy(proxy_name):
    headers = {"Authorization": f"Bearer {secret}"}
    data = {"name": proxy_name}
    try:
        response = requests.put(f"{clash_url}/proxies/🚀 节点选择", headers=headers, json=data)
        if response.status_code == 204:
            print(f"Successfully switched to {proxy_name}")
        else:
            print(f"Failed to switch proxy. Status code: {response.status_code}, response: {response.json()}")
    except TimeoutError as e: 
        print(e)

# 调用示例
switch_proxy('香港 01 | 解锁')


# 主循环，每 3 秒随机切换节点
proxies = get_proxies()
while True:
    proxy_name = random.choice(proxies)
    if '香港' not in proxy_name:
        continue
    switch_proxy(proxy_name)
    time.sleep(3)
