import win32api
from ctypes import WinDLL

from pyHik.libs.windows.argsdef import *

__curdir__ = os.path.abspath(os.path.dirname(__file__))

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
        # pre execution
        create()

    def __del__(self):
        destory()

    ####################################################
    ### Get Last Error                               ###
    ####################################################
    def __NET_DVR_GetLastError(
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
    ### SDK初始化                                    ###
    ####################################################
    def NET_DVR_Init(self):
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
            raise HikError("NET_DVR_Init", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_Init", ret, "SDK initialization failed")

    def NET_DVR_Cleanup(self):
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
            raise HikError("NET_DVR_Cleanup", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_Cleanup", ret, "SDK cleanup failed")

    def NET_DVR_SetConnectTime(
            self,
            dwWaitTime,
            dwTryTimes):
        """
            设置网络连接超时时间和连接尝试次数

        Parameters:
            dwWaitTime : 超时时间，单位毫秒，取值范围[300,75000]，实际最大超时时间因系统的connect超时时间而不同
            dwTryTimes : 连接尝试次数（保留）

        Exception:
            HikError.
        """
        try:
            C_SET_CONNECT_TIME = _HCNetSDK.NET_DVR_SetConnectTime
            C_SET_CONNECT_TIME.argtypes = [DWORD, DWORD]
            C_SET_CONNECT_TIME.restype = BOOL
            ret = C_SET_CONNECT_TIME(DWORD(dwWaitTime), DWORD(dwTryTimes))
        except Exception as err:
            raise HikError("NET_DVR_SetConnectTime", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_SetConnectTime", ret, "Executing failed")

    def NET_DVR_SetReconnect(
            self,
            dwInterval,
            bEnableRecon):
        """
            设置重连功能

        Parameters:
            dwInterval   : 重连间隔，单位:毫秒
            bEnableRecon : 是否重连，0-不重连，1-重连，参数默认值为1

        Exception:
            HikError.
        """
        try:
            C_SET_CONNECT_TIME = _HCNetSDK.NET_DVR_SetReconnect
            C_SET_CONNECT_TIME.argtypes = [DWORD, DWORD]
            C_SET_CONNECT_TIME.restype = BOOL
            ret = C_SET_CONNECT_TIME(DWORD(dwInterval), DWORD(bEnableRecon))
        except Exception as err:
            raise HikError("NET_DVR_SetReconnect", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_SetReconnect", ret, "Executing failed")

    ####################################################
    ### 用户登录                                     ###
    ####################################################
    def NET_DVR_Login_V30(
            self,
            sDVRIP,
            wDVRPort,
            sUserName,
            sPassword,
            lpDeviceInfo):
        """
            用户注册设备

        Parameters:
            sDVRIP          : 设备IP地址或是静态域名，字符数不大于128个
            wDVRPort        : 设备端口号
            sUserName       : 登录的用户名
            sPassword       : 用户密码
            lpDeviceInfo    : 设备信息

        Return
            lUserID : -1表示失败，其他值表示返回的用户ID值。该用户ID具有唯一性，后续对设备的操作都需要通过此ID实现

        Exception:
            HikError.
        """
        try:
            C_LOGIN = _HCNetSDK.NET_DVR_Login_V30
            C_LOGIN.argtypes = [CHARP, WORD, CHARP, CHARP, LPNET_DVR_DEVICEINFO_V30]
            C_LOGIN.restype = LONG

            dIP = bytes(sDVRIP, encoding='utf8')
            username = bytes(sUserName, encoding='utf8')
            password = bytes(sPassword, encoding='utf8')
            lUserID = C_LOGIN(CHARP(dIP), WORD(wDVRPort), CHARP(username), CHARP(password), byref(lpDeviceInfo))
        except Exception as err:
            raise HikError("NET_DVR_Login", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if lUserID == -1:
            raise HikError("NET_DVR_Login", self.__NET_DVR_GetLastError(), "Executing failed")

        return lUserID

    def NET_DVR_Logout(
            self,
            lUserID):
        """
            用户注销

        Parameters:
            lUserID : 用户ID号，NET_DVR_Login等登录接口的返回值

        Exception:
            HikError.
        """
        try:
            C_LOGOUT = _HCNetSDK.NET_DVR_Logout
            C_LOGOUT.argtypes = [LONG]
            C_LOGOUT.restype = BOOL
            ret = C_LOGOUT(LONG(lUserID))
        except Exception as err:
            raise HikError("NET_DVR_Logout", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_Logout", self.__NET_DVR_GetLastError(), "Executing failed")

    ####################################################
    ### 参数配置                                     ###
    ####################################################
    def NET_DVR_GetDVRConfig(
            self,
            lUserID,
            dwCommand,
            lChannel,
            lpOutBuffer):

        """
            获取设备的配置信息

        Parameters:
            lUserID : NET_DVR_Login_V40等登录接口的返回值
            dwCommand : 设备配置命令
            lChannel : 通道号，不同的命令对应不同的取值，如果该参数无效则置为0xFFFFFFFF即可
            lpOutBuffer : 接收数据的缓冲指针

        Exception:
            HikError.
        """
        try:
            C_GET_DVR_CONFIG = _HCNetSDK.NET_DVR_GetDVRConfig
            C_GET_DVR_CONFIG.argtypes = [LONG, DWORD, LONG, POINTER(type(lpOutBuffer)), DWORD, LPDWORD]
            C_GET_DVR_CONFIG.restype = BOOL

            dwReturned = pointer(DWORD())
            ret = C_GET_DVR_CONFIG(LONG(lUserID), DWORD(dwCommand), LONG(lChannel), lpOutBuffer,
                                   DWORD(sizeof(lpOutBuffer)), dwReturned)
        except Exception as err:
            raise HikError("NET_DVR_GetDVRConfig", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_GetDVRConfig", self.__NET_DVR_GetLastError(), "Executing failed")

    def NET_DVR_GetDeviceConfig(
            self,
            lUserID,
            dwCommand,
            dwCount,
            lpInBuffer,
            lpStatusList,
            lpOutBuffer,
            dwOutBufferSize):

        """
            批量获取设备配置信息（带发送数据）。

        Parameters:
            lUserID         : NET_DVR_Login_V40等登录接口的返回值
            dwCommand       : 设备配置命令，参见配置命令
            dwCount         : 一次要获取的配置个数，0和1都表示1个监控点信息，2表示2个监控点信息，以此递增，最大64个
            lpInBuffer      : 配置条件缓冲区指针
            lpStatusList    : 错误信息列表，和要查询的监控点一一对应，例如lpStatusList[2]就对应lpInBuffer[2]，由用户分配内存，每个错误信息为4个字节(1个32位无符号整数值)，参数值：0或者1表示成功，其他值为失败对应的错误号
            lpOutBuffer     : 设备返回的参数内容，和要查询的监控点一一对应。如果某个监控点对应的lpStatusList信息为大于1的值，对应lpOutBuffer的内容就是无效的
            dwOutBufferSize : dwCount个返回结果的总大小

        Exception:
            HikError.
        """
        try:
            C_GET_DEVICE_CONFIG = _HCNetSDK.NET_DVR_GetDeviceConfig
            C_GET_DEVICE_CONFIG.argtypes = [LONG, DWORD, DWORD, VOIDP, DWORD, VOIDP, VOIDP, DWORD]
            C_GET_DEVICE_CONFIG.restype = BOOL

            ret = C_GET_DEVICE_CONFIG(LONG(lUserID), DWORD(dwCommand), DWORD(dwCount), byref(lpInBuffer),
                                      DWORD(sizeof(lpInBuffer)), byref(lpStatusList),
                                      byref(lpOutBuffer), DWORD(dwOutBufferSize))
        except Exception as err:
            raise HikError("NET_DVR_GetDeviceConfig", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_GetDeviceConfig", self.__NET_DVR_GetLastError(), "Executing failed")


    ####################################################
    ### 设备能力集                                   ###
    ####################################################
    def NET_DVR_GetDeviceAbility(
            self,
            lUserID,
            dwAbilityType,
            pInBuf,
            dwInLength,
            pOutBuf,
            dwOutLength):

        """
            批量获取设备配置信息（带发送数据）。

        Parameters:
            lUserID         : NET_DVR_Login_V40等登录接口的返回值
            dwAbilityType   : 能力类型
            pInBuf          : 输入缓冲区指针
            dwInLength      : 输入缓冲区的长度
            pOutBuf         : 输出缓冲区指针
            dwOutLength     : 接收数据的缓冲区的长度

        Exception:
            HikError.
        """
        try:
            C_GET_DEVICE_ABILITY = _HCNetSDK.NET_DVR_GetDeviceAbility
            C_GET_DEVICE_ABILITY.argtypes = [LONG, DWORD, CHARP, DWORD, CHARP, DWORD]
            C_GET_DEVICE_ABILITY.restype = BOOL

            ret = C_GET_DEVICE_ABILITY(LONG(lUserID), DWORD(dwAbilityType),
                                       CHARP(bytes(pInBuf, encoding='utf8')), DWORD(len(pInBuf)),
                                       CHARP(bytes(pOutBuf, encoding='utf8')), DWORD(len(pOutBuf)))
        except Exception as err:
            raise HikError("NET_DVR_GetDeviceAbility", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_GetDeviceAbility", self.__NET_DVR_GetLastError(), "Executing failed")


    ####################################################
    ### 实时预览                                      ###
    ####################################################
    # 实时预览
    def NET_DVR_RealPlay_V30(
            self,
            lUserID,
            lpClientInfo,
            fCallBack,
            pUser,
            bBlocked):
        """
            实时预览（支持多码流）。

        Parameters:
            lUserID         : NET_DVR_Login_V40等登录接口的返回值
            lpClientInfo    : 预览参数
            fCallBack       : 码流数据回调函数
            pUser           : 用户数据
            bBlocked        : 请求码流过程是否阻塞：0－否；1－是

        Return
            lRealHandle : 预览句柄

        Exception:
            HikError.
        """
        try:
            C_REALPLAY_V30 = _HCNetSDK.NET_DVR_RealPlay_V30
            if fCallBack is not None:
                C_REALPLAY_V30.argtypes = [LONG, LPNET_DVR_CLIENTINFO, fRealDataCallBack_V30, VOIDP, BOOL]
                fCallBack = fRealDataCallBack_V30(fCallBack)
            else:
                pass
                C_REALPLAY_V30.argtypes = [LONG, LPNET_DVR_CLIENTINFO, VOIDP, VOIDP, BOOL]
            C_REALPLAY_V30.restype = LONG

            lRealHandle = C_REALPLAY_V30(LONG(lUserID), byref(lpClientInfo), fCallBack, pUser, BOOL(bBlocked))
        except Exception as err:
            raise HikError("NET_DVR_RealPlay_V30", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if lRealHandle == -1:
            raise HikError("NET_DVR_RealPlay_V30", self.__NET_DVR_GetLastError(), "Executing failed")

        return lRealHandle

    def NET_DVR_StopRealPlay(
            self,
            lRealHandle):
        """
            停止预览。

        Parameters:
            lRealHandle : 预览句柄，NET_DVR_RealPlay或者NET_DVR_RealPlay_V30的返回值

        Exception:
            HikError.
        """
        try:
            C_STOP_REALPLAY = _HCNetSDK.NET_DVR_StopRealPlay
            C_STOP_REALPLAY.argtypes = [LONG]
            C_STOP_REALPLAY.restype = BOOL
            ret = C_STOP_REALPLAY(LONG(lRealHandle))
        except Exception as err:
            raise HikError("NET_DVR_StopRealPlay", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_StopRealPlay", self.__NET_DVR_GetLastError(), "Executing failed")

    def NET_DVR_GetRealPlayerIndex(
            self,
            lRealHandle):
        """
            获取预览时用来解码和显示的播放器句柄。

        Parameters:
            lRealHandle : 预览句柄，NET_DVR_RealPlay或者NET_DVR_RealPlay_V30的返回值

        Return
            nPort : 播放句柄， 用户可以通过返回的句柄自行实现播放库SDK提供的其他功能

        Exception:
            HikError.
        """
        try:
            C_GET_REALPLAYER_INDEX = _HCNetSDK.NET_DVR_GetRealPlayerIndex
            C_GET_REALPLAYER_INDEX.argtypes = [LONG]
            C_GET_REALPLAYER_INDEX.restype = INT
            nPort = C_GET_REALPLAYER_INDEX(LONG(lRealHandle))
        except Exception as err:
            raise HikError("NET_DVR_GetRealPlayerIndex", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if nPort == -1:
            raise HikError("NET_DVR_GetRealPlayerIndex", self.__NET_DVR_GetLastError(), "Executing failed")

        return nPort


    # 实时数据回调和录像
    def NET_DVR_SetRealDataCallBack(
            self,
            lRealHandle,
            fCallBack,
            dwUser):
        """
            注册回调函数，捕获实时码流数据。

        Parameters:
            lRealHandle : NET_DVR_RealPlay或NET_DVR_RealPlay_V30的返回值
            fCallBack   : 码流数据回调函数
            dwUser      : 用户数据

        Remarks:
            fCallBack回调函数中不能执行可能会占用时间较长的接口或操作，不建议调用该SDK（HCNetSDK.dll）本身的接口。
            此函数包括开始和停止用户处理SDK捕获的数据, 当回调函数cbRealDataCallBack设为非NULL值时，表示回调和处理数据,当设为NULL时表示停止回调和处理数据。
            回调的第一个包是40个字节的文件头，供后续解码使用，之后回调的是压缩的码流。回调数据最大为256K字节。

        Exception:
            HikError.
        """
        try:
            C_GET_REALPLAYER_INDEX = _HCNetSDK.NET_DVR_SetRealDataCallBack
            C_GET_REALPLAYER_INDEX.argtypes = [LONG, fRealDataCallBack_V30, DWORD]
            C_GET_REALPLAYER_INDEX.restype = BOOL
            ret = C_GET_REALPLAYER_INDEX(LONG(lRealHandle), fRealDataCallBack_V30(fCallBack), DWORD(dwUser))
        except Exception as err:
            raise HikError("NET_DVR_SetRealDataCallBack", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if ret == -1:
            raise HikError("NET_DVR_SetRealDataCallBack", self.__NET_DVR_GetLastError(), "Executing failed")

    def NET_DVR_SaveRealData(
            self,
            lRealHandle,
            sFileName):
        """
            捕获数据并存放到指定的文件中

        Parameters:
            lRealHandle : NET_DVR_RealPlay或NET_DVR_RealPlay_V30的返回值
            sFileName   : 文件路径指针，包括文件名，例如："D:\\test.mp4"

        Remarks:
            V5.0.3.2或以后版本，通过该接口保存录像，保存的录像文件数据超过文件最大限制字节数（默认为1024MB）
            SDK会自动切片，即新建文件进行保存，文件名命名规则为在接口传入的文件名基础上增加数字标识(例如：*_1.mp4、*_2.mp4)”。
            可以调用NET_DVR_GetSDKLocalCfg、NET_DVR_SetSDKLocalCfg(配置类型：NET_DVR_LOCAL_CFG_TYPE_GENERAL)获取和设置切片模式和文件最大限制字节数。

        Exception:
            HikError.
        """
        try:
            C_SAVE_REAL_DATA = _HCNetSDK.NET_DVR_SaveRealData
            C_SAVE_REAL_DATA.argtypes = [LONG, CHARP]
            C_SAVE_REAL_DATA.restype = BOOL
            ret = C_SAVE_REAL_DATA(LONG(lRealHandle), CHARP(bytes(sFileName, encoding='utf8')))
        except Exception as err:
            raise HikError("NET_DVR_SaveRealData", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_SaveRealData", self.__NET_DVR_GetLastError(), "Executing failed")

    def NET_DVR_StopSaveRealData(
            self,
            lRealHandle):
        """
            停止数据捕获。

        Parameters:
            lRealHandle : NET_DVR_RealPlay或NET_DVR_RealPlay_V30的返回值

        Exception:
            HikError.
        """
        try:
            C_STOP_SAVE_REAL_DATA = _HCNetSDK.NET_DVR_StopSaveRealData
            C_STOP_SAVE_REAL_DATA.argtypes = [LONG]
            C_STOP_SAVE_REAL_DATA.restype = BOOL
            ret = C_STOP_SAVE_REAL_DATA(LONG(lRealHandle))
        except Exception as err:
            raise HikError("NET_DVR_StopSaveRealData", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_StopSaveRealData", self.__NET_DVR_GetLastError(), "Executing failed")

    # 预览抓图
    def NET_DVR_SetCapturePictureMode(
            self,
            dwCaptureMode):
        """
            设置抓图模式。

        Parameters:
            dwCaptureMode   : 抓图模式
            *BMP_MODE = 0
            *JPEG_MODE = 1

        Remarks：
            调用该接口设置抓图模式后，调用预览或者回放抓图接口可抓取相应格式的图片。如果抓图模式为JPEG模式，抓取的是JPEG图片，保存路径后缀应为.jpg。
            例如：sPicFileName="D:\\test.jpg"；如果抓图模式为BMP模式，抓取的是BMP图片，保存路径后缀应为.bmp，例如：sPicFileName="D:\\test.bmp"。

        Exception:
            HikError.
        """
        try:
            C_SET_CAPTURE_PICTURE_MODE = _HCNetSDK.NET_DVR_SetCapturePictureMode
            C_SET_CAPTURE_PICTURE_MODE.argtypes = [DWORD]
            C_SET_CAPTURE_PICTURE_MODE.restype = BOOL
            ret = C_SET_CAPTURE_PICTURE_MODE(DWORD(dwCaptureMode))
        except Exception as err:
            raise HikError("NET_DVR_SetCapturePictureMode", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_SetCapturePictureMode", self.__NET_DVR_GetLastError(), "Executing failed")

    def NET_DVR_CapturePicture(
            self,
            lRealHandle,
            sPicFileName):
        """
            预览时，单帧数据捕获并保存成图片。

        Parameters:
            lRealHandle     : NET_DVR_RealPlay或NET_DVR_RealPlay_V30的返回值
            sPicFileName    : 保存图象的文件路径（包括文件名）。路径长度和操作系统有关，sdk不做限制，windows默认路径长度小于等于256字节（包括文件名在内）。

        Remarks：
            在调用该接口之前可以调用NET_DVR_SetCapturePictureMode设置抓图模式，默认为BMP模式。
            如果抓图模式为BMP模式，抓取的是BMP图片，保存路径后缀应为.bmp，例如：sPicFileName="D:\\test.bmp"；如果抓图模式为JPEG模式，抓取的是JPEG图片，保存路径后缀应为.jpg，例如：sPicFileName="D:\\test.jpg"。
            若设备的当前分辨率为2CIF，播放库做了相关处理，抓取的图像为4CIF。
            调用NET_DVR_CapturePicture进行抓图，要求在调用NET_DVR_RealPlay_V40等接口时传入非空的播放句柄（播放库解码显示），否则时接口会返回失败，调用次序错误。

        Exception:
            HikError.
        """
        try:
            C_CAPTURE_PICTURE = _HCNetSDK.NET_DVR_CapturePicture
            C_CAPTURE_PICTURE.argtypes = [LONG, CHARP]
            C_CAPTURE_PICTURE.restype = BOOL
            ret = C_CAPTURE_PICTURE(LONG(lRealHandle), CHARP(bytes(sPicFileName, encoding='utf8')))
        except Exception as err:
            raise HikError("NET_DVR_CapturePicture", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_CapturePicture", self.__NET_DVR_GetLastError(), "Executing failed")

    def NET_DVR_CapturePictureBlock(
            self,
            lRealHandle,
            sPicFileName,
            dwTimeOut):
        """
            预览时抓图并保存成图片文件。

        Parameters:
            lRealHandle     : NET_DVR_RealPlay或NET_DVR_RealPlay_V30的返回值
            sPicFileName    : 保存图象的文件路径（包括文件名）。路径长度和操作系统有关，sdk不做限制，windows默认路径长度小于等于256字节（包括文件名在内）。
            dwTimeOut       : 超时时间，目前无效

        Remarks：
            该接口为预览阻塞模式抓图，预览接口必须传入有效的窗口句柄，正常解码显示的时候才能调用该接口进行抓图。
            图片数据格式支持BMP和JPEG两种，通过NET_DVR_SetCapturePictureMode可以设置数据格式，不同的格式保存文件名使用不同的后缀（.bmp或者.jpg）。

        Exception:
            HikError.
        """
        try:
            C_CAPTURE_PICTURE = _HCNetSDK.NET_DVR_CapturePicture
            C_CAPTURE_PICTURE.argtypes = [LONG, CHARP, DWORD]
            C_CAPTURE_PICTURE.restype = BOOL
            ret = C_CAPTURE_PICTURE(LONG(lRealHandle), CHARP(bytes(sPicFileName, encoding='utf8')), DWORD(dwTimeOut))
        except Exception as err:
            raise HikError("NET_DVR_CapturePictureBlock", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_CapturePictureBlock", self.__NET_DVR_GetLastError(), "Executing failed")

    # 设备抓图
    def NET_DVR_CaptureJPEGPicture(
            self,
            lUserID,
            lChannel,
            lpJpegPara,
            sPicFileName):
        """
            单帧数据捕获并保存成JPEG图。

        Parameters:
            lUserID         : NET_DVR_Login_V40等登录接口的返回值
            lChannel        : 通道号
            lpJpegPara      : JPEG图像参数
            sPicFileName    : 保存JPEG图的文件路径（包括文件名）

        Remarks：
            该接口用于设备的单帧数据捕获，并保存成JPEG图片文件。JPEG抓图功能或者抓图分辨率需要设备支持，如果不支持接口返回失败，错误号23或者29。
            对于DVR、NVR设备，参数wPicQuality支持的分辨率值可通过NET_DVR_GetDeviceAbility获取能力集类型PIC_CAPTURE_ABILITY获取(NET_DVR_COMPRESSIONCFG_ABILITY)得到。
            对接网络摄像机、门禁主机等设备，设备是否支持JPEG抓图功能或者支持的参数能力，可以通过设备能力集进行判断，
            对应设备JPEG抓图能力集(JpegCaptureAbility)，相关接口：NET_DVR_GetDeviceAbility，能力集类型：DEVICE_JPEG_CAP_ABILITY，节点：<ManualCapture>。
            wPicSize设为2抓取的图片分辨率是4CIF还是D1由设备决定，一般为4CIF(P制:704*576/N制:704*480)。

        Exception:
            HikError.
        """
        try:
            C_CAPTURE_JPEG_PICTURE = _HCNetSDK.NET_DVR_CaptureJPEGPicture
            C_CAPTURE_JPEG_PICTURE.argtypes = [LONG, LONG, LPNET_DVR_JPEGPARA, CHARP]
            C_CAPTURE_JPEG_PICTURE.restype = BOOL
            ret = C_CAPTURE_JPEG_PICTURE(LONG(lUserID), LONG(lChannel), byref(lpJpegPara),
                                         CHARP(bytes(sPicFileName, encoding='utf8')))
        except Exception as err:
            raise HikError("NET_DVR_CaptureJPEGPicture", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_CaptureJPEGPicture", self.__NET_DVR_GetLastError(), "Executing failed")

    ####################################################
    ### 云台控制                                     ###
    ####################################################
    # 云台基本控制
    def NET_DVR_PTZControl(
            self,
            lRealHandle,
            dwPTZCommand,
            dwStop):
        """
            云台控制操作(需先启动图象预览)。

        Parameters:
            lRealHandle     : NET_DVR_RealPlay或NET_DVR_RealPlay_V30的返回值
            dwPTZTrackCmd   : 云台控制命令
            dwStop          : 云台停止动作或开始动作：0－开始，1－停止

        Remarks:
            对云台实施的每一个动作都需要调用该接口两次，分别是开始和停止控制，由接口中的最后一个参数（dwStop）决定。在调用此接口之前需要先开启预览。
            与设备之间的云台各项操作的命令都对应于设备与云台之间的控制码，设备会根据目前设置的解码器种类和解码器地址向云台发送控制码。
            如果目前设备上设置的解码器与云台设备的不匹配，需要重新配置设备的解码器。
            如果云台设备所需的解码器设备不支持，则无法用该接口控制。
            云台默认以最大速度动作。

        Exception:
            HikError.
        """
        try:
            C_PTZ_CONTROL = _HCNetSDK.NET_DVR_PTZControl
            C_PTZ_CONTROL.argtypes = [LONG, DWORD, DWORD]
            C_PTZ_CONTROL.restype = BOOL
            ret = C_PTZ_CONTROL(LONG(lRealHandle), DWORD(dwPTZCommand), DWORD(dwStop))
        except Exception as err:
            raise HikError("NET_DVR_PTZControl", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_PTZControl", self.__NET_DVR_GetLastError(), "Executing failed")

    def NET_DVR_PTZControl_Other(
            self,
            lUserID,
            lChannel,
            dwPTZCommand,
            dwStop):
        """
            云台控制操作(不用启动图象预览)。

        Parameters:
            lUserID         : NET_DVR_Login_V40等登录接口的返回值
            lChannel        : 通道号
            dwPTZTrackCmd   : 云台控制命令
            dwStop          : 云台停止动作或开始动作：0－开始，1－停止

        Remarks:
            对云台实施的每一个动作都需要调用该接口两次，分别是开始和停止控制，由接口中的最后一个参数（dwStop）决定。在调用此接口之前需要先注册设备。
            与设备之间的云台各项操作的命令都对应于设备与云台之间的控制码，设备会根据目前设置的解码器种类和解码器地址向云台发送控制码。
            如果目前设备上设置的解码器与云台设备的不匹配，需要重新配置设备的解码器。
            如果云台设备所需的解码器设备不支持，则无法用该接口控制。
            云台默认以最大速度动作。
            通过NET_DVR_PTZControl控制云台，设备接收到控制命令后云台进行相应的动作，如果操作失败则返回错误，运行正常则返回成功。
            而通过NET_DVR_PTZControl_Other控制云台，设备接收到控制命令后直接返回成功。

        Exception:
            HikError.
        """
        try:
            C_PTZ_CONTROL_OTHER = _HCNetSDK.NET_DVR_PTZControl_Other
            C_PTZ_CONTROL_OTHER.argtypes = [LONG, LONG, DWORD, DWORD]
            C_PTZ_CONTROL_OTHER.restype = BOOL
            ret = C_PTZ_CONTROL_OTHER(LONG(lUserID), LONG(lChannel), DWORD(dwPTZCommand), DWORD(dwStop))
        except Exception as err:
            raise HikError("NET_DVR_PTZControl_Other", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_PTZControl_Other", self.__NET_DVR_GetLastError(), "Executing failed")

    def NET_DVR_PTZControlWithSpeed(
            self,
            lRealHandle,
            dwPTZCommand,
            dwStop,
            dwSpeed):
        """
            带速度的云台控制操作(需先启动图象预览)。

        Parameters:
            lRealHandle     : NET_DVR_RealPlay或NET_DVR_RealPlay_V30的返回值
            dwPTZTrackCmd   : 云台控制命令
            dwStop          : 云台停止动作或开始动作：0－开始；1－停止
            dwSpeed         : 云台控制的速度，用户按不同解码器的速度控制值设置。取值范围[1,7]

        Remarks:
            对云台实施的每一个动作都需要调用该接口两次，分别是开始和停止控制，由接口中的最后一个参数（dwStop）决定。在调用此接口之前需要先注册设备。
            与设备之间的云台各项操作的命令都对应于设备与云台之间的控制码，设备会根据目前设置的解码器种类和解码器地址向云台发送控制码。
            如果目前设备上设置的解码器与云台设备的不匹配，需要重新配置设备的解码器。
            如果云台设备所需的解码器设备不支持，则无法用该接口控制。

        Exception:
            HikError.
        """
        try:
            C_PTZ_CONTROL_WITH_SPEED = _HCNetSDK.NET_DVR_PTZControlWithSpeed
            C_PTZ_CONTROL_WITH_SPEED.argtypes = [LONG, DWORD, DWORD, DWORD]
            C_PTZ_CONTROL_WITH_SPEED.restype = BOOL
            ret = C_PTZ_CONTROL_WITH_SPEED(LONG(lRealHandle), DWORD(dwPTZCommand), DWORD(dwStop), DWORD(dwSpeed))
        except Exception as err:
            raise HikError("NET_DVR_PTZControlWithSpeed", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_PTZControlWithSpeed", self.__NET_DVR_GetLastError(), "Executing failed")

    def NET_DVR_PTZControlWithSpeed_Other(
            self,
            lUserID,
            lChannel,
            dwPTZCommand,
            dwStop,
            dwSpeed):
        """
            带速度的云台控制操作(不用启动图象预览)。

        Parameters:
            lUserID         : NET_DVR_Login_V40等登录接口的返回值
            lChannel        : 通道号
            dwPTZTrackCmd   : 云台控制命令
            dwStop          : 云台停止动作或开始动作：0－开始，1－停止
            dwSpeed         : 云台控制的速度，用户按不同解码器的速度控制值设置。取值范围[1,7]

        Remarks:
            对云台实施的每一个动作都需要调用该接口两次，分别是开始和停止控制，由接口中的最后一个参数（dwStop）决定。在调用此接口之前需要先注册设备。
            与设备之间的云台各项操作的命令都对应于设备与云台之间的控制码，设备会根据目前设置的解码器种类和解码器地址向云台发送控制码。
            如果目前设备上设置的解码器与云台设备的不匹配，需要重新配置设备的解码器。
            如果云台设备所需的解码器设备不支持，则无法用该接口控制。
            而通过NET_DVR_PTZControlWithSpeed_Other控制云台，设备接收到控制命令后直接返回成功。

        Exception:
            HikError.
        """
        try:
            C_PTZ_CONTROL_WITH_SPEED_OTHER = _HCNetSDK.NET_DVR_PTZControlWithSpeed_Other
            C_PTZ_CONTROL_WITH_SPEED_OTHER.argtypes = [LONG, LONG, DWORD, DWORD, DWORD]
            C_PTZ_CONTROL_WITH_SPEED_OTHER.restype = BOOL
            ret = C_PTZ_CONTROL_WITH_SPEED_OTHER(LONG(lUserID), LONG(lChannel),
                                                 DWORD(dwPTZCommand), DWORD(dwStop), DWORD(dwSpeed))
        except Exception as err:
            raise HikError("NET_DVR_PTZControlWithSpeed_Other", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_PTZControlWithSpeed_Other", self.__NET_DVR_GetLastError(), "Executing failed")

    # 云台预置点功能
    def NET_DVR_PTZPreset(
            self,
            lRealHandle,
            dwPTZPresetCmd,
            dwPresetIndex):
        """
            云台预置点操作（需先启动预览）。

        Parameters:
            lRealHandle     : NET_DVR_RealPlay或NET_DVR_RealPlay_V30的返回值
            dwPTZPresetCmd  : 操作云台预置点命令
            *SET_PRESET = 8  设置预置点
            *CLE_PRESET = 9  清除预置点
            *GOTO_PRESET = 39  转到预置点
            dwPresetIndex   : 预置点的序号（从1开始），最多支持300个预置点

        Remarks:
            与设备之间的云台各项操作的命令都对应于设备与云台之间的控制码，设备会根据目前设置的解码器种类和解码器地址向云台发送控制码。
            如果目前设备上设置的解码器与云台设备的不匹配，需要重新配置设备的解码器。如果云台设备所需的解码器设备不支持，则无法用该接口控制。

        Exception:
            HikError.
        """
        try:
            C_PTZ_PRESET = _HCNetSDK.NET_DVR_PTZPreset
            C_PTZ_PRESET.argtypes = [LONG, DWORD, DWORD]
            C_PTZ_PRESET.restype = BOOL
            ret = C_PTZ_PRESET(LONG(lRealHandle), DWORD(dwPTZPresetCmd), DWORD(dwPresetIndex))
        except Exception as err:
            raise HikError("NET_DVR_PTZPreset", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_PTZPreset", self.__NET_DVR_GetLastError(), "Executing failed")

    def NET_DVR_PTZPreset_Other(
            self,
            lUserID,
            lChannel,
            dwPTZPresetCmd,
            dwPresetIndex):
        """
            云台预置点操作。

        Parameters:
            lUserID         : NET_DVR_Login_V40等登录接口的返回值
            lChannel        : 通道号
            dwPTZPresetCmd  : 操作云台预置点命令
            dwPresetIndex   : 预置点的序号（从1开始），最多支持300个预置点

        Remarks:
            与设备之间的云台各项操作的命令都对应于设备与云台之间的控制码，设备会根据目前设置的解码器种类和解码器地址向云台发送控制码。
            如果目前设备上设置的解码器与云台设备的不匹配，需要重新配置设备的解码器。如果云台设备所需的解码器设备不支持，则无法用该接口控制。
            通过NET_DVR_PTZPreset控制云台，设备接收到控制命令后云台进行相应的动作，如果操作失败则返回错误，运行正常才返回成功。
            而通过NET_DVR_PTZPreset_Other控制云台，设备接收到控制命令后直接返回成功

        Exception:
            HikError.
        """
        try:
            C_PTZ_PRESET_OTHER = _HCNetSDK.NET_DVR_PTZPreset_Other
            C_PTZ_PRESET_OTHER.argtypes = [LONG, LONG, DWORD, DWORD]
            C_PTZ_PRESET_OTHER.restype = BOOL
            ret = C_PTZ_PRESET_OTHER(LONG(lUserID), LONG(lChannel), DWORD(dwPTZPresetCmd), DWORD(dwPresetIndex))
        except Exception as err:
            raise HikError("NET_DVR_PTZPreset_Other", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_PTZPreset_Other", self.__NET_DVR_GetLastError(), "Executing failed")

    # 云台巡航功能
    def NET_DVR_PTZCruise(
            self,
            lRealHandle,
            dwPTZCruiseCmd,
            byCruiseRoute,
            byCruisePoint,
            wInput):
        """
            云台巡航操作，需先启动预览。

        Parameters:
            lRealHandle     : NET_DVR_RealPlay或NET_DVR_RealPlay_V30的返回值
            dwPTZCruiseCmd  : 操作云台巡航命令
            byCruiseRoute   : 巡航路径，最多支持32条路径（序号从1开始）
            byCruisePoint   : 巡航点，最多支持32个点（序号从1开始）
            wInput          : 不同巡航命令时的值不同，预置点(最大300)、时间(最大255)、速度(最大40)

        Remarks:
            与设备之间的云台各项操作的命令都对应于设备与云台之间的控制码，设备会根据目前设置的解码器种类和解码器地址向云台发送控制码。
            如果目前设备上设置的解码器与云台设备的不匹配，需要重新配置设备的解码器。如果云台设备所需的解码器设备不支持，则无法用该接口控制。

        Exception:
            HikError.
        """
        try:
            C_PTZ_CRUISE = _HCNetSDK.NET_DVR_PTZCruise
            C_PTZ_CRUISE.argtypes = [LONG, DWORD, BYTE, BYTE, DWORD]
            C_PTZ_CRUISE.restype = BOOL
            ret = C_PTZ_CRUISE(LONG(lRealHandle), DWORD(dwPTZCruiseCmd), BYTE(byCruiseRoute), BYTE(byCruisePoint),
                               DWORD(wInput))
        except Exception as err:
            raise HikError("NET_DVR_PTZCruise", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_PTZCruise", self.__NET_DVR_GetLastError(), "Executing failed")

    def NET_DVR_PTZCruise_Other(
            self,
            lUserID,
            lChannel,
            dwPTZCruiseCmd,
            byCruiseRoute,
            byCruisePoint,
            wInput):
        """
            云台巡航操作。

        Parameters:
            lUserID         : NET_DVR_Login_V40等登录接口的返回值
            lChannel        : 通道号
            dwPTZCruiseCmd  : 操作云台巡航命令
            byCruiseRoute   : 巡航路径，最多支持32条路径（序号从1开始）
            byCruisePoint   : 巡航点，最多支持32个点（序号从1开始）
            wInput          : 不同巡航命令时的值不同，预置点(最大300)、时间(最大255)、速度(最大40)

        Remarks:
            与设备之间的云台各项操作的命令都对应于设备与云台之间的控制码，设备会根据目前设置的解码器种类和解码器地址向云台发送控制码。
            如果目前设备上设置的解码器与云台设备的不匹配，需要重新配置设备的解码器。如果云台设备所需的解码器设备不支持，则无法用该接口控制。
            通过NET_DVR_PTZCruise控制云台，设备接收到控制命令后云台进行相应的动作，如果操作失败则返回错误，运行正常则返回成功。
            而通过NET_DVR_PTZCruise_Other控制云台，设备接收到控制命令后直接返回成功。

        Exception:
            HikError.
        """
        try:
            C_PTZ_CRUISE_OTHER = _HCNetSDK.NET_DVR_PTZCruise_Other
            C_PTZ_CRUISE_OTHER.argtypes = [LONG, LONG, DWORD, BYTE, BYTE, WORD]
            C_PTZ_CRUISE_OTHER.restype = BOOL
            ret = C_PTZ_CRUISE_OTHER(LONG(lUserID), LONG(lChannel), DWORD(dwPTZCruiseCmd),
                                     BYTE(byCruiseRoute), BYTE(byCruisePoint), WORD(wInput))
        except Exception as err:
            raise HikError("NET_DVR_PTZCruise_Other", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_PTZCruise_Other", self.__NET_DVR_GetLastError(), "Executing failed")

    # 云台轨迹操作
    def NET_DVR_PTZTrack(
            self,
            lRealHandle,
            dwPTZTrackCmd):
        """
            云台轨迹操作，需先启动预览。

        Parameters:
            lRealHandle     : NET_DVR_RealPlay或NET_DVR_RealPlay_V30的返回值
            dwPTZTrackCmd   : 操作云台轨迹命令

        Remarks:
            与设备之间的云台各项操作的命令都对应于设备与云台之间的控制码，设备会根据目前设置的解码器种类和解码器地址向云台发送控制码。
            如果目前设备上设置的解码器与云台设备的不匹配，需要重新配置设备的解码器。如果云台设备所需的解码器设备不支持，则无法用该接口控制。

        Exception:
            HikError.
        """
        try:
            C_PTZ_TRACK = _HCNetSDK.NET_DVR_PTZTrack
            C_PTZ_TRACK.argtypes = [LONG, DWORD]
            C_PTZ_TRACK.restype = BOOL
            ret = C_PTZ_TRACK(LONG(lRealHandle), DWORD(dwPTZTrackCmd))
        except Exception as err:
            raise HikError("NET_DVR_PTZTrack", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_PTZTrack", self.__NET_DVR_GetLastError(), "Executing failed")

    def NET_DVR_PTZTrack_Other(
            self,
            lUserID,
            lChannel,
            dwPTZTrackCmd):
        """
            云台轨迹操作。

        Parameters:
            lUserID         : NET_DVR_Login_V40等登录接口的返回值
            lChannel        : 通道号
            dwPTZTrackCmd   : 操作云台轨迹命令

        Remarks:
            与设备之间的云台各项操作的命令都对应于设备与云台之间的控制码，设备会根据目前设置的解码器种类和解码器地址向云台发送控制码。
            如果目前设备上设置的解码器与云台设备的不匹配，需要重新配置设备的解码器。如果云台设备所需的解码器设备不支持，则无法用该接口控制。
            通过NET_DVR_PTZTrack控制云台，设备接收到控制命令后云台进行相应的动作，如果操作失败则返回错误，运行正常才返回成功。
            而通过NET_DVR_PTZTrack_Other控制云台，设备接收到控制命令后直接返回成功。

        Exception:
            HikError.
        """
        try:
            C_PTZ_TRACK_OTHER = _HCNetSDK.NET_DVR_PTZTrack_Other
            C_PTZ_TRACK_OTHER.argtypes = [LONG, LONG, DWORD]
            C_PTZ_TRACK_OTHER.restype = BOOL
            ret = C_PTZ_TRACK_OTHER(LONG(lUserID), LONG(lChannel), DWORD(dwPTZTrackCmd))
        except Exception as err:
            raise HikError("NET_DVR_PTZTrack_Other", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_PTZTrack_Other", self.__NET_DVR_GetLastError(), "Executing failed")

    def NET_DVR_RemoteControl(
            self,
            lUserID,
            dwCommand,
            lpInBuffer):
        """
            远程控制。

        Parameters:
            lUserID      : NET_DVR_Login_V40等登录接口的返回值
            dwCommand    : 控制命令
            lpInBuffer   : 输入参数，具体内容跟控制命令相关

        Remarks:
            此功能是对原接口NET_DVR_PTZTrack和NET_DVR_PTZTrack_Other的扩展.
            原来只支持一条轨迹操作，而通过接口NET_DVR_RemoteControl可支持多条轨迹操作，且支持停止轨迹、删除单条轨迹、删除所有轨迹操作。

        Exception:
            HikError.
        """
        try:
            C_REMOTE_CONTROL = _HCNetSDK.NET_DVR_RemoteControl
            C_REMOTE_CONTROL.argtypes = [LONG, DWORD, VOIDP, DWORD]
            C_REMOTE_CONTROL.restype = BOOL
            ret = C_REMOTE_CONTROL(LONG(lUserID), LONG(dwCommand), byref(lpInBuffer), DWORD(sizeof(lpInBuffer)))
        except Exception as err:
            raise HikError("NET_DVR_RemoteControl", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_RemoteControl", self.__NET_DVR_GetLastError(), "Executing failed")


    ####################################################
    ### ISAPI                                        ###
    ####################################################
    def NET_DVR_STDXMLConfig(
            self,
            lUserID,
            lpInputParam,
            lpOutputParam):
        """
            PTZ track controller.

        Parameters:
            lUserID         : User ID, returned from login()
            lpInputParam    : Input parameters
            lpOutputParam   : Output parameters

        Exception:
            HikError.
        """
        try:
            C_STD_XML_CONFIG = _HCNetSDK.NET_DVR_STDXMLConfig
            C_STD_XML_CONFIG.argtypes = [LONG, LPNET_DVR_XML_CONFIG_INPUT, LPNET_DVR_XML_CONFIG_OUTPUT]
            C_STD_XML_CONFIG.restype = BOOL
            ret = C_STD_XML_CONFIG(LONG(lUserID), byref(lpInputParam), byref(lpOutputParam))
        except Exception as err:
            raise HikError("NET_DVR_STDXMLConfig", NET_DVR_UNKNOW, "Executing Failed with error: %s" % str(err))

        if not ret:
            raise HikError("NET_DVR_STDXMLConfig", self.__NET_DVR_GetLastError(), "Executing failed")


if __name__ == "__main__":
    import time

    def callback(lRealHandle, dwDataType, pBuffer, dwBufSize, pUser):
        print("callback")


    pyhik = pyHik()
    pyhik.NET_DVR_Init()

    devInfo = NET_DVR_DEVICEINFO_V30()
    userID = pyhik.NET_DVR_Login_V30("192.168.0.201", 8000, "admin", "ruike2019", devInfo)
    print(userID, devInfo)

    # devConfig = NET_DVR_IPPARACFG_V40()
    # pyhik.NET_DVR_GetDVRConfig(userID, NET_DVR_GET_IPPARACFG_V40, 0, devConfig)
    # print(devConfig)
    #
    # devConfig = NET_DVR_DECODERCFG_V40()
    # pyhik.NET_DVR_GetDVRConfig(userID, NET_DVR_GET_DECODERCFG_V40, devInfo.byStartChan, devConfig)
    # print(devConfig)

    lpClientInfo = NET_DVR_CLIENTINFO()
    lpClientInfo.lChannel = devInfo.byStartChan
    lpClientInfo.lLinkMode = 0
    lpClientInfo.hPlayWnd = 0
    lpClientInfo.byProtoType = 0

    lRealHandle = pyhik.NET_DVR_RealPlay_V30(userID, lpClientInfo, callback, 0, False)
    time.sleep(10)

    pyhik.NET_DVR_StopRealPlay(lRealHandle)



    # buffer = ""
    # lpInputParam = NET_DVR_XML_CONFIG_INPUT()
    # lpInputParam.dwSize = sizeof(lpInputParam)
    # lpInputParam.lpRequestUrl = cast(CHARP(bytes("GET /ISAPI/PTZCtrl/channels/1/presets", encoding='utf8')), VOIDP)
    # lpInputParam.dwRequestUrlLen = 256
    # lpInputParam.dwRecvTimeOut = 3000
    #
    # lpOutputParam = NET_DVR_XML_CONFIG_OUTPUT()
    # lpOutputParam.dwSize = sizeof(lpOutputParam)
    # lpOutputParam.lpOutBuffer = cast(CHARP(bytes(buffer, encoding='utf8')), VOIDP)
    # lpOutputParam.dwOutBufferSize = 1024*1024
    #
    # pyhik.NET_DVR_STDXMLConfig(userID, lpInputParam, lpOutputParam)
    #
    # print(str(cast(lpOutputParam.lpOutBuffer, CHARP).value))
    # print(str(lpOutputParam.dwReturnedXMLSize))

    pyhik.NET_DVR_Logout(userID)
    pyhik.NET_DVR_Cleanup()
