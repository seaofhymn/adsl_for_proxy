# adsl_for_proxy
adsl代理，基于redis数据库
centos7安装tinyproxy：
yum install -y epel-release
yum update -y
yum install -y tinyproxy
vi /etc/tinyproxy/tinyproxy.conf
注释Allow 127.0.0.1
systemctl stop firewalld.service
systemctl enable tinyproxy.service
systemctl restart  tinyproxy.service
