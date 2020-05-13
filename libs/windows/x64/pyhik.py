import os
import win32api

from ctypes import WinDLL
from ctypes import c_void_p, c_uint, c_int, c_char_p, cast, c_bool, c_char, c_ushort, c_long, c_ubyte
from ctypes import byref, pointer, POINTER, WINFUNCTYPE, Structure
from ctypes.wintypes import DWORD, LPDWORD

####################################################
### Data types define                            ###
####################################################
BOOL = c_bool
INT = c_int
LONG = c_long
BYTE = c_ubyte
WORD = c_ushort
CHAR = c_char
HWND = c_uint
CHARP = c_char_p
VOIDP = c_void_p

RD_CBFUNC_TYPE = WINFUNCTYPE(None, LONG, DWORD, BYTE, DWORD, VOIDP)


####################################################
### Global variables                             ###
####################################################
MAX_HOLIDAY_NUM = 32

MAX_ALARMOUT = 4
MAX_IP_ALARMOUT_V40 = 4096
MAX_ANALOG_ALARMOUT = 32
MAX_IP_ALARMOUT = 64
MAX_ALARMOUT_V40 = (MAX_IP_ALARMOUT_V40 + MAX_ANALOG_ALARMOUT)
MAX_ALARMOUT_V30 = (MAX_ANALOG_ALARMOUT + MAX_IP_ALARMOUT)

MAX_EXCEPTIONNUM_V30 = 32
MAX_EXCEPTIONNUM = 16

NAME_LEN = 32
PASSWD_LEN = 16
MAX_DOMAIN_NAME = 64
DEV_ID_LEN = 32

CHAN_NO_LEN = 24

SERIALNO_LEN = 48
STREAM_ID_LEN = 32

MAX_ANALOG_CHANNUM = 32
MAX_IP_CHANNEL = 32

MAX_PRESET_V30 = 256
MAX_CRUISE_V30 = 256
MAX_TRACK_V30 = 256

PHONENUMBER_LEN = 32

MAX_SERIAL_PORT = 8

MAX_CHANNUM_V30 = (MAX_ANALOG_CHANNUM + MAX_IP_CHANNEL)

# configure
NET_DVR_GET_TIMECFG = 118 # 获取时间参数
NET_DVR_GET_ZONEANDDST = 128 # 获取时区和夏时制参数
NET_DVR_GET_RS232CFG_V30 = 1036 # 获取RS232串口参数
NET_DVR_GET_DECODERCFG_V30 = 1042 # 获取解码器参数
NET_DVR_GET_IPPARACFG_V40 = 1062 # 获取IP接入配置
NET_DVR_GET_DEVICECFG_V40 = 1100 # 获取设备参数(扩展)
NET_DVR_GET_HOLIDAY_PARAM_CFG = 1240 # 获取节假日参数
NET_DVR_GET_DEVSERVER_CFG = 3257 # 获取模块服务配置
NET_DVR_GET_EXCEPTIONCFG_V40 = 6177 # 获取异常参数
NET_DVR_GET_DECODERCFG_V40 = 6328 # 获取RS485(云台解码器)参数

# PTZ
LIGHT_PWRON         = 2 # 接通灯光电源
WIPER_PWRON         = 3 # 接通雨刷开关
FAN_PWRON           = 4 # 接通风扇开关
HEATER_PWRON        = 5 # 接通加热器开关
AUX_PWRON1          = 6 # 接通辅助设备开关
AUX_PWRON2          = 7 # 接通辅助设备开关
SET_PRESET          = 8 # 设置预置点
CLE_PRESET          = 9 # 清除预置点

ZOOM_IN             = 11 # 焦距以速度SS变大(倍率变大)
ZOOM_OUT            = 12 # 焦距以速度SS变小(倍率变小)
FOCUS_NEAR          = 13 # 焦点以速度SS前调
FOCUS_FAR           = 14 # 焦点以速度SS后调
IRIS_OPEN           = 15 # 光圈以速度SS扩大
IRIS_CLOSE          = 16 # 光圈以速度SS缩小

TILT_UP             = 21 # 云台以SS的速度上仰
TILT_DOWN           = 22 # 云台以SS的速度下俯
PAN_LEFT            = 23 # 云台以SS的速度左转
PAN_RIGHT           = 24 # 云台以SS的速度右转
UP_LEFT             = 25 # 云台以SS的速度上仰和左转
UP_RIGHT            = 26 # 云台以SS的速度上仰和右转
DOWN_LEFT           = 27 # 云台以SS的速度下俯和左转
DOWN_RIGHT          = 28 # 云台以SS的速度下俯和右转
PAN_AUTO            = 29 # 云台以SS的速度左右自动扫描

FILL_PRE_SEQ        = 30 # 将预置点加入巡航序列
SET_SEQ_DWELL       = 31 # 设置巡航点停顿时间
SET_SEQ_SPEED       = 32 # 设置巡航速度
CLE_PRE_SEQ         = 33 # 将预置点从巡航序列中删除
STA_MEM_CRUISE      = 34 # 开始记录轨迹
STO_MEM_CRUISE      = 35 # 停止记录轨迹
RUN_CRUISE          = 36 # 开始轨迹
RUN_SEQ             = 37 # 开始巡航
STOP_SEQ            = 38 # 停止巡航
GOTO_PRESET         = 39 # 快球转到预置点

DEL_SEQ             = 43 # 删除巡航路径
STOP_CRUISE         = 44 # 停止轨迹
DELETE_CRUISE       = 45 # 删除单条轨迹
DELETE_ALL_CRUISE   = 46 # 删除所有轨迹

PAN_CIRCLE          = 50 # 云台以SS的速度自动圆周扫描
DRAG_PTZ            = 51 # 拖动PTZ
LINEAR_SCAN         = 52 # 区域扫描   //2014-03-15
CLE_ALL_PRESET      = 53 # 预置点全部清除
CLE_ALL_SEQ         = 54 # 巡航全部清除
CLE_ALL_CRUISE      = 55 # 轨迹全部清除

POPUP_MENU          = 56 # 显示操作菜单

TILT_DOWN_ZOOM_IN   = 58 # 云台以SS的速度下俯&&焦距以速度SS变大(倍率变大)
TILT_DOWN_ZOOM_OUT  = 59 # 云台以SS的速度下俯&&焦距以速度SS变小(倍率变小)
PAN_LEFT_ZOOM_IN    = 60 # 云台以SS的速度左转&&焦距以速度SS变大(倍率变大)
PAN_LEFT_ZOOM_OUT   = 61 # 云台以SS的速度左转&&焦距以速度SS变小(倍率变小)
PAN_RIGHT_ZOOM_IN   = 62 # 云台以SS的速度右转&&焦距以速度SS变大(倍率变大)
PAN_RIGHT_ZOOM_OUT  = 63 # 云台以SS的速度右转&&焦距以速度SS变小(倍率变小)
UP_LEFT_ZOOM_IN     = 64 # 云台以SS的速度上仰和左转&&焦距以速度SS变大(倍率变大)
UP_LEFT_ZOOM_OUT    = 65 # 云台以SS的速度上仰和左转&&焦距以速度SS变小(倍率变小)
UP_RIGHT_ZOOM_IN    = 66 # 云台以SS的速度上仰和右转&&焦距以速度SS变大(倍率变大)
UP_RIGHT_ZOOM_OUT   = 67 # 云台以SS的速度上仰和右转&&焦距以速度SS变小(倍率变小)
DOWN_LEFT_ZOOM_IN   = 68 # 云台以SS的速度下俯和左转&&焦距以速度SS变大(倍率变大)
DOWN_LEFT_ZOOM_OUT  = 69 # 云台以SS的速度下俯和左转&&焦距以速度SS变小(倍率变小)
DOWN_RIGHT_ZOOM_IN  = 70 # 云台以SS的速度下俯和右转&&焦距以速度SS变大(倍率变大)
DOWN_RIGHT_ZOOM_OUT = 71 # 云台以SS的速度下俯和右转&&焦距以速度SS变小(倍率变小)
TILT_UP_ZOOM_IN     = 72 # 云台以SS的速度上仰&&焦距以速度SS变大(倍率变大)
TILT_UP_ZOOM_OUT    = 73 # 云台以SS的速度上仰&&焦距以速度SS变小(倍率变小)

__curdir__ = os.path.abspath(os.path.dirname(__file__))


