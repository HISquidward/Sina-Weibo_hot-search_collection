# coding: utf-8
import time
import pandas as pd
import requests
import re
import csv
import urllib3
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


if __name__ == "__main__":
    # os.environ['NO_PROXY'] = 'https://tophub.today/n/KqndgxeLl9'

    urllib3.disable_warnings()

    now_time = int(time.time())
    timeArray = time.localtime(now_time)
    date = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(type(date))

    name = date[:13] + ':00_热搜.csv'

    f = open(name, mode='a', encoding='utf-8', newline='')
    csv_writer = csv.DictWriter(f, fieldnames=[
        '排名',
        '标题',
        '热度',
        '网址'
    ])
    csv_writer.writeheader()

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    headers = {
        'User-Agent': user_agent
    }

    url = 'https://tophub.today/n/KqndgxeLl9'  # 微博网址
    ret = requests.get(url, verify=False, headers=headers)
    test = ret.text  # .encode('iso-8859-1').decode('utf-8')

    u_title = '<td class="al"><a href=".*?" target="_blank" rel="nofollow" itemid=".*?">(.*?)</a></td>'

    u_amount = '<td>(.*?)</td>'

    u_num = '<td align="center">(.*?).</td>'

    u_url = '<td align="right"><a class="collect-a" href="(.*?) title="查看详细" target="_blank" rel="nofollow"><i class="m-n">&#xe652;</i></a></td>'

#    https: // tophub.today /l?

    title = re.findall(u_title, test)
    amount = re.findall(u_amount, test)
    category = re.findall(u_num, test)
    href = re.findall(u_url, test)
    title = title[:50]
    amount = amount[:50]

    for i in range(len(category)):
        new_category = category[i]
        new_href = href[i]
        new_title = title[i]
        new_amount = amount[i]

        dit = {
            '排名': new_category,
            '标题': new_title,
            '热度': new_amount,
            '网址': 'https://tophub.today' + new_href
        }
        print(dit)
        csv_writer.writerow(dit)

    file = name
    df = pd.read_csv(name)

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
    <p><a href="{}">{}-----{}</a></p>
    <p><a href="{}">{}-----{}</a></p>
    <p><a href="{}">{}-----{}</a></p>
    <p><a href="{}">{}-----{}</a></p>
    '''.format(df.iloc[0, :]['网址'], df.iloc[0, :]['标题'], df.iloc[0, :]['热度'],
               df.iloc[1, :]['网址'], df.iloc[1, :]['标题'], df.iloc[1, :]['热度'],
               df.iloc[2, :]['网址'], df.iloc[2, :]['标题'], df.iloc[2, :]['热度'],
               df.iloc[3, :]['网址'], df.iloc[3, :]['标题'], df.iloc[3, :]['热度'],
               df.iloc[4, :]['网址'], df.iloc[4, :]['标题'], df.iloc[4, :]['热度'],
               df.iloc[5, :]['网址'], df.iloc[5, :]['标题'], df.iloc[5, :]['热度'],
               df.iloc[6, :]['网址'], df.iloc[6, :]['标题'], df.iloc[6, :]['热度'],
               df.iloc[7, :]['网址'], df.iloc[7, :]['标题'], df.iloc[7, :]['热度'],
               df.iloc[8, :]['网址'], df.iloc[8, :]['标题'], df.iloc[8, :]['热度'],
               df.iloc[9, :]['网址'], df.iloc[9, :]['标题'], df.iloc[9, :]['热度'])

    mer.attach(MIMEText(head, 'html', 'utf-8'))
    fujian = MIMEText(open(name, 'rb').read(), 'base64', 'utf-8')
    fujian["Content-Type"] = 'application/octet-stream'  # 附件内容
    fujian.add_header('Content-Disposition', 'file', filename=('utf-8', '', '微博热搜.csv'))
    mer.attach(fujian)

    mer['Subject'] = date[:13] + ':00 微博热搜榜单'  # 邮件主题
    mer['From'] = (u'阿鹏的消息助手 <%s>' % number)  # 发送人
    mer['To'] = to  # 接收人

    # 5.发送邮件
    s = smtplib.SMTP_SSL('smtp.qq.com', 465)
    s.login(number, smtp)
    s.send_message(mer)  # 发送邮件
    s.quit()
    print('成功发送')





