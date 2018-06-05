#coding=utf-8  
  
import socket  
import optparse  
  
def connScan(tgtHost,tgtPort):  
    try:  
        connSkt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
        connSkt.connect((tgtHost,tgtPort))  
        print("[+]%d/tcp open" % tgtPort)  
        connSkt.close()  
    except:   
        print("[-]%d/tcp close" % tgtPort)  
  
def portScan(tgtHost):  
    try:  
        tgtIP = socket.gethostbyname(tgtHost)  
    except:  
        print("[-]cannot connect %s" % tgtIP)  
        return  
    try:  
        tgtName = socket.gethostbyaddr(tgtIP)  
        print("\n[+]Scan results for:" + tgtName[0])  
    except:  
        print("\n[+]scan results for:" + tgtIP)  
        socket.setdefaulttimeout(1)  
        for port in range(0, 65535):  
            print("scanning port:" + str(port))  
            connScan(tgtHost,int(port))   
  
def main():  
    parser = optparse.OptionParser()  
    parser.add_option("-H","--Host",dest='tgtHost',help='input Host address')  
    (options,args) = parser.parse_args()  
    tgtHost = options.tgtHost  
    if (tgtHost == None):  
        print('----you must input Host-----')  
        exit(0)  
    portScan(tgtHost)  
if __name__=='__main__':  
    main() 
