# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

# Python 正逆解测试
import ctypes
import os
import sys
import time

if __name__ == "__main__":
    CUR_PATH = os.path.dirname(__file__)
    dllPath = os.path.join(CUR_PATH, "RM_Base.dll")
    pDll = ctypes.cdll.LoadLibrary(dllPath)


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


    class DevMsg(ctypes.Structure):
        _fields_ = [("position", Pos),
                    ("quaternion", Quat),
                    ("euler", Euler)]

    #   API 初始化
    pDll.RM_API_Init(65, 0)

    #   连接机械臂
    byteIP = bytes("192.168.1.18", "gbk")
    nSocket = pDll.Arm_Socket_Start(byteIP, 8080, 200)
    print(nSocket)

    #   初始位置
    float_joint = ctypes.c_float * 6
    joint1 = float_joint()
    joint1[0] = 0
    joint1[1] = 0
    joint1[2] = 90
    joint1[3] = 0
    joint1[4] = 90
    joint1[5] = 0
    pDll.Movej_Cmd.argtypes = (ctypes.c_int, ctypes.c_float * 6, ctypes.c_byte, ctypes.c_float, ctypes.c_bool)
    pDll.Movej_Cmd.restype = ctypes.c_int
    nRet = pDll.Movej_Cmd(nSocket, joint1, 20, 0, 1)
    print("Movej_Cmd ret:" + str(nRet))
    time.sleep(1)

    #   正解
    pDll.Algo_Forward_Kinematics.argtype = (ctypes.c_float * 6)
    pDll.Algo_Forward_Kinematics.restype = DevMsg
    compute_pose = DevMsg()

    compute_pose = pDll.Algo_Forward_Kinematics(joint1)

    print("求解位置：" + str(compute_pose.position.x) + "," + str(compute_pose.position.y) + "," +
          str(compute_pose.position.z))

    print("求解姿态：" + str(compute_pose.euler.rx) + "," + str(compute_pose.euler.ry) + "," +
          str(compute_pose.euler.rz))

    #   逆解
    q_out = float_joint()
    compute_pose.position.x += 0.1
    pDll.Algo_Inverse_Kinematics.argtypes = (ctypes.c_float * 6,
                                        ctypes.POINTER(DevMsg),
                                        ctypes.c_float * 6,
                                        ctypes.c_uint8)
    pDll.Algo_Inverse_Kinematics.argtype = ctypes.c_int
    res = pDll.Algo_Inverse_Kinematics(joint1, compute_pose, q_out, ctypes.c_uint8(1))
    print("逆解结果:" + str(res))

    i = 1
    while i < 3:
        time.sleep(1)
        i += 1

    #   关闭连接
    pDll.Arm_Socket_Close(nSocket)
