# Final

## 数据预分析

|event_time |event_type |product_id |category_id |category_code |brand |price |user_id|user_session|
|-|-|-|-|-|-|-|-|-|

依据以下数据初测，删除下面3列字段
+ `category_code`,train中非nan值占比6164/416962=0.015, test中99/5164=0.019
	主要包含 
	```python
	['accessories.bag', 'accessories.cosmetic_bag', 'apparel.glove',
       'appliances.environment.air_conditioner',
       'appliances.environment.vacuum', 'appliances.personal.hair_cutter',
       'furniture.bathroom.bath', 'furniture.living_room.cabinet',
       'furniture.living_room.chair', 'stationery.cartrige']
	```
+ `brand` train中非nan值站比252018/416962=0.604,test中3088/5164=0.598
	主要包含
	```python
	['airnails', 'almea', 'andrea', 'ardell', 'art-visage', 'artex',
       'australis', 'balbcare', 'barbie', 'batiste', 'beautix',
       'beauty-free', 'beautyblender', 'beauugreen', 'benovy', 'bergamo',
       'bespecial', 'binacil', 'bioaqua', 'biofollica', 'biore', 'blise',
       'blixz', 'bluesky', 'bodipure', 'bodyton', 'bosnic', 'bpw.style',
       'browxenna', 'busch', 'candy', 'carmex', 'chi', 'cnd', 'coifin',
       'concept', 'consly', 'coocla', 'cosima', 'cosmoprofi', 'coxir',
       'cruset', 'cuccio', 'cutrin', 'de.lux', 'deoproce', 'depilflax',
       'dermacol', 'dermal', 'dizao', 'domix', 'dorena', 'dr.gloderm',
       'egomania', 'elizavecca', 'ellips', 'elskin', 'embryolisse',
       'emil', 'enas', 'enigma', 'enjoy', 'entity', 'eos', 'estel',
       'estelare', 'eunyul', 'f.o.x', 'fancy', 'farmavita', 'farmona',
       'farmstay', 'fedua', 'finish', 'fly', 'foamie', 'freedecor',
       'freshbubble', 'frozen', 'gehwol', 'glysolid', 'godefroy', 'grace',
       'grattol', 'happyfons', 'haruyama', 'helloganic', 'i-laq',
       'igrobeauty', 'ingarden', 'inm', 'inoface', 'insight', 'irisk',
       'italwax', 'jaguar', 'jas', 'jessnail', 'joico', 'juno', 'kaaral',
       'kamill', 'kapous', 'kares', 'kaypro', 'keen', 'kerasys', 'keune',
       'kims', 'kinetics', 'kiss', 'kocostar', 'koelcia', 'koelf',
       'konad', 'koreatida', 'kosmekka', 'labay', 'laboratorium', 'lador',
       'ladykin', 'lakme', 'lamixx', 'latinoil', 'lebelage', 'levissime',
       'levrana', 'lianail', 'likato', 'limoni', 'litaline', 'lovely',
       'lowence', 'lsanic', 'lunaris', 'macadamia', 'mane', 'marathon',
       'markell', 'marutaka-foot', 'masura', 'matrix', 'mavala', 'max',
       'meisterwerk', 'metzger', 'mielle', 'milv', 'miskin', 'missha',
       'moyou', 'nagaraku', 'naturmed', 'nefertiti', 'neoleor', 'nirvel',
       'nitrile', 'nitrimax', 'oniq', 'opi', 'orly', 'osmo', 'ovale',
       'parachute', 'petitfee', 'philips', 'plazan', 'pnb', 'polarus',
       'pole', 'profepil', 'profhenna', 'protokeratin', 'provoc',
       'radius', 'rasyan', 'refectocil', 'riche', 'rocknailstar', 'rosi',
       'roubloff', 'runail', 's.care', 'sanoto', 'sawa', 'severina',
       'shary', 'shik', 'siberina', 'skinity', 'skinlite', 'skipofit',
       'smart', 'soleo', 'solomeya', 'sophin', 'staleks', 'strong', 'sun',
       'sunuv', 'supertan', 'swarovski', 'tannymaxx', 'tazol', 'tertio',
       'thuya', 'tosowoong', 'treaclemoon', 'trind', 'uno', 'uskusi',
       'veraclara', 'vilenta', 'voesh', 'vosev', 'weaver', 'yoko',
       'ypsed', 'yu-r', 'zab', 'zeitun', 'zinger']
	```
+ `user_session`意义不明

