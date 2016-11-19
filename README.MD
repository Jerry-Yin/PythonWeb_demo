python web 开发实例，学习出处：


    http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320118765877e93ecea4e6449acb157e9efae8b40b6000



开源框架：Flask (需要以python3运行)
    http://flask.pocoo.org/

	实际的Web App应该拿到用户名和口令后，去数据库查询再比对，来判断用户是否能登录成功。
	除了Flask，常见的Python Web框架还有：
	Django：全能型Web框架；
	web.py：一个小巧的Web框架；
	Bottle：和Flask类似的Web框架；
	Tornado：Facebook的开源异步Web框架。
	当然了，因为开发Python的Web框架也不是什么难事，我们后面也会讲到开发Web框架的内容。


有了Web框架，我们在编写Web应用时，注意力就从WSGI处理函数转移到URL+对应的处理函数，这样，编写Web App就更加简单了。

在编写URL处理函数时，除了配置URL外，从HTTP请求拿到用户数据也是非常重要的。Web框架都提供了自己的API来实现这些功能。Flask通过request.form['name']来获取表单的内容。

