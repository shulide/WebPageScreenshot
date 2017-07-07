#! /bin/bash
eval `./process_cgi.sh $*`
echo "Content-type: text/plain; charset=utf-8"  
echo       #此处必须有输出一个空行,所有 CGI 程序都有此规定  

#echo "src="${FORM_src}
#echo "file="${FORM_file}

if [ -z ${FORM_src} ];then
	echo "NOARGS"
	exit 1
fi

if [ -z ${FORM_file} ];then
	echo "NARGS"
	exit 1
fi

pic_root='/home/snapshot/apache-tomcat-7.0.55/webapps/snapshots/pictures'
curpath=`pwd`

if [ ! -d "${pic_root}" ];then
	mkdir -p $pic_root
fi

url="$(echo "${FORM_src}" | base64 -d)"

containitem=false
while read line
do
	result="$(echo "${url}" | grep "${line}")"

	if [[ "$result" != "" ]];then
		containitem=true
		break
	fi
done<urllist.txt

#echo "url=${url}"
#echo "containitem=${containitem}"
if [ "${containitem}" = true ] ; then
	#echo "use slimerjs"
	export SLIMERJSLAUNCHER=${curpath}/firefox/firefox
	export  DISPLAY=:7

	./slimerjs-0.10.3/slimerjs  ./slimerjs-0.10.3/screenpage.js  "${url}" "${pic_root}/${FORM_file}"  >>/dev/null	
else
	#echo "use wkhtmltoimage"
        ./wkhtmltoimage --quality 30  --load-error-handling ignore "${url}"  "${pic_root}/${FORM_file}"  >>/dev/null
fi

./ftpupload.sh ${pic_root}  ${FORM_file} >>/dev/null
rm -rf ${pic_root}/${FORM_file}

echo "snapshots/${FORM_file}"