对数据进行转换
+ `category_id`,后缀都是e+18，处理时去除
	```python
	[1.49e+18, 1.50e+18, 1.51e+18, 1.52e+18, 1.53e+18, 1.54e+18,
       1.55e+18, 1.56e+18, 1.58e+18, 1.59e+18, 1.60e+18, 1.61e+18,
       1.63e+18, 1.64e+18, 1.65e+18, 1.66e+18, 1.72e+18, 1.73e+18,
       1.75e+18, 1.76e+18, 1.78e+18, 1.79e+18, 1.80e+18, 1.81e+18,
       1.82e+18, 1.84e+18, 1.86e+18, 1.87e+18, 1.89e+18, 1.90e+18,
       1.91e+18, 1.92e+18, 1.93e+18, 1.94e+18, 1.96e+18, 1.98e+18,
       1.99e+18, 2.00e+18, 2.01e+18, 2.02e+18, 2.03e+18, 2.04e+18,
       2.06e+18, 2.07e+18, 2.08e+18, 2.09e+18, 2.10e+18, 2.11e+18,
       2.12e+18, 2.13e+18, 2.14e+18, 2.15e+18, 2.16e+18, 2.19e+18,
       2.20e+18]
	```
+ `event_type`,只有4种`['cart', 'purchase', 'remove_from_cart', 'view']`，可以转换成编号
## 用户信息查看
user_id=1的购买历程
```python
                 event_time        event_type  product_id   category_id 
0   2019-10-01 00:00:00 UTC              cart     5773203  1.490000e+18   
1   2019-10-01 00:00:03 UTC              cart     5773353  1.490000e+18   
2   2019-10-01 00:00:07 UTC              cart     5723490  1.490000e+18   
3   2019-10-01 00:02:32 UTC              cart     5857283  1.490000e+18   
4   2019-10-01 00:02:40 UTC              cart     5723523  1.490000e+18   
5   2019-10-01 00:03:23 UTC              cart     5773313  1.490000e+18   
6   2019-10-01 00:05:27 UTC              cart     5659825  1.490000e+18   
7   2019-10-01 00:08:08 UTC  remove_from_cart     5659825  1.490000e+18   
8   2019-10-01 00:12:50 UTC          purchase     5659639  1.490000e+18   
9   2019-10-01 00:12:50 UTC          purchase     5857283  1.490000e+18   
10  2019-10-01 00:12:50 UTC          purchase     5853646  1.490000e+18   
11  2019-10-01 00:12:50 UTC          purchase     5834462  1.490000e+18   
12  2019-10-01 00:12:50 UTC          purchase     5802428  1.490000e+18   
13  2019-10-01 00:12:50 UTC          purchase     5784983  2.200000e+18   
14  2019-10-01 00:12:50 UTC          purchase     5773353  1.490000e+18   
15  2019-10-01 00:12:50 UTC          purchase     5773313  1.490000e+18   
16  2019-10-01 00:12:50 UTC          purchase     5773203  1.490000e+18   
17  2019-10-01 00:12:50 UTC          purchase     5773201  1.490000e+18   
18  2019-10-01 00:12:50 UTC          purchase     5770051  1.490000e+18   
19  2019-10-01 00:12:50 UTC          purchase     5770041  1.490000e+18   
20  2019-10-01 00:12:50 UTC          purchase     5739989  1.490000e+18   
21  2019-10-01 00:12:50 UTC          purchase     5723529  1.490000e+18   
22  2019-10-01 00:12:50 UTC          purchase     5723523  1.490000e+18   
23  2019-10-01 00:12:50 UTC          purchase     5723490  1.490000e+18   
24  2019-10-01 00:12:50 UTC          purchase     5700046  1.490000e+18   
25  2019-10-01 00:12:50 UTC          purchase     5688124  1.490000e+18   
26  2019-10-01 00:12:50 UTC          purchase        5385  1.490000e+18
```
发现标签对应最后一行记录,而且前面竟然没有任何查看记录，另外其余的信息表明最后一条记录不一定是purchase.

