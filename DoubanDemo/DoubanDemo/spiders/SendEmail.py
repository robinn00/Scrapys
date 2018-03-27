#!/usr/bin/python
# _*_ coding:utf-8 _*_
# author:robinn

from scrapy.mail import MailSender

if __name__ == "__main__":
    ms = MailSender(smtphost="smtp.163.com",mailfrom="ozivizo@163.com",smtpuser="ozivizo@163.com",smtppass="doxdox45600",smtpport=25,smtptls=True)
    ms.send(to='3110056662@qq.com',subject='testhe',body='ssssssssssss',cc='1641213130@qq.com',mimetype="text/plain")