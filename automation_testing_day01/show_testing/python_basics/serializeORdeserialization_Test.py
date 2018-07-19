#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: Peng Chao
import json
'''
序列化：把python的对象编码转换为json格式的字符串
	就是把python的内置数据类型（list  tuple  dict）转为str（json格式）
	json-->dump(针对文件) dumps
	


反序列化：把json格式的字符串解码为python数据对象
    就是把str（json格式）转为python内置数据类型（list，dict）
    json-->load(针对文件) loads
    
'''
'''
#字典的序列化与反序列化操作
'''
dict1 ={"Data":{"Order":[{"PhoneNO":"13500000000","RefunName":"未申请","OrderID":"7fa155ca-9aea-4b90-b18d-0c1a87e7286c","OrderStatus":100,"OrderStatusName":"待支付","PayName":"","SaleOrderCode":"KXE201805251002002900000000217","DistributorID":0,"OrderSourceID":0,"ShopID":0,"WareHouseID":0,"SubmitDate":"0001-01-01 00:00:00","PayDate":"0001-01-01 00:00:00","TotalAmount":1,"PayPrice":0.01,"Consignee":"啊路521","Province":"福建省","City":"福州市","District":"仓山区","ConsigneeAddress":"地址2","ConsigneePhone":"13500000000","TransCompanyID":0,"CreateTime":"2018-05-25 10:02:00","Taxes":0.0,"Shipment":0.0,"CouponFee":0.0,"WarehouseName":'null',"DeliveryTime":"0001-01-01 00:00:00","OrderType":'null',"ReportType":'null',"Address":"福建省福州市仓山区地址2","PayPlatformName":'null',"SkuKeyInfo":'null',"nickname":'null',"ParentName":'null',"ParentDealerID":16,"TotalPayPrice":0.01}],"Consignee":[{"Consignee":"啊路521","Province":"福建省","City":"福州市","District":"仓山区","Street":"仓山镇","ConsigneeAddress":"地址2","ConsigneePhone":"13500000000","Address":"福建省福州市仓山区仓山镇地址2"}],"Commodity":[{"Thumb":"http://108.52.223.203:80/TempUpload//Comp052156506.jpg","CommodityName":"哈密瓜","Property":"500g","RecommendSalePrice":0.01,"Amount":1,"CommodityID":41,"SkuKey":"20180521001","StockAmount":0,"SalePrice":0.01}],"OrderTrack":[{"OrderTrackID":"b7e6e21a-1027-4a62-9fcd-5ba001909634","OrderID":"7fa155ca-9aea-4b90-b18d-0c1a87e7286c","TrackType":"100","TrackMemo":"提交订单","CreateBy":"217","CreateTime":"2018/5/25 10:02:00","OrderStatusName":"待支付","OuterStatusName":"待支付","PayStatue":"未付款","CreateName":"平常心"}]},"Status":'true',"Message":"请求成功","ResponseCode":0}

#取出data下面->Order->PhoneNO对应的value是不是1350000000
print dict1['Data']['Order'][0]['PhoneNO']

print u'字典未序列化之前的数据类型：{0}'.format(type(dict1))

#对字典dict1进行序列化操作;字典中有中文处理方式：ensure_ascii=False
dict1_str = json.dumps(dict1,ensure_ascii=False)

print u'字典序列化之后：\n',dict1_str,'\n序列化之后得类型为：\n',type(dict1_str)
#将序列化之后得内容进行拆分为list
# s=dict1_str.split(",")
# print s
# print s[4]
#对字符串dict1_str进行反序列化操作
dict2_str = json.dumps(dict1,ensure_ascii=False)
dic_str = json.loads(dict2_str)
#输出格式是字典dict
print u'对字符串dict1_str进行反序列化：\n',dic_str,'\n类型是：',type(dic_str)
#dict2_str = json.loads(dict1_str,encoding='utf-8',ensure_ascii=False)
#print dict2_str
'''
对列表进行序列化与反序列化操作
'''
listt = [1,14,52,36,24,84]
print u'列表listt没有序列化之前得内容：{0},类型：{1}'.format(listt,type(listt))
list_dumps = json.dumps(listt)
print u'对列表进行序列化操作后的内容事：{0},类型：{1}'.format(list_dumps,type(list_dumps))
list_loads = json.loads(list_dumps)
print u'对字符串list_dumps进行反序列化操作后的内容是：{0},类型：{1}'.format(list_loads,type(list_loads))
'''
对元组进行序列化与反序列化操作,结果是list列表

'''
tuple1 = (24,51,28,98,63,0,14)
print u'元组未序列化之前的内容：{0},类型：{1}'.format(tuple1,type(tuple1))
tuple1_dumps=json.dumps(tuple1)
print u'元组进行序列化之后得内容是：{0},类型是：{1}'.format(tuple1_dumps,type(tuple1_dumps))
tuple1_loads = json.loads(tuple1_dumps)
print u'对字符串进行反序列化后得内容：{0}，类型是：{1}'.format(tuple1_loads,type(tuple1_loads))

'''
文件的序列化与反序列化运用
序列化：就是将内容写入到文件中
反序列化：就是读取文件中的内容
'''
data = {'name':'admin'}
print type(data)
data1 = json.dump(data,'t.text','w')