对user_id=1的用户记录按照product_id分类
```python
(1, 5385)
                 event_time event_type   category_id  price  user_id
26  2019-10-01 00:12:50 UTC   purchase  1.490000e+18   3.89        1
(1, 5659639)
                event_time event_type   category_id  price  user_id
8  2019-10-01 00:12:50 UTC   purchase  1.490000e+18   0.95        1
(1, 5659825)
                event_time        event_type   category_id  price  user_id
6  2019-10-01 00:05:27 UTC              cart  1.490000e+18   0.95        1
7  2019-10-01 00:08:08 UTC  remove_from_cart  1.490000e+18   0.95        1
(1, 5688124)
                 event_time event_type   category_id  price  user_id
25  2019-10-01 00:12:50 UTC   purchase  1.490000e+18   0.32        1
(1, 5700046)
                 event_time event_type   category_id  price  user_id
24  2019-10-01 00:12:50 UTC   purchase  1.490000e+18    0.4        1
(1, 5723490)
                 event_time event_type   category_id  price  user_id
2   2019-10-01 00:00:07 UTC       cart  1.490000e+18   2.62        1
23  2019-10-01 00:12:50 UTC   purchase  1.490000e+18   2.62        1
(1, 5723523)
                 event_time event_type   category_id  price  user_id
4   2019-10-01 00:02:40 UTC       cart  1.490000e+18   2.62        1
22  2019-10-01 00:12:50 UTC   purchase  1.490000e+18   2.62        1
(1, 5723529)
                 event_time event_type   category_id  price  user_id
21  2019-10-01 00:12:50 UTC   purchase  1.490000e+18   2.94        1
(1, 5739989)
                 event_time event_type   category_id  price  user_id
20  2019-10-01 00:12:50 UTC   purchase  1.490000e+18   3.49        1
(1, 5770041)
                 event_time event_type   category_id  price  user_id
19  2019-10-01 00:12:50 UTC   purchase  1.490000e+18   2.81        1
(1, 5770051)
                 event_time event_type   category_id  price  user_id
18  2019-10-01 00:12:50 UTC   purchase  1.490000e+18   2.81        1
(1, 5773201)
                 event_time event_type   category_id  price  user_id
17  2019-10-01 00:12:50 UTC   purchase  1.490000e+18   2.62        1
(1, 5773203)
                 event_time event_type   category_id  price  user_id
0   2019-10-01 00:00:00 UTC       cart  1.490000e+18   2.62        1
16  2019-10-01 00:12:50 UTC   purchase  1.490000e+18   2.62        1
(1, 5773313)
                 event_time event_type   category_id  price  user_id
5   2019-10-01 00:03:23 UTC       cart  1.490000e+18   2.62        1
15  2019-10-01 00:12:50 UTC   purchase  1.490000e+18   2.62        1
(1, 5773353)
                 event_time event_type   category_id  price  user_id
1   2019-10-01 00:00:03 UTC       cart  1.490000e+18   2.62        1
14  2019-10-01 00:12:50 UTC   purchase  1.490000e+18   2.62        1
(1, 5784983)
                 event_time event_type   category_id  price  user_id
13  2019-10-01 00:12:50 UTC   purchase  2.200000e+18   1.24        1
(1, 5802428)
                 event_time event_type   category_id  price  user_id
12  2019-10-01 00:12:50 UTC   purchase  1.490000e+18   0.44        1
(1, 5834462)
                 event_time event_type   category_id  price  user_id
11  2019-10-01 00:12:50 UTC   purchase  1.490000e+18   0.79        1
(1, 5853646)
                 event_time event_type   category_id  price  user_id
10  2019-10-01 00:12:50 UTC   purchase  1.490000e+18   0.79        1
(1, 5857283)
                event_time event_type   category_id  price  user_id
3  2019-10-01 00:02:32 UTC       cart  1.490000e+18   2.62        1
9  2019-10-01 00:12:50 UTC   purchase  1.490000e+18   2.62        1
```

train数据集和test数据集中的user_id互不重合，因此需要依赖train用户购买记录进行分类，并将test中的用户映射进前面的分类。

## XGBoost
先对用户特征手动提取，之后在XGBoost里分类，训练不出来，而且手动提取特征损失了信息。

## 基于item的推荐算法
在不考虑时间顺序的情况下，根据用户的购买记录，按照item进行分类，评分使用操作进行分数叠加

### 无监督学习
另外trival的想法，某个商品用户浏览次数较多，而且还没有购买，那么极有可能会再次进行操作。通过这种方式引入时序和操作信息。
+ 直接选择最多的商品 0.215 / 209
+ 直接选择最后一次的商品 0.236 / 183

选择出现次数最多的商品没有考虑删除购物车的操作，需要正向处理
+ 将cart=5,remove_from_cart=-5, purchase=-10,view=1
+ 选择加权值最大，且最后一次操作，次数最多的商品 0.269 / 147

尝试提高view的权重至2，并没有明显变化
### 监督学习-权重法

将权重在训练集里学习，然后再预测