####################################################
### Error codes                                  ###
####################################################
NET_DVR_UNKNOW                          = -1 # DLL加载错误
NET_DVR_NOERROR                         = 0 # 没有错误
NET_DVR_PASSWORD_ERROR                  = 1 # 用户名密码错误
NET_DVR_NOENOUGHPRI                     = 2 # 权限不足
NET_DVR_NOINIT                          = 3 # 没有初始化
NET_DVR_CHANNEL_ERROR                   = 4 # 通道号错误
NET_DVR_OVER_MAXLINK                    = 5 # 连接到DVR的客户端个数超过最大
NET_DVR_VERSIONNOMATCH                  = 6 # 版本不匹配
NET_DVR_NETWORK_FAIL_CONNECT            = 7 # 连接服务器失败
NET_DVR_NETWORK_SEND_ERROR              = 8 # 向服务器发送失败
NET_DVR_NETWORK_RECV_ERROR              = 9 # 从服务器接收数据失败
NET_DVR_NETWORK_RECV_TIMEOUT            = 10 # 从服务器接收数据超时
NET_DVR_NETWORK_ERRORDATA               = 11 # 传送的数据有误
NET_DVR_ORDER_ERROR                     = 12 # 调用次序错误
NET_DVR_OPERNOPERMIT                    = 13 # 无此权限
NET_DVR_COMMANDTIMEOUT                  = 14 # DVR命令执行超时
NET_DVR_ERRORSERIALPORT                 = 15 # 串口号错误
NET_DVR_ERRORALARMPORT                  = 16 # 报警端口错误
NET_DVR_PARAMETER_ERROR                 = 17 # 参数错误
NET_DVR_CHAN_EXCEPTION                  = 18 # 服务器通道处于错误状态
NET_DVR_NODISK                          = 19 # 没有硬盘
NET_DVR_ERRORDISKNUM                    = 20 # 硬盘号错误
NET_DVR_DISK_FULL                       = 21 # 服务器硬盘满
NET_DVR_DISK_ERROR                      = 22 # 服务器硬盘出错
NET_DVR_NOSUPPORT                       = 23 # 服务器不支持
NET_DVR_BUSY                            = 24 # 服务器忙
NET_DVR_MODIFY_FAIL                     = 25 # 服务器修改不成功
NET_DVR_PASSWORD_FORMAT_ERROR           = 26 # 密码输入格式不正确
NET_DVR_DISK_FORMATING                  = 27 # 硬盘正在格式化，不能启动操作
NET_DVR_DVRNORESOURCE                   = 28 # DVR资源不足
NET_DVR_DVROPRATEFAILED                 = 29 # DVR操作失败
NET_DVR_OPENHOSTSOUND_FAIL              = 30 # 打开PC声音失败
NET_DVR_DVRVOICEOPENED                  = 31 # 服务器语音对讲被占用
NET_DVR_TIMEINPUTERROR                  = 32 # 时间输入不正确
NET_DVR_NOSPECFILE                      = 33 # 回放时服务器没有指定的文件
NET_DVR_CREATEFILE_ERROR                = 34 # 创建文件出错
NET_DVR_FILEOPENFAIL                    = 35 # 打开文件出错
NET_DVR_OPERNOTFINISH                   = 36 # 上次的操作还没有完成
NET_DVR_GETPLAYTIMEFAIL                 = 37 # 获取当前播放的时间出错
NET_DVR_PLAYFAIL                        = 38 # 播放出错
NET_DVR_FILEFORMAT_ERROR                = 39 # 文件格式不正确
NET_DVR_DIR_ERROR                       = 40 # 路径错误
NET_DVR_ALLOC_RESOURCE_ERROR            = 41 # 资源分配错误
NET_DVR_AUDIO_MODE_ERROR                = 42 # 声卡模式错误
NET_DVR_NOENOUGH_BUF                    = 43 # 缓冲区太小
NET_DVR_CREATESOCKET_ERROR              = 44 # 创建SOCKET出错
NET_DVR_SETSOCKET_ERROR                 = 45 # 设置SOCKET出错
NET_DVR_MAX_NUM                         = 46 # 个数达到最大
NET_DVR_USERNOTEXIST                    = 47 # 用户不存在
NET_DVR_WRITEFLASHERROR                 = 48 # 写FLASH出错
NET_DVR_UPGRADEFAIL                     = 49 # DVR升级失败
NET_DVR_CARDHAVEINIT                    = 50 # 解码卡已经初始化过
NET_DVR_PLAYERFAILED                    = 51 # 调用播放库中某个函数失败
NET_DVR_MAX_USERNUM                     = 52 # 设备端用户数达到最大
NET_DVR_GETLOCALIPANDMACFAIL            = 53 # 获得客户端的IP地址或物理地址失败
NET_DVR_NOENCODEING                     = 54 # 该通道没有编码
NET_DVR_IPMISMATCH                      = 55 # IP地址不匹配
NET_DVR_MACMISMATCH                     = 56 # MAC地址不匹配
NET_DVR_UPGRADELANGMISMATCH             = 57 # 升级文件语言不匹配
NET_DVR_MAX_PLAYERPORT                  = 58 # 播放器路数达到最大
NET_DVR_NOSPACEBACKUP                   = 59 # 备份设备中没有足够空间进行备份
NET_DVR_NODEVICEBACKUP                  = 60 # 没有找到指定的备份设备
NET_DVR_PICTURE_BITS_ERROR              = 61 # 图像素位数不符，限24色
NET_DVR_PICTURE_DIMENSION_ERROR         = 62 # 图片高*宽超限， 限128*256
NET_DVR_PICTURE_SIZ_ERROR               = 63 # 图片大小超限，限100K
NET_DVR_LOADPLAYERSDKFAILED             = 64 # 载入当前目录下Player Sdk出错
NET_DVR_LOADPLAYERSDKPROC_ERROR         = 65 # 找不到Player Sdk中某个函数入口
NET_DVR_LOADDSSDKFAILED                 = 66 # 载入当前目录下DSsdk出错
NET_DVR_LOADDSSDKPROC_ERROR             = 67 # 找不到DsSdk中某个函数入口
NET_DVR_DSSDK_ERROR                     = 68 # 调用硬解码库DsSdk中某个函数失败
NET_DVR_VOICEMONOPOLIZE                 = 69 # 声卡被独占
NET_DVR_JOINMULTICASTFAILED             = 70 # 加入多播组失败
NET_DVR_CREATEDIR_ERROR                 = 71 # 建立日志文件目录失败
NET_DVR_BINDSOCKET_ERROR                = 72 # 绑定套接字失败
NET_DVR_SOCKETCLOSE_ERROR               = 73 # socket连接中断，此错误通常是由于连接中断或目的地不可达
NET_DVR_USERID_ISUSING                  = 74 # 注销时用户ID正在进行某操作
NET_DVR_SOCKETLISTEN_ERROR              = 75 # 监听失败
NET_DVR_PROGRAM_EXCEPTION               = 76 # 程序异常
NET_DVR_WRITEFILE_FAILED                = 77 # 写文件失败
NET_DVR_FORMAT_READONLY                 = 78 # 禁止格式化只读硬盘
NET_DVR_WITHSAMEUSERNAME                = 79 # 用户配置结构中存在相同的用户名
NET_DVR_DEVICETYPE_ERROR                = 80 # 导入参数时设备型号不匹配
NET_DVR_LANGUAGE_ERROR                  = 81 # 导入参数时语言不匹配
NET_DVR_PARAVERSION_ERROR               = 82 # 导入参数时软件版本不匹配
NET_DVR_IPCHAN_NOTALIVE                 = 83 # 预览时外接IP通道不在线
NET_DVR_RTSP_SDK_ERROR                  = 84 # 加载高清IPC通讯库StreamTransClient.dll失败
NET_DVR_CONVERT_SDK_ERROR               = 85 # 加载转码库失败
NET_DVR_IPC_COUNT_OVERFLOW              = 86 # 超出最大的ip接入通道数
NET_DVR_MAX_ADD_NUM                     = 87 # 添加标签(一个文件片段64)等个数达到最大
NET_DVR_PARAMMODE_ERROR                 = 88 # 图像增强仪，参数模式错误（用于硬件设置时，客户端进行软件设置时错误值）
NET_DVR_CODESPITTER_OFFLINE             = 89 # 视频综合平台，码分器不在线
NET_DVR_BACKUP_COPYING                  = 90 # 设备正在备份
NET_DVR_CHAN_NOTSUPPORT                 = 91 # 通道不支持该操作
NET_DVR_CALLINEINVALID                  = 92 # 高度线位置太集中或长度线不够倾斜
NET_DVR_CALCANCELCONFLICT               = 93 # 取消标定冲突，如果设置了规则及全局的实际大小尺寸过滤
NET_DVR_CALPOINTOUTRANGE                = 94 # 标定点超出范围
NET_DVR_FILTERRECTINVALID               = 95 # 尺寸过滤器不符合要求
NET_DVR_DDNS_DEVOFFLINE                 = 96 # 设备没有注册到ddns上
NET_DVR_DDNS_INTER_ERROR                = 97 # DDNS 服务器内部错误
NET_DVR_FUNCTION_NOT_SUPPORT_OS         = 98 # 此功能不支持该操作系统
NET_DVR_DEC_CHAN_REBIND                 = 99 # 解码通道绑定显示输出次数受限
NET_DVR_INTERCOM_SDK_ERROR              = 100 # 加载当前目录下的语音对讲库失败
NET_DVR_NO_CURRENT_UPDATEFILE           = 101 # 没有正确的升级包
NET_DVR_USER_NOT_SUCC_LOGIN             = 102 # 用户还没登陆成功
NET_DVR_USE_LOG_SWITCH_FILE             = 103 # 正在使用日志开关文件
NET_DVR_POOL_PORT_EXHAUST               = 104 # 端口池中用于绑定的端口已耗尽
NET_DVR_PACKET_TYPE_NOT_SUPPORT         = 105 # 码流封装格式错误
NET_DVR_IPPARA_IPID_ERROR               = 106 # IP接入配置时IPID有误


####################################################
### Error definitions                            ###
####################################################
class HikError(Exception):
    __qualname__ = 'HikError'

    def __init__(self, function, code, text):
        self.__function = function
        self.__code = code
        self.__text = text

    @property
    def message(self):
        return "%s(%s): %s" % (str(self.__function), str(self.__code), str(self.__text))


####################################################
### Structures to be used in the library         ###
####################################################
class NET_DVR_IPADDR(Structure):
    _fields_ = [
                ("sIpV4", CHAR * 16), # IPv4地址
                ("byIPv6", BYTE * 128) # IPv6地址
                ]

LPNET_DVR_IPADDR = POINTER(NET_DVR_IPADDR)

class NET_DVR_TIME(Structure):
    _fields_ = [
                ("dwYear", DWORD), # 年
                ("dwMonth", DWORD), # 月
                ("dwDay", DWORD), # 日
                ("dwHour", DWORD), # 时
                ("dwMinute", DWORD), # 分
                ("dwSecond", DWORD) # 秒
                ]

LPNET_DVR_TIME = POINTER(NET_DVR_TIME)

class NET_DVR_TIMEPOINT(Structure):
    _fields_ = [
                ("dwMonth", DWORD), # 月 0-11表示1-12个月
                ("dwWeekNo", DWORD), # 第几周 0－第1周 1－第2周 2－第3周 3－第4周 4－最后一周
                ("dwWeekDate", DWORD), # 星期几 0－星期日 1－星期一 2－星期二 3－星期三 4－星期四 5－星期五 6－星期六
                ("dwHour", DWORD), # 小时    开始时间0－23 结束时间1－23
                ("dwMin", DWORD) # 分    0－59
                ]

LPNET_DVR_TIMEPOINT = POINTER(NET_DVR_TIMEPOINT)

class NET_DVR_ZONEANDDST(Structure):
    _fields_ = [
                ("dwSize", DWORD),
                ("dwZoneIndex", DWORD), # 应用层软件使用NET_DVR_NTPPARA 中的cTimeDifferenceH 或cTimeDifferenceM 来设置时区，此处用获取的值填充，不对用户提供输入编辑框
                ("byRes1", BYTE * 12), # 保留
                ("dwEnableDST", DWORD), # 是否启用夏时制 0－不启用 1－启用
                ("byDSTBias", BYTE), # 夏令时偏移值，30min, 60min, 90min, 120min, 以分钟计，传递原始数值
                ("byRes2", BYTE * 3),
                ("struBeginPoint", NET_DVR_TIMEPOINT), # 夏时制开始时间
                ("struEndPoint", NET_DVR_TIMEPOINT) # 夏时制停止时间
                ]

LPNET_DVR_ZONEANDDST = POINTER(NET_DVR_ZONEANDDST)

class NET_DVR_HOLIDATE_MODEA(Structure):
    _fields_ = [
                ("byStartMonth", BYTE), # 开始月 从1开始
                ("byStartDay", BYTE), # 开始日 从1开始
                ("byEndMonth", BYTE), # 结束月
                ("byEndDay", BYTE), # 结束日
                ("byRes", BYTE * 4) # 保留字节
                ]

LPNET_DVR_HOLIDATE_MODEA = POINTER(NET_DVR_HOLIDATE_MODEA)

class NET_DVR_HOLIDATE_MODEB(Structure):
    _fields_ = [
                ("byStartMonth", BYTE), # 从1开始
                ("byStartWeekNum", BYTE), # 第几个星期 从1开始
                ("byStartWeekday", BYTE), # 星期几
                ("byEndMonth", BYTE), # 从1开始
                ("byEndWeekNum", BYTE),  # 第几个星期 从1开始
                ("byEndWeekday", BYTE),  # 星期几
                ("byRes", BYTE * 2)  # 保留字节
                ]

