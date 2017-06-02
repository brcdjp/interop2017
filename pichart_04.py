#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import paramiko

# 全体のフォントサイズを設定
plt.rcParams.update({'font.size': 20})
label = ["Freeza", "Goku"]
# color = ("red", "blue")
color = ("#cc33ff", "#ff9933")

while True:
    HOST = '172.24.182.43'
    USER = 'pi'
    PSWD = 'interop2017'

    LOCAL_PATH = r"C:\Users\wsakurai\PycharmProjects\exercise01\result.json"
    REMOTE_PATH = "/home/pi/interop2017/result.json"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(HOST, username=USER, password=PSWD)

    sftp = ssh.open_sftp()
    sftp.get(REMOTE_PATH, LOCAL_PATH)
    sftp.close()

    ssh.close()

    f = open("result.json", 'r')
    data_str = f.read()
    f.close()

    freeza_str = data_str[data_str.find(":")+2:data_str.find(",")]
    goku_str = data_str[data_str.find(":", data_str.find(",")+1)+2:data_str.find("}")]

    data = [int(freeza_str), int(goku_str)]

    # アスペクト比を補正しないと，楕円のグラフになってしまう
    plt.axis('equal')

    plt.pie(data,
            autopct='%1.1f%%',  # グラフ中に割合を表示
            pctdistance=0.6,    # 割合の位置を指定 0が中心, 1が外周
            startangle=90,		# グラフの開始位置を12時の位置に変更
            labels=label,
            labeldistance=1.1,  # ラベルの位置を指定
            colors=color,
            # textprops={'color': "white", 'weight': "bold"},
            shadow=False,
            explode=(0.02, 0.02),
            wedgeprops={'linewidth': 3, 'edgecolor':"white"}
            )

    plt.pause(10)
    plt.cla()
