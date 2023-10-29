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
    joint1[0] = 18.44
    joint1[1] = -10.677
    joint1[2] = -124.158
    joint1[3] = -15
    joint1[4] = -45.131
    joint1[5] = -71.455
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


    for num in range(0, 3):
        # 移动至原点
        po1 = Pose()
        po1.position.x = 0.2
        po1.position.y = 0.2
        po1.position.z = 0.2
        po1.euler.rx = 3.141
        po1.euler.ry = 0
        po1.euler.rz = 1.569
        pDll.Movel_Cmd.argtypes = (ctypes.c_int, Pose, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movel_Cmd.restype = ctypes.c_int
        ret = pDll.Movel_Cmd(nSocket, po1, 80, 0, 1)
        if ret != 0:
            print("Movel_Cmd 1 失败:" + str(ret))
            sys.exit()

        po2 = Pose()
        po2.position.x = 0.17
        po2.position.y = 0.23
        po2.position.z = 0.2
        po2.euler.rx = 3.141
        po2.euler.ry = 0
        po2.euler.rz = 1.569

        po3 = Pose()
        po3.position.x = 0.14
        po3.position.y = 0.2
        po3.position.z = 0.2
        po3.euler.rx = 3.141
        po3.euler.ry = 0
        po3.euler.rz = 1.569
        pDll.Movec_Cmd.argtypes = (
        ctypes.c_int, Pose, Pose, ctypes.c_byte, ctypes.c_float, ctypes.c_byte, ctypes.c_bool)
        pDll.Movec_Cmd.restype = ctypes.c_int
        ret = pDll.Movec_Cmd(nSocket, po2, po3, 80, 0, 0, 1)
        if ret != 0:
            print("Movec_Cmd 1 失败:" + str(ret))
            sys.exit()

        po4 = Pose()
        po4.position.x = 0.2
        po4.position.y = 0.08
        po4.position.z = 0.2
        po4.euler.rx = 3.141
        po4.euler.ry = 0
        po4.euler.rz = 1.569

        po5 = Pose()
        po5.position.x = 0.26
        po5.position.y = 0.2
        po5.position.z = 0.2
        po5.euler.rx = 3.141
        po5.euler.ry = 0
        po5.euler.rz = 1.569

        ret = pDll.Movec_Cmd(nSocket, po4, po5, 80, 0, 0, 1)
        if ret != 0:
            print("Movel_Cmd 2 失败:" + str(ret))
            sys.exit()

        po6 = Pose()
        po6.position.x = 0.23
        po6.position.y = 0.23
        po6.position.z = 0.2
        po6.euler.rx = 3.141
        po6.euler.ry = 0
        po6.euler.rz = 1.569
        ret = pDll.Movec_Cmd(nSocket, po6, po1, 80, 0, 0, 1)
        if ret != 0:
            print("Movel_Cmd 2 失败:" + str(ret))
            sys.exit()

    print("cycle draw 8 demo")


    #   关闭连接
    pDll.Arm_Socket_Close(nSocket)