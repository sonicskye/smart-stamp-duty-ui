'''
sonicskye
w3functions.py
Contains reusable functions for the program
'''

from web3 import Web3
from eth_account.messages import defunct_hash_message
from vars import provider, contractAbi, contractAddress, chainID
import utilities as u
import binascii



# @dev instantiation of Web3 class
web3 = Web3(Web3.HTTPProvider(provider, request_kwargs={'timeout': 60}))


# @dev createnewkey will create an Ethereum keypair. It returns address and private key respectively
# @param password is the password to generate the keypair
# @param address is the first output
# @param privateKey is the second output
"""
# keypair generation
addr,privkey = createnewkeylocal('abc')
print(addr,privkey)
"""
def createnewkeylocal(password):
    acct = w3.eth.account.create(password)
    return acct.address, acct.privateKey.hex()


# @dev gasprice computes the gas price
# @dev manually determined
# @dev for testing, set gasprice to 0
# @Todo create gas strategy https://web3py.readthedocs.io/en/stable/gas_price.html
def gasprice():
    return web3.toWei(3, 'gwei')


# @dev nonce computes the nonce or the number of transactions created by the address
def nonce(address):
    return web3.eth.getTransactionCount(address)


# @dev callfunc is a common function to call a contract's function
# @dev can only be used to call functions without arguments
# @param cAddress is contract address
# @param cAbi is contract ABI
def callfunc(cAddress, cAbi, functionName):
    myContract = web3.eth.contract(address=cAddress, abi=cAbi)
    functionToCall = myContract.functions[functionName]
    functionResult = functionToCall().call()
    return functionResult


# @dev getstampcount calls "getStampCount" function in smart contract
# @dev returns number of stamp
def getstampcount():
    functionName = "getStampCount"
    return callfunc(contractAddress, contractAbi, functionName)


# @dev getstamplist calls "getStampList" function in smart contract
# @dev returns a list of stamps
def getstamplist():
    functionName = "getStampList"
    return callfunc(contractAddress, contractAbi, functionName)


# @dev getstampcodes gets stamp codes only and put them in an array
def getstampcodes():
    stampCodes = getstamplist()
    stampCodeList = []
    stampCodeList.clear()
    for stampCode in stampCodes:
        #print (stampCode)
        stampCodeList.append(binascii.hexlify(stampCode).decode('utf-8'))
    return stampCodeList


# @dev getstampdetail calls "getStampDetail" function in smart contract
# @dev returns the detail of the stamp based on stampcode: StampCode, StampName, StampPrice, RegulationReference, StampIndex, IsActive
# @param stampcode is the primary key or identifier for the stamp
def getstampdetail(stampcode):
    myContract = web3.eth.contract(address=contractAddress, abi=contractAbi)
    functionName = "getStampDetail"
    functionToCall = myContract.functions[functionName]
    functionResult = functionToCall(stampcode).call()
    return functionResult


def getstampnamefromcode(stampcode):
    myContract = web3.eth.contract(address=contractAddress, abi=contractAbi)
    functionName = "getStampDetail"
    functionToCall = myContract.functions[functionName]
    functionResult = functionToCall(stampcode).call()
    return functionResult[1]


# @dev getstampactivation checks the isactive status of stampcode
def getstampactivation(stampcode):
    stampDetail = getstampdetail(stampcode)
    return stampDetail[5]


# @dev getstampcodes gets stamp codes only and put them in an array
def getactivestampcodes():
    stampCodes = getstamplist()
    stampCodeList = []
    stampCodeList.clear()
    for stampCode in stampCodes:
        if getstampactivation(stampCode):
            stampCodeList.append(binascii.hexlify(stampCode).decode('utf-8'))
    return stampCodeList


# @dev getpaymentcount calls "getPaymentCount" function in smart contract
# @dev returns number of stamp
def getpaymentcount():
    functionName = "getPaymentCount"
    return callfunc(contractAddress, contractAbi, functionName)


# @dev getpaylist calls "getPayList" function in smart contract
# @dev returns a list of stamps
def getpaylist():
    functionName = "getPayList"
    return callfunc(contractAddress, contractAbi, functionName)


# @dev getpaymentdetail calls "getPaymentDetail" function in smart contract
# @dev returns the detail of the stamp based on payCode
# @param payCode is the primary key or identifier for the payment
def getpaymentdetail(payCode):
    myContract = web3.eth.contract(address=contractAddress, abi=contractAbi)
    functionName = "getPaymentDetail"
    functionToCall = myContract.functions[functionName]
    functionResult = functionToCall(payCode).call()
    return functionResult


# @dev createstamp executes transaction "createStamp" function in smart contract and sends it to the network
# @dev returns the transaction ID
# @param bytes32 StampCode;
# @param string StampName;
# @param uint32 StampPrice;
# @param string RegulationReference;
# @param bool IsActive;
def createstamp(stampcode, stampname, stampprice, regulationreference, isactive, address, privateKey):
    # gas cost based on trial on Remix is 158985
    # gas cost based on trial on Ganache is 174771 and 173969
    # for Rinkeby, give more gas
    gas = 3000000
    myContract = web3.eth.contract(address=contractAddress, abi=contractAbi)
    detailTx = {'chainId': chainID, 'gas': gas, 'gasPrice': gasprice(), 'nonce': nonce(address), }
    unsignedTx = myContract.functions.createStamp(stampcode, stampname, stampprice, regulationreference, isactive).buildTransaction(detailTx)
    signedTx = web3.eth.account.signTransaction(unsignedTx, private_key=privateKey)
    # send the transaction
    #web3.eth.sendRawTransaction(signedTx.rawTransaction)
    try:
        web3.eth.sendRawTransaction(signedTx.rawTransaction)
        return "Transaction ID: " + web3.toHex(web3.sha3(signedTx.rawTransaction))
    except:
        return "transaction failed"


