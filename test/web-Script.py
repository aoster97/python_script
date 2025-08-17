import requests
from bs4 import BeautifulSoup
import re
import time
import os
import random

def results_size_in_bytes(results):
    """估算results列表大小，简单地用字符串长度求和，utf-8编码下近似"""
    size = 0
    for r in results:
        # 拼成一段字符串，计算utf-8字节长度
        s = (
            r['标题'] + r['日期'] + r['描述'] + r['地点'] + r['链接'] + r['匹配的搜索字符串'] + r['完整div内容']
        )
        size += len(s.encode('utf-8'))
    return size

def save_results_to_txt(results, filename="matched_results.txt"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_dir, filename)

    with open(filepath, "a", encoding="utf-8") as f:  # 追加写
        for r in results:
            f.write("🎯 匹配结果:\n")
            f.write(f"标题: {r['标题']}\n")
            f.write(f"日期: {r['日期']}\n")
            f.write(f"描述: {r['描述']}\n")
            f.write(f"地点: {r['地点']}\n")
            f.write(f"链接: {r['链接']}\n")
            f.write(f"匹配关键词: {r['匹配的搜索字符串']}\n")
            f.write("完整div内容:\n")
            f.write(r["完整div内容"] + "\n")
            f.write("-" * 80 + "\n")

    print(f"\n✅ 追加写入 {len(results)} 条结果，文件：{filepath}")

def scrape_titles(base_url, search_strings, max_pages=500, start_page=1, max_buffer_size=1*1024*1024):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Referer': base_url,
        'Connection': 'keep-alive'
    }

    results_buffer = []
    visited_urls = set()
    next_url = f"{base_url}index.php?a=lists&cityid=11&page={start_page}"

    for page in range(start_page, start_page + max_pages):
        if not next_url or next_url in visited_urls:
            print("🚫 没有更多页面或已访问过")
            break
        visited_urls.add(next_url)

        try:
            response = requests.get(next_url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"⚠️ 第 {page} 页请求失败：{e}，等待10秒后重试一次")
            time.sleep(10)
            try:
                response = requests.get(next_url, headers=headers, timeout=10)
                response.raise_for_status()
            except requests.RequestException as e:
                print(f"❌ 重试后依然失败，跳过第 {page} 页：{e}")
                continue

        soup = BeautifulSoup(response.text, 'html.parser')

        info_items = soup.find_all('div', class_='InfoItem col-20')
        if not info_items:
            print(f"⛔ 第 {page} 页没有任何有效内容，停止爬取")
            break

        print(f"\n📄 正在处理第 {page} 页，共 {len(info_items)} 个 div")

        for item in info_items:
            title_div = item.find('div', class_='Title')
            desc_div = item.find('div', class_='Desc')

            if not (title_div and desc_div):
                continue

            title = title_div.text.strip()
            desc = desc_div.text.strip()
            text_to_search = f"{title} {desc}"

            matched = None
            for search_string in search_strings:
                if search_string and re.search(search_string, text_to_search, re.IGNORECASE):
                    matched = search_string
                    break

            if not matched:
                continue

            state_div = item.find('div', class_='State')
            date_span = state_div.find('span').text.strip() if state_div and state_div.find('span') else '未知'

            location_div = item.find('div', class_='Location')
            location_span = location_div.find('span') if location_div else None
            location = location_span.text.strip() if location_span else '未知'

            link_tag = item.find('a')
            link = link_tag['href'] if link_tag and 'href' in link_tag.attrs else '无链接'

            result = {
                '完整div内容': str(item),
                '标题': title,
                '日期': date_span,
                '描述': desc,
                '地点': location,
                '链接': f"{base_url}{link}" if link != '无链接' else '无链接',
                '匹配的搜索字符串': matched
            }

            results_buffer.append(result)

            print(f"✅ 匹配: {title} | 关键词: {matched} | 链接 :{base_url}{link}")

            # 检查缓存大小，达到阈值则写入文件，清空缓存
            if results_size_in_bytes(results_buffer) >= max_buffer_size:
                save_results_to_txt(results_buffer)
                results_buffer.clear()

        # 找下一页链接
        next_page_tag = soup.find('a', string=re.compile(r'下一页'))
        if next_page_tag and next_page_tag.get('href'):
            next_href = next_page_tag.get('href')
            if not next_href.startswith("http"):
                next_url = base_url.rstrip('/') + '/' + next_href.lstrip('/')
            else:
                next_url = next_href
        else:
            print("🚫 没有找到下一页链接，停止翻页")
            break

        delay = random.randint(3, 10)
        print(f"⏳ 等待 {delay} 秒后继续...")
        time.sleep(delay)

    # 爬取结束，写入剩余缓存数据
    if results_buffer:
        save_results_to_txt(results_buffer)
        results_buffer.clear()

def main():
    base_url = "https://4.pin251.xyz/"

    search_strings = [

    ]

    start_page = 1  # 起始页
    scrape_titles(base_url, search_strings, max_pages=550, start_page=start_page)

if __name__ == "__main__":
    main()
