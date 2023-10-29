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
    # float_joint = ctypes.c_float * 6
    # joint1 = float_joint()
    # joint1[0] = 0
    # joint1[1] = 0
    # joint1[2] = 0
    # joint1[3] = 0
    # joint1[4] = 0
    # joint1[5] = 0
    # pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
    # pDll.Movej_Cmd.restype = ctypes.c_int
    # ret = pDll.Movej_Cmd(nSocket, joint1, 20, 0, 1)
    #
    # if ret != 0:
    #     print("设置初始位置失败:" + str(ret))
    #     sys.exit()

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


    for num in range(0, 1):
        # 移动至原点
        po1 = Pose()
        po1.position.x = 0.0
        po1.position.y = 0.0
        po1.position.z = 0.5
        po1.euler.rx = 0.0
        po1.euler.ry = -1.57
        po1.euler.rz = -3.14
        pDll.Movel_Cmd.argtypes = (ctypes.c_int, Pose, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movel_Cmd.restype = ctypes.c_int
        ret = pDll.Movel_Cmd(nSocket, po1, 20, 0, 1)
        if ret != 0:
            print("Movel_Cmd 1 失败:" + str(ret))
            sys.exit()


        po2 = Pose()
        po2.position.x = 0.0
        po2.position.y = 0.0
        po2.position.z = 0.5
        po2.rx = 0.868
        po2.ry = -0.302
        po2.rz = -1.176

        pDll.Movel_Cmd.argtypes = (ctypes.c_int, Pose, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
        pDll.Movel_Cmd.restype = ctypes.c_int
        ret = pDll.Movel_Cmd(nSocket, po1, 20, 0, 1)
        if ret != 0:
            print("Movel_Cmd 1 失败:" + str(ret))
            sys.exit()


    #   关闭连接
    pDll.Arm_Socket_Close(nSocket)