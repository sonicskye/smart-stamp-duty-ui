'''
sonicskye
ftest.py
Contains commands to test the functions on functions.py
'''

import w3functions as f
import utilities as u
import bloomfilter as b
import binascii

web3 = f.web3
###################################### testing #######################################

#funcName = "getPaymentOfStampAtIndex"
#params = ("0x01",1)
#print(callfunc(contractAddress, contractAbi, funcName, params))


#successful
privKey = "0b295aa109fcc22c6bc165fa213c952523cf1bef115483992e2afd8ccb47991e"
addr = "0x06667BE53072905D1146f0Ab303D2a059c684F3a"
print (f.createstamp(web3.toBytes(1), "Rp3000", 3000, "UU Bea Meterai 1985", True, addr, privKey))
print (f.createstamp(web3.toBytes(2), "Rp6000", 6000, "UU Bea Meterai 1985", True, addr, privKey))
print (f.createstamp(web3.toBytes(3), "Rp500", 500, "UU Bea Meterai 1985 tapi sudah tidak laku", False, addr, privKey))
print (f.createstamp(web3.toBytes(4), "Rp1000", 1000, "UU Bea Meterai 1985 tapi sudah tidak laku", False, addr, privKey))

#activation and deactivation
print (f.stampdeactivate(web3.toBytes(1), addr, privKey))
print (f.stampactivate(web3.toBytes(1), addr, privKey))

ts, st = u.gettimestamp()
print (f.createpayment(u.sha1string(u.sha1string("abc") + addr + "0x0100000000000000000000000000000000000000000000000000000000000000" + st), u.sha1string("abc"), web3.toBytes(1), b.createstringbloomfilter(u.getwords("bloom filter one")), addr, privKey))
print (f.createpayment(u.sha1string(u.sha1string("def") + addr + "0x0200000000000000000000000000000000000000000000000000000000000000" + st), u.sha1string("def"), web3.toBytes(2), b.createstringbloomfilter(u.getwords("bloom filter one two")), addr, privKey))
print (f.createpayment(u.sha1string(u.sha1string("ghi") + addr + "0x0100000000000000000000000000000000000000000000000000000000000000" + st), u.sha1string("ghi"), web3.toBytes(1), b.createstringbloomfilter(u.getwords("bloom filter one two three")), addr, privKey))
print (f.createpayment(u.sha1string(u.sha1string("jkl") + addr + "0x0200000000000000000000000000000000000000000000000000000000000000" + st), u.sha1string("jkl"), web3.toBytes(2), b.createstringbloomfilter(u.getwords("bloom filter one two three four")), addr, privKey))
print (f.createpayment(u.sha1string(u.sha1string("mno") + addr + "0x0200000000000000000000000000000000000000000000000000000000000000" + st), u.sha1string("mno"), web3.toBytes(2), b.createstringbloomfilter(u.getwords("bloom filter one two three four five")), addr, privKey))

#print (getstampcount())
#print (getstamplist())

print (f.getstampcount())

stampCodes = f.getstamplist()
#print (stampCodes)
for stampCode in stampCodes:
    #print(web3.toHex(stampCode))
    stampDetail = f.getstampdetail(web3.toHex(stampCode))
    # @dev hexlify to convert it into hex values
    # @dev then decode to remove the b
    print (stampDetail)
    #print(binascii.hexlify(stampDetail[0]).decode('utf-8'))
    #results:
    #0x0100000000000000000000000000000000000000000000000000000000000000
    #0x0200000000000000000000000000000000000000000000000000000000000000

print (f.getpaymentcount())
paymentCodes = f.getpaylist()
for paymentCode in paymentCodes:
    print(f.getpaymentdetail(web3.toHex(paymentCode)))

#print (eventstampdutypayment(web3.toBytes(1)))
#print (eventstampdutypayment(addr))

message = "abc"
signature = f.sign(message, privKey)
print(signature)
print(f.verifysignfrommessage(message, signature, addr))