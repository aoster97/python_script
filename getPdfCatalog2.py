import PyPDF2

# PDF 文件路径
pdf_path = "/Users/aochenwen/Downloads/x86汇编语言-从实模式到保护模式-完整扫描版.pdf"

# 打开 PDF 文件
with open(pdf_path, "rb") as f:
    reader = PyPDF2.PdfReader(f)

    # 获取目录（书签）
    try:
        outlines = reader.getOutlines()
    except Exception as e:
        print(f"⚠️ 读取目录时出错: {e}")
        outlines = []

    def parse_outline(outline, level=0):
        """ 递归解析目录（outline）"""
        if isinstance(outline, list):  # 处理嵌套目录
            for item in outline:
                parse_outline(item, level + 1)
        elif isinstance(outline, PyPDF2.generic.Destination):  # 处理单个目录项
            title = outline.title.strip()  # 去掉首尾空格
            title = title.encode("utf-8", "ignore").decode("utf-8")  # 过滤非法字符
            title = title.replace("\t", " ").replace("\n", " ")  # 替换 `\t` 和 `\n`

            try:
                page_num = reader.get_destination_page_number(outline) + 1  # 获取页码
            except Exception as e:
                page_num = "Unknown"
                print(f"⚠️ 无法解析目录 {title} 的页码: {e}")

            print(f"{'#' * level} {title} (Page {page_num})")

        elif isinstance(outline, float):  # 跳过 float 类型的书签
            print(f"⚠️ 跳过无效的书签（类型为 float）: {outline}")

        else:
            print(f"⚠️ 跳过未知的目录类型: {outline}（类型: {type(outline)}）")

    parse_outline(outlines)
