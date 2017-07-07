  <<使用说明>>
  
一、安装软件组成
（1）下载wkhtmltoimage
wget https://downloads.wkhtmltopdf.org/0.12/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz

（2）下载slimerjs
wget https://download.slimerjs.org/releases/0.10.3/slimerjs-0.10.3.tar.bz2

（3）下载firefox
wget https://ftp.mozilla.org/pub/firefox/releases/38.0/linux-x86_64/zh-CN/firefox-38.0.tar.bz2

（4）安装中文字体
 yum -y groupinstall chinese-support

 vim /etc/sysconfig/i18n
 修改环境变量为：
 =====================================
  LANG="zh_CN.GBK"
  SUPPORTED="zh_CN.UTF-8:zh_CN:zh:en_US.UTF-8:en_US:en"
 =====================================
 使得配置的环境变量生效
  source /etc/sysconfig/i18n
 
 （5）安装Xvfb。
  yum -y install Xvfb
  
 （6）如果是docker的话,运行
  dbus-uuidgen > /var/lib/dbus/machine-id
  重新生成UUID
  
 二、下载解压后整理的文件结构
 注：这里以tomcat 配置cgi的方式。
   -apache-tomcat-7.0.55-src/webapps/snapshots/cgi-bin
   \
   |- firefox        [文件夹]火狐浏览器程序
      |-...
   |- ftpupload.sh  FTP上传程序
   |- process_cgi.sh  CGI解析脚本
   |- slimerjs-0.10.3  [文件夹]SLIMIERJS程序
     |-screenpage.js   网页截图JS脚本程序
	 |-...
   |- snapshot.cgi   截图快照脚本
   |- urllist.txt    区分解析器的URL列表
   |- wkhtmltoimage   wkhtmltoimage截图程序
   
 三、启动Xvfb
  \
   |-xvfb
     |- pro-xvfb.sh
	 |-  readme.txt
	 |-  shutdown-xvfb.sh
	 |-  start-xvfb.sh
  (1)启动xvfb服务
     ./start-xvfb.sh
  (2)停止xvfb服务
	 ./shutdown-xvfb.sh
	 
四、启动停止启动
 （1）启动截图服务
	cd apache-tomcat-7.0.55
	bin/startup.sh 

（2）停止截图服务
	cd apache-tomcat-7.0.55
	bin/shutdown.sh 