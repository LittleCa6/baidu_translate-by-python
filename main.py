from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import *
import http.client
import hashlib
import urllib
import random
import json
# 传值给appid
def click_appid():
    res_appid = input_appid_text.get()
    input_appid.configure(text='Appid='+ res_appid[0:7] + 'XXXXXXXXXX')
# 传值给secretKey
def click_secretKey():
    res_secretKey = input_secretKey_text.get()
    input_secretKey.configure(text= 'SecreKey='+ res_secretKey[0:5] +  'XXXXXXXXXXXXXXX')
# 初始化
window = Tk()
window.title('Translate')
window.geometry('1200x500')
# 显示appid和secretKey
input_appid = Label(window,text='Appid')
input_appid.grid(column=0,row=0)
input_secretKey = Label(window,text='SecreKey')
input_secretKey.grid(column=0,row=1)
# 输入appid和secreKey
input_appid_text = Entry(window,width=10)
input_appid_text.grid(column=1,row=0)
input_secretKey_text = Entry(window,width=10)
input_secretKey_text.grid(column=1,row=1)
# 确定输入
input_appid_button = Button(window,text='输入',command=click_appid)
input_appid_button.grid(column=2,row=0)
input_secretKey_button = Button(window,text='输入',command=click_secretKey)
input_secretKey_button.grid(column=2,row=1)
# 单选框(输入语言)
text_fromLang = Label(window,text='输入语言')
text_fromLang.grid(column=0,row=2)
text_fromcombo = Combobox(window)
text_fromcombo['values'] = ('auto','zh','en','jp','kor','wyw',)
text_fromcombo.current(0)
text_fromcombo.grid(column=1,row=2)
# 单选框(输出语言)
text_toLang = Label(window,text='输出语言')
text_toLang.grid(column=0,row=3)
text_tocombo = Combobox(window)
text_tocombo['values'] = ('zh','en','jp','kor','wyw',)
text_tocombo.current(0)
text_tocombo.grid(column=1,row=3)
# 翻译
empty_text = Label(window,text='')
empty_text.grid(column=0,row=4)
input_q = scrolledtext.ScrolledText(window,width=30)
input_q.grid(column=0,row=5)
# 翻译
def Translate():
    input_dst.delete(1.0, END)
    fromLang = text_fromcombo.get()
    toLang = text_tocombo.get()
    appid = '20190123000258725'
    secretKey = 'Iqp0DZAzdo9J6XWEaUi1'


    # appid = input_appid_text.get()
    # secretKey = input_secretKey_text.get()
    q = input_q.get(1.0,'end')
    httpClient = None
    myurl = '/api/trans/vip/translate'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        result_trans_result = result['trans_result'][0]['dst']
        input_dst.insert(INSERT, result_trans_result)
        print(result)
    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()

translate_text = Button(window,text='翻译',command=Translate)
translate_text.grid(column=1,row=5)
input_dst = scrolledtext.ScrolledText(window,width=100)
input_dst.grid(column=2,row=5)

window.mainloop()





