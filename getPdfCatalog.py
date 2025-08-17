import PyPDF2


# /Users/aochenwen/Documents/C Primer Plus 第6版 中文版.pdf
# /Users/aochenwen/Documents/Netty权威指南 第2版.pdf
# /Users/aochenwen/Documents/NIO与Socket编程技术指南.pdf
# /Users/aochenwen/Desktop/Downloads/作系统真象还原 (郑纲) .pdf
# /Users/aochenwen/Desktop/Downloads/深入理解Java虚拟机：JVM高级特性与最佳实践（第3版）周志明.pdf
# /Users/aochenwen/Documents/汇编语言-第四版-王爽.pdf
# /Users/aochenwen/Documents/图解TCP_IP_第5版.pdf
# /Users/aochenwen/Documents/design-patterns-zh.pdf
# /Users/aochenwen/Documents/DAMA数据管理知识体系指南 第二版.pdf
# /Users/aochenwen/Documents/Wireshark网络分析的艺术.pdf
# /Users/aochenwen/Documents/《图解HTTP》完整彩色版.pdf
# /Users/aochenwen/Downloads/[琢石成器—Windows环境下32位汇编语言程序设计].罗云彬.第三版.pdf
# /Users/aochenwen/Downloads/精通Java并发编程（第2版）.pdf
# /Users/aochenwen/Downloads/Akka实战 in action中文版.pdf
# /Users/aochenwen/Downloads/Akka应用模式：分布式应用程序设计实践指南.pdf
# /Users/aochenwen/Documents/algos_ dstructure/算法的书籍/算法图解.pdf

# 打开 PDF 文件
with open('E:\流畅的python.pdf', 'rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    # 获取目录
    outlines = reader.getOutlines()
    def parse_outline(outline, level=0):
        """ 递归解析目录（outline）"""
        if isinstance(outline, list):  # 处理嵌套目录（目录结构是层级化的）
            for item in outline:
                parse_outline(item, level + 1)
        elif isinstance(outline, PyPDF2.generic.Destination):  # 处理单个目录项
            title = outline.title.strip()  # 去掉首尾空格
            title = title.encode('utf-8', 'ignore').decode('utf-8')  # 过滤非法字符
            title = title.replace("\t", " ").replace("\n", " ")  # 替换 `\t` 和 `\n`

            try:
                page_num = reader.get_destination_page_number(outline) + 1  # 获取页码
            except Exception:
                page_num = "Unknown"  # 可能某些 PDF 不支持页码解析

            print(f"{'#' * level} {title} (Page {page_num})")  # 使用 `repr()` 让输出更稳定


    parse_outline(outlines)