LPNET_DVR_HOLIDATE_MODEB = POINTER(NET_DVR_HOLIDATE_MODEB)

class NET_DVR_HOLIDATE_MODEC(Structure):
    _fields_ = [
                ("wStartYear", WORD), # 年
                ("byStartMon", BYTE), # 月
                ("byStartDay", BYTE), # 日
                ("wEndYear", WORD), # 年
                ("byEndMon", BYTE),  # 月
                ("byEndDay", BYTE)  # 日
                ]

LPNET_DVR_HOLIDATE_MODEC = POINTER(NET_DVR_HOLIDATE_MODEC)

class NET_DVR_HOLIDATE_UNION(Structure):
    _fields_ = [
                ("dwSize", DWORD), # 联合体大小 12字节
                ("struModeA", NET_DVR_HOLIDATE_MODEA), # 模式A
                ("struModeB", NET_DVR_HOLIDATE_MODEB), # 模式B
                ("struModeC", NET_DVR_HOLIDATE_MODEC) # 模式C
                ]

LPNET_DVR_HOLIDATE_UNION = POINTER(NET_DVR_HOLIDATE_UNION)

class NET_DVR_HOLIDAY_PARAM(Structure):
    _fields_ = [
                ("byEnable", BYTE), # 是否启用
                ("byDateMode", BYTE), # 日期模式 0-模式A 1-模式B 2-模式C
                ("byRes1", BYTE * 2), # 保留字节
                ("uHolidate", NET_DVR_HOLIDATE_UNION), # 假日日期
                ("byName", BYTE * NAME_LEN), # 假日名称
                ("byRes2", BYTE * 20) # 保留字节
                ]

LPNET_DVR_HOLIDAY_PARAM = POINTER(NET_DVR_HOLIDAY_PARAM)

class NET_DVR_HOLIDAY_PARAM_CFG(Structure):
    _fields_ = [
                ("dwSize", DWORD), # 结构体大小
                ("struHolidayParam", NET_DVR_HOLIDAY_PARAM * MAX_HOLIDAY_NUM), # 假日参数
                ("byRes", DWORD * 40) # 保留参数
                ]

LPNET_DVR_HOLIDAY_PARAM_CFG = POINTER(NET_DVR_HOLIDAY_PARAM_CFG)

class NET_DVR_HANDLEEXCEPTION(Structure):
    _fields_ = [
                ("dwHandleType", DWORD),
                ("byRelAlarmOut", BYTE * MAX_ALARMOUT)
                # 数组0-盘满,1- 硬盘出错,2-网线断,3-局域网内IP 地址冲突,4-非法访问, 5-输入/输出视频制式不匹配, 6-视频信号异常
                ]

LPNET_DVR_HANDLEEXCEPTION = POINTER(NET_DVR_HANDLEEXCEPTION)

class NET_DVR_EXCEPTION(Structure):
    _fields_ = [
                ("dwSize", DWORD),
                ("struExceptionHandleType", NET_DVR_HANDLEEXCEPTION * MAX_EXCEPTIONNUM)
                # 数组0-盘满,1- 硬盘出错,2-网线断,3-局域网内IP 地址冲突,4-非法访问, 5-输入/输出视频制式不匹配, 6-视频信号异常
                ]

LPNET_DVR_EXCEPTION = POINTER(NET_DVR_EXCEPTION)

class NET_DVR_HANDLEEXCEPTION_V30(Structure):
    _fields_ = [
                ("dwHandleType", DWORD), # 处理方式,处理方式的"或"结果
                                        # 0x00: 无响应
                                        # 0x01: 监视器上警告
                                        # 0x02: 声音警告
                                        # 0x04: 上传中心
                                        # 0x08: 触发报警输出
                                        # 0x10: 触发JPRG抓图并上传Email
                                        # 0x20: 无线声光报警器联动
                                        # 0x40: 联动电子地图(目前只有PCNVR支持)
                                        # 0x200: 抓图并上传FTP
                                        # 0x2000:短信报警
                ("byRelAlarmOut", BYTE * MAX_ALARMOUT_V30)
                # 报警触发的输出通道,报警触发的输出,为1表示触发该输出
                ]

LPNET_DVR_HANDLEEXCEPTION_V30 = POINTER(NET_DVR_HANDLEEXCEPTION_V30)

class NET_DVR_EXCEPTION_V30(Structure):
    _fields_ = [
                ("dwSize", DWORD),
                ("struExceptionHandleType", NET_DVR_HANDLEEXCEPTION_V30 * MAX_EXCEPTIONNUM_V30)
                # 数组0-盘满,1- 硬盘出错,2-网线断,3-局域网内IP 地址冲突, 4-非法访问, 5-输入/输出视频制式不匹配, 6-视频信号异常, 7-录像异常 8-阵列异常，9-前端/录像分辨率不匹配异常，10-行车超速(车载专用) 11-热备异常（N+1使用）12-温度，13-子系统异常，14-风扇异常, 15-POE供电异常, 16-POC异常,数组17-电源电压波动异常
                ]

LPNET_DVR_EXCEPTION_V30 = POINTER(NET_DVR_EXCEPTION_V30)

class NET_DVR_HANDLEEXCEPTION_V41(Structure):
    _fields_ = [
                ("dwHandleType", DWORD), # 异常处理,异常处理方式的"或"结果
                                        # 0x00: 无响应
                                        # 0x01: 监视器上警告
                                        # 0x02: 声音警告
                                        # 0x04: 上传中心
                                        # 0x08: 触发报警输出
                                        # 0x10: 触发JPRG抓图并上传Email
                                        # 0x20: 无线声光报警器联动
                                        # 0x40: 联动电子地图(目前只有PCNVR支持)
                                        # 0x200: 抓图并上传FTP
                                        # 0x400: 虚交侦测 联动 聚焦模式（提供可配置项，原先设备自动完成）IPC5.1.0
                                        # 0x800: PTZ联动跟踪(球机跟踪目标)
                                        # 0x4000:白光灯报警
                                        # 0x10000:短信报警
                ("dwMaxRelAlarmOutChanNum", DWORD), # 触发的报警输出通道数（只读）最大支持数
                ("dwRelAlarmOut", DWORD * MAX_ALARMOUT_V40), # 触发报警通道
                ("byRes", BYTE * 64) # 保留
                ]

LPNET_DVR_HANDLEEXCEPTION_V41 = POINTER(NET_DVR_HANDLEEXCEPTION_V41)

class NET_DVR_EXCEPTION_V40(Structure):
    _fields_ = [
                ("dwSize", DWORD), # 结构体大小
                ("dwMaxGroupNum", DWORD), # 设备支持的最大组数
                ("struExceptionHandleType", NET_DVR_HANDLEEXCEPTION_V41 * MAX_EXCEPTIONNUM_V30),
                ("byRes", BYTE * 128) # 保留
                ]

LPNET_DVR_EXCEPTION_V40 = POINTER(NET_DVR_EXCEPTION_V40)

class NET_DVR_PPPCFG(Structure):
    _fields_ = [
                ("sRemoteIP", CHAR * 16), # 远端IP地址
                ("sLocalIP", CHAR * 16), # 本地IP地址
                ("sLocalIPMask", CHAR * 16), # 本地IP地址掩码
                ("sUsername", BYTE * NAME_LEN), # 用户名
                ("sPassword", BYTE * PASSWD_LEN), # 密码
                ("byPPPMode", BYTE), # PPP模式, 0－主动，1－被动
                ("byRedial", DWORD), # 是否回拨 ：0-否,1-是
                ("byRedialMode", BYTE), # 回拨模式,0-由拨入者指定,1-预置回拨号码
                ("byDataEncrypt", BYTE), # 数据加密,0-否,1-是
                ("dwMTU", DWORD), # MTU
                ("sTelephoneNumber", CHAR * PHONENUMBER_LEN) # 电话号码
                ]

LPNET_DVR_PPPCFG = POINTER(NET_DVR_PPPCFG)

class NET_DVR_PPPCFG_V30(Structure):
    _fields_ = [
                ("struRemoteIP", NET_DVR_IPADDR), # 远端IP地址
                ("struLocalIP", NET_DVR_IPADDR), # 本地IP地址
                ("sLocalIPMask", CHAR * 16), # 本地IP地址掩码
                ("sUsername", BYTE * NAME_LEN), # 用户名
                ("sPassword", BYTE * PASSWD_LEN), # 密码
                ("byPPPMode", BYTE), # PPP模式, 0－主动，1－被动
                ("byRedial", DWORD), # 是否回拨 ：0-否,1-是
                ("byRedialMode", BYTE), # 回拨模式,0-由拨入者指定,1-预置回拨号码
                ("byDataEncrypt", BYTE), # 数据加密,0-否,1-是
                ("dwMTU", DWORD), # MTU
                ("sTelephoneNumber", CHAR * PHONENUMBER_LEN) # 电话号码
                ]

LPNET_DVR_PPPCFG_V30 = POINTER(NET_DVR_PPPCFG_V30)

class NET_DVR_DIRECT_CONNECT_CHAN_INFO(Structure):
    _fields_ = [
                ("byEnable", BYTE), # 是否启用
                ("byProType", BYTE), # 协议类型，0-私有协议(default), (需要从设备获取能力)
                ("byZeroChan", BYTE), # 是否是零通道,0-不是，1-是
                ("byPriority", BYTE), # 优先级
                ("sUserName", BYTE * NAME_LEN), # 用户名
                ("sPassword", BYTE * PASSWD_LEN), # 密码
                ("byDomain", BYTE * MAX_DOMAIN_NAME), # 设备域名
                ("struIP", NET_DVR_IPADDR), # IP地址
                ("wDVRPort", WORD), # 端口号
                ("byStreamType", BYTE), # 主码流:0; 子码流：1
                ("byOnline", BYTE), # 只读，0-不在线 1-在线
                ("dwChannel", DWORD), # 通道号
                ("byTransProtocol", BYTE), # 协议类型，0-TCP，1-UDP，2-多播
                ("byLocalBackUp", BYTE), # 本地备份: 0-不启用CVR本地备份，1-启用CVR本地备份--即回放时的流一份在录像卷，一份在存档卷（本地备份）
                ("wDirectLastTime", WORD), # 导播持续时间
                ("byChanNo", BYTE * CHAN_NO_LEN) # 通道编号--用于VAG取流
                ]

LPNET_DVR_DIRECT_CONNECT_CHAN_INFO = POINTER(NET_DVR_DIRECT_CONNECT_CHAN_INFO)

class NET_DVR_PU_STREAM_URL(Structure):
    _fields_ = [
                ("byEnable", BYTE),
                ("strURL", BYTE),
                ("byTransPortocol", BYTE), # 传输协议类型 0-tcp  1-UDP
                ("wIPID", WORD), # 设备ID号，wIPID = iDevInfoIndex + iGroupNO*64 +1
                ("byChannel", BYTE), # 通道号
                ("byRes", BYTE * 7)
                ]

LPNET_DVR_PU_STREAM_URL = POINTER(NET_DVR_PU_STREAM_URL)

