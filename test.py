# -*- coding: utf-8 -*-
"""
@Time       : 2023/2/9 16:26
@Author     : Sun
@Email      : 18814563079@163.com
@Project    : 空心风
@File       : test.py
@Description:
@Software   : PyCharm
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib_extend


def test1():
    """
    绘制2m以下的风
    :return:
    """
    matplotlib_extend.change_barb_of_draw_below_2m()
    lon = np.linspace(30, 40, 11)
    lat = np.linspace(40, 30, 11)
    u = np.random.random((11, 11)) * 4
    v = np.random.random((11, 11)) * 4
    ws = np.sqrt(u ** 2 + v ** 2)
    ax = plt.axes((0.05, 0.05, 0.9, 0.9))
    ax.barbs(lon, lat, u, v, pivot="tip", barb_increments=dict(half=2, full=4, flag=20), rounding=False, fill_empty=True)
    for i in range(11):
        for j in range(11):
            plt.text(lon[i], lat[j], '{:.2f}'.format(ws[j, i]), ha='center', va='center')
    plt.savefig("test1.png")


def test2():
    """
    绘制空心旗子
    :return:
    """
    matplotlib_extend.change_barb_of_draw_empty_flag()
    lon = np.linspace(30, 40, 11)
    lat = np.linspace(40, 30, 11)
    u = np.random.random((11, 11)) * 40
    v = np.random.random((11, 11)) * 40
    ws = np.sqrt(u ** 2 + v ** 2)
    ax = plt.axes((0.05, 0.05, 0.9, 0.9))
    ax.barbs(lon, lat, u, v, pivot="tip", barb_increments=dict(half=2, full=4, flag=20), rounding=False, fill_empty=True)
    for i in range(11):
        for j in range(11):
            plt.text(lon[i], lat[j], '{:.2f}'.format(ws[j, i]), ha='center', va='center')
    plt.savefig("test2.png")


def test3():
    """
    绘制实心+空心旗子
    :return:
    """
    matplotlib_extend.change_barb_of_draw_two_flag()
    lon = np.linspace(30, 40, 11)
    lat = np.linspace(40, 30, 11)
    u = np.random.random((11, 11)) * 100
    v = np.random.random((11, 11)) * 100
    ws = np.sqrt(u ** 2 + v ** 2)
    ax = plt.axes((0.05, 0.05, 0.9, 0.9))
    ax.barbs(lon, lat, u, v, pivot="tip", barb_increments=dict(half=2, full=4, empty_flag=20, full_flag=50), rounding=False, fill_empty=True)
    for i in range(11):
        for j in range(11):
            plt.text(lon[i], lat[j], '{:.2f}'.format(ws[j, i]), ha='center', va='center')
    plt.savefig("test3.png")


def run_it():
    test1()
    test2()
    test3()


if __name__ == '__main__':
    run_it()
