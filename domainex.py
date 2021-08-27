import socket

print("[1]: get host by name") 
print("[2]: get host by addr")
result_num = int(input("choose num: "))

#set domain url to extract domain ip
if result_num == 1:
    
    #choose what u want
    print("did u want add")
    print("[1]: www.domainname.com") #just write web domain name exaple : google and he will autofill web following www. amd .com
    print("[2]: www.domainname.net") #just write web domain name exaple : google and he will autofill web following www. amd .net
    print("[3]: don't add anything") #write web url examle : www.google.com
    result_num2 =int(input("Choose num: "))

    if result_num2 == 1:
        domain = input("Enter Domain: ")
        www= "www."+domain+".com"
        socket_print = socket.gethostbyname(www)
        print(socket_print)

    elif result_num2 == 2:

        domain = input("Enter Domain: ")
        www2 = "www."+domain+".net"
        socket_print = socket.gethostbyname(www2)
        print(socket_print)

    
    elif result_num2 == 3:
        domain3 = input("Enter Domain Url: ")
        socket_print = socket.gethostbyname(domain3)
        print(socket_print)

    #if u want continue

    print("did u want get host by addr?")
    print("[1]: No")
    print("[2]: Yes")
    result_num3 = int(input('Choose Num: '))

    if result_num3 == 1:
        quit()
    try:
        if result_num3 == 2:
            do_ip = input("Enter Domain IP: ")
            ip_resu = socket.gethostbyaddr(do_ip)
            print(ip_resu)
    except socket.herror:
        print("can't find Domain")

#set domain ip to extract domain url
try:
    if result_num == 2:
        ip = input("Enter Domain ip: ")
        socket_print1 = socket.gethostbyaddr(ip)
        print(socket_print1)
except socket.herror:
    print("can't find Domain")