class NET_DVR_PU_STREAM_URL_CFG(Structure):
    _fields_ = [
                ("byEnable", BYTE),
                ("byRes", BYTE * 3),
                ("byStreamMediaIP", BYTE * 64), # 流媒体IP
                ("wStreamMediaPort", WORD), # 流媒体端口
                ("byTransmitType", BYTE), # 流媒体传输协议 0- TCP  1- UDP
                ("byRes1", BYTE * 33),
                ("byDevIP", BYTE * 64), # 设备IP
                ("wDevPort", BYTE), # 设备端口
                ("byChannel", BYTE), # 通道号
                ("byTransMode", BYTE), # 传输模式 0-主码流 1- 子码流
                ("byProType", BYTE),
                # 家类型 0-私有 1-大华 2-汉邦 3-郎驰 4-蓝色星际 NET_DVR_GetIPCProtoList接口获取
                # VQD流媒体下只支持 0，1方式；直连支持 0，1，2，3，4
                ("byTransProtocol", BYTE), # 传输协议类型0-TCP,  1-UDP,  2-多播方式,  3-RTP
                ("byRes3", BYTE * 2),
                ("sUserName", BYTE * NAME_LEN), # 设备登陆用户名
                ("sPassWord", BYTE * PASSWD_LEN), # 设备登陆密码
                ("byRes2", BYTE) # 预留
                ]

LPNET_DVR_PU_STREAM_URL_CFG = POINTER(NET_DVR_PU_STREAM_URL_CFG)

class NET_DVR_STREAM_TYPE_UNION(Structure):
    _fields_ = [
                ("struChanInfo", NET_DVR_DIRECT_CONNECT_CHAN_INFO),
                ("struStreamUrl", NET_DVR_PU_STREAM_URL),
                ("struStreamUrlCfg", NET_DVR_PU_STREAM_URL_CFG)
                ]

LPNET_DVR_STREAM_TYPE_UNION = POINTER(NET_DVR_STREAM_TYPE_UNION)


class NET_DVR_DEVICEINFO_V30(Structure):
    _fields_ = [
                ("sSerialNumber", BYTE * SERIALNO_LEN), # 序列号
                ("byAlarmInPortNum", BYTE), # 报警输入个数
                ("byAlarmOutPortNum", BYTE), # 报警输出个数
                ("byDiskNum", BYTE), # 硬盘个数
                ("byDVRType", BYTE), # 设备类型, 1:DVR 2:ATM DVR 3:DVS ......
                ("byChanNum", BYTE), # 模拟通道个数
                ("byStartChan", BYTE), # 起始通道号,例如DVS-1,DVR - 1
                ("byAudioChanNum", BYTE), # 语音通道数
                ("byIPChanNum", BYTE), # 最大数字通道个数，低位
                ("byZeroChanNum", BYTE), # 零通道编码个数 //2010-01-16
                ("byMainProto", BYTE), # 主码流传输协议类型 0-private, 1-rtsp,2-同时支持private和rtsp
                ("bySubProto", BYTE), # 子码流传输协议类型0-private, 1-rtsp,2-同时支持private和rtsp
                ("bySupport", BYTE), # 能力，位与结果为0表示不支持，1表示支持，
                                    # bySupport & 0x1, 表示是否支持智能搜索
                                    # bySupport & 0x2, 表示是否支持备份
                                    # bySupport & 0x4, 表示是否支持压缩参数能力获取
                                    # bySupport & 0x8, 表示是否支持多网卡
                                    # bySupport & 0x10, 表示支持远程SADP
                                    # bySupport & 0x20, 表示支持Raid卡功能
                                    # bySupport & 0x40, 表示支持IPSAN 目录查找
                                    # bySupport & 0x80, 表示支持rtp over rtsp
                ("bySupport1", BYTE), # 能力集扩充，位与结果为0表示不支持，1表示支持
                                    # bySupport1 & 0x1, 表示是否支持snmp v30
                                    # bySupport1 & 0x2, 支持区分回放和下载
                                    # bySupport1 & 0x4, 是否支持布防优先级
                                    # bySupport1 & 0x8, 智能设备是否支持布防时间段扩展
                                    # bySupport1 & 0x10, 表示是否支持多磁盘数（超过33个）
                                    # bySupport1 & 0x20, 表示是否支持rtsp over http
                                    # bySupport1 & 0x80, 表示是否支持车牌新报警信息2012-9-28, 且还表示是否支持NET_DVR_IPPARACFG_V40结构体
                ("bySupport2", BYTE), # 能力，位与结果为0表示不支持，非0表示支持
                                    # bySupport2 & 0x1, 表示解码器是否支持通过URL取流解码
                                    # bySupport2 & 0x2,  表示支持FTPV40
                                    # bySupport2 & 0x4,  表示支持ANR
                                    # bySupport2 & 0x8,  表示支持CCD的通道参数配置
                                    # bySupport2 & 0x10,  表示支持布防报警回传信息（仅支持抓拍机报警 新老报警结构）
                                    # bySupport2 & 0x20,  表示是否支持单独获取设备状态子项
                                    # bySupport2 & 0x40,  表示是否是码流加密设备
                ("wDevType", WORD), # 设备型号
                ("bySupport3", BYTE), # 能力集扩展，位与结果为0表示不支持，1表示支持
                                    # bySupport3 & 0x1, 表示是否支持批量配置多码流参数
                                    # bySupport3 & 0x4 表示支持按组配置， 具体包含 通道图像参数、报警输入参数、IP报警输入、输出接入参数、
                                    # 用户参数、设备工作状态、JPEG抓图、定时和时间抓图、硬盘盘组管理
                                    # bySupport3 & 0x8为1 表示支持使用TCP预览、UDP预览、多播预览中的"延时预览"字段来请求延时预览（后续都将使用这种方式请求延时预览）。而当bySupport3 & 0x8为0时，将使用 "私有延时预览"协议。
                                    # bySupport3 & 0x10 表示支持"获取报警主机主要状态（V40）"。
                                    # bySupport3 & 0x20 表示是否支持通过DDNS域名解析取流
                ("byMultiStreamProto", BYTE), # 是否支持多码流,按位表示,0-不支持,1-支持,bit1-码流3,bit2-码流4,bit7-主码流，bit-8子码流
                ("byStartDChan", BYTE), # 起始数字通道号,0表示无效
                ("byStartDTalkChan", BYTE), # 起始数字对讲通道号，区别于模拟对讲通道号，0表示无效
                ("byHighDChanNum", BYTE), # 数字通道个数，高位
                ("bySupport4", BYTE), # 能力集扩展，位与结果为0表示不支持，1表示支持
                                    # bySupport4 & 0x4表示是否支持拼控统一接口
                                    # bySupport4 & 0x80 支持设备上传中心报警使能。表示判断调用接口是 NET_DVR_PDC_RULE_CFG_V42还是 NET_DVR_PDC_RULE_CFG_V41
                ("byLanguageType", BYTE), # 支持语种能力,按位表示,每一位0-不支持,1-支持
                                        # byLanguageType 等于0 表示 老设备
                                        # byLanguageType & 0x1表示支持中文
                                        # byLanguageType & 0x2表示支持英文
                ("byVoiceInChanNum", BYTE), # 音频输入通道数
                ("byStartVoiceInChanNo", BYTE), # 音频输入起始通道号 0表示无效
                ("bySupport5", BYTE), # 按位表示,0-不支持,1-支持,bit0-支持多码流
                                    # bySupport5 &0x01表示支持wEventTypeEx ,兼容dwEventType 的事件类型（支持行为事件扩展）--先占住，防止冲突
                                    # bySupport5 &0x04表示是否支持使用扩展的场景模式接口
                                    # bySupport5 &0x08 设备返回该值表示是否支持计划录像类型V40接口协议(DVR_SET_RECORDCFG_V40/ DVR_GET_RECORDCFG_V40)(在该协议中设备支持类型类型13的配置)
                                    # 之前的部分发布的设备，支持录像类型13，则配置录像类型13。如果不支持，统一转换成录像类型3兼容处理。SDK通过命令探测处理)
                                    # bySupport5 &0x10 设备返回改值表示支持超过255个预置点
                ("bySupport6", BYTE), # 能力，按位表示，0-不支持,1-支持
                                    # bySupport6 0x1  表示设备是否支持压缩
                                    # bySupport6 0x2 表示是否支持流ID方式配置流来源扩展命令，DVR_SET_STREAM_SRC_INFO_V40
                                    # bySupport6 0x4 表示是否支持事件搜索V40接口
                                    # bySupport6 0x8 表示是否支持扩展智能侦测配置命令
                                    # bySupport6 0x40表示图片查询结果V40扩展
                ("byMirrorChanNum", BYTE), # 镜像通道个数，<录播主机中用于表示导播通道>
                ("wStartMirrorChanNo", WORD), # 起始镜像通道号
                ("bySupport7", BYTE), # 能力,按位表示,0-不支持,1-支持
                                    # bySupport7 & 0x1  表示设备是否支持 INTER_VCA_RULECFG_V42 扩展
                                    # bySupport7 & 0x2  表示设备是否支持 IPC HVT 模式扩展
                                    # bySupport7 & 0x04  表示设备是否支持 返回锁定时间
                                    # bySupport7 & 0x08  表示设置云台PTZ位置时，是否支持带通道号
                                    # bySupport7 & 0x10  表示设备是否支持双系统升级备份
                                    # bySupport7 & 0x20  表示设备是否支持 OSD字符叠加 V50
                                    # bySupport7 & 0x40  表示设备是否支持 主从跟踪（从摄像机）
                                    # bySupport7 & 0x80  表示设备是否支持 报文加密
                ("byRes2", BYTE) # 保留
                ]

LPNET_DVR_DEVICEINFO_V30 = POINTER(NET_DVR_DEVICEINFO_V30)

class NET_DVR_CLIENTINFO(Structure):
    _fields_ = [
                ("lChannel", LONG), # 通道号
                ("lLinkMode", LONG), # 最高位(31)为0表示主码流，为1表示子，0－30位表示码流连接方式: 0：TCP方式,1：UDP方式,2：多播方式,3 - RTP方式，4-RTP/RTSP,5-RSTP/HTTP
                ("hPlayWnd", HWND), # 播放窗口的句柄,为NULL表示不播放图象
                ("sMultiCastIP", CHARP), # 多播组地址
                ("byProtoType", BYTE), # 应用层取流协议，0-私有协议，1-RTSP协议
                ("byRes", CHAR * 3) # 保留
                ]

LPNET_DVR_CLIENTINFO = POINTER(NET_DVR_CLIENTINFO)

