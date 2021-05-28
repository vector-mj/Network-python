from scapy.all import ARP, Ether, srp
from colored import fg,bg,attr
import random,os
from time import sleep
def randomColor():
    r = lambda: random.randint(0,255)
    return('#%02X%02X%02X' % (r(),r(),r()))
def banner():
    banners=[
            """
    ┬  ┬┌─┐┌─┐┌┬┐┌─┐┬─┐ [NETWORK SCANNER]
    └┐┌┘├┤ │   │ │ │├┬┘ [github.com/vector-mj]
     └┘ └─┘└─┘ ┴ └─┘┴└─ 
    """
        ]
    print(fg(randomColor())+random.choice(banners)+attr('reset'))
def showScan(target_ip,time,clear):
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    print(""+fg('blue')+"IP"+reset+"-"*15+fg('blue')+"MAC"+reset+"-".ljust(15,"-"))
    res=""
    for client in clients:
        res = "|"+fg('green')+str(client['ip']).ljust(14," ")+reset+"  "+fg('red')+client['mac']+reset+"|"
        print(res)
    print("-"*35)
    sleep(time)
    if clear:
        os.system("cls")
#####################################################
reset= attr('reset')
os.system("cls")
banner()
target_ip = input(fg('blue')+"[*]"+reset+fg('green')+" Enter a CIDR like this "+reset+fg('#FF9800')+"192.168.1.1/24 "+reset+fg('green')+">"+reset)
res = target_ip.split(' ')
if (len(res)==3 and res[1]=='--live'):
    print(fg('blue')+"[*]"+reset+fg('green')+" Scanning ...\n "+reset)
    for i in range(int(res[2])):
        showScan(res[0],0,False)
else:
    print(fg('blue')+"[*]"+reset+fg('green')+" Scanning ...\n "+reset)
    showScan(res[0],0,False)
s = input("END ...")