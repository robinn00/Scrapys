#!/usr/bin/python
# _*_ coding:utf-8 _*_
# author:robinn

from scrapy.mail import MailSender

if __name__ == "__main__":
    ms = MailSender(smtphost="smtp.163.com",mailfrom="@163.com",smtpuser="@163.com",smtppass="",smtpport=25,smtptls=True)
    ms.send(to='@qq.com',subject='testhe',body='ssssssssssss',cc='@qq.com',mimetype="text/plain")