import urllib
import requests
import os
from time import sleep

proxy = {
    'http': 'http://178.62.24.94:80',
}



def getRange(ip_add):
    target = 'https://www.statsnode.com/reverse-ip-lookup/' + ip_add + '/'
    try:
        pagedata = urllib.urlopen(target, proxies=proxy).read()
        sleep(2)
    except:
        pass
    ranges = pagedata.split('/reverse-ip-lookup/')
    ranges[0] = ''
    for ips in ranges:
        my_ip = ips.split('/')[0]
        if my_ip == '':
            continue
        open('vuln666.txt', 'a+').write(my_ip + '\n')

def revLook(filename):
    ip_list = open(filename, 'r').read().split('\n')
    
os.system('clear')
def main():
    print '                                                  '
    print '                                                  '
    print '   ### ######     ######                               '
    print '    #  #     #    #     #   ##   #    #  ####  ######  '
    print '    #  #     #    #     #  #  #  ##   # #    # #       '
    print '    #  ######     ######  #    # # #  # #      #####   '
    print '    #  #          #   #   ###### #  # # #  ### #       '
    print '    #  #          #    #  #    # #   ## #    # #       '
    print '   ### #          #     # #    # #    #  ####  ######  '
    print '                                                  '
    print '        '
    print '    #####                                              '
    print '   #     #  ####    ##   #    # #    # ###### #####    '
    print '   #       #    #  #  #  ##   # ##   # #      #    #   '
    print '    #####  #      #    # # #  # # #  # #####  #    #   '
    print '         # #      ###### #  # # #  # # #      #####    '
    print '   #     # #    # #    # #   ## #   ## #      #   #    '
    print '    #####   ####  #    # #    # #    # ###### #    #   '
    print '                                                  '
    print '               IP RANGE SCANNER V2                                     '
    print '                                                  '
    print '                 Created Murrez                   '
    print '         https://instagram:/murrez.sec/           '
    print '                                                  '
    print '         [+] No IP Ban                            '
    print '         [+] Proxy Actived                        '
    print '         [+] Auto ViewDNS IP Scan                        '
    print '                                                  '
    firstRun = raw_input(' IP list ? : ')
    boostMode = raw_input(' Starting ? : ')
    if boostMode == '':
        firstRun = open(firstRun, 'r').read().split('\n')
        for indIP in firstRun:
            getRange(indIP)
        tmp = open('vuln666.txt', 'r').readlines()
        print ' Number of IPs\'s  : ' + str(len(tmp)-1)
        revLook('vuln666.txt')
    else:
        tmp = open(firstRun, 'r').readlines()
        print ' Number of IPs \'s  : ' + str(len(tmp))
        revLook(firstRun)
main()
def viewDNS():
os.system('python viewdns.py')
viewDNS()