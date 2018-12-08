'''
sonicskye@2018
account.py is used to create a new Ethereum address
can also be used to generate a vanity address
'''

import w3functions as f

web3 = f.web3

HEXCHAR = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e", "f"]


# @dev create a new account (local, not hosted)
# @dev https://ethereum.stackexchange.com/questions/32940/how-can-i-generate-a-wallet-in-python
# @dev https://web3py.readthedocs.io/en/latest/web3.eth.account.html
def createaccount():
    acc = web3.eth.account.create()
    return acc.address, acc.privateKey.hex()


# @dev base58check is used to check a word which needs to be Base58
def hexcharcheck(thekeyword):
    # need to check each character from input
    res = True
    for s in thekeyword:
        if s not in HEXCHAR:
            res = False
    return res


def iterate(thekeyword):
    success = False
    i = 0
    while not success:
        print("Iteration #: " + str(i))
        address, privateKey = createaccount()
        if thekeyword in address:
            print("Result: ")
            print("    address        = " + str(address))
            print("    private key    = " + str(privateKey))
            success = True
            return address, privateKey
        i += 1


#addr, priv = createaccount()
#print(addr, priv)

if __name__ == '__main__':
    keyWord = "ABCD"
    # check base58 validity before iterating
    if hexcharcheck(keyWord):
        iterate(keyWord)
    else:
        print("Invalid HEX character(s) detected")
