# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

# 假设这是你的 HTML 字符串
html_string = """
 <ul>
                      <li class="chaper">第一章 SQL语言</li>
                                                    
                                          <li class="lesson cur">
                        <a href="/center/course/lesson/index?id=12703_396307" title="SQL结构化查询语言概述 23分钟"><span class="num fl">1-1</span><p class="fl">SQL结构化查询语言概述 23分钟</p><span class="time fr">22:45</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396306" title="数据表定义与数据操纵 54分钟"><span class="num fl">1-2</span><p class="fl">数据表定义与数据操纵 54分钟</p><span class="time fr">53:41</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396305" title="表结构修改与索引创建 24分钟"><span class="num fl">1-3</span><p class="fl">表结构修改与索引创建 24分钟</p><span class="time fr">23:16</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396304" title="SELECT简单查询与分组查询 43分钟"><span class="num fl">1-4</span><p class="fl">SELECT简单查询与分组查询 43分钟</p><span class="time fr">42:59</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396303" title="SELECT连接查询 43分钟"><span class="num fl">1-5</span><p class="fl">SELECT连接查询 43分钟</p><span class="time fr">42:47</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396302" title="SELECT子查询与集合查询 43分钟"><span class="num fl">1-6</span><p class="fl">SELECT子查询与集合查询 43分钟</p><span class="time fr">42:20</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396301" title="视图与断言 44分钟"><span class="num fl">1-7</span><p class="fl">视图与断言 44分钟</p><span class="time fr">43:30</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396308" title="权限管理 25分钟"><span class="num fl">1-8</span><p class="fl">权限管理 25分钟</p><span class="time fr">25:00</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396300" title="嵌入SQL与面向对象SQL 25分钟"><span class="num fl">1-9</span><p class="fl">嵌入SQL与面向对象SQL 25分钟</p><span class="time fr">30:04</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396299" title="触发器、存储过程与存储函数 35分钟"><span class="num fl">1-10</span><p class="fl">触发器、存储过程与存储函数 35分钟</p><span class="time fr">34:41</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396298" title="课程知识小节串讲 42分钟"><span class="num fl">1-11</span><p class="fl">课程知识小节串讲 42分钟</p><span class="time fr">40:30</span></a>
                      </li>
                                                                        
                    
                      <li class="lesson exam ">
                        <a href="/center/course/lesson/index?id=12703_401710" title="SQL语言 习题"><span class="num fl">1-12</span><i class="icon"></i></span><p class="fl">SQL语言 习题</p><span class="look fr">查看练习</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396297" title="SQL查询语言习题精讲一 48分钟"><span class="num fl">1-13</span><p class="fl">SQL查询语言习题精讲一 48分钟</p><span class="time fr">47:10</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396296" title="SQL查询语言习题精讲二 28分钟"><span class="num fl">1-14</span><p class="fl">SQL查询语言习题精讲二 28分钟</p><span class="time fr">27:26</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396295" title="SQL查询语言习题精讲三 47分钟"><span class="num fl">1-15</span><p class="fl">SQL查询语言习题精讲三 47分钟</p><span class="time fr">51:01</span></a>
                      </li>
                                                                                            <li class="chaper">第二章 数据库设计与运行管理</li>
                                                    
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396294" title="数据库设计及运行管理-课程内容介绍 14分钟"><span class="num fl">2-1</span><p class="fl">数据库设计及运行管理-课程内容介绍 14分钟</p><span class="time fr">14:54</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396293" title="数据库设计过程综述 40分钟"><span class="num fl">2-2</span><p class="fl">数据库设计过程综述 40分钟</p><span class="time fr">40:09</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396310" title="概念结构设计与ER图 42分钟"><span class="num fl">2-3</span><p class="fl">概念结构设计与ER图 42分钟</p><span class="time fr">41:41</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396292" title="逻辑结构设计与ER转换规则 38分钟"><span class="num fl">2-4</span><p class="fl">逻辑结构设计与ER转换规则 38分钟</p><span class="time fr">37:55</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396309" title="数据库的运行和管理 40分钟"><span class="num fl">2-5</span><p class="fl">数据库的运行和管理 40分钟</p><span class="time fr">39:25</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396291" title="数据库设计及运行管理知识要点串讲 40分钟"><span class="num fl">2-6</span><p class="fl">数据库设计及运行管理知识要点串讲 40分钟</p><span class="time fr">30:37</span></a>
                      </li>
                                                                        
                    
                      <li class="lesson exam ">
                        <a href="/center/course/lesson/index?id=12703_401765" title="数据库设计与运行管理 习题"><span class="num fl">2-7</span><i class="icon"></i></span><p class="fl">数据库设计与运行管理 习题</p><span class="look fr">查看练习</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396290" title="习题精讲一（选择题） 52分钟"><span class="num fl">2-8</span><p class="fl">习题精讲一（选择题） 52分钟</p><span class="time fr">51:55</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396289" title="习题精讲二（分析题） 44分钟"><span class="num fl">2-9</span><p class="fl">习题精讲二（分析题） 44分钟</p><span class="time fr">44:17</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396311" title="习题精讲三（分析题） 34分钟"><span class="num fl">2-10</span><p class="fl">习题精讲三（分析题） 34分钟</p><span class="time fr">33:27</span></a>
                      </li>
                                                                                            <li class="chaper">第三章 数据库发展和新技术</li>
                                                    
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396288" title="数据库发展和新技术-课程内容介绍 12分钟"><span class="num fl">3-1</span><p class="fl">数据库发展和新技术-课程内容介绍 12分钟</p><span class="time fr">11:46</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396312" title="分布式数据库（一） 42分钟"><span class="num fl">3-2</span><p class="fl">分布式数据库（一） 42分钟</p><span class="time fr">41:49</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396287" title="分布式数据库（二） 24分钟"><span class="num fl">3-3</span><p class="fl">分布式数据库（二） 24分钟</p><span class="time fr">23:16</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396313" title="WEB与数据库 30分钟"><span class="num fl">3-4</span><p class="fl">WEB与数据库 30分钟</p><span class="time fr">29:25</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396314" title="XML与数据库 12分钟"><span class="num fl">3-5</span><p class="fl">XML与数据库 12分钟</p><span class="time fr">12:17</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396286" title="ODBS对象数据库 28分钟"><span class="num fl">3-6</span><p class="fl">ODBS对象数据库 28分钟</p><span class="time fr">28:14</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396285" title="DW、DM、ERP与DSS 44分钟"><span class="num fl">3-7</span><p class="fl">DW、DM、ERP与DSS 44分钟</p><span class="time fr">43:17</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396284" title="NoSQL数据库 11分钟"><span class="num fl">3-8</span><p class="fl">NoSQL数据库 11分钟</p><span class="time fr">11:06</span></a>
                      </li>
                                                                        
                    
                      <li class="lesson exam ">
                        <a href="/center/course/lesson/index?id=12703_401766" title="数据库发展和新技术 习题"><span class="num fl">3-9</span><i class="icon"></i></span><p class="fl">数据库发展和新技术 习题</p><span class="look fr">查看练习</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396315" title="习题精讲一 31分钟"><span class="num fl">3-10</span><p class="fl">习题精讲一 31分钟</p><span class="time fr">31:22</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396283" title="习题精讲二 30分钟"><span class="num fl">3-11</span><p class="fl">习题精讲二 30分钟</p><span class="time fr">30:20</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_396282" title="习题精讲三 41分钟"><span class="num fl">3-12</span><p class="fl">习题精讲三 41分钟</p><span class="time fr">41:02</span></a>
                      </li>
                                                                                            <li class="chaper">第四章 云计算机与大数据处理</li>
                                                    
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_708638" title="云计算机与大数据处理－本章主要内容简介 9分钟"><span class="num fl">4-1</span><p class="fl">云计算机与大数据处理－本章主要内容简介 9分钟</p><span class="time fr">09:11</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_708637" title="云计算的特征与分类 23分钟"><span class="num fl">4-2</span><p class="fl">云计算的特征与分类 23分钟</p><span class="time fr">22:51</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_708636" title="云计算的关键技术 21分钟"><span class="num fl">4-3</span><p class="fl">云计算的关键技术 21分钟</p><span class="time fr">21:03</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_708635" title="云计算的实施与安全性 18分钟"><span class="num fl">4-4</span><p class="fl">云计算的实施与安全性 18分钟</p><span class="time fr">18:34</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_708634" title="大数据基本概念和应用 18分钟"><span class="num fl">4-5</span><p class="fl">大数据基本概念和应用 18分钟</p><span class="time fr">17:26</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_708633" title="大数据处理技术 44分钟"><span class="num fl">4-6</span><p class="fl">大数据处理技术 44分钟</p><span class="time fr">43:58</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_708632" title="云计算与大数据处理-章节知识总结 15分钟"><span class="num fl">4-7</span><p class="fl">云计算与大数据处理-章节知识总结 15分钟</p><span class="time fr">15:45</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_708631" title="云计算与大数据处理-题精讲一 24分钟"><span class="num fl">4-8</span><p class="fl">云计算与大数据处理-题精讲一 24分钟</p><span class="time fr">24:30</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_708630" title="云计算与大数据处理-习题精讲二 40分钟"><span class="num fl">4-9</span><p class="fl">云计算与大数据处理-习题精讲二 40分钟</p><span class="time fr">40:06</span></a>
                      </li>
                                                                        
                    
                      <li class="lesson exam ">
                        <a href="/center/course/lesson/index?id=12703_719931" title="云计算与大数据处理  作业"><span class="num fl">4-10</span><i class="icon"></i></span><p class="fl">云计算与大数据处理  作业</p><span class="look fr">查看练习</span></a>
                      </li>
                                                                                            <li class="chaper">第五章 非关系数据库NoSQL</li>
                                                    
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_713072" title="非关系数据库NoSQL-章节内容介绍"><span class="num fl">5-1</span><p class="fl">非关系数据库NoSQL-章节内容介绍</p><span class="time fr">11:11</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_713071" title="NoSQL相关理论基础：一致性理论"><span class="num fl">5-2</span><p class="fl">NoSQL相关理论基础：一致性理论</p><span class="time fr">29:09</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_714977" title="NoSQL相关理论基础：分区、存储分布、查询模型"><span class="num fl">5-3</span><p class="fl">NoSQL相关理论基础：分区、存储分布、查询模型</p><span class="time fr">46:12</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_714976" title="NoSQL数据库的类型"><span class="num fl">5-4</span><p class="fl">NoSQL数据库的类型</p><span class="time fr">51:16</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_714975" title="NoSQL章节知识要点小结"><span class="num fl">5-5</span><p class="fl">NoSQL章节知识要点小结</p><span class="time fr">17:42</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_716965" title="NoSQL习题讲解一"><span class="num fl">5-6</span><p class="fl">NoSQL习题讲解一</p><span class="time fr">25:20</span></a>
                      </li>
                                                                        
                                          <li class="lesson ">
                        <a href="/center/course/lesson/index?id=12703_716964" title="NoSQL习题讲解二"><span class="num fl">5-7</span><p class="fl">NoSQL习题讲解二</p><span class="time fr">15:08</span></a>
                      </li>
                                                                        
                    
                      <li class="lesson exam ">
                        <a href="/center/course/lesson/index?id=12703_719930" title="非关系数据库NoSQL-章节配套习题"><span class="num fl">5-8</span><i class="icon"></i></span><p class="fl">非关系数据库NoSQL-章节配套习题</p><span class="look fr">查看练习</span></a>
                      </li>
 </ul>
"""

soup = BeautifulSoup(html_string, "html.parser")

lesson_list = soup.find_all("li", class_="lesson")

# 遍历所有课程项
for li in lesson_list:
    lesson_num = li.find("span", class_="num").get_text(strip=True)  # 课程编号
    lesson_name = li.find("p", class_="fl").get_text(strip=True)  # 课程名称
    print(f"{lesson_num} {lesson_name}")