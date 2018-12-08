'''
sonicskye@2018
This is the instantiation of the design form
And should be the main app for GUI

https://nikolak.com/pyqt-qt-designer-getting-started/
'''

from PyQt4 import QtGui, QtCore
import design
import sys
import w3functions as f
import binascii
import utilities as u
import bloomfilter as bf

# Ganache
#privKey = "0b295aa109fcc22c6bc165fa213c952523cf1bef115483992e2afd8ccb47991e"
#addr = "0x06667BE53072905D1146f0Ab303D2a059c684F3a"

# Rinkeby funded
privKey = "5f294da09a4cf1e3d34bd4827bd42f791e7e0464cd72f64445cee619e5418c47"
addr = "0xcA4637C7E2a42f787d4b3C9F476B9716ABCD3838"

web3 = f.web3


class SSDApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        #super(SSDApp, self).__init__(parent)
        super(self.__class__, self).__init__()
        self.setupUi(self)
        # sets layout
        self.setupSignals()

    # define all functions to be connected to events
    def setupSignals(self):
        # stamp side
        self.btLoadStamp.clicked.connect(self.loadstampcode)
        self.cbStampCode.currentIndexChanged.connect(self.loadstampdata)
        self.btSaveStamp.clicked.connect(self.createstamp)
        self.btStampSetActivation.clicked.connect(self.changeactivation)
        # payment side
        self.btGetDocPath.clicked.connect(self.getfilepath)
        self.btGenDocHash.clicked.connect(self.generatesha1file)
        self.cbStampCodePayment.currentIndexChanged.connect(self.loadstampdatapayment)
        self.btGenPayCode.clicked.connect(self.generatepaycode)
        self.btGenBloomFilter.clicked.connect(self.generatebloomfilter)
        self.btSavePayment.clicked.connect(self.createpayment)
        # payment history
        self.btLoadPaymentHistory.clicked.connect(self.getpaymenthistory)
        # content matching
        self.btContentMatching.clicked.connect(self.contentmatching)

    # @dev loadstampcode loads the stamp codes and put them to cbStampCode
    # @dev handles btLoadStamp.clicked
    def loadstampcode(self):
        lst = f.getstampcodes()
        # for the stamp part
        self.cbStampCode.clear()
        self.cbStampCode.addItems(lst)

    # @dev loadstampdata loads the stamp data to the correct entries whenever the combobox cbStampCode is switched
    # @dev handles cbStampCode.currentIndexChanged
    def loadstampdata(self):
        # get the code in the correct format
        # self.pteStampLog.appendPlainText(str(self.cbStampCode.currentIndex()))
        if self.cbStampCode.currentIndex() >= 0:
            self.leStampCode.setText(self.cbStampCode.itemText(self.cbStampCode.currentIndex()))
            # convert the stamp code
            stampCodeRaw = binascii.unhexlify(self.cbStampCode.currentText().encode('utf-8'))
            stampDetail = f.getstampdetail(stampCodeRaw)
            # StampCode, StampName, StampPrice, RegulationReference, IsActive
            self.leStampName.setText(stampDetail[1])
            self.sbStampPrice.setValue(stampDetail[2])
            self.teRegulationRef.setText(stampDetail[3])
            #self.pteStampLog.appendPlainText(str(stampDetail[4]))
            self.chStampIsActive.setChecked(stampDetail[5])

    # @dev createstamp creates a new stamp
    def createstamp(self):
        # createstamp(stampcode, stampname, stampprice, regulationreference, isactive, address, privateKey)
        if self.chStampIsActive.checkState() == True:
            checked = True
        else:
            checked = False
        #logData = str(checked)
        stampCodeRaw = binascii.unhexlify(self.leStampCode.text().encode('utf-8'))
        logData = f.createstamp(stampCodeRaw, self.leStampName.text(), self.sbStampPrice.value(), self.teRegulationRef.toPlainText(), checked, addr, privKey)
        self.pteStampLog.appendPlainText("Create Stamp: " + logData)
        return True

    # @dev changeactivation changes the active status - active or inactive
    def changeactivation(self):
        if self.leStampCode.text() == "":
            return False
        stampCodeRaw = binascii.unhexlify(self.leStampCode.text().encode('utf-8'))
        if self.chStampIsActive.checkState():
            checked = True
            if f.getstampactivation(stampCodeRaw) == False:
                # activates
                logData = f.stampactivate(stampCodeRaw, addr, privKey)
                self.pteStampLog.appendPlainText("Change Activation to " + str(checked) + ": " + logData)
                return True
        elif not self.chStampIsActive.checkState():
            checked = False
            if f.getstampactivation(stampCodeRaw) == True:
                # deactivates
                logData = f.stampdeactivate(stampCodeRaw, addr, privKey)
                self.pteStampLog.appendPlainText("Change Activation to " + str(checked) + ": " + logData)
                return True

    # @dev getfilepath will get a file path
    def getfilepath(self):
        filepath = QtGui.QFileDialog.getOpenFileName(self)
        if filepath:
            self.leDocPath.setText(filepath)
            self.updatetimestamp()
            self.loadstampcodepayment()
            self.generatesha1file()
            # for development only
            # @ToDo should call this from setting
            self.lePayerAddress.setText(addr)

    # @dev sha1file calls sha1file from utilities.sha1file to compute SHA1 value of a file
    def generatesha1file(self):
        if self.leDocPath.text() != "":
            filepath = self.leDocPath.text()
            self.leDocHash.setText(u.sha1file(filepath))

    def updatetimestamp(self):
        present_qdatetime = QtCore.QDateTime.currentDateTime()
        #present_qdatetime.toMSecsSinceEpoch()
        #present_qdatetime.setMSecsSinceEpoch(1000 * i_unix_time_it)
        #self.ptePaymentLog.appendPlainText(str(present_qdatetime)))
        self.dteTimestamp.setDateTime(present_qdatetime)

    # @dev loadstampcodepayment loads stamp code for the payment part
    # @dev only shows active stamp code
    def loadstampcodepayment(self):
        lst = f.getactivestampcodes()
        # for the payment part
        self.cbStampCodePayment.clear()
        self.cbStampCodePayment.addItems(lst)

    # @dev loadstampdatapayment loads the stamp data to the correct entries
    #   whenever the combobox cbStampCodePayment is switched
    # @dev handles cbStampCode.currentIndexChanged
    def loadstampdatapayment(self):
        # get the code in the correct format
        if self.cbStampCodePayment.currentIndex() >= 0:
            # convert the stamp code
            stampCodeRaw = binascii.unhexlify(self.cbStampCodePayment.currentText().encode('utf-8'))
            stampDetail = f.getstampdetail(stampCodeRaw)
            # StampCode, StampName, StampPrice, RegulationReference, IsActive
            self.leStampNamePayment.setText(stampDetail[1])
            self.sbStampPricePayment.setValue(stampDetail[2])
            # self.pteStampLog.appendPlainText(str(stampDetail[4]))

    # @dev generatepaycode computes sha1 of several parameters from the UI
    def generatepaycode(self):
        ts, st = u.gettimestamp()
        theText = self.leDocHash.text() + self.lePayerAddress.text() + self.cbStampCodePayment.currentText() + self.dteTimestamp.text()
        self.lePayCode.setText(u.sha1string(theText))

    # @dev generatebloomfilter generates bloom filter from plaintext supplied
    def generatebloomfilter(self):
        alist = u.getwords(self.teWordList.toPlainText())
        bfValue = bf.createstringbloomfilter(alist)
        self.teBloomFilter.setText(bfValue)

    # @dev createpayment sends payment
    def createpayment(self):
        payCodeRaw = binascii.unhexlify(self.lePayCode.text().encode('utf-8'))
        stampCodeRaw = binascii.unhexlify(self.cbStampCodePayment.currentText().encode('utf-8'))
        # createpayment(payCode, docHash, stampCode, bloomFilter, address, privateKey)
        logData = f.createpayment(payCodeRaw, self.leDocHash.text(), stampCodeRaw,
                                self.teBloomFilter.toPlainText(), addr, privKey)
        self.ptePaymentLog.appendPlainText("Create Payment: " + logData)
        return True

    # @dev getpaymenthistory returns payment history
    # @dev shows the result in a table
    # #https://pythonspot.com/qt4-table/
    '''
        bytes32 PayCode;
        string DocHash;
        uint256 PayIndex;
        address Payer;
        bytes32 StampCode;
        string BloomFilter;
    '''
    def getpaymenthistory(self):
        # setup column
        table = self.tbPaymentHistory
        table.setColumnCount(5)

        # setup label
        #table.setHorizontalHeaderLabels(QtCore.QString("PayCode;DocHash;Payer;StampCode;BloomFilter;").split(";"))
        table.setHorizontalHeaderLabels(["PayCode","DocHash", "PayerAddress", "StampName", "BloomFilter"])

        # fill up the data
        paymentCodes = f.getpaylist()
        table.setRowCount(len(paymentCodes))
        i = 0
        for paymentCode in paymentCodes:
            paymentDetail = f.getpaymentdetail(web3.toHex(paymentCode))
            table.setItem(i, 0, QtGui.QTableWidgetItem(binascii.hexlify(paymentDetail[0]).decode('utf-8')))
            table.setItem(i, 1, QtGui.QTableWidgetItem(paymentDetail[1]))
            table.setItem(i, 2, QtGui.QTableWidgetItem(str(paymentDetail[3])))
            table.setItem(i, 3, QtGui.QTableWidgetItem(f.getstampnamefromcode(paymentDetail[4])))
            table.setItem(i, 4, QtGui.QTableWidgetItem(paymentDetail[5]))
            i += 1
        return

    # @dev contentmatching is a tool to test a bloom filter against a word list
    # @dev wordlist needs to be converted into a list of words
    def contentmatching(self):
        wordlist = u.getwords(self.teCMWordList.toPlainText())
        res = bf.teststringbloomfilter(self.teCMBloomFilter.toPlainText(), wordlist)
        self.pteCMResult.appendPlainText("Comparison Result: " + str(res) + "%")


def main():
    app = QtGui.QApplication(sys.argv)
    form = SSDApp()
    form.show()
    #app.exec_()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
