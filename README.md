#基于Python，前端基于Echarts,按照不同的维度展示数据

###日志可视化三步走
1.按需展示数据。比如统计url,ip,status分别访问多少次，把前几名统计出来:

简单的切割了几百行的日志, 通过readFile.py处理结果：
```base
('208.115.111.74', '/robots.txt', '404', 3)
('111.85.41.230', '/data/uploads/2014/0801/11/small_53db0525e3c0a.jpg', '200', 2)
('111.85.41.230', '/data/uploads/2014/0801/11/small_53db052801af8.jpg', '200', 2)
('198.245.51.90', '/robots.txt', '404', 2)
('111.85.41.230', '/data/uploads/2014/0801/11/small_53db051a317e8.jpg', '200', 2)
('111.85.41.230', '/data/uploads/2014/0801/11/small_53db051d2f4e2.jpg', '200', 2)
('111.85.41.230', '/data/uploads/2014/0801/11/small_53db052cda7f7.jpg', '200', 2)
('111.85.41.230', '/data/uploads/2014/0801/11/small_53db0520523aa.jpg', '200', 2)
('111.85.41.230', '/data/uploads/2014/0801/11/small_53db052374a98.jpg', '200', 2)
('113.95.36.30', '/favicon.ico', '404', 2)
```

2.通过浏览器展示
生成list，通过saver.py把拼接的sql插入Mysql数据库
运行flask_web.py，当用户请求指定的Url，把查询Mysql的结果通过Web展示:
![](https://github.com/luyidong/log_visual/blob/master/screen/http-url.jpg)
3.第二步只是简单的完成了页面展示，为了更好的展示页面，可以借用第三方库Highcharts和Echarts:
拼接Sql
```base
select status,sum(value) from fable_log group by status
+--------+------------+
| status | sum(value) |
+--------+------------+
|    200 |      15529 |
|    206 |          6 |
|    301 |          2 |
|    304 |       3549 |
|    403 |          1 |
|    404 |        847 |
+--------+------------+
6 rows in set (0.02 sec)
```
信息可视化展示
![](https://github.com/luyidong/log_visual/blob/master/screen/http-status.png)

简单的三步，完成了汇总数据的展示，让数据更加一目了然,通过Web图形展示比发邮件读文字强多了。。。

更进一步，比如基于网页埋点做的IP地址位置的数据分析等.
