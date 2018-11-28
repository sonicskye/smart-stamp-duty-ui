# Smart Stamp Duty User Interface
Smart Stamp Duty User Interface is the interface for [Smart Stamp Duty's Ethereum-based smart contract](https://github.com/sonicskye/smart-stamp-duty).

## Requirements

* Python3.5.3+
* [Web3.py](https://pypi.org/project/web3/)
* hashlib

For the Bloom Filter part, the requirements are:
* [Cython](http://cython.org) or [bitarray](https://github.com/ilanschnell/bitarray)
* [pybloof](https://github.com/jhgg/pybloof)

The code is tested on [Ganache](http://truffleframework.com/ganache/), connected through http

The GUI is built by using Qt4 designer and requires PyQt4 to run.
* Python3-qt4

## Notes
This UI is a proof-of-concept of Smart Stamp Duty. The variables related to the smart contract can be found on vars.py.
The address and the private key information can be found on main.py. The pair is created by Ganache.

To run this UI, run `python main.py`