  <<ʹ��˵��>>
  
һ����װ������
��1������wkhtmltoimage
wget https://downloads.wkhtmltopdf.org/0.12/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz

��2������slimerjs
wget https://download.slimerjs.org/releases/0.10.3/slimerjs-0.10.3.tar.bz2

��3������firefox
wget https://ftp.mozilla.org/pub/firefox/releases/38.0/linux-x86_64/zh-CN/firefox-38.0.tar.bz2

��4����װ��������
 yum -y groupinstall chinese-support

 vim /etc/sysconfig/i18n
 �޸Ļ�������Ϊ��
 =====================================
  LANG="zh_CN.GBK"
  SUPPORTED="zh_CN.UTF-8:zh_CN:zh:en_US.UTF-8:en_US:en"
 =====================================
 ʹ�����õĻ���������Ч
  source /etc/sysconfig/i18n
 
 ��5����װXvfb��
  yum -y install Xvfb
  
 ��6�������docker�Ļ�,����
  dbus-uuidgen > /var/lib/dbus/machine-id
  ��������UUID
  
 �������ؽ�ѹ��������ļ��ṹ
 ע��������tomcat ����cgi�ķ�ʽ��
   -apache-tomcat-7.0.55-src/webapps/snapshots/cgi-bin
   \
   |- firefox        [�ļ���]������������
      |-...
   |- ftpupload.sh  FTP�ϴ�����
   |- process_cgi.sh  CGI�����ű�
   |- slimerjs-0.10.3  [�ļ���]SLIMIERJS����
     |-screenpage.js   ��ҳ��ͼJS�ű�����
	 |-...
   |- snapshot.cgi   ��ͼ���սű�
   |- urllist.txt    ���ֽ�������URL�б�
   |- wkhtmltoimage   wkhtmltoimage��ͼ����
   
 ��������Xvfb
  \
   |-xvfb
     |- pro-xvfb.sh
	 |-  readme.txt
	 |-  shutdown-xvfb.sh
	 |-  start-xvfb.sh
  (1)����xvfb����
     ./start-xvfb.sh
  (2)ֹͣxvfb����
	 ./shutdown-xvfb.sh
	 
�ġ�����ֹͣ����
 ��1��������ͼ����
	cd apache-tomcat-7.0.55
	bin/startup.sh 

��2��ֹͣ��ͼ����
	cd apache-tomcat-7.0.55
	bin/shutdown.sh 