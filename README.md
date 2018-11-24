# Smart Stamp Duty User Interface
Smart Stamp Duty User Interface is the interface for [Smart Stamp Duty's Ethereum-based smart contract](https://github.com/sonicskye/smart-stamp-duty).

## Requirements

* Python3.5.3+
* [Web3.py](https://pypi.org/project/web3/)
* hashlib

For the Bloom Filter part (which is optional), the requirements are:
* [Cython](http://cython.org) or [bitarray](https://github.com/ilanschnell/bitarray)
* [pybloof](https://github.com/jhgg/pybloof)

If you want to compile your solidity contract inside python, then these are required

* [solc](https://solidity.readthedocs.io/en/develop/installing-solidity)
* [py-solc](https://github.com/ethereum/py-solc)
* [eth-testrpc](https://github.com/pipermerriam/eth-testrpc)

use pip3 install eth-testrpc

The code is tested on [Ganache](http://truffleframework.com/ganache/), connected through http