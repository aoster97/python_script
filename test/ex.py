import os
import re
from collections import defaultdict
from datetime import datetime

def extract_grouped_by_keyword(txt_path, html_output_path="grouped_results.html"):
    if not os.path.exists(txt_path):
        print(f"❌ 找不到文件：{txt_path}")
        return

    with open(txt_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 每条记录按 🎯 分隔
    entries_raw = content.split("🎯 匹配结果:")

    grouped = defaultdict(list)  # keyword -> list of (date, link)

    for block in entries_raw:
        link_match = re.search(r"链接:\s*(https?://[^\s]+)", block)
        keyword_match = re.search(r"匹配关键词:\s*(.*)", block)
        date_match = re.search(r"日期:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", block)

        if link_match and keyword_match and date_match:
            link = link_match.group(1).strip()
            keyword = keyword_match.group(1).strip()
            date_str = date_match.group(1).strip()
            try:
                date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            except ValueError:
                date_obj = datetime(1900, 1, 1)  # fallback
            grouped[keyword].append((date_obj, link))

    # 写 HTML 输出
    html = ['<html><head><meta charset="utf-8"><title>按关键词分组结果</title></head><body>']

    for keyword, records in sorted(grouped.items()):
        html.append(f"<h2>关键词：{keyword}</h2>")
        html.append('<table border="1" cellspacing="0" cellpadding="5">')
        html.append("<tr><th>链接</th><th>日期</th></tr>")

        # 按日期升序排列
        for date_obj, link in sorted(records):
            date_str = date_obj.strftime("%Y-%m-%d")
            html.append(
                f"<tr><td><a href='{link}' target='_blank'>{link}</a></td><td>{date_str}</td></tr>"
            )

        html.append("</table><br>")

    html.append("</body></html>")

    with open(html_output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(html))

    print(f"✅ 已分组生成HTML，共 {len(grouped)} 个关键词，保存为：{html_output_path}")


if __name__ == "__main__":
    extract_grouped_by_keyword("matched_results.txt")
