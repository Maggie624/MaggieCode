"""
hotfix
"""
import unittest
import os
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from HTMLTestRunner import HTMLTestRunner
import time

from TBtestProject.data import mail
import smtplib
from TBtestProject.case.models.HTMLTestRunner import HTMLTestRunner
# from HTMLTestRunner import HTMLTestRunner

def add_cases(test_dir, pattern='test_*.py'):
    """加载测试用例"""
    discover = unittest.defaultTestLoader.discover(test_dir, pattern=pattern)
    return discover

def run_test(discover):
    """运行所有测试用例，生成测试报告"""
    report_dir = os.path.dirname(os.path.dirname(__file__)) + '/report/'
    now = time.strftime('%Y-%m-%d-%H:%M:%S')
    file_name = report_dir + now + 'result.html'
    print("file_name="+file_name)
    fp = open(file_name, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description=now+'\n'+'测试用例执行情况：')
    runner.run(discover)
    fp.close()

def get_newest_report():
    """返回最新生成的测试报告的文件路径"""
    report_dir = os.path.dirname(os.path.dirname(__file__)) + '/report/'
    lists = os.listdir(report_dir)
    lists.sort(key=lambda fn: os.path.getmtime((report_dir + '/' + fn)))
    print(lists)
    file_new = os.path.join(report_dir, lists[-1])
    print("file_new"+file_new)
    print(file_new)
    return file_new


def send_email():
    """发送邮件，测试报告的内容作为邮件主体"""
    report_url = get_newest_report()
    fp = open(report_url, 'rb')
    body = fp.read()               # 正文
    fp.close()
    subject = report_url.split('/')[-1].replace('result.html', '')+' 测试报告'     # 标题

    msg = MIMEMultipart('alternative')
    msg['Subject'] = Header(subject, 'utf-8')
    text = MIMEText(body, 'html', 'utf-8')
    msg.attach(text)     # 添加正文

    att = MIMEText(body, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = "attachment;filename=" + report_url.split('/')[-1]
    print('1111======'+att['Content-Disposition'])
    msg.attach(att)     # 添加附件

    smtp = smtplib.SMTP()
    smtp.connect(mail.smtpserver)
    smtp.login(mail.sender, mail.psw)
    smtp.sendmail(mail.sender, mail.receiver, msg.as_string())
    smtp.quit()

if __name__ == "__main__":

    test_dir = os.path.dirname(__file__) + '/test_case'
    discover = add_cases(test_dir)  # 获取test_case下的所有测试用例
    run_test(discover)
    send_email()