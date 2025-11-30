import requests

proxies = []

# Get proxies from raw text files
raw_proxy_sites = [
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
    "https://api.openproxylist.xyz/http.txt",
    "https://openproxylist.xyz/http.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
    "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
]

for site in raw_proxy_sites:
    try:
        response = requests.get(site, timeout=10)
        response.raise_for_status()  # Kiểm tra nếu có lỗi HTTP
        for line in response.text.split('\n'):
            line = line.strip()
            if ':' in line:
                parts = line.split(':', maxsplit=1)
                if len(parts) == 2:
                    ip, port = parts
                    proxies.append(f'{ip}:{port}')
    except requests.RequestException as e:
        print(f"Không thể tải proxy từ {site}: {e}")

if proxies:
    with open('proxy.txt', 'w') as f:
        for proxy in proxies:
            f.write(proxy + '\n')
    print("Đã lưu vào file proxy.txt")
    print("C25 Tool")
else:
    print("Không có proxy hợp lệ để lưu.")
