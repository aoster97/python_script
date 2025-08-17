import re
from datetime import timedelta
from bs4 import BeautifulSoup


def parse_time(time_str):
    """将时间字符串（MM:SS 或 HH:MM:SS）转换为timedelta对象"""
    parts = time_str.split(':')
    if len(parts) == 2:
        minutes, seconds = map(int, parts)
        return timedelta(minutes=minutes, seconds=seconds)
    elif len(parts) == 3:
        hours, minutes, seconds = map(int, parts)
        return timedelta(hours=hours, minutes=minutes, seconds=seconds)
    return timedelta()


def format_timedelta(td):
    """将timedelta格式化为HH:MM:SS或MM:SS"""
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return f"{minutes:02d}:{seconds:02d}"


def split_chapter_duration(total_duration, max_hours=1):
    """如果章节时长超过max_hours小时，则分割成多个时段"""
    max_seconds = max_hours * 3600
    total_seconds = total_duration.total_seconds()
    if total_seconds <= max_seconds:
        return [total_duration]

    segments = []
    remaining = total_duration
    while remaining.total_seconds() > max_seconds:
        segments.append(timedelta(seconds=max_seconds))
        remaining -= timedelta(seconds=max_seconds)
    if remaining.total_seconds() > 0:
        segments.append(remaining)
    return segments


# 读取文件
try:
    with open('解析时间总和按章节.txt', 'r', encoding='utf-8') as file:
        html_content = file.read()
except FileNotFoundError:
    print("错误：找不到文件 '解析时间总和按章节.txt'")
    exit(1)

# 解析HTML内容
soup = BeautifulSoup(html_content, 'html.parser')

chapters = []
current_chapter = None
current_lessons = []

# 提取章节和课程
for li in soup.find_all('li'):
    if li.get('class') and 'chaper' in li.get('class'):
        if current_chapter:
            chapters.append((current_chapter, current_lessons))
            current_lessons = []
        current_chapter = li.text.strip()
    elif li.get('class') and 'lesson' in li.get('class'):
        time_span = li.find('span', class_='time fr')
        if time_span:
            current_lessons.append((li.find('p', class_='fl').text.strip(), time_span.text.strip()))

if current_chapter and current_lessons:
    chapters.append((current_chapter, current_lessons))

# 处理并输出结果
print("课程时间解析结果：")
print("=" * 50)

total_course_duration = timedelta()
for chapter_idx, (chapter, lessons) in enumerate(chapters, 1):
    chapter_duration = timedelta()
    for lesson, time_str in lessons:
        chapter_duration += parse_time(time_str)
    total_course_duration += chapter_duration

    print(f"\n第{chapter_idx}章: {chapter}")
    print(f"总时长: {format_timedelta(chapter_duration)}")

    # 分割超过1小时的章节
    segments = split_chapter_duration(chapter_duration)
    if len(segments) > 1:
        print(f"  分段数: {len(segments)}")
        print("  1倍速:")
        for seg_idx, segment in enumerate(segments, 1):
            print(f"    分段 {seg_idx}: {format_timedelta(segment)}")
        print("  1.5倍速:")
        for seg_idx, segment in enumerate(segments, 1):
            print(f"    分段 {seg_idx}: {format_timedelta(segment / 1.5)}")
        print("  2倍速:")
        for seg_idx, segment in enumerate(segments, 1):
            print(f"    分段 {seg_idx}: {format_timedelta(segment / 2)}")
    else:
        print(f"  1倍速: {format_timedelta(chapter_duration)}")
        print(f"  1.5倍速: {format_timedelta(chapter_duration / 1.5)}")
        print(f"  2倍速: {format_timedelta(chapter_duration / 2)}")

print("\n" + "=" * 50)
print(f"课程总时长: {format_timedelta(total_course_duration)}")
print(f"1.5倍速总时长: {format_timedelta(total_course_duration / 1.5)}")
print(f"2倍速总时长: {format_timedelta(total_course_duration / 2)}")