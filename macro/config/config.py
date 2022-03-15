# -*- coding:utf-8 -*-
import os
import sys

class Config:
    logging_dir = os.path.join(os.path.dirname(__file__), '../logs')
    log_config = dict(
        handlers=[
            dict(sink=os.path.join(logging_dir, "info.log"),
                 # serialize=True,
                 format="[{time}:{function}:{line}] {message}",
                 level='INFO',
                 colorize=True,
                 rotation='1 day',
                 retention='7 day',
                 encoding='utf-8',
                 ),
            dict(sink=sys.stderr,
                 # serialize=True,
                 format="[{time}:{function}:{line}] {message}",
                 level='INFO',
                 colorize=True,
                 ),

            dict(sink=os.path.join(logging_dir, "error.log"),
                 # serialize=True,
                 format="[{time}:{function}:{line}] {message}",
                 level='WARNING',
                 colorize=True,
                 rotation='1 day',
                 retention='7 day',
                 encoding='utf-8',
                 ),
        ]
    )


def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


# UI界面要用
TMP_DIR = ""
WATCHING = 10
EDITING = 20
SETTING = 30

# Hook文件使用
LEFT_ONCE = 1000
RIGHT_ONCE = 1001
LEFT_DOWN = 1002
LEFT_UP = 1003
RIGHT_DOWN = 1004
RIGHT_UP = 1005
WHEEL = 1006
MOVE = 1007

IS_RUNNING = 0

KEY_ALT_DOWN = 260
KEY_DOWN = 256
KEY_UP = 257

# UI 与 各界面交互时 使用
STOP = 1008
RECORDING = 1009

# 设置参数
MOUSE_ACCURACY = 0
DELAY_ACCURACY = 0
IMAGE_ACCURACY = 90
DELETE_TIME_ACCURACY = 400

ORIGIN_MOUSE_ACCURACY = 0
ORIGIN_DELAY_ACCURACY = 0
ORIGIN_IMAGE_ACCURACY = 90

# 排序
NAMESORT_ZHENG = 1
NAMESORT_FAN = 2
TIMESORT_ZHENG = 3
TIMESORT_FAN = 4

# 录音文件
VOICE_RECORD_RECORDING = 3000
VOICE_RECORD_STOP = 4000

# 当前存储文件的名字
TMP_FILE_PATH = ""


# 编辑器要用的宏定义
SAVE_AND_TELL_ME = -10
SAVE_DONT_TELL_ME = -11
SAVE_AND_CHECK = -12
SAVE_AND_EXE = -13

# 编译器和控制类
CHECK = 10
CHECK_GOOD_MES = "GOOD_CHECK"
CHECK_BAD_MES = "BAD_CHECK"

MODIFY = 20
MODIFY_GOOD_MES = "GOOD_MODIFY"

EXECUTE = 30


{
    "refresh_token": "25.954fd2ae1cc25cd896629bb29536e761.315360000.1933751274.282335-23980846",
    "expires_in": 2592000,
    "session_key": "9mzdA5x1uAcbIlsWAAc4lWRi\/2OcvnNDjBiAQsfljXFqEESjTNpkkr0QfC\/18ERhLiBcgtUKwYLehsWfiuv74lVlhL7IIA==",
    "access_token": "24.865801bc4a50405cc6e4dca67a0d11d5.2592000.1620983274.282335-23980846",
    "scope": "audio_voice_assistant_get brain_enhanced_asr audio_tts_post brain_speech_realtime public brain_all_scope picchain_test_picchain_api_scope brain_asr_async wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test\u6743\u9650 vis-classify_flower lpq_\u5f00\u653e cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base smartapp_mapp_dev_manage iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi fake_face_detect_\u5f00\u653eScope vis-ocr_\u865a\u62df\u4eba\u7269\u52a9\u7406 idl-video_\u865a\u62df\u4eba\u7269\u52a9\u7406 smartapp_component smartapp_search_plugin avatar_video_test",
    "session_secret": "8bce754c450b580455b160853b0a0e74"
}

