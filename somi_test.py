import ctypes
import os
import sys
import time

if __name__ == "__main__":
    CUR_PATH = os.path.dirname(os.path.realpath(__file__))
    dllPath = os.path.join(CUR_PATH, "RM_Base.dll")
    pDll = ctypes.cdll.LoadLibrary(dllPath)

    #   API 初始化
    pDll.RM_API_Init(65, 0)

    #   连接机械臂
    byteIP = bytes("192.168.1.18", "gbk")
    nSocket = pDll.Arm_Socket_Start(byteIP, 8080, 200)
    print(nSocket)

    #   设置机械臂末端参数为初始值
    nRet = pDll.Set_Arm_Tip_Init(nSocket, 1)
    print(nRet)

    #   初始位置
    float_joint = ctypes.c_float * 6
    joint1 = float_joint()
    joint1[0] = 0
    joint1[1] = 0
    joint1[2] = 0
    joint1[3] = 0
    joint1[4] = 0
    joint1[5] = 0
    pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
    pDll.Movej_Cmd.restype = ctypes.c_int
    ret = pDll.Movej_Cmd(nSocket, joint1, 20, 0, 1)

    if ret != 0:
        print("设置初始位置失败:" + str(ret))
        sys.exit()

    class Pos(ctypes.Structure):
        _fields_ = [("x", ctypes.c_float),
                    ("y", ctypes.c_float),
                    ("z", ctypes.c_float)]

    class Quat(ctypes.Structure):
        _fields_ = [("w", ctypes.c_float),
                    ("x", ctypes.c_float),
                    ("y", ctypes.c_float),
                    ("z", ctypes.c_float)]

    class Euler(ctypes.Structure):
        _fields_ = [("rx", ctypes.c_float),
                    ("ry", ctypes.c_float),
                    ("rz", ctypes.c_float)]
    #   画八字
    class Pose(ctypes.Structure):
        _fields_ = [("position", Pos),
                    ("quaternion", Quat),
                    ("euler", Euler)]


    for num in range(0, 2):
        ### 第一组：横向运动
        float_joint = ctypes.c_float * 6
        joint2 = float_joint()
        joint2[0] = 18.983
        joint2[1] = 18.300
        joint2[2] = -57.897
        joint2[3] = 19.721
        joint2[4] = -37.836
        joint2[5] = -52.395
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint2, 20, 0, 1)

        float_joint = ctypes.c_float * 6
        joint3 = float_joint()
        joint3[0] = -35.425
        joint3[1] = 5.695
        joint3[2] = -48.613
        joint3[3] = 7.925
        joint3[4] = -33.875
        joint3[5] = 6.008
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint3, 20, 0, 1)


    for num in range(0, 1):
        ### 第二组：纵向运动
        # 先到上面
        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = -35.300
        joint4[1] = -11.537
        joint4[2] = 39.976
        joint4[3] = 7.903
        joint4[4] = 29.415
        joint4[5] = 6.102
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 20, 0, 1)

        # 再到下面
        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = -9.004
        joint4[1] = -24.072
        joint4[2] = -64.452
        joint4[3] = -11.641
        joint4[4] = -65.957
        joint4[5] = 5.921
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 20, 0, 1)

    # 小范围地面画
    for num in range(0,2):
        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = 22.781
        joint4[1] = -24.078
        joint4[2] = -55.313
        joint4[3] = 14.797
        joint4[4] = -66.486
        joint4[5] = 5.858
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 80, 0, 1)

        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = -9.004
        joint4[1] = -24.072
        joint4[2] = -64.452
        joint4[3] = -11.641
        joint4[4] = -65.957
        joint4[5] = 5.921
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 80, 0, 1)

    # 画两个侧面
    for num in range(0, 1):
        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = -59.368
        joint4[1] = -30.855
        joint4[2] = -10.589
        joint4[3] = -42.186
        joint4[4] = -47.918
        joint4[5] = 0.306
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 20, 0, 1)
        time.sleep(2)

        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = 83.417
        joint4[1] = -18.465
        joint4[2] = -29.157
        joint4[3] = -0.664
        joint4[4] = -29.440
        joint4[5] = 0.512
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 20, 0, 1)
        time.sleep(2)

    # 扭曲着斜向上 -> 另一侧向后
        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = -6.847
        joint4[1] = -59.963
        joint4[2] = -108.790
        joint4[3] = -96.719
        joint4[4] = -116.099
        joint4[5] = -45.422
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 20, 0, 1)

        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = 7.823
        joint4[1] = -62.159
        joint4[2] = -109.271
        joint4[3] = -78.707
        joint4[4] = -124.604
        joint4[5] = 0.542
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 80, 0, 1)
        time.sleep(2)

        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = 23.878
        joint4[1] = -35.763
        joint4[2] = 30.737
        joint4[3] = -60.188
        joint4[4] = 42.854
        joint4[5] = 0.528
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 20, 0, 1)
        time.sleep(2)

    # 面前走直线
        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = -5.557
        joint4[1] = 20.529
        joint4[2] = -85.499
        joint4[3] = 5.932
        joint4[4] = -85.295
        joint4[5] = -21.156
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 10, 0, 1)
        time.sleep(1)

        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = -1.089
        joint4[1] = -12.556
        joint4[2] = -47.912
        joint4[3] = 4.626
        joint4[4] = -66.345
        joint4[5] = -21.047
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 5, 0, 1)
        time.sleep(2)


    # 开始转圈
    for num in range(0, 1):
        # 初始点
        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = 24.197
        joint4[1] = 50.692
        joint4[2] = -72.445
        joint4[3] = 43.718
        joint4[4] = -66.367
        joint4[5] = -21.126
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 20, 0, 1)

        # 高位转
        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = 44.920
        joint4[1] = 31.948
        joint4[2] = -121.055
        joint4[3] = 10.329
        joint4[4] = -34.380
        joint4[5] = -21.071
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 20, 0, 1)
        time.sleep(1)

        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = -38.850
        joint4[1] = 29.939
        joint4[2] = -121.003
        joint4[3] = 10.305
        joint4[4] = -34.314
        joint4[5] = -21.125
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 10, 0, 1)
        time.sleep(1)

        # 低位转
        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = 45.112
        joint4[1] = -43.853
        joint4[2] = -126.661
        joint4[3] = 137.211
        joint4[4] = -81.705
        joint4[5] = -20.992
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 10, 0, 1)
        time.sleep(2)

        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = -67.917
        joint4[1] = -58.926
        joint4[2] = -132.235
        joint4[3] = 177.436
        joint4[4] = -99.250
        joint4[5] = -21.165
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 10, 0, 1)
        time.sleep(2)

    for num in range(0, 1):
        # 高位转（反）
        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = -38.850
        joint4[1] = 29.939
        joint4[2] = -121.003
        joint4[3] = 10.305
        joint4[4] = -34.314
        joint4[5] = -21.125
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 10, 0, 1)

        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = 44.920
        joint4[1] = 31.948
        joint4[2] = -121.055
        joint4[3] = 10.329
        joint4[4] = -34.380
        joint4[5] = -21.071
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 10, 0, 1)

    # 第一遍慢速
    for num in range(0, 1):
        # 从上到下转
        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = -23.255
        joint4[1] = 28.708
        joint4[2] = -32.747
        joint4[3] = 100.915
        joint4[4] = 62.756
        joint4[5] = -61.638
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 20, 0, 1)

        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = 2.863
        joint4[1] = 41.487
        joint4[2] = -72.419
        joint4[3] = 110.729
        joint4[4] = -73.524
        joint4[5] = -61.601
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 20, 0, 1)

        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = 46.036
        joint4[1] = 31.988
        joint4[2] = -120.165
        joint4[3] = 7.203
        joint4[4] = -33.906
        joint4[5] = -61.574
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 20, 0, 1)

        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = -46.288
        joint4[1] = 18.389
        joint4[2] = -119.167
        joint4[3] = -2.642
        joint4[4] = -33.884
        joint4[5] = -61.619
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 20, 0, 1)

    # 第二遍快速
    for num in range(0, 1):
        # 从上到下转
        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = 2.863
        joint4[1] = 41.487
        joint4[2] = -72.419
        joint4[3] = 110.729
        joint4[4] = -73.524
        joint4[5] = -61.601
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 50, 0, 1)

        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = 46.036
        joint4[1] = 31.988
        joint4[2] = -120.165
        joint4[3] = 7.203
        joint4[4] = -33.906
        joint4[5] = -61.574
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 50, 0, 1)

        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = -23.255
        joint4[1] = 28.708
        joint4[2] = -32.747
        joint4[3] = 100.915
        joint4[4] = 62.756
        joint4[5] = -61.638
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 50, 0, 1)

        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = -46.288
        joint4[1] = 18.389
        joint4[2] = -119.167
        joint4[3] = -2.642
        joint4[4] = -33.884
        joint4[5] = -61.619
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 50, 0, 1)

    # 后方画弧线
    for num in range(0, 2):
        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = -78.317
        joint4[1] = 8.901
        joint4[2] = -60.257
        joint4[3] = -8.898
        joint4[4] = -108.347
        joint4[5] = -21.139
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 10, 0, 1)

        float_joint = ctypes.c_float * 6
        joint4 = float_joint()
        joint4[0] = -23.101
        joint4[1] = -31.555
        joint4[2] = 42.213
        joint4[3] = 57.545
        joint4[4] = 41.093
        joint4[5] = -21.133
        pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movej_Cmd.restype = ctypes.c_int
        ret = pDll.Movej_Cmd(nSocket, joint4, 40, 0, 1)


        for i in range(0, 2):
            float_joint = ctypes.c_float * 6
            joint4 = float_joint()
            joint4[0] = -29.411
            joint4[1] = -21.404
            joint4[2] = 19.142
            joint4[3] = -17.531
            joint4[4] = 74.108
            joint4[5] = -21.117
            pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
            pDll.Movej_Cmd.restype = ctypes.c_int
            ret = pDll.Movej_Cmd(nSocket, joint4, 40, 0, 1)

            float_joint = ctypes.c_float * 6
            joint4 = float_joint()
            joint4[0] = -39.997
            joint4[1] = -38.454
            joint4[2] = 39.873
            joint4[3] = -26.434
            joint4[4] = 77.059
            joint4[5] = -21.029
            pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
            pDll.Movej_Cmd.restype = ctypes.c_int
            ret = pDll.Movej_Cmd(nSocket, joint4, 40, 0, 1)

    # 横着扫 停一下 转过来，转过去
    float_joint = ctypes.c_float * 6
    joint4 = float_joint()
    joint4[0] = 84.325
    joint4[1] = -96.329
    joint4[2] = 133.016
    joint4[3] = 9.033
    joint4[4] = 46.060
    joint4[5] = -21.123
    pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
    pDll.Movej_Cmd.restype = ctypes.c_int
    ret = pDll.Movej_Cmd(nSocket, joint4, 20, 0, 1)
    time.sleep(3)

    float_joint = ctypes.c_float * 6
    joint4 = float_joint()
    joint4[0] = 82.003
    joint4[1] = -29.979
    joint4[2] = 112.313
    joint4[3] = -54.022
    joint4[4] = 89.480
    joint4[5] = -21.158
    pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
    pDll.Movej_Cmd.restype = ctypes.c_int
    ret = pDll.Movej_Cmd(nSocket, joint4, 20, 0, 1)

    float_joint = ctypes.c_float * 6
    joint4 = float_joint()
    joint4[0] = 83.647
    joint4[1] = -27.713
    joint4[2] = 112.409
    joint4[3] = 78.642
    joint4[4] = 96.491
    joint4[5] = -21.000
    pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
    pDll.Movej_Cmd.restype = ctypes.c_int
    ret = pDll.Movej_Cmd(nSocket, joint4, 20, 0, 1)
    time.sleep(1)

    float_joint = ctypes.c_float * 6
    joint4 = float_joint()
    joint4[0] = 78.994
    joint4[1] = -22.203
    joint4[2] = 71.390
    joint4[3] = -72.121
    joint4[4] = 81.971
    joint4[5] = -21.070
    pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
    pDll.Movej_Cmd.restype = ctypes.c_int
    ret = pDll.Movej_Cmd(nSocket, joint4, 20, 0, 1)
    time.sleep(1)

    float_joint = ctypes.c_float * 6
    joint4 = float_joint()
    joint4[0] = 47.065
    joint4[1] = 48.968
    joint4[2] = -107.605
    joint4[3] = -21.203
    joint4[4] = -21.280
    joint4[5] = -2.246
    pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
    pDll.Movej_Cmd.restype = ctypes.c_int
    ret = pDll.Movej_Cmd(nSocket, joint4, 20, 0, 1)

    float_joint = ctypes.c_float * 6
    joint4 = float_joint()
    joint4[0] = 40.415
    joint4[1] = 16.815
    joint4[2] = -91.389
    joint4[3] = 5.004
    joint4[4] = -61.441
    joint4[5] = -2.158
    pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
    pDll.Movej_Cmd.restype = ctypes.c_int
    ret = pDll.Movej_Cmd(nSocket, joint4, 20, 0, 1)

    float_joint = ctypes.c_float * 6
    joint4 = float_joint()
    joint4[0] = 7.713
    joint4[1] = 57.733
    joint4[2] = -53.469
    joint4[3] = -33.277
    joint4[4] = -82.617
    joint4[5] = -2.169
    pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
    pDll.Movej_Cmd.restype = ctypes.c_int
    ret = pDll.Movej_Cmd(nSocket, joint4, 20, 0, 1)

    float_joint = ctypes.c_float * 6
    joint4 = float_joint()
    joint4[0] = 56.686
    joint4[1] = 56.947
    joint4[2] = -53.375
    joint4[3] = -27.347
    joint4[4] = -82.445
    joint4[5] = -2.124
    pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
    pDll.Movej_Cmd.restype = ctypes.c_int
    ret = pDll.Movej_Cmd(nSocket, joint4, 2, 0, 1)


    print("cycle draw 8 demo")


    #   关闭连接
    pDll.Arm_Socket_Close(nSocket)