#!/usr/bin/env python3.6

import matplotlib as mpl
import matplotlib.pyplot as plt
import csv


price1 = []
date1 = []
i1 = 0
with open('../ProjData/Data/ETFs/xlf.us.txt') as csvfile:
    CSV = csv.reader(csvfile, delimiter=',')
    for line in CSV:
        if (i1 is 15):
            price1.append(line[2])
            date1.append(line[0])
            i1 = 0
        i1 += 1

    print(len(price1))
    # plot points along new axis
    mpl.use('agg')  # create a resultant .png file
    fig = plt.figure(1, figsize=(27, 28))  # set figure size
    ax = fig.add_subplot(111)
    ax.plot(date1, price1)
    fig.savefig('FinanceETF.png', bbox_inches='tight')
price3 = []
date3 = []
i3 = 0
with open('../ProjData/Data/ETFs/xli.us.txt') as csvfile:
    CSV = csv.reader(csvfile, delimiter=',')
    for line in CSV:
        if (i3 is 15):
            price3.append(line[2])
            date3.append(line[0])
            i3 = 0
        i3 += 1

    print(len(price3))
    # plot points along new axis
    mpl.use('agg')  # create a resultant .png file
    fig = plt.figure(3, figsize=(27, 28))  # set figure size
    ax = fig.add_subplot(111)
    ax.plot(date3, price3)
    fig.savefig('IndustrialETF.png', bbox_inches='tight')
price2 = []
date2 = []
i2 = 0
with open('../ProjData/Data/ETFs/xlv.us.txt') as csvfile:
    CSV = csv.reader(csvfile, delimiter=',')
    for line in CSV:
        if (i2 is 15):
            price2.append(line[2])
            date2.append(line[0])
            i2 = 0
        i2 += 1

    print(len(price2))
    # plot points along new axis
    mpl.use('agg')  # create a resultant .png file
    fig = plt.figure(2, figsize=(27, 28))  # set figure size
    ax = fig.add_subplot(111)
    ax.plot(date2, price2)
    fig.savefig('HealthcareETF.png', bbox_inches='tight')

price4 = []
date4 = []
i4 = 0

with open('../ProjData/Data/ETFs/dia.us.txt') as csvfile:
    CSV = csv.reader(csvfile, delimiter=',')
    for line in CSV:
        if (i4 is 15):
            price4.append(line[2])
            date4.append(line[0])
            i4 = 0
        i4 += 1

    print(len(price4))
    # plot points along new axis
    mpl.use('agg')  # create a resultant .png file
    fig = plt.figure(4, figsize=(27, 28))  # set figure size
    ax = fig.add_subplot(111)
    ax.plot(date4, price4)
    fig.savefig('DJI-ETF.png', bbox_inches='tight')

