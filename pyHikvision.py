import platform
sysstr = platform.system()
sysbit = platform.architecture()[0]
if sysstr == 'Windows':
    if sysbit == '32bit':
        from .libs.windows.x86.pyhik import *
    if sysbit == '64bit':
        from .libs.windows.x64.pyhik import *
elif sysstr == 'Linux':
    pass
    # if sysbit == '32bit':
    #     from .libs.bit32.libNeoService4c import pyNeoService, Endpos
    # if sysbit == '64bit':
    #     from .libs.bit64.libNeoService4c import pyNeoService, Endpos


class Hikvision():
    """
        Application class implementation
    """
    def __init__(self):
        self.__pyhik = pyHik()

        self.__userIDs = []
        self.__devInfo = {}

        self.__realHandles = {}

    @property
    def userIDs(self):
        return self.__userIDs

    @property
    def realHandles(self):
        return self.__realHandles

    ####################################################
    ### 初始化与连接设置                              ###
    ####################################################
    def initialize(self):
        """
            Initialize. Call this function before using any of the other APIs

        Exception:
            HikError.
        """

        self.__pyhik.NET_DVR_Init()
        self.__userIDs = []
        self.__devInfo = {}
        self.__realHandles = {}

    def finalize(self):
        """
            Release. If initialize() was called, invoke this function at program exit

        Exception:
            HikError.
        """

        self.__pyhik.NET_DVR_Cleanup()
        self.__userIDs = []
        self.__devInfo = {}
        self.__realHandles = {}

    def set_connect_time(self, waitTime, times = 1):
        """
            设置网络连接超时时间和连接尝试次数

        Parameters:
            waitTime : 超时时间，单位毫秒，取值范围[300,75000]，实际最大超时时间因系统的connect超时时间而不同
            times    : 连接尝试次数（保留）

        Exception:
            HikError.
        """

        self.__pyhik.NET_DVR_SetConnectTime(waitTime, times)

    def set_reconnect(self, interval, enableRecon = True):
        """
            设置重连功能

        Parameters:
            interval    : 重连间隔，单位:毫秒
            enableRecon : 是否重连，0-不重连，1-重连，参数默认值为1

        Exception:
            HikError.
        """

        self.__pyhik.NET_DVR_SetReconnect(interval, enableRecon)


    ####################################################
    ### 登录与登出                                    ###
    ####################################################
    def login(self, ip, port, username, password):
        """
            用户注册设备

        Parameters:
            ip          : 设备IP地址或是静态域名，字符数不大于128个
            port        : 设备端口号
            username    : 登录的用户名
            password    : 用户密码

        Return
            userID : 该用户ID具有唯一性，后续对设备的操作都需要通过此ID实现

        Exception:
            HikError.
        """

        devInfo = NET_DVR_DEVICEINFO_V30()
        userID = self.__pyhik.NET_DVR_Login_V30(ip, port, username, password, devInfo)
        if userID not in self.__userIDs:
            self.__userIDs.append(userID)
            self.__devInfo[userID] = devInfo
        return userID


    def logout(self, userID = None):
        """
            用户注销

        Parameters:
            userID : 用户ID号，NET_DVR_Login等登录接口的返回值, 设置为None时，将全部已登陆设备全部登出。

        Exception:
            HikError.
        """

        if userID is None:
            userID = self.__userIDs
        else:
            userID = [userID]

        for id in userID:
            try:
                self.__pyhik.NET_DVR_Logout(id)
            except Exception as err:
                pass
            finally:
                if userID in self.__userIDs:
                    self.__userIDs.remove(id)
                    self.__devInfo.pop(id)

    ####################################################
    ### 设备配置                                     ###
    ####################################################
    def get_ip_recource_config(self, userID, group):
        """
            获取IP设备资源及IP通道资源

        Parameters:
            userID : 用户ID号
            group  : 组号，从0开始，每组64个通道

        Exception:
            HikError.
        """

        ipResourceConfig = NET_DVR_IPPARACFG_V40()
        self.__pyhik.NET_DVR_GetDVRConfig(userID, NET_DVR_GET_IPPARACFG_V40, group, ipResourceConfig)
        return self.__struct2dict(ipResourceConfig)


    def get_decoder_config(self, userID, channel):
        """
            获取云台解码器参数

        Parameters:
            userID  : 用户ID号
            channel : 通道号

        Exception:
            HikError.
        """

        decoderConfig = NET_DVR_DECODERCFG_V40()
        self.__pyhik.NET_DVR_GetDVRConfig(userID, NET_DVR_GET_IPPARACFG_V40, channel, decoderConfig)
        return self.__struct2dict(decoderConfig)


    ####################################################
    ### 实时预览                                      ###
    ####################################################
    def start_realplay(self, userID, playWND, linkMode = 0, protoType = 0, callbackFunc = None, userData = None, blocked = True):
        """
            实时预览（支持多码流）。

        Parameters:
            userID          : 用户ID号
            playWND         : 播放窗口的句柄，为0表示不显示图像
            linkMode        : 最高位(31)为0表示主码流，为1表示子码流；0～30位表示连接方式：0－TCP方式，1－UDP方式，2－多播方式
            protoType       : 应用层取流协议，0-私有协议，1-RTSP协议
            callbackFunc    : 码流数据回调函数
            userData        : 用户数据
            blocked         : 请求码流过程是否阻塞：0－否；1－是

        Return
            lRealHandle : 预览句柄

        Exception:
            HikError.
        """

        lpClientInfo = NET_DVR_CLIENTINFO()
        lpClientInfo.lChannel = self.__devInfo[userID]["byStartChan"]
        lpClientInfo.lLinkMode = linkMode
        lpClientInfo.hPlayWnd = playWND
        lpClientInfo.byProtoType = protoType

        lRealHandle = self.__pyhik.NET_DVR_RealPlay_V30(userID, lpClientInfo, callbackFunc, userData, blocked)
        if lRealHandle not in self.__realHandles:
            self.__realHandles[userID] = lRealHandle
        return lRealHandle

    def stop_realplay(self, realHandle = None):
        """
            停止数据捕获。

        Parameters:
            lRealHandle : 预览句柄， 设置为None时，将全部已开启播放的设备全部登出。

        Exception:
            HikError.
        """

        if realHandle is None:
            realHandle = self.__realHandles
        else:
            realHandle = [realHandle]

        for handle in realHandle:
            try:
                self.__pyhik.NET_DVR_StopRealPlay(handle)
            except Exception as err:
                pass
            finally:
                if handle in self.__realHandles:
                    self.__realHandles.pop(handle)

    def get_realplay_index(self, realHandle):
        """
            获取预览时用来解码和显示的播放器句柄。

        Parameters:
            realHandle : 预览句柄

        Return
            portIndex : 播放句柄， 用户可以通过返回的句柄自行实现播放库SDK提供的其他功能

        Exception:
            HikError.
        """

        return self.__pyhik.NET_DVR_GetRealPlayerIndex(realHandle)

    def set_callback_func(self, realHandle, callbackFunc, userData):
        """
            注册回调函数，捕获实时码流数据。

        Parameters:
            realHandle      : 预览句柄
            callbackFunc    : 码流数据回调函数
            userData        : 用户数据

        Remarks:
            fCallBack回调函数中不能执行可能会占用时间较长的接口或操作，不建议调用该SDK（HCNetSDK.dll）本身的接口。
            此函数包括开始和停止用户处理SDK捕获的数据, 当回调函数cbRealDataCallBack设为非NULL值时，表示回调和处理数据,当设为NULL时表示停止回调和处理数据。
            回调的第一个包是40个字节的文件头，供后续解码使用，之后回调的是压缩的码流。回调数据最大为256K字节。

        Exception:
            HikError.
        """

        self.__pyhik.NET_DVR_SetRealDataCallBack(realHandle, callbackFunc, userData)


    ####################################################
    ### 录像                                         ###
    ####################################################
    def save_realdata(self, realHandle, fileName):
        """
            捕获数据并存放到指定的文件中

        Parameters:
            realHandle : 预览句柄
            fileName   : 文件路径指针，包括文件名，例如："D:\\test.mp4"

        Remarks:
            V5.0.3.2或以后版本，通过该接口保存录像，保存的录像文件数据超过文件最大限制字节数（默认为1024MB）
            SDK会自动切片，即新建文件进行保存，文件名命名规则为在接口传入的文件名基础上增加数字标识(例如：*_1.mp4、*_2.mp4)”。
            可以调用NET_DVR_GetSDKLocalCfg、NET_DVR_SetSDKLocalCfg(配置类型：NET_DVR_LOCAL_CFG_TYPE_GENERAL)获取和设置切片模式和文件最大限制字节数。

        Exception:
            HikError.
        """

        self.__pyhik.NET_DVR_SaveRealData(realHandle, fileName)

    def stop_save_realdata(self, realHandle):
        """
            停止数据捕获。

        Parameters:
            realHandle : 预览句柄

        Exception:
            HikError.
        """

        self.__pyhik.NET_DVR_StopSaveRealData(realHandle)


    ####################################################
    ### 抓图                                         ###
    ####################################################
    def capture_picture(self, realHandle, picFileName, captureMode = 0, timeout = None):
        """
            预览时，单帧数据捕获并保存成图片。

        Parameters:
            realHandle     : NET_DVR_RealPlay或NET_DVR_RealPlay_V30的返回值
            picFileName    : 保存图象的文件路径（包括文件名）。路径长度和操作系统有关，sdk不做限制，windows默认路径长度小于等于256字节（包括文件名在内）。
            captureMode    : 抓图模式  BMP_MODE - 0  JPEG_MODE - 1
            timeout        : 超时时间，目前无效

        Remarks：
            默认为BMP模式。
            如果抓图模式为BMP模式，抓取的是BMP图片，保存路径后缀应为.bmp，例如：sPicFileName="D:\\test.bmp"；如果抓图模式为JPEG模式，抓取的是JPEG图片，保存路径后缀应为.jpg，例如：sPicFileName="D:\\test.jpg"。
            若设备的当前分辨率为2CIF，播放库做了相关处理，抓取的图像为4CIF。
            调用NET_DVR_CapturePicture进行抓图，要求在调用NET_DVR_RealPlay_V40等接口时传入非空的播放句柄（播放库解码显示），否则时接口会返回失败，调用次序错误。

        Exception:
            HikError.
        """

        self.__pyhik.NET_DVR_SetCapturePictureMode(captureMode)

        if timeout is not None:
            self.__pyhik.NET_DVR_CapturePicture(realHandle, picFileName)
        else:
            self.__pyhik.NET_DVR_CapturePictureBlock(realHandle, picFileName, timeout)

    def capture_picture_without_realplay(self, userID, picFileName, picSize = 0, picQuality = 2):
        """
            没有启动实时预览时，单帧数据捕获并保存成JPEG图。

        Parameters:
            userID      : 用户ID号
            picFileName : 保存图象的文件路径（包括文件名）。路径长度和操作系统有关，sdk不做限制，windows默认路径长度小于等于256字节（包括文件名在内）。
            picSize     : JPEG图像分辨率
            picQuality  : 图像质量

        Remarks：
            该接口用于设备没有启动实时预览时的单帧数据捕获，并保存成JPEG图片文件。JPEG抓图功能或者抓图分辨率需要设备支持，如果不支持接口返回失败，错误号23或者29。

            注意：当图像压缩分辨率为VGA时，支持0=CIF, 1=QCIF, 2=D1抓图，
            当分辨率为3=UXGA(1600x1200), 4=SVGA(800x600), 5=HD720p(1280x720),6=VGA,7=XVGA, 8=HD900p 仅支持当前分辨率的抓图

            picQuality图片质量系数 0-最好 1-较好 2-一般

            对于DVR、NVR设备，参数picQuality支持的分辨率值可通过NET_DVR_GetDeviceAbility获取能力集类型PIC_CAPTURE_ABILITY获取(NET_DVR_COMPRESSIONCFG_ABILITY)得到。
            对接网络摄像机、门禁主机等设备，设备是否支持JPEG抓图功能或者支持的参数能力，可以通过设备能力集进行判断，
            对应设备JPEG抓图能力集(JpegCaptureAbility)，相关接口：NET_DVR_GetDeviceAbility，能力集类型：DEVICE_JPEG_CAP_ABILITY，节点：<ManualCapture>。
            picSize设为2抓取的图片分辨率是4CIF还是D1由设备决定，一般为4CIF(P制:704*576/N制:704*480)。

            可以通过能力集获取
            0-CIF，           1-QCIF，           2-D1，         3-UXGA(1600x1200), 4-SVGA(800x600),5-HD720p(1280x720)，
            6-VGA，           7-XVGA，           8-HD900p，     9-HD1080，     10-2560*1920，
            11-1600*304，     12-2048*1536，     13-2448*2048,  14-2448*1200， 15-2448*800，
            16-XGA(1024*768), 17-SXGA(1280*1024),18-WD1(960*576/960*480),      19-1080i,      20-576*576，
            21-1536*1536,     22-1920*1920,      23-320*240,    24-720*720,    25-1024*768,
            26-1280*1280,     27-1600*600,       28-2048*768,   29-160*120,    55-3072*2048,
            64-3840*2160,     70-2560*1440,      75-336*256,
            78-384*256,         79-384*216,        80-320*256,    82-320*192,    83-512*384,
            127-480*272,      128-512*272,       161-288*320,   162-144*176,   163-480*640,
            164-240*320,      165-120*160,       166-576*720,   167-720*1280,  168-576*960,
            180-180*240,      181-360*480,       182-540*720,    183-720*960,  184-960*1280,
            185-1080*1440,      215-1080*720(占位，未测试),  216-360x640(占位，未测试),245-576*704(占位，未测试)
            500-384*288,
            0xff-Auto(使用当前码流分辨率)

        Exception:
            HikError.
        """

        lpJpegPara = NET_DVR_JPEGPARA()
        lpJpegPara.wPicSize = picSize
        lpJpegPara.wPicQuality = picQuality

        self.__pyhik.NET_DVR_CaptureJPEGPicture(userID, self.__devInfo[userID]["byStartChan"], lpJpegPara, picFileName)


    ####################################################
    ### 云台控制                                     ###
    ####################################################
    def PTZ_control(self, userID, command, isStopped, speed = None):
        """
            云台控制操作。

        Parameters:
            userID      : 用户ID号
            command     : 云台控制命令
            isStopped   : 云台停止动作或开始动作：0－开始，1－停止
            speed       : 云台控制的速度，用户按不同解码器的速度控制值设置。取值范围[1,7], 设置为None，默认为最大速度

        Remarks:
            对云台实施的每一个动作都需要调用该接口两次，分别是开始和停止控制，由接口中的最后一个参数（isStopped）决定。在调用此接口之前需要先开启预览。
            与设备之间的云台各项操作的命令都对应于设备与云台之间的控制码，设备会根据目前设置的解码器种类和解码器地址向云台发送控制码。
            如果目前设备上设置的解码器与云台设备的不匹配，需要重新配置设备的解码器。
            如果云台设备所需的解码器设备不支持，则无法用该接口控制。
            云台默认以最大速度动作。

        Exception:
            HikError.
        """

        if userID in self.__realHandles:
            if speed is not None:
                self.__pyhik.NET_DVR_PTZControlWithSpeed(self.__realHandles[userID], command, isStopped, speed)
            else:
                self.__pyhik.NET_DVR_PTZControl(self.__realHandles[userID], command, isStopped)
        else:
            if speed is not None:
                self.__pyhik.NET_DVR_PTZControlWithSpeed_Other(userID, self.__devInfo[userID]["byStartChan"], command, isStopped, speed)
            else:
                self.__pyhik.NET_DVR_PTZControl_Other(userID, self.__devInfo[userID]["byStartChan"], command, isStopped)


    ####################################################
    ### 云台预置点                                   ###
    ####################################################
    def PTZ_preset(self, userID, command, index):
        """
            云台预置点操作。

        Parameters:
            userID      : 用户ID号
            command     : 操作云台预置点命令 SET_PRESET = 8  设置预置点 CLE_PRESET = 9  清除预置点 GOTO_PRESET = 39  转到预置点
            index       : 预置点的序号（从1开始），最多支持300个预置点

        Remarks:
            与设备之间的云台各项操作的命令都对应于设备与云台之间的控制码，设备会根据目前设置的解码器种类和解码器地址向云台发送控制码。
            如果目前设备上设置的解码器与云台设备的不匹配，需要重新配置设备的解码器。如果云台设备所需的解码器设备不支持，则无法用该接口控制。

        Exception:
            HikError.
        """

        if userID in self.__realHandles:
            self.__pyhik.NET_DVR_PTZPreset(self.__realHandles[userID], command, index)
        else:
            self.__pyhik.NET_DVR_PTZPreset_Other(userID, self.__devInfo[userID]["pyStartChan"], command, index)

    def get_PTZ_preset_list(self, userID, timeout = 3000):
        """
            获取预置点列表。

        Parameters:
            userID      : 用户ID号
            timeout     : 接收超时时间，单位：ms，填0则使用默认超时5s

        Exception:
            HikError.
        """

        buffer = ""
        lpInputParam = NET_DVR_XML_CONFIG_INPUT()
        lpInputParam.dwSize = sizeof(lpInputParam)
        lpInputParam.lpRequestUrl = cast(CHARP(bytes("GET /ISAPI/PTZCtrl/channels/1/presets", encoding='utf8')), VOIDP)
        lpInputParam.dwRequestUrlLen = 256
        lpInputParam.dwRecvTimeOut = timeout

        lpOutputParam = NET_DVR_XML_CONFIG_OUTPUT()
        lpOutputParam.dwSize = sizeof(lpOutputParam)
        lpOutputParam.lpOutBuffer = cast(CHARP(bytes(buffer, encoding='utf8')), VOIDP)
        lpOutputParam.dwOutBufferSize = 1024*300

        self.__pyhik.NET_DVR_STDXMLConfig(userID, lpInputParam, lpOutputParam)



    ####################################################
    ### 云台巡航                                     ###
    ####################################################
    def PTZ_cruise(self, userID, command, route, point, input):
        """
            云台巡航操作。

        Parameters:
            userID  : 用户ID号
            command : 操作云台巡航命令
            route   : 巡航路径，最多支持32条路径（序号从1开始）
            point   : 巡航点，最多支持32个点（序号从1开始）
            input   : 不同巡航命令时的值不同，预置点(最大300)、时间(最大255)、速度(最大40)

        Remarks:
            与设备之间的云台各项操作的命令都对应于设备与云台之间的控制码，设备会根据目前设置的解码器种类和解码器地址向云台发送控制码。
            如果目前设备上设置的解码器与云台设备的不匹配，需要重新配置设备的解码器。如果云台设备所需的解码器设备不支持，则无法用该接口控制。

        Exception:
            HikError.
        """

        if userID in self.__realHandles:
            self.__pyhik.NET_DVR_PTZCruise(self.__realHandles[userID], command, route, point, input)
        else:
            self.__pyhik.NET_DVR_PTZCruise_Other(userID, self.__devInfo[userID]["pyStartChan"], command, route, point, input)


    ####################################################
    ### 云台轨迹                                     ###
    ####################################################
    def PTZ_track(self, userID, command):
        """
            云台轨迹操作。

        Parameters:
            userID  : 用户ID号
            command : 操作云台轨迹命令

        Remarks:
            与设备之间的云台各项操作的命令都对应于设备与云台之间的控制码，设备会根据目前设置的解码器种类和解码器地址向云台发送控制码。
            如果目前设备上设置的解码器与云台设备的不匹配，需要重新配置设备的解码器。如果云台设备所需的解码器设备不支持，则无法用该接口控制。

        Exception:
            HikError.
        """
        if userID in self.__realHandles:
            self.__pyhik.NET_DVR_PTZTrack(self.__realHandles[userID], command)
        else:
            self.__pyhik.NET_DVR_PTZTrack_Other(userID, self.__devInfo[userID]["pyStartChan"], command)



    ####################################################
    ### 其他                                         ###
    ####################################################
    def __struct2dict(self, struct):
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








