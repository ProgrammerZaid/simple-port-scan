from scapy.all import*
def scan_me():
    target=input("IP:")
    port=input("Port:")
    ans,unans=sr(IP(dst=str(target))/TCP(sport=3333,dport=int(port),flags="FPU"),timeout=3,verbose=0)
    if ans:
        for s,r in ans:
            if r.haslayer(TCP) and r[TCP].flags==0x14:
                print("it is open")
                print(ans)
    else:
        print(unans)
        print("it is close")
print("1-scanning")
choose=input()
if choose=="1":
    while 1:
        scan_me()
