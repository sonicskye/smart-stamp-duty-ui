import functions as f
import utilities as u

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

print (f.createpayment(web3.toBytes(5), u.getsha1string("abc"), web3.toBytes(1), "bloom filter", addr, privKey))
print (f.createpayment(web3.toBytes(6), u.getsha1string("def"), web3.toBytes(2), "bloom filter2", addr, privKey))
print (f.createpayment(web3.toBytes(7), u.getsha1string("ghi"), web3.toBytes(1), "bloom filter3", addr, privKey))
print (f.createpayment(web3.toBytes(8), u.getsha1string("jkl"), web3.toBytes(2), "bloom filter4", addr, privKey))

#print (getstampcount())
#print (getstamplist())

print (f.getstampcount())
stampCodes = f.getstamplist()
for stampCode in stampCodes:
    #print(web3.toHex(stampCode))
    print(f.getstampdetail(web3.toHex(stampCode)))
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