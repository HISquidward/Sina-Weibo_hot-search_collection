import time
import pandas as pd
import requests
import re
import csv
import urllib3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


df = pd.read_csv('2022-03-04热搜.csv')

print(df)

number = '990340996@qq.com'
smtp = 'ypdvamqiieufbbbe'
to = '761454838@qq.com'  # 可以是非QQ的邮箱

mer = MIMEMultipart()
# 设置邮件正文内容
head = '''
<p>微博热搜榜信息</p>
<p>最热门词条为</p>
<p><a href="{}">{}-----{}</a></p>
<p>排名前五的热搜</p>
<p><a href="{}">{}>-----{}</a></p>
<p><a href="{}">{}-----{}</a></p>
<p><a href="{}">{}-----{}</a></p>
<p><a href="{}">{}-----{}</a></p>
<p><a href="{}">{}-----{}</a></p>
'''.format(df.iloc[0, :]['网址'], df.iloc[0, :]['标题'], df.iloc[0, :]['热度'],
           df.iloc[1, :]['网址'], df.iloc[1, :]['标题'], df.iloc[1, :]['热度'],
           df.iloc[2, :]['网址'], df.iloc[2, :]['标题'], df.iloc[2, :]['热度'],
           df.iloc[3, :]['网址'], df.iloc[3, :]['标题'], df.iloc[3, :]['热度'],
           df.iloc[4, :]['网址'], df.iloc[4, :]['标题'], df.iloc[4, :]['热度'],
           df.iloc[5, :]['网址'], df.iloc[5, :]['标题'], df.iloc[5, :]['热度'])

mer.attach(MIMEText(head, 'html', 'utf-8'))
fujian = MIMEText(open('2022-03-04热搜.csv', 'rb').read(), 'base64', 'utf-8')
fujian["Content-Type"] = 'application/octet-stream'  # 附件内容
fujian.add_header('Content-Disposition', 'file', filename=('utf-8', '', '微博热搜.csv'))
mer.attach(fujian)

mer['Subject'] = '微博热搜榜单'  # 邮件主题
mer['From'] = number  # 发送人
mer['To'] = to  # 接收人

# 5.发送邮件
s = smtplib.SMTP_SSL('smtp.qq.com', 465)
s.login(number, smtp)
s.send_message(mer)  # 发送邮件
s.quit()
print('成功发送')