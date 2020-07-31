def ip_address_check(ip):
    if ip.count(".") != 3:
        return False
    octets = ip.split('.')
    for o in octets:
        if o.isdigit() == False:
            return False
        if int(o) < 0 or int(o) > 255:
            return False
    return True




ip0 = '255.1.3.35'
ans0 = True
ip1 = '270.1.3.35'
ans1 = False
ip2 = '255.1.3'
ans2 = False
ip3 = 'a12.1.3.35'
ans3 = False
assert ip_address_check(ip0) == ans0
assert ip_address_check(ip1) == ans1
assert ip_address_check(ip2) == ans2
assert ip_address_check(ip3) == ans3