# 编译器模块要用的
VK_CODE = {
    'backspace': 0x08,
    'tab': 0x09,
    'clear': 0x0C,
    'enter': 0x0D,
    'shift': 0x10,
    'ctrl': 0x11,
    'alt': 0x12,
    'pause': 0x13,
    'caps_lock': 0x14,
    'esc': 0x1B,
    'spacebar': 0x20,
    'page_up': 0x21,
    'page_down': 0x22,
    'end': 0x23,
    'home': 0x24,
    'left_arrow': 0x25,
    'up_arrow': 0x26,
    'right_arrow': 0x27,
    'down_arrow': 0x28,
    'select': 0x29,
    'print': 0x2A,
    'execute': 0x2B,
    'print_screen': 0x2C,
    'ins': 0x2D,
    'del': 0x2E,
    'help': 0x2F,
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    'a': 0x41,
    'b': 0x42,
    'c': 0x43,
    'd': 0x44,
    'e': 0x45,
    'f': 0x46,
    'g': 0x47,
    'h': 0x48,
    'i': 0x49,
    'j': 0x4A,
    'k': 0x4B,
    'l': 0x4C,
    'm': 0x4D,
    'n': 0x4E,
    'o': 0x4F,
    'p': 0x50,
    'q': 0x51,
    'r': 0x52,
    's': 0x53,
    't': 0x54,
    'u': 0x55,
    'v': 0x56,
    'w': 0x57,
    'x': 0x58,
    'y': 0x59,
    'z': 0x5A,
    'numpad_0': 0x60,
    'numpad_1': 0x61,
    'numpad_2': 0x62,
    'numpad_3': 0x63,
    'numpad_4': 0x64,
    'numpad_5': 0x65,
    'numpad_6': 0x66,
    'numpad_7': 0x67,
    'numpad_8': 0x68,
    'numpad_9': 0x69,
    'multiply_key': 0x6A,
    'add_key': 0x6B,
    'separator_key': 0x6C,
    'subtract_key': 0x6D,
    'decimal_key': 0x6E,
    'divide_key': 0x6F,
    'F1': 0x70,
    'F2': 0x71,
    'F3': 0x72,
    'F4': 0x73,
    'F5': 0x74,
    'F6': 0x75,
    'F7': 0x76,
    'F8': 0x77,
    'F9': 0x78,
    'F10': 0x79,
    'F11': 0x7A,
    'F12': 0x7B,
    'F13': 0x7C,
    'F14': 0x7D,
    'F15': 0x7E,
    'F16': 0x7F,
    'F17': 0x80,
    'F18': 0x81,
    'F19': 0x82,
    'F20': 0x83,
    'F21': 0x84,
    'F22': 0x85,
    'F23': 0x86,
    'F24': 0x87,
    'num_lock': 0x90,
    'scroll_lock': 0x91,
    'left_shift': 0xA0,
    'right_shift ': 0xA1,
    'left_control': 0xA2,
    'right_control': 0xA3,
    'left_menu': 0xA4,
    'right_menu': 0xA5,
    'browser_back': 0xA6,
    'browser_forward': 0xA7,
    'browser_refresh': 0xA8,
    'browser_stop': 0xA9,
    'browser_search': 0xAA,
    'browser_favorites': 0xAB,
    'browser_start_and_home': 0xAC,
    'volume_mute': 0xAD,
    'volume_Down': 0xAE,
    'volume_up': 0xAF,
    'next_track': 0xB0,
    'previous_track': 0xB1,
    'stop_media': 0xB2,
    'play/pause_media': 0xB3,
    'start_mail': 0xB4,
    'select_media': 0xB5,
    'start_application_1': 0xB6,
    'start_application_2': 0xB7,
    'attn_key': 0xF6,
    'crsel_key': 0xF7,
    'exsel_key': 0xF8,
    'play_key': 0xFA,
    'zoom_key': 0xFB,
    'clear_key': 0xFE,
    '+': 0xBB,
    ',': 0xBC,
    '-': 0xBD,
    '.': 0xBE,
    '/': 0xBF,
    '`': 0xC0,
    ';': 0xBA,
    '[': 0xDB,
    '\\': 0xDC,
    ']': 0xDD,
    "'": 0xDE,
    '`': 0xC0
}
