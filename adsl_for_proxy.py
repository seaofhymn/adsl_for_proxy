import redis
import os
import re
import time
import subprocess

def get_ip():
    while True:
        ret = os.popen('ifconfig').read()
        pattern = re.compile('ppp0' + '.*?inet.*?(\d+\.\d+\.\d+\.\d+).*?netmask', re.S)
        result = re.search(pattern, ret)
        if result:
            ip = result.group(1)
            return str(ip)
        else:
            pass

def main():
    while True:
        try:
            r = redis.StrictRedis(host="", port=6379, password="", decode_responses=True,
                                  db=0)
            r.delete('proxy')
            print("删除完毕")
            print("重新拨号")
            os.system("pppoe-stop")
            time.sleep(2)
            (status, output) = subprocess.getstatusoutput("pppoe-start")
            while True:
                if status == 0:
                    print("拨号完毕")
                    r = redis.StrictRedis(host="", port=6379, password="", decode_responses=True,
                                    db=0)
                    ip = get_ip()
                    print("得到ip:%s"%ip)
                    r.set('proxy', ip)
                    print("成功写入")
                    print("----------sleeping---------")
                    time.sleep(40)
                    break
                else:
                    continue
        except Exception as e:
            print("错误：%s"%e)
            print("重新开启中")
            os.system("pppoe-stop")
            time.sleep(2)
            os.system("pppoe-start")
            time.sleep(8)

if __name__ == "__main__":
    main()