class NET_DVR_PREVIEWINFO(Structure):
    _fields_ = [
                ("lChannel",LONG), # 通道号
                ("dwStreamType", DWORD), # 码流类型，0-主码流，1-子码流，2-码流3，3-码流4, 4-码流5,5-码流6,7-码流7,8-码流8,9-码流9,10-码流10
                ("dwLinkMode", DWORD), # 0：TCP方式,1：UDP方式,2：多播方式,3 - RTP方式，4-RTP/RTSP,5-RSTP/HTTP ,6- HRUDP（可靠传输） ,7-RTSP/HTTPS
                ("hPlayWnd", HWND), # 播放窗口的句柄,为NULL表示不播放图象
                ("bBlocked", DWORD), # 0-非阻塞取流, 1-阻塞取流, 如果阻塞SDK内部connect失败将会有5s的超时才能够返回,不适合于轮询取流操作.
                ("bPassbackRecord", DWORD), # 0-不启用录像回传,1启用录像回传
                ("byPreviewMode", BYTE), # 预览模式，0-正常预览，1-延迟预览
                ("byStreamID", BYTE * STREAM_ID_LEN), # 流ID，lChannel为0xffffffff时启用此参数
                ("byProtoType", BYTE), # 应用层取流协议，0-私有协议，1-RTSP协议,2-SRTP码流加密（对应此结构体中dwLinkMode 字段，支持如下方式, 为1，表示udp传输方式，信令走TLS加密，码流走SRTP加密，为2，表示多播传输方式，信令走TLS加密，码流走SRTP加密）
                ("byRes1", BYTE), # 保留
                ("byVideoCodingType", BYTE), # 码流数据编解码类型 0-通用编码数据 1-热成像探测器产生的原始数据（温度数据的加密信息，通过去加密运算，将原始数据算出真实的温度值）
                ("dwDisplayBufNum", DWORD), # 播放库播放缓冲区最大缓冲帧数，范围1-50，置0时默认为1
                ("byNPQMode", BYTE), # NPQ是直连模式，还是过流媒体 0-直连 1-过流媒体
                ("byRecvMetaData", BYTE), # 是否接收metadata数据，设备是否支持该功能通过GET /ISAPI/System/capabilities 中DeviceCap.SysCap.isSupportMetadata是否存在且为true
                ("byRes",CHAR * 214) # 保留
                ]

LPNET_DVR_PREVIEWINFO = POINTER(NET_DVR_PREVIEWINFO)

class NET_DVR_IPDEVINFO_V31(Structure):
    _fields_ = [
                ("byEnable", BYTE), # 该IP设备是否有效
                ("byProType", BYTE), # 协议类型，0-私有协议，1-松下协议，2-索尼
                ("byEnableQuickAdd", BYTE), # 0 不支持快速添加  1 使用快速添加 , 快速添加需要设备IP和协议类型，其他信息由设备默认指定
                ("byCameraType", BYTE), # 通道接入的相机类型，值为 0-无意义，1-老师跟踪，2-学生跟踪，3-老师全景，4-学生全景，5-多媒体，6–教师定位,7-学生定位,8-板书定位,9-板书相机
                ("sUserName", BYTE * NAME_LEN), # 用户名
                ("sPassword", BYTE * PASSWD_LEN), # 密码
                ("byDomain", BYTE * MAX_DOMAIN_NAME), # 设备域名
                ("struIP", NET_DVR_IPADDR), # IP地址
                ("wDVRPort", WORD), # 端口号
                ("szDeviceID", BYTE * DEV_ID_LEN), # 设备ID
                ("byEnableTiming", BYTE), # 0-保留，1-不启用NVR对IPC自动校时，2-启用NVR对IPC自动校时
                ("byCertificateValidation", BYTE) # 证书验证
                                                # byCertificateValidation:bit0: 0-不启用证书验证 1-启用证书验证
                                                # byCertificateValidation:bit1: 0-不启用默认通信端口 1-启用默认通信端口
                ]

LPNET_DVR_IPDEVINFO_V31 = POINTER(NET_DVR_IPDEVINFO_V31)

class NET_DVR_STREAM_MODE(Structure):
    _fields_ = [
                ("byGetStreamType", BYTE),
                ("byRes", BYTE * 3),
                ("uGetStream", NET_DVR_STREAM_TYPE_UNION)
                ]

LPNET_DVR_STREAM_MODE = POINTER(NET_DVR_STREAM_MODE)

class NET_DVR_IPPARACFG_V40(Structure):
    _fields_ = [
                ("dwSize", DWORD), # 结构大小
                ("dwGroupNum", DWORD), # 设备支持的总组数
                ("dwAChanNum", DWORD), # 最大模拟通道个数
                ("dwDChanNum", DWORD), # 数字通道个数
                ("dwStartDChan", DWORD), # 起始数字通道
                ("byAnalogChanEnable", BYTE * MAX_CHANNUM_V30), # 模拟通道是否启用，从低到高表示1-64通道，0表示无效 1有效
                ("struIPDevInfo", NET_DVR_IPDEVINFO_V31), # IP设备
                ("struStreamMode", NET_DVR_STREAM_MODE),
                ("byRes2", BYTE * 20) # 保留字节
                ]

LPNET_DVR_IPPARACFG_V40 = POINTER(NET_DVR_IPPARACFG_V40)

class NET_DVR_DEVSERVER_CFG(Structure):
    _fields_ = [
                ("dwSize", DWORD),
                ("byIrLampServer", BYTE), # 红外灯设置 0～禁用，1～启用
                ("bytelnetServer", BYTE), # telnet设置 0～禁用，1～启用
                ("byABFServer", BYTE), # ABF设置 0～启用，1～禁用
                ("byEnableLEDStatus", BYTE), # 状态指示灯控制 0～禁用，1～启用
                ("byEnableAutoDefog", BYTE), # 自动除雾控制 0～启用，1～禁用
                ("byEnableSupplementLight", BYTE), # 补光灯控制0-启用，1-禁用
                ("byEnableDeicing", BYTE), # 除冰功能 0-关闭，1-开启
                ("byEnableVisibleMovementPower", BYTE), # 可见光机芯电源开关 0-关闭，1-开启
                ("byEnableThermalMovementPower", BYTE), # 热成像机芯电源开关 0-关闭，1-开启
                ("byEnablePtzPower", BYTE), # 云台电源开关 0-关闭，1-开启
                ("byPowerSavingControl", BYTE),  # 低功耗策略 0-保留 1-休眠模式 2-低功耗模式 低功耗模式下 可见光机芯电源、热成像机芯电源、云台电源控制生效
                ("byCaptureWithSupplimentLightEnabled", BYTE),  # 启用抓拍补光使能 0-关闭，1-开启
                ("byRes", BYTE * 244)
                ]

LPNET_DVR_DEVSERVER_CFG = POINTER(NET_DVR_DEVSERVER_CFG)

class NET_DVR_DECODERCFG_V30(Structure):
    _fields_ = [
                ("dwSize", DWORD),
                ("dwBaudRate", DWORD), # 波特率(bps)，0－50，1－75，2－110，3－150，4－300，5－600，6－1200，7－2400，8－4800，9－9600，10－19200， 11－38400，12－57600，13－76800，14－115.2k;
                ("byDataBit", BYTE), # 数据有几位 0－5位，1－6位，2－7位，3－8位;
                ("byStopBit", BYTE), # 停止位 0－1位，1－2位;
                ("byParity", BYTE), # 校验 0－无校验，1－奇校验，2－偶校验;
                ("byFlowcontrol", BYTE), # 0－无，1－软流控,2-硬流控
                ("wDecoderType", WORD), # 解码器类型, 从0开始，对应ptz协议列表从NET_DVR_IPC_PROTO_LIST得到
                ("wDecoderAddress", WORD), # 解码器地址:0 - 255
                ("bySetPreset", BYTE * MAX_PRESET_V30), # 预置点是否设置,0-没有设置,1-设置
                ("bySetCruise", BYTE * MAX_CRUISE_V30), # 巡航是否设置: 0-没有设置,1-设置
                ("bySetTrack", BYTE * MAX_TRACK_V30) # 轨迹是否设置,0-没有设置,1-设置
                ]

LPNET_DVR_DECODERCFG_V30 = POINTER(NET_DVR_DECODERCFG_V30)

class NET_DVR_DECODERCFG_V40(Structure):
    _fields_ = [
                ("dwSize", DWORD),
                ("dwBaudRate", DWORD), # 波特率(bps)，0－50，1－75，2－110，3－150，4－300，5－600，6－1200，7－2400，8－4800，9－9600，10－19200， 11－38400，12－57600，13－76800，14－115.2k;
                ("byDataBit", BYTE),  # 数据有几位 0－5位，1－6位，2－7位，3－8位;
                ("byStopBit", BYTE),  # 停止位 0－1位，1－2位;
                ("byParity", BYTE),  # 校验 0－无校验，1－奇校验，2－偶校验;
                ("byFlowcontrol", BYTE),  # 0－无，1－软流控,2-硬流控
                ("wDecoderType", WORD),  # 解码器类型, 从0开始，对应ptz协议列表从NET_DVR_IPC_PROTO_LIST得到
                ("wDecoderAddress", WORD),  # 解码器地址:0 - 255
                ("bySetPreset", BYTE * MAX_PRESET_V30),  # 预置点是否设置,0-没有设置,1-设置
                ("bySetCruise", BYTE * MAX_CRUISE_V30),  # 巡航是否设置: 0-没有设置,1-设置
                ("bySetTrack", BYTE * MAX_TRACK_V30), # 轨迹是否设置,0-没有设置,1-设置
                ("bySerialNO", BYTE), # 串口编号
                ("byWorkMode", BYTE), # 工作模式， 1-矩阵串口控制，2-屏幕控制，3-透明通道模式 4-PPP模式 5-控制台模式 6-串口直连 7-键盘控制 8-监控板管理 9-控制云台 12-LED显示，13-触发抓拍数据传输
                ("byRes", BYTE * 254) # 保留
                ]

LPNET_DVR_DECODERCFG_V40 = POINTER(NET_DVR_DECODERCFG_V40)

class NET_DVR_RS232CFG(Structure):
    _fields_ = [
                ("dwSize", DWORD),
                ("dwBaudRate", DWORD), # 波特率(bps)，0－50，1－75，2－110，3－150，4－300，5－600，6－1200，7－2400，8－4800，9－9600，10－19200， 11－38400，12－57600，13－76800，14－115.2k;
                ("byDataBit", BYTE), # 数据有几位 0－5位，1－6位，2－7位，3－8位;
                ("byStopBit", BYTE), # 停止位 0－1位，1－2位;
                ("byParity", BYTE), # 校验 0－无校验，1－奇校验，2－偶校验;
                ("byFlowcontrol", BYTE), # 0－无，1－软流控,2-硬流控
                ("dwWorkMode", DWORD), # 工作模式，0－窄带传输(232串口用于PPP拨号)，1－控制台(232串口用于参数控制)，2－透明通道
                ("struPPPConfig", NET_DVR_PPPCFG)
                ]
LPNET_DVR_RS232CFG = POINTER(NET_DVR_RS232CFG)

