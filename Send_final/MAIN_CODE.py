import sys
import tkinter
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import PyQt5.QtWidgets as QtWidgets
from tkinter import filedialog
from tkinter import messagebox
from PyQt5 import QtCore, QtGui , QtWidgets

from tkinter import * 
from tkinter import messagebox 
  

import pickle
import pandas as pd
import numpy as np
import cv2

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns

import time

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn import metrics


app1 = QtWidgets.QApplication(sys.argv)
screen = app1.primaryScreen()
size = screen.size()
BG_Image='A3.png'
image = cv2.imread(BG_Image)
image=cv2.resize(image, (size.width(),size.height()))
cv2.imwrite('y1.jpg', image)


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Reds):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    #print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('TRUE CLASS')
    plt.xlabel('PREDICTED CLASS')
    plt.tight_layout()


print('******Start*****')
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow1(object):
    

    def setupUii(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1200,800)
        MainWindow.setStyleSheet(_fromUtf8("\n""background-image: url(y1.jpg);\n"""))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        

        self.u_user_label3 = QtWidgets.QLabel(MainWindow)
        self.u_user_label3.setGeometry(QtCore.QRect(810, 180, 131, 31))
        self.u_user_label3.setFont(QFont('Courier New', 10))
        self.u_user_label3.setObjectName(_fromUtf8("u_user_label"))
        self.u_user_label3.setStyleSheet("background-image: url(gray.jpg);;border: 2px solid red")
        self.uname_lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.uname_lineEdit.setGeometry(QtCore.QRect(950, 180, 131, 31))
        self.uname_lineEdit.setFont(QFont('Courier New', 10))
        self.uname_lineEdit.setText(_fromUtf8(""))
        self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))
        self.uname_lineEdit.setStyleSheet("background-image: url(gray.jpg);;border: 2px solid red")
        
        #Title
        self.u_user_label2 = QtWidgets.QLabel(MainWindow)
        self.u_user_label2.setGeometry(QtCore.QRect(300, 20, 650, 40))
        self.u_user_label2.setObjectName(_fromUtf8("u_user_label2"))
        self.u_user_label2.setFont(QFont('Courier New', 20))
        self.u_user_label2.setStyleSheet("background-image: url(milkwhite.jpg);;border: 2px solid magneta")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(950, 360, 131, 27))
        self.pushButton.setFont(QFont('Century', 10))
        self.pushButton.clicked.connect(self.quit)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n""color: rgb(0, 0, 0);"))
        self.pushButton.setStyleSheet("background-image: url(white.jpg);;border: 2px solid red")
        self.pushButton.setObjectName(_fromUtf8("pushButton"))


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(950, 240, 131, 27))
        self.pushButton_2.setFont(QFont('Century', 10))
        self.pushButton_2.clicked.connect(self.show1)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n""color: rgb(0, 0, 0);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.setStyleSheet("background-image: url(white.jpg);;border: 2px solid red")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(950, 280, 131, 27))
        self.pushButton_4.setFont(QFont('Century', 10))
        self.pushButton_4.clicked.connect(self.show2)
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n""color: rgb(0, 0, 0);"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.setStyleSheet("background-image: url(white.jpg);;border: 2px solid red")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(950, 320, 131, 27))
        self.pushButton_5.setFont(QFont('Century', 10))
        self.pushButton_5.clicked.connect(self.show3)
        self.pushButton_5.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n""color: rgb(0, 0, 0);"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.setStyleSheet("background-image: url(white.jpg);;border: 2px solid red")
        
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
       
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "DoS ATTCK DETECTION USING LSTM", None))
        self.pushButton_2.setText(_translate("MainWindow", "TEST", None))
        self.pushButton_4.setText(_translate("MainWindow", "TRAIN", None))
        self.pushButton_5.setText(_translate("MainWindow", "RESULT", None))
        self.pushButton.setText(_translate("MainWindow", "EXIT", None))
        self.u_user_label2.setText(_translate("Dialog", "DoS ATTCK DETECTION USING LSTM", None))
        self.u_user_label3.setText(_translate("Dialog", "Data Number", None))

    def quit(self):
        print ('Process end')
        print ('******End******')
        quit()
         
    def show1(self):
        print('TEST\n')
        print('TEST\n')
        Vidnam=self.uname_lineEdit.text()
        Vidnam =int(Vidnam)
        print('User selected data:',Vidnam)
        #Load Block
        file= open("LSTM.keras",'rb')
        LSTM_Model = pickle.load(file)
        file.close()

        #Load Block
        file= open("y.dat",'rb')
        y = pickle.load(file)
        file.close()

        #Load Block
        file= open("X.dat",'rb')
        X = pickle.load(file)
        file.close()

        X_Test=X[Vidnam]
        print(X_Test)
        X_Test=X_Test.reshape(1,-1)

        predicted_res= int(abs(LSTM_Model.predict(X_Test)))
        if predicted_res==0:
            print('------------------------------------------------\n')
            print('                 Normal Operation               \n')
            print('------------------------------------------------\n')
        else:
            print('------------------------------------------------\n')
            print('                   DoS Attack                   \n')
            print('------------------------------------------------\n')



    def show2(self):
        print('TRAIN\n')
        data = pd.read_csv('dataset_sdn.csv')
        print('Attribute \n',data.head())
        data=data[:10000]
        raw_data=data.copy()
        X = raw_data.drop(columns=["dt", "src", "dst", "label"])
        X = pd.get_dummies(X)
        y = raw_data["label"]

        from sklearn.preprocessing import StandardScaler

        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        # LSTM
        import tensorflow as tf
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import LSTM, Dense

        seq_length = 19


        # Reshape data to fit the LSTM input requirements
        X = X.reshape((X.shape[0], X.shape[1], 1))

        # Build the LSTM model
        model = Sequential([
            LSTM(100, activation='relu', input_shape=(seq_length, 1)),
            Dense(1)
        ])

        model.compile(optimizer='adam', loss='mean_squared_error')
        model.summary()

        # Train the model
        model.fit(X, y, epochs=500, batch_size=32, validation_data=(X, y))

        # Predict on the test set
        y_pred = model.predict(X)

        # Plot the results
        plt.figure(figsize=(10, 6))
        plt.plot(y, label='Actual')
        plt.plot(y_pred, label='Predicted')
        plt.title('LSTM Predictions vs Actual')
        plt.legend()
        plt.show()




    def show3(self):
        print('RESULTS\n')
        data = pd.read_csv('dataset_sdn.csv')
        print('Attribute \n',data.head())
        data=data[:10000]

        print('Total Attributes in datset',data.info())

        figure(figsize=(12, 7), dpi=80)
        plt.barh(list(dict(data.src.value_counts()).keys()), dict(data.src.value_counts()).values(), color='yellow')

        for idx, val in enumerate(dict(data.src.value_counts()).values()):
            plt.text(x = val, y = idx-0.2, s = str(val), color='b', size = 13)

        plt.xlabel('Number of Requests')
        plt.ylabel('IP addres of sender')
        plt.title('Number of all reqests')
        plt.show()

        figure(figsize=(12, 7), dpi=80)
        plt.barh(list(dict(data[data.label == 1].src.value_counts()).keys()), dict(data[data.label == 1].src.value_counts()).values(), color='cyan')

        for idx, val in enumerate(dict(data[data.label == 1].src.value_counts()).values()):
            plt.text(x = val, y = idx-0.2, s = str(val), color='red', size = 13)

        plt.xlabel('Number of Requests')
        plt.ylabel('IP addres of sender')
        plt.title('Number of Attack requests')
        plt.show()

        figure(figsize=(12, 7), dpi=80)
        plt.barh(list(dict(data.src.value_counts()).keys()), dict(data.src.value_counts()).values(), color='pink')
        plt.barh(list(dict(data[data.label == 1].src.value_counts()).keys()), dict(data[data.label == 1].src.value_counts()).values(), color='purple')

        for idx, val in enumerate(dict(data.src.value_counts()).values()):
            plt.text(x = val, y = idx-0.2, s = str(val), color='r', size = 13)

        for idx, val in enumerate(dict(data[data.label == 1].src.value_counts()).values()):
            plt.text(x = val, y = idx-0.2, s = str(val), color='w', size = 13)


        plt.xlabel('Number of Requests')
        plt.ylabel('IP addres of sender')
        plt.legend(['All','malicious'])
        plt.title('Number of requests from different IP adress')
        plt.show()


        figure(figsize=(10, 6), dpi=80)
        plt.bar(list(dict(data.Protocol.value_counts()).keys()), dict(data.Protocol.value_counts()).values(), color='r')
        plt.bar(list(dict(data[data.label == 1].Protocol.value_counts()).keys()), dict(data[data.label == 1].Protocol.value_counts()).values(), color='b')

        plt.text(x = 0 - 0.15, y = 41321 + 200, s = str(41321), color='black', size=17)
        plt.text(x = 1 - 0.15, y = 33588 + 200, s = str(33588), color='black', size=17)
        plt.text(x = 2 - 0.15, y = 29436 + 200, s = str(29436), color='black', size=17)

        plt.text(x = 0 - 0.15, y = 9419 + 200, s = str(9419), color='w', size=17)
        plt.text(x = 1 - 0.15, y = 17499 + 200, s = str(17499), color='w', size=17)
        plt.text(x = 2 - 0.15, y = 13866 + 200, s = str(13866), color='w', size=17)

        plt.xlabel('Protocol')
        plt.ylabel('Count')
        plt.legend(['All', 'malicious'])
        plt.title('The number of requests from different protocols')
        plt.show()

        #Process

        label_dict = dict(data.label.value_counts())
        sns.countplot(data.label)
        labels = ["Maliciuous",'Benign']
        sizes = [dict(data.label.value_counts())[0], dict(data.label.value_counts())[1]]
        plt.figure(figsize = (13,8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.legend(["Maliciuous", "Benign"])
        plt.title('The percentage of Benign and Maliciuos Requests in dataset')
        plt.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screen = app.primaryScreen()
    print('Screen: %s' % screen.name())
    size = screen.size()
    print('Size: %d x %d' % (size.width(), size.height()))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUii(MainWindow)
    MainWindow.move(10, 10)
    MainWindow.show()
    sys.exit(app.exec_())


