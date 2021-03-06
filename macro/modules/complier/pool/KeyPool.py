
class KeyPool:

    def initKeyList(self):
        self.__mouseKeyList=[
        '左键',
        '右键',
        '中键'
        ]
        self.__keyList=[
        'Cancel',
        '取消',
        'Backspace',
        '后退',
        'Tab',
        'Clear',
        'Enter',
        '回车',
        'Shift',
        '左shift',
        'Control',
        '左控制',
        'alt',
        'Alt',
        '左alt',
        'Pause',
        '暂停',
        'CapsLock',
        '大小写',
        'Esc',
        '返回',
        'Space',
        '空格',
        'PgUp',
        'PgDn',
        'End',
        'Home',
        'Left',
        '左',
        'Up',
        '上',
        'Right',
        '右',
        'Down',
        '下',
        'Select',
        '选择',
        'Print',
        '打印',
        'Execute',
        '执行',
        'PrintScreen',
        '打印屏幕',
        'Ins',
        '插入',
        'Del',
        '删除',
        'Help',
        '帮助',
        '左0',
        '左1',
        '左2',
        '左3',
        '左4',
        '左5',
        '左6',
        '左7',
        '左8',
        '左9',
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z',
        'Numpad0',
        '0',
        '右0',
        'Numpad1',
        '1',
        '右1',
        'Numpad2',
        '2',
        '右2',
        'Numpad3',
        '3',
        '右3',
        'Numpad4',
        '4',
        '右4',
        'Numpad5',
        '5',
        '右5',
        'Numpad6',
        '6',
        '右6',
        'Numpad7',
        '7',
        '右7',
        'Numpad8',
        '8',
        '右8',
        'Numpad9',
        '9',
        '右9',
        'MultiplyKey',
        '乘',
        'AddKey',
        '加',
        'SeparatorKey',
        '分隔',
        'SubtractKey',
        '减',
        'DecimalKey',
        '小数',
        'DivideKey',
        '除以',
        'F1',
        'F2',
        'F3',
        'F4',
        'F5',
        'F6',
        'F7',
        'F8',
        'F9',
        'F10',
        'F11',
        'F12',
        'F13',
        'F14',
        'F15',
        'F16',
        'F17',
        'F18',
        'F19',
        'F20',
        'F21',
        'F22',
        'F23',
        'F24',
        'NumLock',
        'ScrollLock',
        'Lshift',
        'Rshift',
        'Lcontrol',
        'Rcontrol',
        'Lmenu',
        'Rmenu',
        'BrowserBack',
        'BrowserForward',
        'BrowserRefresh',
        'BrowserStop',
        'BrowserSearch',
        'BrowserFavorites',
        'BrowserStart_and_home',
        'VolumeMute',
        'VolumeDown',
        'VolumeUp',
        'NextTrack',
        'PreviousTrack',
        'StopMedia',
        'PlayMedia',
        'PauseMedia',
        'StartMail',
        'SelectMedia',
        'StartApplication1',
        'StartApplication2',
        'AttnKey',
        'CrselKey',
        'ExselKey',
        'PlayKey',
        'ZoomKey',
        'ClearKey',
        '+',
        ',',
        '-',
        '.',
        '/',
        '`',
        ';',
        '[',
        '\\',
        ']',
        '\''
        ] 
        
        self.__keyMappingList={
        'backspace':'backspace',
        'Backspace':'backspace',
        '后退':'backspace',
        'tab':'tab',
        'Tab':'tab',

        'clear':'clear',
        'Clear':'clear',
        'enter':'enter',
        'Enter':'enter',
        '回车':'enter',
        'shift':'shift',
        'Shift':'shift',
        'ctrl':'ctrl',
        'Ctrl':'ctrl',
        'Control':'ctrl',
        'alt':'alt',
        'Alt':'alt',
        'pause':'pause',
        'Pause':'pause',
        
        'caps_lock':'caps_lock',
        'CapsLock':'caps_lock',
        '大小写':'caps_lock',
        'esc':'esc',
        'Esc':'esc',

        'space':'spacebar',
        'Space':'spacebar',
        '空格':'spacebar',
        'page_up':'page_up',
        'PgUp':'page_up',

        'page_down':'page_down',
        'PgDn':'page_down',

        'end':'end',
        'End':'end',

        'home':'home',
        'Home':'home',


        'left_arrow':'left_arrow',
        'Left':'left_arrow',
        
        'up_arrow':'up_arrow',
        'Up':'up_arrow',

        'right_arrow':'right_arrow',
        'Right':'right_arrow',

        'down_arrow':'down_arrow',
        'Down':'down_arrow',

        'select':'select',
        'Select':'select',

        'print':'print',
        'Print':'print',

        'execute':'execute',
        'Execute':'execute',

        'print_screen':'print_screen',
        'PrintScreen':'print_screen',

        'ins':'ins',
        'Ins':'ins',

        'del':'del',
        'Del':'del',

        'help':'help',
        'Help':'help',
        '0':'0',
        '1':'1',
        '2':'2',
        '3':'3',
        '4':'4',
        '5':'5',
        '6':'6',
        '7':'7',
        '8':'8',
        '9':'9',
        'a':'a',
        'b':'b',
        'c':'c',
        'd':'d',
        'e':'e',
        'f':'f',
        'g':'g',
        'h':'h',
        'i':'i',
        'j':'j',
        'k':'k',
        'l':'l',
        'm':'m',
        'n':'n',
        'o':'o',
        'p':'p',
        'q':'q',
        'r':'r',
        's':'s',
        't':'t',
        'u':'u',
        'v':'v',
        'w':'w',
        'x':'x',
        'y':'y',
        'z':'z',
        'numpad_0':'numpad_0',
        'Numpad0':'numpad_0',
        'numpad_1':'numpad_1',
        'Numpad1':'numpad_1',
        'numpad_2':'numpad_2',
        'Numpad2':'numpad_2',
        'numpad_3':'numpad_3',
        'Numpad3':'numpad_3',
        'numpad_4':'numpad_4',
        'Numpad4':'numpad_4',
        'numpad_5':'numpad_5',
        'Numpad5':'numpad_5',
        'numpad_6':'numpad_6',
        'Numpad6':'numpad_6',
        'numpad_7':'numpad_7',
        'Numpad7':'numpad_7',
        'numpad_8':'numpad_8',
        'Numpad8':'numpad_8',
        'numpad_9':'numpad_9',
        'Numpad9':'numpad_9',


        'multiply_key':'multiply_key',
        'MultiplyKey':'multiply_key',
        'add_key':'add_key',
        'AddKey':'add_key',
        'separator_key':'separator_key',
        'SeparatorKey':'separator_key',

        'subtract_key':'subtract_key',
        'SubtractKey':'subtract_key',
        'decimal_key':'decimal_key',
        'DecimalKey':'decimal_key',
        'divide_key':'divide_key',
        'DivideKey':'divide_key',
        'F1':'F1',
        'F2':'F2',
        'F3':'F3',
        'F4':'F4',
        'F5':'F5',
        'F6':'F6',
        'F7':'F7',
        'F8':'F8',
        'F9':'F9',
        'F10':'F10',
        'F11':'F11',
        'F12':'F12',
        'F13':'F13',
        'F14':'F14',
        'F15':'F15',
        'F16':'F16',
        'F17':'F17',
        'F18':'F18',
        'F19':'F19',
        'F20':'F20',
        'F21':'F21',
        'F22':'F22',
        'F23':'F23',
        'F24':'F24',
        'num_lock':'num_lock',
        'NumLock':'num_lock',
        'scroll_lock':'scroll_lock',
        'ScrollLock':'scroll_lock',
        'left_shift':'left_shift',
        'Lshift':'left_shift',
        'right_shift ':'right_shift ',
        'Rshift':'right_shift ',
        'left_control':'left_control',
        'Lcontrol':'left_control',
        'right_control':'right_control',
        'Rcontrol':'right_control',
        'left_menu':'left_menu',
        'Lmenu':'left_menu',
        'right_menu':'right_menu',
        'Rmenu':'right_menu',
        'browser_back':'browser_back',
        'BrowserBack':'browser_back',
        'browser_forward':'browser_forward',
        'BrowserForward':'browser_forward',
        'browser_refresh':'browser_refresh',
        'BrowserRefresh':'browser_refresh',
        'browser_stop':'browser_stop',
        'BrowserStop':'browser_stop',
        'browser_search':'browser_search',
        'BrowserSearch':'browser_search',
        'browser_favorites':'browser_favorites',
        'BrowserFavorites':'browser_favorites',
        'browser_start_and_home':'browser_start_and_home',
        'BrowserStart_and_home':'browser_start_and_home',
        'volume_mute':'volume_mute',
        'VolumeMute':'volume_mute',
        'volume_Down':'volume_Down',
        'VolumeDown':'volume_Down',
        'volume_up':'volume_up',
        'VolumeUp':'volume_up',
        'next_track':'next_track',
        'NextTrack':'next_track',
        'previous_track':'previous_track',
        'PreviousTrack':'previous_track',
        'stop_media':'stop_media',
        'StopMedia':'stop_media',

        'play/pause_media':'play/pause_media',
        'PlayMedia':'play/pause_media',
        'PauseMedia':'play/pause_media',

        'start_mail':'start_mail',
        'StartMail':'start_mail',
        'select_media':'select_media',
        'SelectMedia':'select_media',
        'start_application_1':'start_application_1',
        'StartApplication_1':'start_application_1',
        'start_application_2':'start_application_2',
        'StartApplication_2':'start_application_2',
        'attn_key':'attn_key',
        'AttnKey':'attn_key',
        'crsel_key':'crsel_key',
        'CrselKey':'crsel_key',
        'exsel_key':'exsel_key',
        'ExselKey':'exsel_key',
        'play_key':'play_key',
        'PlayKey':'play_key',
        'zoom_key':'zoom_key',
        'ZoomKey':'zoom_key',
        'clear_key':'clear_key',
        'ClearKey':'clear_key',

         '+':'+',
         ',':',',
         '-':'-',
         '.':'.',
         '/':'/',
         '`':'`',
         ';':';',
         '[':'[',
         '\\':'\\',
         ']':']',
         '\'':'\''
        }
    def __init__(self):
        self.initKeyList()

    def judge(self,keyName):
        return keyName in self.__keyList


    def convert(self,str):
        if(self.__keyMappingList.__contains__(str)):
            return self.__keyMappingList[str]
        else:
            return str