class NET_DVR_SINGLE_RS232(Structure):
    _fields_ = [
                ("dwBaudRate", DWORD), # 波特率(bps)，0－50，1－75，2－110，3－150，4－300，5－600，6－1200，7－2400，8－4800，9－9600，10－19200， 11－38400，12－57600，13－76800，14－115.2k;
                ("byDataBit", BYTE), # 数据有几位 0－5位，1－6位，2－7位，3－8位
                ("byStopBit", BYTE), # 停止位 0－1位，1－2位
                ("byParity", BYTE), # 校验 0－无校验，1－奇校验，2－偶校验
                ("byFlowcontrol", BYTE), # 0－无，1－软流控,2-硬流控
                ("dwWorkMode", DWORD) # 工作模式，0－232串口用于PPP拨号，1－232串口用于参数控制，2－透明通道 3- ptz模式,审讯温湿度传感器, 4-报警盒模式  5-矩阵串口控制 6-屏幕控制 7-串口直连 8-键盘控制 9-监控板管理 10-控制云台
                ]
LPNET_DVR_SINGLE_RS232 = POINTER(NET_DVR_SINGLE_RS232)

class NET_DVR_RS232CFG_V30(Structure):
    _fields_ = [
                ("dwSize", DWORD),
                ("struRs232", NET_DVR_SINGLE_RS232 * MAX_SERIAL_PORT), # 注意：此结构修改了，原来是单个结构，现在修改为了数组结构
                ("struPPPConfig", NET_DVR_PPPCFG_V30)
                ]
LPNET_DVR_RS232CFG_V30 = POINTER(NET_DVR_RS232CFG_V30)

class NET_DVR_SDKLOCAL_CFG(Structure):
    _fields_ = [
                ("byEnableAbilityParse", BYTE), # 使用能力集解析库,0-不使用,1-使用,默认不使用
                ("byVoiceComMode", BYTE), # 对讲模式，0-使用对讲库（默认），1-使用windows api模式
                ("byLoginWithSimXml", BYTE), # 登录时使用模拟能力,0-不使用,1-使用,默认不使用
                ("byCompatibleType", BYTE),
                ("byRes", BYTE * 380), # 保留
                ("byProtectKey", BYTE * 128) # 默认设置为0
                ]
LPNET_DVR_SDKLOCAL_CFG = POINTER(NET_DVR_SDKLOCAL_CFG)

class NET_DVR_JPEGPARA(Structure):
    _fields_ = [
                ("wPicSize", WORD), # 注意：当图像压缩分辨率为VGA时，支持0 = CIF, 1 = QCIF, 2 = D1抓图，
                            # 当分辨率为3 = UXGA(1600x1200), 4 = SVGA(800x600), 5 = HD720p(1280x720), 6 = VGA, 7 = XVGA, 8 = HD900p
                            # 仅支持当前分辨率的抓图
                            #
                            # 可以通过能力集获取
                            # 0 - CIF， 1 - QCIF， 2 - D1， 3 - UXGA(1600x1200), 4 - SVGA(800x600), 5 - HD720p(1280x720)，
                            # 6 - VGA， 7 - XVGA， 8 - HD900p，9 - HD1080，10 - 2560 * 1920，
                            # 11 - 1600 * 304，12 - 2048 * 1536，13 - 2448 * 2048, 14 - 2448 * 1200， 15 - 2448 * 800，
                            # 16 - XGA(1024 * 768), 17 - SXGA(1280 * 1024), 18 - WD1(960 * 576 / 960 * 480), 19 - 1080
                            # i, 20 - 576 * 576，
                            # 21 - 1536 * 1536, 22 - 1920 * 1920, 23 - 320 * 240, 24 - 720 * 720, 25 - 1024 * 768,
                            # 26 - 1280 * 1280, 27 - 1600 * 600, 28 - 2048 * 768, 29 - 160 * 120, 55 - 3072 * 2048,
                            # 64 - 3840 * 2160, 70 - 2560 * 1440, 75 - 336 * 256,
                            # 78 - 384 * 256, 79 - 384 * 216, 80 - 320 * 256, 82 - 320 * 192, 83 - 512 * 384,
                            # 127 - 480 * 272, 128 - 512 * 272, 161 - 288 * 320, 162 - 144 * 176, 163 - 480 * 640,
                            # 164 - 240 * 320, 165 - 120 * 160, 166 - 576 * 720, 167 - 720 * 1280, 168 - 576 * 960,
                            # 180 - 180 * 240, 181 - 360 * 480, 182 - 540 * 720, 183 - 720 * 960, 184 - 960 * 1280,
                            # 185 - 1080 * 1440, 215 - 1080 * 720(占位，未测试), 216 - 360
                            # x640(占位，未测试), 245 - 576 * 704(占位，未测试)
                            # 500 - 384 * 288,
                            # 0xff - Auto(使用当前码流分辨率)
                ("wPicQuality",WORD) # 图片质量系数 0-最好 1-较好 2-一般
                ]

LPNET_DVR_JPEGPARA = POINTER(NET_DVR_JPEGPARA)


########################################################################################################################
########################################################################################################################
###########     ***                          *                                                     *         ###########
###########      *                           *                                                     *         ###########
###########      *      *** ***     ***      *        ****      *** ***      ****      *****     ******      ###########
###########      *     *   *   *    *   *    *       *    *    *   *   *    *    *    *     *      *         ###########
###########      *     *   *   *    *   *    *       ******    *   *   *    ******    *     *      *         ###########
###########      *     *   *   *    ****     *  *    *         *   *   *    *         *     *      *  *      ###########
###########     ***    *   *   *    *        ***      ****     *       *     ****     *     *      ***       ###########
###########                         *                                                                        ###########
###########                         *                                                                        ###########
########################################################################################################################
########################################################################################################################
_HCCore = _zlib1 = _YUVProcess = _SuperRender = _ssleay32 = _PlayCtrl = \
    _NPQos = _libmmd = _libeay32 = _HXVA = _hpr = _hlog = _GdiPlus = _AudioRender = None

_HCNetSDK = None

def create():
    global _HCCore, _zlib1, _YUVProcess, _SuperRender, _ssleay32, _PlayCtrl, \
        _NPQos, _libmmd, _libeay32, _HXVA, _hpr, _hlog, _GdiPlus, _AudioRender
    global _HCNetSDK

    # _AudioRender = cdll.LoadLibrary(os.path.join(os.getcwd(), 'AudioRender.dll'))
    # _GdiPlus = cdll.LoadLibrary(os.path.join(os.getcwd(), 'GdiPlus.dll'))
    # _hlog = cdll.LoadLibrary(os.path.join(os.getcwd(), 'hlog.dll'))
    # _hpr = cdll.LoadLibrary(os.path.join(os.getcwd(), 'hpr.dll'))
    # _HXVA = cdll.LoadLibrary(os.path.join(os.getcwd(), 'HXVA.dll'))
    # _libeay32 = cdll.LoadLibrary(os.path.join(os.getcwd(), 'libeay32.dll'))
    # _libmmd = cdll.LoadLibrary(os.path.join(os.getcwd(), 'libmmd.dll'))
    # _NPQos = cdll.LoadLibrary(os.path.join(os.getcwd(), 'NPQos.dll'))
    # _PlayCtrl = cdll.LoadLibrary(os.path.join(os.getcwd(), 'PlayCtrl.dll'))
    # _ssleay32 = cdll.LoadLibrary(os.path.join(os.getcwd(), 'ssleay32.dll'))
    # _SuperRender = cdll.LoadLibrary(os.path.join(os.getcwd(), 'SuperRender.dll'))
    # _YUVProcess = cdll.LoadLibrary(os.path.join(os.getcwd(), 'YUVProcess.dll'))
    # _zlib1 = cdll.LoadLibrary(os.path.join(os.getcwd(), 'zlib1.dll'))
    _HCCore = WinDLL(os.path.join(__curdir__, 'HCCore.dll'))
    _HCNetSDK = WinDLL(os.path.join(__curdir__, 'HCNetSDK.dll'))

def destory():
    global _HCCore, _zlib1, _YUVProcess, _SuperRender, _ssleay32, _PlayCtrl, \
        _NPQos, _libmmd, _libeay32, _HXVA, _hpr, _hlog, _GdiPlus, _AudioRender
    global _HCNetSDK

    win32api.FreeLibrary(_HCNetSDK._handle)
    win32api.FreeLibrary(_HCCore._handle)