# @dev stampactivate activates the stamp of stampcode
def stampactivate(stampcode, address, privateKey):
    # gas cost based on trial on Remix is 22556
    gas = 50000
    myContract = web3.eth.contract(address=contractAddress, abi=contractAbi)
    detailTx = {'chainId': chainID, 'gas': gas, 'gasPrice': gasprice(), 'nonce': nonce(address), }
    unsignedTx = myContract.functions.stampActivate(stampcode).buildTransaction(detailTx)
    signedTx = web3.eth.account.signTransaction(unsignedTx, private_key=privateKey)
    try:
        web3.eth.sendRawTransaction(signedTx.rawTransaction)
        return "Transaction ID: " + web3.toHex(web3.sha3(signedTx.rawTransaction))
    except:
        return "transaction failed"


# @dev stampdeactivate deactivates the stamp of stampcode
def stampdeactivate(stampcode, address, privateKey):
    # gas cost based on trial on Remix is 7808
    gas = 50000
    myContract = web3.eth.contract(address=contractAddress, abi=contractAbi)
    detailTx = {'chainId': chainID, 'gas': gas, 'gasPrice': gasprice(), 'nonce': nonce(address), }
    unsignedTx = myContract.functions.stampDeactivate(stampcode).buildTransaction(detailTx)
    signedTx = web3.eth.account.signTransaction(unsignedTx, private_key=privateKey)
    try:
        web3.eth.sendRawTransaction(signedTx.rawTransaction)
        return "Transaction ID: " + web3.toHex(web3.sha3(signedTx.rawTransaction))
    except:
        return "Transaction failed"


# @dev createpayment executes transaction "createPayment" function in smart contract and sends it to the network
# @dev returns the transaction ID
# @param bytes32 PayCode;
# @param string DocHash;
# @param bytes32 StampCode;
# @param string BloomFilter;
def createpayment(payCode, docHash, stampCode, bloomFilter, address, privateKey):
    # gas cost based on trial on Remix is 412152
    # gas cost based on trial on Ganache is 456456
    # after adding bloom filter, the gas should increase significantly. for 100 char of BF, the gas is 543997
    gas = 5000000
    myContract = web3.eth.contract(address=contractAddress, abi=contractAbi)
    detailTx = {'chainId': chainID, 'gas': gas, 'gasPrice': gasprice(), 'nonce': nonce(address), }
    ts, st = u.gettimestamp()
    tsInt = int(ts)
    stString = str(st)
    payerSignature = str(sign(docHash, privateKey))
    #print (payerSignature)
    unsignedTx = myContract.functions.createPayment(payCode, docHash, stampCode, bloomFilter, tsInt, stString, payerSignature).buildTransaction(detailTx)
    signedTx = web3.eth.account.signTransaction(unsignedTx, private_key=privateKey)
    # send the transaction
    # web3.eth.sendRawTransaction(signedTx.rawTransaction)
    # remove the error message
    try:
        web3.eth.sendRawTransaction(signedTx.rawTransaction)
        return "Transaction ID: " + web3.toHex(web3.sha3(signedTx.rawTransaction))
    except:
        return "Transaction failed"


# @dev sign will produce signature from a local key
# @param message is the message to be signed (not the hash value)
# @param privateKey is the private key to be used for signing
def sign(message, privateKey):
    messageHash = defunct_hash_message(text=message)
    signedMessage = web3.eth.account.signHash(messageHash, private_key=privateKey)
    return web3.toHex(signedMessage.signature)


# @dev verifysignfrommessage verifies signature from a message
def verifysignfrommessage(message, signature, senderAddress):
    messageHash = defunct_hash_message(text=message)
    recoveredSenderAddress = web3.eth.account.recoverHash(messageHash, signature=signature)
    if (senderAddress == recoveredSenderAddress):
        return True
    else:
        return False


# @dev verifysignfrommessage verifies signature from a message
def verifysignfromhash(messageHash, signature, senderAddress):
    recoveredSenderAddress = web3.eth.account.recoverHash(messageHash, signature=signature)
    if (recoveredSenderAddress == senderAddress):
        return True
    else:
        return False


# @dev eventstampdutypayment check the event eStampDutyPayment
# @dev based on payCode
# @dev DO NOT USE. THIS WILL CRASH GANACHE
def eventstampdutypayment(payer):
    myContract = web3.eth.contract(address=contractAddress, abi=contractAbi)
    #myFilter = myContract.events.eStampDutyPayment.createFilter(fromBlock='latest', argument_filters={'payer':payer})
    myFilter = myContract.events.eStampDutyPayment.createFilter(fromBlock='0', toBlock='latest', argument_filters={'payer':payer})
    #event_signature_hash = web3.sha3(text="eStampDutyPayment(bytes32, string, bytes32, string, address)").hex()
    #event_filter = web3.eth.filter({
    #    "address": contractAddress,
    #    "topics": [event_signature_hash],
    #})
    #return event_filter.get_all_entries()
    return myFilter.get_all_entries()
    #myFilter = myContract.eventFilter('eStampDutyPayment', {'fromBlock':0, 'toBlock':'latest'})
    #eventList = myFilter.get_all_entries()
    #return eventList