####################################################
### API function declarations                    ###
####################################################
class pyHik:
    """
        API class implementation
    """
    global _HCNetSDK

    def __init__(self):
        # status defination
        self.__inRealPlay = False

        # pre execution
        create()


    def __del__(self):
        destory()

    @property
    def inRealPlay(self):
        return self.__inRealPlay

    ####################################################
    ### Get Last Error                               ###
    ####################################################
    def __get_last_error(
        self):
        """
            Get last error.

        Exception:
            HikError.
        """
        error = NET_DVR_UNKNOW
        try:
            C_GET_LAST_ERROR = _HCNetSDK.NET_DVR_GetLastError
            C_GET_LAST_ERROR.restype = DWORD
            error = C_GET_LAST_ERROR()
        except Exception:
            pass
        finally:
            return error

    ####################################################
    ### SDK initialization and termination functions ###
    ####################################################
    def init(
        self):
        """
            Initialize the SDK. Call this function before using any of the other APIs

        Exception:
            HikError.
        """
        try:
            C_INITIALIZE = _HCNetSDK.NET_DVR_Init
            C_INITIALIZE.restype = BOOL
            ret = C_INITIALIZE()
        except Exception as err:
            raise HikError("init", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("init", self.__get_last_error(), "SDK initialization failed")

    def cleanup(
        self):
        """
            Release the SDK. If init() was called, invoke this function at program exit

        Exception:
            HikError.
        """
        try:
            C_CLEANUP = _HCNetSDK.NET_DVR_Cleanup
            C_CLEANUP.restype = BOOL
            ret = C_CLEANUP()
        except Exception as err:
            raise HikError("cleanup", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("cleanup", self.__get_last_error(), "SDK cleanup failed")

    def set_connect_time(
        self,
        dwWaitTime,
        dwTryTimes
        ):
        """
            Set network connection timeout and connection attempt times. Default timeout is 3s.

        Parameters:
            dwWaitTime : timeout, unit:ms, range:[300,75000]
            dwTryTimes : Number of attempts for connection

        Exception:
            HikError.
        """
        try:
            C_SET_CONNECT_TIME = _HCNetSDK.NET_DVR_SetConnectTime
            C_SET_CONNECT_TIME.argtypes = [DWORD, DWORD]
            C_SET_CONNECT_TIME.restype = BOOL
            ret = C_SET_CONNECT_TIME(DWORD(dwWaitTime), DWORD(dwTryTimes))
        except Exception as err:
            raise HikError("set_connect_time", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("set_connect_time", self.__get_last_error(), "Executing failed")

    def set_reconnect(
        self,
        interval,
        enableReconnect
        ):
        """
            Set reconnecting time interval. Default reconnect interval is 5 seconds.

        Parameters:
            interval        : Reconnecting interval, unit:ms, default:30s
            enableReconnect : Enable or disable reconnect function, 0-disable, 1-enable(default)

        Exception:
            HikError.
        """
        try:
            C_SET_CONNECT_TIME = _HCNetSDK.NET_DVR_SetReconnect
            C_SET_CONNECT_TIME.argtypes = [DWORD, DWORD]
            C_SET_CONNECT_TIME.restype = BOOL
            ret = C_SET_CONNECT_TIME(DWORD(interval), DWORD(enableReconnect))
        except Exception as err:
            raise HikError("set_reconnect", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("set_reconnect", self.__get_last_error(), "Executing failed")


    ####################################################
    ### Device login functions                       ###
    ####################################################
    def login(
        self,
        dIP,
        dPort,
        username,
        password
        ):
        """
            Login to the device

        Parameters:
            dIP      : IP address of the device
            dPort    : Port number of the device
            username : Username for login
            password : Password

        Return
            userID : Unique user ID and device info, else -1 on failure
            dInfo : Device info

        Exception:
            HikError.
        """
        try:
            C_LOGIN = _HCNetSDK.NET_DVR_Login_V30
            C_LOGIN.argtypes = [CHARP, WORD, CHARP, CHARP, LPNET_DVR_DEVICEINFO_V30]
            C_LOGIN.restype = LONG

            device_info = NET_DVR_DEVICEINFO_V30()
            dIP = bytes(dIP, encoding='utf8')
            username = bytes(username, encoding='utf8')
            password = bytes(password, encoding='utf8')
            user_id = C_LOGIN(CHARP(dIP), WORD(dPort), CHARP(username), CHARP(password), byref(device_info))
        except Exception as err:
            raise HikError("login", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if user_id == -1:
            raise HikError("login", self.__get_last_error(), "Executing failed")

        self.__inRealPlay = False
        return user_id, self.__struct2dict(device_info)

    def logout(
        self,
        userId):
        """
            Logout from the device

        Parameters:
            userId : User ID, returned from login()

        Exception:
            HikError.
        """
        try:
            C_LOGOUT = _HCNetSDK.NET_DVR_Logout
            C_LOGOUT.argtypes = [LONG]
            C_LOGOUT.restype = BOOL
            ret = C_LOGOUT(LONG(userId))
        except Exception as err:
            raise HikError("logout", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("logout", self.__get_last_error(), "Executing failed")

        self.__inRealPlay = False


    ####################################################
    ### Device configure                             ###
    ####################################################
    def get_resource_config(
        self,
        userId):
        """
            Get config

        Parameters:
            userId : User ID, returned from login()

        Exception:
            HikError.
        """
        try:
            C_GET_DVR_CONFIG = _HCNetSDK.NET_DVR_GetDVRConfig
            C_GET_DVR_CONFIG.argtypes = [LONG, DWORD, LONG, LPNET_DVR_IPPARACFG_V40, DWORD, LPDWORD]
            C_GET_DVR_CONFIG.restype = BOOL

            lpOutBuffer = NET_DVR_IPPARACFG_V40()
            dwReturned = pointer(DWORD())
            ret = C_GET_DVR_CONFIG(LONG(userId), DWORD(NET_DVR_GET_IPPARACFG_V40), LONG(0), lpOutBuffer, DWORD(lpOutBuffer.__sizeof__()), dwReturned)
        except Exception as err:
            raise HikError("get_resource_config", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("get_resource_config", self.__get_last_error(), "Executing failed")

        return self.__struct2dict(lpOutBuffer)

    def get_decoder_config(
        self,
        userId,
        channel):
        """
            Get config

        Parameters:
            userId  : User ID, returned from login()
            channel : Analog channel number

        Exception:
            HikError.
        """
        try:
            C_GET_DVR_CONFIG = _HCNetSDK.NET_DVR_GetDVRConfig
            C_GET_DVR_CONFIG.argtypes = [LONG, DWORD, LONG, LPNET_DVR_DECODERCFG_V40, DWORD, LPDWORD]
            C_GET_DVR_CONFIG.restype = BOOL

            lpOutBuffer = NET_DVR_DECODERCFG_V40()
            dwReturned = pointer(DWORD())
            ret = C_GET_DVR_CONFIG(LONG(userId), DWORD(NET_DVR_GET_DECODERCFG_V40), LONG(channel), lpOutBuffer, DWORD(lpOutBuffer.__sizeof__()), dwReturned)
        except Exception as err:
            raise HikError("get_decoder_config", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("get_decoder_config", self.__get_last_error(), "Executing failed")

        return self.__struct2dict(lpOutBuffer)


    ####################################################
    ### Live view functions                          ###
    ####################################################
    def start_real_play(
        self,
        userId,
        channel,
        playWND,
        realDataCbk,
        userData,
        blocked
        ):
        """
            Starting live view

        Parameters:
            userId       : User ID, returned from login()
            channel      : Analog channel number
            playWND      : Live view windows id
            realDataCbk  : Real-time stream data callback function
            userData     : User data, Set None.
            blocked      : Whether to set stream data requesting process blocked or not: 0-no, 1-yes

        Return
            lRealHandle : live view handle for use in stopRealPlay()

        Exception:
            HikError.
        """
        try:
            C_REALPLAY = _HCNetSDK.NET_DVR_RealPlay_V30
            if realDataCbk is not None:
                C_REALPLAY.argtypes = [LONG, LPNET_DVR_CLIENTINFO, RD_CBFUNC_TYPE, VOIDP, BOOL]
                realDataCbk = RD_CBFUNC_TYPE(realDataCbk)
            else:
                C_REALPLAY.argtypes = [LONG, LPNET_DVR_CLIENTINFO, VOIDP, VOIDP, BOOL]
            C_REALPLAY.restype = LONG

            ipClientInfo = NET_DVR_CLIENTINFO()
            ipClientInfo.lChannel = channel
            ipClientInfo.dwLinkMode = 0
            ipClientInfo.hPlayWnd = playWND
            ipClientInfo.sMultiCastIP = None

            lRealHandle = C_REALPLAY(LONG(userId), byref(ipClientInfo), realDataCbk, userData, BOOL(blocked))
        except Exception as err:
            raise HikError("start_real_play", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if lRealHandle == -1:
            raise HikError("start_real_play", self.__get_last_error(), "Executing failed")

        self.__inRealPlay = True
        return lRealHandle

    def stop_real_play(
        self,
        realHandle):
        """
            Stopping live view

        Parameters:
            realHandle : live view handle, return value from startRealPlay()

        Exception:
            HikError.
        """
        try:
            C_STOP_REALPLAY = _HCNetSDK.NET_DVR_StopRealPlay
            C_STOP_REALPLAY.argtypes = [LONG]
            C_STOP_REALPLAY.restype = BOOL
            ret = C_STOP_REALPLAY(LONG(realHandle))
        except Exception as err:
            raise HikError("stop_real_play", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("stop_real_play", self.__get_last_error(), "Executing failed")
        self.__inRealPlay = False

    def get_real_player_index(
        self,
        realHandle):
        """
            Get player handle to use with other player SDK functions

        Parameters:
            realHandle : live view handle, return value from startRealPlay()

        Return
            nPort : return value for PlayM4 SDK

        Exception:
            HikError.
        """
        try:
            C_GET_REALPLAYER_INDEX = _HCNetSDK.NET_DVR_GetRealPlayerIndex
            C_GET_REALPLAYER_INDEX.argtypes = [LONG]
            C_GET_REALPLAYER_INDEX.restype = INT
            nPort = C_GET_REALPLAYER_INDEX(LONG(realHandle))
        except Exception as err:
            raise HikError("get_real_player_index", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if nPort == -1:
            raise HikError("get_real_player_index", self.__get_last_error(), "Executing failed")

        return nPort

    def set_real_data_callBack(
        self,
        realHandle,
        realDataCbk,
        dwUser):
        """
            Get player handle to use with other player SDK functions

        Parameters:
            realHandle : live view handle, return value from startRealPlay()
            realDataCbk : Callback function
            dwUser : User data, Set 0.

        Exception:
            HikError.
        """
        try:
            C_GET_REALPLAYER_INDEX = _HCNetSDK.NET_DVR_SetRealDataCallBack
            C_GET_REALPLAYER_INDEX.argtypes = [LONG, RD_CBFUNC_TYPE, DWORD]
            C_GET_REALPLAYER_INDEX.restype = BOOL
            ret = C_GET_REALPLAYER_INDEX(LONG(realHandle), RD_CBFUNC_TYPE(realDataCbk), DWORD(dwUser))
        except Exception as err:
            raise HikError("set_real_data_callBack", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if ret == -1:
            raise HikError("set_real_data_callBack", self.__get_last_error(), "Executing failed")

    ####################################################
    ### Video Record functions                       ###
    ####################################################
    def start_record(
        self,
        realHandle,
        fileName):
        """
            Start record frame to file.

        Parameters:
            realHandle : live view handle, return value from startRealPlay()
            fileName   : file name of the frame recording.

        Exception:
            HikError.
        """
        try:
            C_SAVE_REAL_DATA = _HCNetSDK.NET_DVR_SaveRealData
            C_SAVE_REAL_DATA.argtypes = [LONG, CHARP]
            C_SAVE_REAL_DATA.restype = BOOL
            fileName = bytes(fileName, encoding='utf8')
            ret = C_SAVE_REAL_DATA(LONG(realHandle), CHARP(fileName))
        except Exception as err:
            raise HikError("start_record", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("start_record", self.__get_last_error(), "Executing failed")

    def stop_record(
        self,
        realHandle):
        """
            Stop record frame to file.

        Parameters:
            realHandle : live view handle, return value from startRealPlay()

        Exception:
            HikError.
        """
        try:
            C_STOP_SAVE_REAL_DATA = _HCNetSDK.NET_DVR_StopSaveRealData
            C_STOP_SAVE_REAL_DATA.argtypes = [LONG]
            C_STOP_SAVE_REAL_DATA.restype = BOOL
            ret = C_STOP_SAVE_REAL_DATA(LONG(realHandle))
        except Exception as err:
            raise HikError("stop_record", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("stop_record", self.__get_last_error(), "Executing failed")

    ####################################################
    ### Picture capture                              ###
    ####################################################
    def capture_picture(
        self,
        realHandle,
        fileName):
        """
            capture picture to file.

        Parameters:
            realHandle : live view handle, return value from startRealPlay()
            fileName   : file name of the picture capture.

        Exception:
            HikError.
        """
        try:
            C_CAPTURE_PICTURE = _HCNetSDK.NET_DVR_CapturePicture
            C_CAPTURE_PICTURE.argtypes = [LONG, CHARP]
            C_CAPTURE_PICTURE.restype = BOOL
            fileName = bytes(fileName, encoding='utf8')
            ret = C_CAPTURE_PICTURE(LONG(realHandle), CHARP(fileName))
        except Exception as err:
            raise HikError("capture_picture", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("capture_picture", self.__get_last_error(), "Executing failed")

    def capture_jpeg_picture(
        self,
        userId,
        channel,
        size,
        quality,
        fileName):
        """
            capture jpeg picture to file.

        Parameters:
            realHandle : User Id, return value from login()
            channel    : Channel index for capturing the picture
            size       : Target JPEG picture size
            quality    : Target JPEG picture quality
            fileName   : file name of the picture capture.

        Exception:
            HikError.
        """
        try:
            C_CAPTURE_JPEG_PICTURE = _HCNetSDK.NET_DVR_CaptureJPEGPicture
            C_CAPTURE_JPEG_PICTURE.argtypes = [LONG, LONG, LPNET_DVR_JPEGPARA, CHARP]
            C_CAPTURE_JPEG_PICTURE.restype = BOOL
            fileName = bytes(fileName, encoding='utf8')
            jpegParam = NET_DVR_JPEGPARA()
            jpegParam.wPicSize = size
            jpegParam.wPicQuality = quality
            ret = C_CAPTURE_JPEG_PICTURE(LONG(userId), LONG(channel), byref(jpegParam), CHARP(fileName))
        except Exception as err:
            raise HikError("capture_jpeg_picture", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("capture_jpeg_picture", self.__get_last_error(), "Executing failed")

    ####################################################
    ### Control                                      ###
    ####################################################
    def PTZ_preset(
        self,
        realHandle,
        dwPTZPresetCmd,
        dwPresetIndex):
        """
            PTZ preset controller.

        Parameters:
            realHandle      : live view handle, return value from startRealPlay()
            dwPTZPresetCmd  : Preset command
            dwPresetIndex   : Preset index

        Exception:
            HikError.
        """
        try:
            C_PTZ_PRESET = _HCNetSDK.NET_DVR_PTZPreset
            C_PTZ_PRESET.argtypes = [LONG, DWORD, DWORD]
            C_PTZ_PRESET.restype = BOOL
            ret = C_PTZ_PRESET(LONG(realHandle), DWORD(dwPTZPresetCmd), DWORD(dwPresetIndex))
        except Exception as err:
            raise HikError("PTZ_preset", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("PTZ_preset", self.__get_last_error(), "Executing failed")

    def PTZ_preset_other(
        self,
        userId,
        channel,
        dwPTZPresetCmd,
        dwPresetIndex):
        """
            PTZ preset controller, this func need decoder supported.

        Parameters:
            userId          : User ID, returned from login()
            channel         : Analog channel number
            dwPTZPresetCmd  : Preset command
            dwPresetIndex   : Preset index

        Exception:
            HikError.
        """
        try:
            C_PTZ_PRESET_OTHER = _HCNetSDK.NET_DVR_PTZPreset_Other
            C_PTZ_PRESET_OTHER.argtypes = [LONG, LONG, DWORD, DWORD]
            C_PTZ_PRESET_OTHER.restype = BOOL
            ret = C_PTZ_PRESET_OTHER(LONG(userId), LONG(channel), DWORD(dwPTZPresetCmd), DWORD(dwPresetIndex))
        except Exception as err:
            raise HikError("PTZ_preset_other", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("PTZ_preset_other", self.__get_last_error(), "Executing failed")

    def PTZ_cruise(
        self,
        realHandle,
        dwPTZCruiseCmd,
        byCruiseRoute,
        byCruisePoint,
        wInput):
        """
            PTZ cruise controller.

        Parameters:
            realHandle      : live view handle, return value from startRealPlay()
            dwPTZCruiseCmd  : Cruise command
            byCruiseRoute   : Cruise route, start on 1, 32 max supported
            byCruisePoint   : Cruise point, start on 1, 32 max supported
            wInput          : input value base on different Cruise command, e.q. preset, time, speed

        Exception:
            HikError.
        """
        try:
            C_PTZ_PRESET = _HCNetSDK.NET_DVR_PTZCruise
            C_PTZ_PRESET.argtypes = [LONG, DWORD, BYTE, BYTE, DWORD]
            C_PTZ_PRESET.restype = BOOL
            ret = C_PTZ_PRESET(LONG(realHandle), DWORD(dwPTZCruiseCmd), BYTE(byCruiseRoute), BYTE(byCruisePoint), DWORD(wInput))
        except Exception as err:
            raise HikError("PTZ_cruise", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("PTZ_cruise", self.__get_last_error(), "Executing failed")

    def PTZ_cruise_other(
        self,
        userId,
        channel,
        dwPTZCruiseCmd,
        byCruiseRoute,
        byCruisePoint,
        wInput):
        """
            PTZ preset controller, this func need decoder supported.

        Parameters:
            userId          : User ID, returned from login()
            channel         : Analog channel number
            dwPTZCruiseCmd  : Cruise command
            byCruiseRoute   : Cruise route, start on 1, 32 max supported
            byCruisePoint   : Cruise point, start on 1, 32 max supported
            wInput          : input value base on different Cruise command, e.q. preset, time, speed

        Exception:
            HikError.
        """
        try:
            C_PTZ_CRUISE_OTHER = _HCNetSDK.NET_DVR_PTZCruise_Other
            C_PTZ_CRUISE_OTHER.argtypes = [LONG, LONG, DWORD, BYTE, BYTE, WORD]
            C_PTZ_CRUISE_OTHER.restype = BOOL
            ret = C_PTZ_CRUISE_OTHER(LONG(userId), LONG(channel), DWORD(dwPTZCruiseCmd), BYTE(byCruiseRoute), BYTE(byCruisePoint), WORD(wInput))
        except Exception as err:
            raise HikError("PTZ_cruise_other", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("PTZ_cruise_other", self.__get_last_error(), "Executing failed")

    def PTZ_track(
        self,
        realHandle,
        dwPTZTrackCmd):
        """
            PTZ track controller.

        Parameters:
            realHandle      : live view handle, return value from startRealPlay()
            dwPTZTrackCmd   : Track command

        Exception:
            HikError.
        """
        try:
            C_PTZ_TRACK = _HCNetSDK.NET_DVR_PTZTrack
            C_PTZ_TRACK.argtypes = [LONG, DWORD]
            C_PTZ_TRACK.restype = BOOL
            ret = C_PTZ_TRACK(LONG(realHandle), DWORD(dwPTZTrackCmd))
        except Exception as err:
            raise HikError("PTZ_track", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("PTZ_track", self.__get_last_error(), "Executing failed")

    def PTZ_track_other(
        self,
        userId,
        channel,
        dwPTZTrackCmd):
        """
            PTZ preset controller, this func need decoder supported.

        Parameters:
            userId          : User ID, returned from login()
            channel         : Analog channel number
            dwPTZTrackCmd   : Track command

        Exception:
            HikError.
        """
        try:
            C_PTZ_TRACK_OTHER = _HCNetSDK.NET_DVR_PTZTrack_Other
            C_PTZ_TRACK_OTHER.argtypes = [LONG, LONG, DWORD]
            C_PTZ_TRACK_OTHER.restype = BOOL
            ret = C_PTZ_TRACK_OTHER(LONG(userId), LONG(channel), DWORD(dwPTZTrackCmd))
        except Exception as err:
            raise HikError("PTZ_track_other", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("PTZ_track_other", self.__get_last_error(), "Executing failed")

    def PTZ_control(
        self,
        realHandle,
        dwPTZCommand,
        dwStop):
        """
            PTZ track controller.

        Parameters:
            realHandle      : live view handle, return value from startRealPlay()
            dwPTZTrackCmd   : Control command
            dwStop          : Start - 0, Stop - 1

        Exception:
            HikError.
        """
        try:
            C_PTZ_CONTROL = _HCNetSDK.NET_DVR_PTZControl
            C_PTZ_CONTROL.argtypes = [LONG, DWORD, DWORD]
            C_PTZ_CONTROL.restype = BOOL
            ret = C_PTZ_CONTROL(LONG(realHandle), DWORD(dwPTZCommand), DWORD(dwStop))
        except Exception as err:
            raise HikError("PTZ_control", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("PTZ_control", self.__get_last_error(), "Executing failed")

    def PTZ_control_other(
        self,
        userId,
        channel,
        dwPTZCommand,
        dwStop):
        """
            PTZ preset controller, this func need decoder supported.

        Parameters:
            userId          : User ID, returned from login()
            channel         : Analog channel number
            dwPTZTrackCmd   : Control command
            dwStop          : Start - 0, Stop - 1

        Exception:
            HikError.
        """
        try:
            C_PTZ_CONTROL_OTHER = _HCNetSDK.NET_DVR_PTZControl_Other
            C_PTZ_CONTROL_OTHER.argtypes = [LONG, LONG, DWORD, DWORD]
            C_PTZ_CONTROL_OTHER.restype = BOOL
            ret = C_PTZ_CONTROL_OTHER(LONG(userId), LONG(channel), DWORD(dwPTZCommand), DWORD(dwStop))
        except Exception as err:
            raise HikError("PTZ_control_other", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("PTZ_control_other", self.__get_last_error(), "Executing failed")

    def PTZ_control_with_speed(
        self,
        realHandle,
        dwPTZCommand,
        dwStop,
        dwSpeed):
        """
            PTZ track controller.

        Parameters:
            realHandle      : live view handle, return value from startRealPlay()
            dwPTZTrackCmd   : Control command
            dwStop          : Start - 0, Stop - 1
            dwSpeed         : Speed, range 1-7

        Exception:
            HikError.
        """
        try:
            C_PTZ_CONTROL_WITH_SPEED = _HCNetSDK.NET_DVR_PTZControlWithSpeed
            C_PTZ_CONTROL_WITH_SPEED.argtypes = [LONG, DWORD, DWORD, DWORD]
            C_PTZ_CONTROL_WITH_SPEED.restype = BOOL
            ret = C_PTZ_CONTROL_WITH_SPEED(LONG(realHandle), DWORD(dwPTZCommand), DWORD(dwStop), DWORD(dwSpeed))
        except Exception as err:
            raise HikError("PTZ_control_with_speed", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("PTZ_control_with_speed", self.__get_last_error(), "Executing failed")

    def PTZ_control_with_speed_other(
        self,
        userId,
        channel,
        dwPTZCommand,
        dwStop,
        dwSpeed):
        """
            PTZ preset controller, this func need decoder supported.

        Parameters:
            userId          : User ID, returned from login()
            channel         : Analog channel number
            dwPTZTrackCmd   : Control command
            dwStop          : Start - 0, Stop - 1
            dwSpeed         : Speed, range 1-7

        Exception:
            HikError.
        """
        try:
            C_PTZ_CONTROL_WITH_SPEED_OTHER = _HCNetSDK.NET_DVR_PTZControlWithSpeed_Other
            C_PTZ_CONTROL_WITH_SPEED_OTHER.argtypes = [LONG, LONG, DWORD, DWORD, DWORD]
            C_PTZ_CONTROL_WITH_SPEED_OTHER.restype = BOOL
            ret = C_PTZ_CONTROL_WITH_SPEED_OTHER(LONG(userId), LONG(channel), DWORD(dwPTZCommand), DWORD(dwStop), DWORD(dwSpeed))
        except Exception as err:
            raise HikError("PTZ_control_with_speed_other", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("PTZ_control_with_speed_other", self.__get_last_error(), "Executing failed")

    def __struct2dict(
        self,
        struct):
        """
        Convert a structure to a dict
        """
        try:
            _sf = struct._fields_
            _dict = {}
            for (_fn, _ft) in _sf:
                _v = struct.__getattribute__(_fn)
                if (type(_v)) != int:
                    _v = str(cast(_v, CHARP).value, "utf-8")
                _dict[_fn] = _v
            return _dict
        except Exception as err:
            return {}
