       #  delay = s[i][0]
      #      event_type = s[i][1].upper()
     #       message = s[i][2].lower()
    #        action = s[i][3]
import re
from win32 import win32api
from win32.lib import win32con
from win32 import win32gui
from os import path
# from typing import final


class codetransfer:
    def init_keyword_list(self):
        self.keyword_list=['延迟','鼠标','左移','上移','下移','右移','左键','右键','上滚轮','下滚轮','双击','拖动','移动到','松开','横坐标','纵坐标','键盘','(.*?)键','按下','持续','起点','终点','定义','变量','为','令','加','减','乘','除以','大于','小于','等于','不是','而且','或者','左括号','右括号','如果','那么','否则','条件结束','循环开始','直到','当','循环结束','继续','退出循环','退出所有循环','and','not','or','(',')','+','-','*','/','=','>','<','==','=','画面','图中','图的','文字中','图存在于','pic_in','文字存在于','words_in','打印','输出','中键','的数字','左上角','右下角','连点器','次','间隔','等待图','出现']
        self.begin_keyword_list=['延迟','鼠标','键盘','定义','令','如果','那么','否则','条件结束','循环开始','直到','当','循环结束','继续','退出循环','退出所有循环','打印','输出','连点器','等待图']     
        self.operator_unmapping_keyword_list=['加','减','乘','除以']  
        self.cmpoper_unmapping_keyword_list=['小于','大于','等于','小于等于','大于等于','不是','而且','或者']
        self.prioper_unmapping_keyword_list=['左括号','右括号']
        self.picoperator_unmapping_keyword_list=['图存在于']
        self.word_picoperator_unmapping_keyword_list=['文字存在于']

        #self.oper_list=self.operator_unmapping_keyword_list+self.cmpoper_unmapping_keyword_list+self.prioper_unmapping_keyword_list+self.picoperator_unmapping_keyword_list+self.word_picoperator_unmapping_keyword_list+self.special_keyword_list+self.cmpoper_keyword_list+self.operator_keyword_list+self.prioper_keyword_list+self.picoperator_keyword_list+self.word_picoperator_keyword_list

        self.special_keyword_list=['>=','<=','==','小于等于','大于等于']
        self.cmpoper_keyword_list=['<','>','==','>=','<=','not','and','or']
        self.operator_keyword_list=['+','-','*','/']
        self.prioper_keyword_list=['(',')']
        self.picoperator_keyword_list=['pic_in','words_in']
        self.word_picoperator_keyword_list=['words_in']
        self.var_num_list=[]
        self.area_num=0
        self.error_list=[]
        self.const_list=['画面']
    def init_command_list(self):
        self.command_list=[
        r'延迟 (.*?)$',
        r'鼠标 左移 (.*?)$',
        r'鼠标 右移 (.*?)$',
        r'鼠标 上移 (.*?)$',
        r'鼠标 下移 (.*?)$',
        r'鼠标 上滚轮 (.*?)$',
        r'鼠标 下滚轮 (.*?)$',        
        r'鼠标 左键 点击$',
        r'鼠标 中键 点击$',
        r'鼠标 右键 点击$',
        r'鼠标 左键 双击$',
        r'鼠标 中键 双击$',
        r'鼠标 右键 双击$',
        r'鼠标 左键 按下$',
        r'鼠标 中键 按下$',
        r'鼠标 右键 按下$',        
        r'鼠标 左键 松开$',
        r'鼠标 中键 松开$',
        r'鼠标 右键 松开$',
        r'鼠标 左键 拖动 起点 横坐标 \d+ 纵坐标 \d+ 终点 横坐标 \d+ 纵坐标 \d+$',
        r'鼠标 右键 拖动 起点 横坐标 \d+ 纵坐标 \d+ 终点 横坐标 \d+ 纵坐标 \d+$',
       # r'鼠标 左键 拖动$',
       # r'鼠标 右键 拖动$',
        r'鼠标 移动到 横坐标 (.*?) 纵坐标 (.*?)$',
        r'鼠标 移动到 画面 (.*?) 图中',
 
        r'鼠标 移动到 (.*?) 图的 (.*?) 图中',
        r'鼠标 移动到 画面 (.*?) 文字中',

        r'鼠标 移动到 (.*?) 图的 (.*?) 文字中',
        r'键盘 按下 (.*?)键 持续 \d+$',
        r'键盘 按下 (.*?)键$',
        r'键盘 松开 (.*?)键$',
        r'定义 (.*?) 变量 (.*?)$',
        r'定义 (.*?) 变量 (.*?) 为 (.*?)$',
        r'定义 (.*?) 变量 (.*?) = (.*?)$',
        r'令 (.*?) 为 (.*?)$',
        r'令 (.*?) = (.*?)$',
        r'如果 (.*?)$',
        r'那么$',
        r'否则$',
        r'条件结束$',
        r'循环开始$',
        r'直到 (.*?)$',
        r'当 (.*?)$',
        r'循环结束',
        r'继续$',
        r'退出循环$',
        r'退出所有循环$',
        r'打印 (.*?)$',
        r'输出 (.*?)$',
        r'连点器 (.*?) 次 横坐标 (.*?) 纵坐标 (.*?) 左键 间隔 (.*?)$',
        r'连点器 (.*?) 次 横坐标 (.*?) 纵坐标 (.*?) 右键 间隔 (.*?)$',
        r'等待图 (.*?) 出现$'
        ]
        self.command_get_key_list=[
        r'键盘 按下 (.*?) 键 ',
        r'键盘 按下 (.*?) 键$',
        r'键盘 松开 (.*?) 键$'
        ]
        self.command_def_strvar=[
        r'定义 字符串 变量'
        ]
        self.command_branch_list=[
        r'如果 (.*?)$',
        r'那么$',
        r'否则$',
        r'条件结束$'        
        ]
        self.command_loop_list=[
        r'循环开始$',
        r'直到 (.*?)$',
        r'当 (.*?)$',
        r'循环结束',
        ]
        self.one_para_list=[
        r'延迟 (.*?)$',
        r'鼠标 左移 (.*?)$',
        r'鼠标 右移 (.*?)$',
        r'鼠标 上移 (.*?)$',
        r'鼠标 下移 (.*?)$',
        r'鼠标 上滚轮 (.*?)$',
        r'鼠标 下滚轮 (.*?)$',
        ]
        self.one_para_ari_str_list=[
        r'输出 (.*?)$'
        ]
        self.get_pos=r'鼠标 移动到 横坐标 (.*?) 纵坐标 (.*?)$'
        self.get_spic=r'鼠标 移动到 画面 (.*?) 图中$'
        self.get_lpic_spic=r'鼠标 移动到 (.*?) 图的 (.*?) 图中$'

        self.get_word=r'鼠标 移动到 画面 (.*?) 文字中$'
        self.get_lpic_word=r'鼠标 移动到 (.*?) 图的 (.*?) 文字中$'
  

        self.get_spic_bool=r'(.*?) 存在于 画面$'
        self.get_spic_lpic_bool=r'(.*?) 存在于 (.*?)$'
        self.get_int_from_pic=r'画面 左上角 横坐标 (.*?) 纵坐标 (.*?) 右下角 横坐标 (.*?) 纵坐标 (.*?) 的数字$'
        self.get_left_click_fun=r'连点器 (.*?) 次 横坐标 (.*?) 纵坐标 (.*?) 左键 间隔 (.*?)$'
        self.get_right_click_fun=r'连点器 (.*?) 次 横坐标 (.*?) 纵坐标 (.*?) 右键 间隔 (.*?)$'
        self.get_wait_pic=r'等待图 (.*?) 出现$'
    def init_key_list(self):
        self.mouse_key_list=[
        '左键',
        '右键',
        '中键'
        ]
        self.key_list=[
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
    
    def init_transfer_list(self):
        self.equipment=[]
        self.equipment_list=[
        r'鼠标$',
        r'键盘$',
        r'定义$',
        r'令',
        r'如果',
        r'那么',
        r'否则',
        r'条件结束',
        r'继续$',
        r'退出循环$',
        r'循环开始$',
        r'直到$',
        r'当$',
        r'循环结束$',
        r'退出所有循环$',
        r'输出$'        
        ]
        self.part=[]
        self.part_list=[
        r'上滚轮$',
        r'下滚轮$',
        r'左键$',
        r'右键$',
        r'中键$',
        r'(.*?)键$'
        ]        
        self.action=[]
        self.action_list=[
        r'延迟$',
        r'左移$',
        r'右移$',
        r'上移$',
        r'下移$',
        r'点击$',
        r'双击$',
        r'松开$',
        r'按下$',
        r'按下$',
        r'拖动$',
        r'移动到$'
        ]
        self.parameters=[]
        self.top=0

    def init_exp(self):
        self.exp=''
    def init_variable_list(self):
        self.var_type_list=[
        '图片',
        '整型',
        '字符串',
        '布尔型'
        ]
        self.var_type_num=4
        #self.varpic_list=[]
        #self.varint_list=[]
        #self.varstr_list=[]
        #self.varbool_list=[]
        self.var_list=[]
        for i in range (self.var_type_num):
            self.var_list.append([])
        self.boolean_list=[
        '真',
        '非',
        'true',
        'false'
        ]
        self.get_var_type=r'定义 (.*?) 变量'
        self.get_var_val=r'变量 (.*?)$'
        self.get_ass_list=[r"令 (.*?) 为",r"令 (.*?) ="]
   
    def init_mapping_list(self):
        self.operator_mapping_list={
        '加':'+',
        '减':'-',
        '乘':'*',
        '除以':'/',
        }
        self.special_keyword_mapping_list={
        '小于等于':'小于  等于',
        '<=':'<  =',
        '大于等于':'大于  等于',
        '>=':'>  =',
        '==':'=  ='
        }
        self.cmpoper_mapping_list={
        '小于':'<',
        '大于':'>',
        '等于':'==',
        '小于等于':'<=',
        '大于等于':'>=',
        '而且':'and',
        '不是':'not',
        '或者':'or'
        }        
        self.var_mapping_list={
        '图片':0,
        '整型':1,
        '字符串':2,
        '布尔型':3            
        }
        self.boolean_mapping_list={
        '真':'true',
        '非':'false',
        'true':'true',
        'false':'false'
        }
        self.prioper_mapping_list={
        '左括号':'(',
        '右括号':')',
        '(':'(',
        ')':')'
        }
        self.picoperator_mapping_list={
        '图存在于':'pic_in',
        '文字存在于':'words_in'
        }
        self.prioper_count={
        '左括号':1,
        '右括号':-1,
        '(':1,
        ')':-1
        }
        self.key_mapping_list={
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
        
    def __init__(self,script_path):
        self.file_path=script_path
        #f=open(config.TMP_DIR + "\macro\modules\complier\grammar.txt",'w',encoding='utf8')

        self.init_keyword_list()
        self.init_command_list()
        self.init_key_list()
        self.init_transfer_list()
        self.init_variable_list()
        self.init_mapping_list()
        self.init_exp()
        self.stage=[]
        self.space=[]

    def modify1(self):
        self.codetxt=open(self.file_path, 'r', encoding='utf8').read()
        self.space=[]
        self.codetxt=self.codetxt.replace('，','')
        self.codetxt=self.codetxt.replace('\n','')
        self.codetxt=self.codetxt.strip(' ')
        for line in self.begin_keyword_list:
            self.codetxt=self.codetxt.replace(line,'\n'+line)

        self.codetxt=self.codetxt.strip('\n')    
        self.user_command_list=self.codetxt.split('\n')
        i=0
        for line1 in self.user_command_list:
            #line1=line1.lower()
            for line2 in self.keyword_list:
                line1=line1.replace(line2,' '+line2+' ')
            for line2 in self.special_keyword_list:
                line1=line1.replace(self.special_keyword_mapping_list[line2],line2)

            line2=line2.replace('= =','==')
            if(line1.find('字符串')>0 and line1.find('为')>0):
                temp=line1.find('为')
                stemp=line1[temp+2:]
                line1=line1[:temp+2]+stemp.replace(' ','')
            if(line1.find('字符串')>0 and line1.find('=')>0):
                temp=line1.find('=')
                stemp=line1[temp+2:]
                line1=line1[:temp+2]+stemp.replace(' ','')

            while(line1!=line1.replace('  ',' ')):
                line1=line1.replace('  ',' ')
            line1=line1.strip(' ')
            
            self.user_command_list[i]=line1
            i+=1
        #print(self.user_command_list)
        i=0
        cnt=0
        for line1 in self.user_command_list:
            self.space.append(cnt)
            temp=line1.split(' ')

            if(len(temp)!=0):
                if(temp[0]=='如果' or temp[0]=='循环开始' or temp[0]=='当'):
                    cnt+=1
                if(temp[0]=='那么' or temp[0]=='否则'):
                    self.space[i]-=1
                if(temp[0]=='条件结束'or temp[0]=='直到' or temp[0]=='循环结束'):
                    cnt-=1
                    self.space[i]=cnt
          
            i+=1
            

      
    def modified_file(self):
        self.modify1()
        i = 0
        f = open(self.file_path, 'w', encoding='utf-8')
        for line1 in self.user_command_list:
            print(self.space[i]*'    '+line1,file=f)
            i+=1
        f.close()
        return True


    def modify2(self):
        self.user_command_list=open(self.file_path, 'r', encoding='utf8').readlines()
        i=0
        print(self.user_command_list)
        for line1 in self.user_command_list:
            line1=line1.replace('\n','')
            if(line1.find('#')>=0):
                temp=line1.find('#')
                line1=line1[:temp]
            for line2 in self.keyword_list:
                line1=line1.replace(line2,' '+line2+' ')
            for line2 in self.special_keyword_list:
                line1=line1.replace(self.special_keyword_mapping_list[line2],line2)


            line2=line2.replace('= =','==')
            if(line1.find('字符串')>0 and line1.find('为')>0):
                temp=line1.find('为')
                stemp=line1[temp+2:]
                line1=line1[:temp+2]+stemp.replace(' ','')
            if(line1.find('字符串')>0 and line1.find('=')>0):
                temp=line1.find('=')
                stemp=line1[temp+2:]
                line1=line1[:temp+2]+stemp.replace(' ','')

            while(line1!=line1.replace('  ',' ')):
                line1=line1.replace('  ',' ')
            line1=line1.strip(' ')


            self.user_command_list[i]=line1
            i+=1
        print(self.user_command_list)

                


    def get_key(self,str):
        for line in self.command_get_key_list:
            key=re.findall(line,str)
            if(key):
                return key[0]

    def check_get_key(self,str):
        key=self.get_key(str)
        if(key and (key not in self.key_list)):
            self.exp='无法识别的按键'
            return False
        else:
            return True

    def def_var(self,str):
        temp=str.split(' ')
        if(temp[0]=='定义'):
            return True
        else:
            return False

    def get_type(self,str):
        temp=re.findall(self.get_var_type,str)
        return temp[0]

    def check_ariexp(self,str,var):
        
        if(self.check_int_from_pic(str)):
            return True
        unit=str.split(' ')
        #print(unit)
        isoper=False
        cnt=0
        for i in range (0,len(unit)):
            if(isoper):
                if((unit[i] not in self.operator_unmapping_keyword_list) and (unit[i] not in self.operator_keyword_list)):
                    if((unit[i]== self.prioper_unmapping_keyword_list[0])or(unit[i] == self.prioper_keyword_list[0])):
                        self.exp='表达式的括号存在错误'
                        return False 
                    if((unit[i]==self.prioper_unmapping_keyword_list[1])or(unit[i]==self.prioper_keyword_list[1])):
                        cnt+=self.prioper_count[unit[i]]
                        if(cnt<0):
                            self.exp='表达式的括号存在错误'
                            return False      
                        isoper=not isoper  
                    else:                      
                        self.exp='表达式运算符错误'
                        return False  
                         
            else:
                if((unit[i]== self.prioper_unmapping_keyword_list[1])or(unit[i] == self.prioper_keyword_list[1])):
                    self.exp='表达式的括号存在错误'
                    return False  
                if((unit[i]== self.prioper_unmapping_keyword_list[0])or(unit[i] == self.prioper_keyword_list[0])):
                    cnt+=self.prioper_count[unit[i]]
                    if(cnt<0):
                        self.exp='表达式的括号存在错误'
                        return False      
                    isoper=not isoper
                else:
                    if(unit[i] not in self.var_list[var] and(not unit[i].isdigit())):
                        #self.exp=unit[i]+'变量类型错误或者该变量没有声明'
                        self.exp='表达式变量错误'
                        return False                     
            isoper=not isoper


        if(not isoper):
            self.exp='表达式错误'
            return False
        if(cnt!=0):
            self.exp='表达式的括号存在错误'
            return False        

        return True

    def check_boolexp(self,str):
        unit=str.split(' ')
        isoper=False
        cnt=0
        is_pic_pic=False
        is_words_pic=False
        #print(unit)
        for i in range (0,len(unit)):
           
            if(isoper):
                if((unit[i] not in self.operator_unmapping_keyword_list) and (unit[i] not in self.operator_keyword_list) and(unit[i] not in self.cmpoper_keyword_list) and (unit[i] not in self.cmpoper_unmapping_keyword_list) and (unit[i] not in self.picoperator_keyword_list) and (unit[i] not in self.picoperator_unmapping_keyword_list) and (unit[i] not in self.word_picoperator_keyword_list) and (unit[i] not in self.word_picoperator_unmapping_keyword_list)):
                    if((unit[i]== self.prioper_unmapping_keyword_list[0])or(unit[i] == self.prioper_keyword_list[0])):
                        self.exp='表达式的括号存在错误'
                        return False 

                    if(unit[i] in self.picoperator_unmapping_keyword_list or unit[i] in self.picoperator_keyword_list):
                        is_pic_pic=True
                    
                    if(unit[i] in self.word_picoperator_unmapping_keyword_list or unit[i] in self.word_picoperator_keyword_list):
                        is_words_pic=True

                    if((unit[i]==self.prioper_unmapping_keyword_list[1])or(unit[i]==self.prioper_keyword_list[1])):
                        cnt+=self.prioper_count[unit[i]]
                        if(cnt<0):
                            self.exp='表达式的括号存在错误'
                            return False      
                        isoper=not isoper  
                    else: 
                        print(unit[i])
                        self.exp='表达式运算符错误'
                        return False       



            else:
                if((unit[i]== self.prioper_unmapping_keyword_list[1])or(unit[i] == self.prioper_keyword_list[1])):
                    self.exp='表达式的括号存在错误'
                    return False 
                if((unit[i]== self.prioper_unmapping_keyword_list[0])or(unit[i] == self.prioper_keyword_list[0])):
                    cnt+=self.prioper_count[unit[i]]
                    if(cnt<0):
                        self.exp='表达式的括号存在错误'
                        return False      
                    isoper=not isoper
                else:
                    if((unit[i]!='画面')and(self.get_ass_type(unit[i])==-1)and (unit[i] not in self.boolean_list) and(not unit[i].isdigit())):
                        if(is_pic_pic):
                            is_pic_pic=False
                            if((unit[i] not in self.var_list[0] and unit[i]!='画面') or unit[i-2] not in self.var_list[0]):
                                self.exp='图片变量错误'
                                return False
                        if(is_words_pic):
                            is_words_pic=False
                            if((unit[i] not in self.var_list[0] and unit[i]!='画面')):
                                self.exp='图片变量错误'
                                return False
                        if((unit[i]=='不是')):
                            isoper=not isoper
                        else:
                            if(i+1<len(unit) and (unit[i+1] in self.word_picoperator_unmapping_keyword_list or unit[i+1] in self.word_picoperator_keyword_list)):
                                hehe=1
                            else:
                        #self.exp=unit[i]+'变量类型错误或者该变量没有声明'
                                self.exp='表达式变量错误'
                                return False                     
            isoper=not isoper
        if(not isoper):
            self.exp='表达式错误'
            return False  

        if(cnt!=0):
            self.exp='表达式的括号存在错误'
            return False   
        return True   



    def check_def_var(self,str):
        if(not self.def_var(str)):
            return True

        var_type=self.get_type(str)
        if(var_type not in self.var_type_list):
            self.exp='无法识别的变量类型'
            return False

        var=self.var_mapping_list[var_type]
        temp1=re.findall(self.get_var_val,str)
        #print(self.get_var_val)
        #print(temp1)
        #print(str)
        temp2=temp1[0].split(' ')
        var_name=temp2[0].strip(' ')
        
        if(var_name in self.keyword_list):
            self.exp='变量名与已有的关键词重复'
            return False
        if(var_name.isdigit()):
            self.exp='变量名不能为数字'
            return False            
        if(var_name in self.key_list):
            self.exp='变量名和按键名重复'
            return False         
        for i in range (self.var_type_num):
            if(var_name in self.var_list[i]):
                self.exp='变量名与已有的变量重复'
                return False             

        if(len(temp2)==1):
            self.var_list[var].append(var_name)
            return True
        if(var==0):
            if(str.find('为')>=0):
                pic_name=str[str.find('为')+2:]
            if(str.find('=')>=0):
                pic_name=str[str.find('=')+2:]
            if(self.img_exists(pic_name)):
                self.var_list[var].append(var_name)
                self.var_num_list[self.area_num][var]+=1
                return True
            else:
                self.exp="图片不存在"
                return False

        if(var==1):
            if(str.find('为')>=0):
                exp=str[str.find('为')+2:]
            if(str.find('=')>=0):
                exp=str[str.find('=')+2:]

            if(self.check_ariexp(exp,var)):
                self.var_list[var].append(var_name)
                self.var_num_list[self.area_num][var]+=1
                return True  
                
            else:
                self.var_list[var].append(var_name)
                return False       

        if(var==2):
            self.var_list[var].append(var_name)
            self.var_num_list[self.area_num][var]+=1
            return True
            # if(re.findall(r'\'(.*?)\'',str)):
            #     return True
            # else:
            #     return False
        if(var==3):
            if(str.find('为')>=0):
                exp=str[str.find('为')+2:]
            if(str.find('=')>=0):
                exp=str[str.find('=')+2:]
                
            if(self.check_boolexp(exp)):
                self.var_list[var].append(var_name)
                self.var_num_list[self.area_num][var]+=1
                return True  
                
            else:
                self.var_list[var].append(var_name)
                return False             

    def get_ass_name(self,str):
        for line in self.get_ass_list:
            temp=re.findall(line,str)
            return temp[0]

    def ass_var(self,str):
        temp=str.split(' ')
        if(temp[0]=='令'):
            return True
        else:
            return False
    def get_ass_type(self,str):
        flag=False
        for i in range(self.var_type_num):
            if(str in self.var_list[i]):
                flag=True
                type_name=i  
        if(flag):
            return type_name
        else:
            return -1  

    def int_from_pic(self,str):
        if(re.findall(self.get_int_from_pic,str)):
            return True
        else:
            return False

    def check_int_from_pic(self,str):
        if(not self.int_from_pic(str)):
            return False 
        temp=re.findall(self.get_int_from_pic,str)
        print(temp)
        for i in range(0,4):
            if(not self.check_ariexp(temp[0][i],1)):
                return False
        return True 

    def check_ass_var(self,str):
        if(not self.ass_var(str)):
            return True 
        ass_name=self.get_ass_name(str)
        type_name=self.get_ass_type(ass_name)

        if(type_name==-1):
            self.exp="使用未命名的变量"
        if(str.find('为')>=0):
            temp=str[str.find('为')+2:]
        if(str.find('=')>=0):
            temp=str[str.find('=')+2:]
        temp=temp.strip(' ')
        ltemp=temp.split(' ')
        #print(temp)
        if(type_name==0):
            if(str.find('为')>=0):
                pic_name=str[str.find('为')+2:]
            if(str.find('=')>=0):
                pic_name=str[str.find('=')+2:]
            if(self.img_exists(pic_name)):
                return True
            else:
                self.exp="图片不存在"
                return False
        if(type_name==1):
            if(str.find('为')>=0):
                exp=str[str.find('为')+2:]
            if(str.find('=')>=0):
                exp=str[str.find('=')+2:]

    

            if(self.check_ariexp(exp,type_name)):
                return True  
            else:
                return False  

        if(type_name==2):
            return True

        if(type_name==3):
            if(str.find('为')>=0):
                exp=str[str.find('为')+2:]
            if(str.find('=')>=0):
                exp=str[str.find('=')+2:]
            if(self.check_boolexp(exp)):
                return True  
            else:
                return False  
                       
    def branch_begin(self,str):
        temp=str.split(' ')
        if(temp[0]=='如果'):
            return True
        else:
            return False        
    def check_branch_begin(self,str):
        if(not self.branch_begin(str)):
            return True 
        if(self.check_boolexp(str[3:])):
            return True
        else:
            return False

    def loop1_begin(self,str):
        temp=str.split(' ')
        if(len(temp)<1):
            return False        
        if(temp[0]=='直到'):
            return True
        else:
            return False  
    def check_loop1_begin(self,str):
        if(not self.loop1_begin(str)):
            return True 
        if(self.check_boolexp(str[3:])):
            return True
        else:
            return False

    def loop2_begin(self,str):
        temp=str.split(' ')
        if(len(temp)<1):
            return False
        if(temp[0]=='当'):
            return True
        else:
            return False  
    def check_loop2_begin(self,str):
        if(not self.loop2_begin(str)):
            return True 
        if(self.check_boolexp(str[2:])):
            return True
        else:
            return False

    def mouse_move_pos(self,str):
        temp=str.split(' ')
        if(len(temp)<3):
            return False
        if(temp[0]=='鼠标' and temp[1]=="移动到" and temp[2]=="横坐标"):
            return True
        else:
            return False        
    def check_mouse_move_pos(self,str):
        if(not self.mouse_move_pos(str)):
            return True 
        if(re.findall(self.get_pos,str)):
            temp=re.findall(self.get_pos,str)
            if(len(temp[0])!=2):
                self.exp="参数错误"
                return False
            for line in temp[0]:
                if(not self.check_ariexp(line, 1)):
                    return False
            return True
        self.exp="参数错误"
        return False
#鼠标 移动到 画面 (.*?)图中
    def check_pic(self,str):
        if(str in self.var_list[0] or self.img_exists(str)):
            return True
        else:
            return False

    def mouse_move_spic(self,str):
        temp=str.split(' ')
        if(len(temp)<5):
            return False           
        if(temp[0]=='鼠标' and temp[1]=="移动到" and temp[2]=="画面" and "图中" in temp):
            return True
        else:
            return False 

    def check_mouse_move_spic(self,str):
        if(not self.mouse_move_spic(str)):
            return True 
       
        if(re.findall(self.get_spic,str)):
            temp=re.findall(self.get_spic,str)
            if(self.check_pic(temp[0])):
                 return True
            else:
                self.exp="图片变量不存在"
                return False

        self.exp="语法错误"
        return False
#'鼠标 移动到 (.*?)图的 (.*?)图中'
    def mouse_move_lpic_spic(self,str):
        temp=str.split(' ')
        if(len(temp)<6):
            return False           
        if(temp[0]=='鼠标' and temp[1]=="移动到" and temp[3]=="图的" and temp[5]=="图中"):
            return True
        else:
            return False 

    def check_mouse_move_lpic_spic(self,str):
        if(not self.mouse_move_lpic_spic(str)):
            return True 
        
        if(re.findall(self.get_lpic_spic,str)):
            cnt=0
            temp=re.findall(self.get_lpic_spic,str)
            if(self.check_pic(temp[0][0])and self.check_pic(temp[0][1])):
                return True
            else:
                self.exp="图片变量不存在"
                return False
        self.exp="语法错误"
        return False

    def mouse_move_lpic_word(self,str):
        temp=str.split(' ')
        if(len(temp)<6):
            return False           
        if(temp[0]=='鼠标' and temp[1]=="移动到" and "图的" in temp and "文字中" in temp):
            return True
        else:
            return False 

    def check_mouse_move_lpic_word(self,str):
        if(not self.mouse_move_lpic_word(str)):
            return True 
       
        if(re.findall(self.get_lpic_word,str)):
            temp=re.findall(self.get_lpic_word,str)
            if(self.check_pic(temp[0][0])):

                 return True
            else:
                self.exp="图片变量不存在"
                return False
 
        self.exp="语法错误"
        return False

    def mouse_move_word(self,str):
        temp=str.split(' ')
        if(len(temp)<5):
            return False           
        if(temp[0]=='鼠标' and temp[1]=="移动到" and temp[2]=="画面" and "文字中" in temp):
            return True
        else:
            return False 

    def check_mouse_move_word(self,str):
        if(not self.mouse_move_word(str)):
            return True 
       
        if(re.findall(self.get_word,str)):
            return True
       

        self.exp="语法错误"
        return False

    def one_para(self,str):
        for line in self.one_para_list:
            if(re.findall(line,str)):
                return True
        return False
   
    def check_one_para(self,str):
        if(not self.one_para(str)):
            return True 
        
        for line in self.one_para_list:
            if(re.findall(line,str)):
                temp=re.findall(line,str)
                if(self.check_ariexp(temp[0],1)):
                    return True
                else:
                    
                    return False

        self.exp="语法错误"
        return False   



    def one_para_ari_str(self,str):
        for line in self.one_para_ari_str_list:
            if(re.findall(line,str)):
                return True
        return False

    def check_one_para_ari_str(self,str):
        if(not self.one_para_ari_str(str)):
            return True 
        
        for line in self.one_para_ari_str_list:
            if(re.findall(line,str)):
                temp=re.findall(line,str)
                if(self.check_ariexp(temp[0],1)):
                    return True
                else:
                    return False

        self.exp="语法错误"
        return False   


    def clear_var(self):
        #print(self.var_num_list)
        for i in range (0,3):
            for j in range(self.var_num_list[self.area_num][i]):
                self.var_list[i].pop()

    def keyboard_op(self,str):
        temp=str.split(' ')
        if(len(temp)<3):
            return False           
        if(temp[0]=='键盘'):
            return True
        else:
            return False 

    def print_word(self,str):
        temp=str.split(' ')
        if(temp):
            if(temp[0]=='打印'):
                return True
        return False

    def print_exp(self,str):
        temp=str.split(' ')
        if(temp):
            if(temp[0]=='输出'):
                return True
        return False

    def left_click_fun(self,str):
        if(re.findall(self.get_left_click_fun,str)):
            return True
        else:
            return False

    def check_left_click_fun(self,str):
        if(not self.left_click_fun(str)):
            return True
        temp=re.findall(self.get_left_click_fun,str)
        for line in temp[0]:
            
            if(not self.check_ariexp(line,1)):
                return False
        return True

    def right_click_fun(self,str):
        if(re.findall(self.get_right_click_fun,str)):
            return True
        else:
            return False


    def check_right_click_fun(self,str):
        if(not self.right_click_fun(str)):
            return True
        temp=re.findall(self.get_right_click_fun,str)
        for line in temp[0]:
            if(not self.check_ariexp(line,1)):
                return False
        return True

    def wait_pic(self,str):
        if(re.findall(self.get_wait_pic,str)):
            return True
        else:
            return False
        
    def check_wait_pic(self,str):
        if(not self.wait_pic(str)):
            return True
        temp=re.findall(self.get_wait_pic,str)
        if(self.check_pic(temp[0])):
            return True  
        else:
            return False

    def img_exists(self,img_name):
        img_path=self.find_imgpath(img_name)
        return path.isfile(img_path)

    def find_imgpath(self,img_name):
        img_path=path.dirname(__file__)
        for i in range(3):
            img_path=path.dirname(img_path)
        img_path+='\\img\\'
        img_path+=img_name
        # print(img_path)
        return img_path

    def check(self):
        top=0
        self.error_list=[]
        self.var_num_list=[]
        self.var_list=[]
        for i in range (self.var_type_num):
            self.var_list.append([])
        branch_list=[]
        else_list=[]

        i=0
        for j in range(100):
            branch_list.append(0)
            else_list.append(0)
            self.var_num_list.append([])
            for k in range(4):
                self.var_num_list[j].append(0)
        branch_now=0
        loop1_now=0
        loop2_now=0
        next_branch=False
        self.stage=[]
        empty_line=0
        for line1 in self.user_command_list:
            
            
            if(line1==''):
                empty_line+=1
                continue   
            i+=1  
            flag=False
            self.area_num=loop1_now+loop2_now+branch_now
            for line2 in self.command_list:
            
                if(re.findall(line2,line1)):
                    flag=True
            if(flag==False):
                self.exp="语法错误"                    
            if(flag and (next_branch and line1!='那么')):
                flag=False
                self.exp="条件语法错误"
            
            if(next_branch):
                next_branch=False


            for line2 in self.command_branch_list:
                
                if(re.findall(line2,line1)):
                    if(line2=='如果 (.*?)$'):
                        next_branch=True
                        branch_now+=1
                        branch_list[branch_now]+=1
                    if(line2=='否则$'):
                        else_list[branch_now]+=1
                        if(else_list[branch_now]>branch_list[branch_now]):
                            flag=False
                            self.exp="条件语法错误"
                    if(line2=='条件结束$'):
                        else_list[branch_now]=branch_list[branch_now]
                        branch_now-=1
                        self.clear_var()
                        if(branch_now<0):
                            flag=False
                            self.exp="条件语法错误"

            for line2 in self.command_loop_list:
                if(re.findall(line2,line1)):
                    if(line2=='循环开始$'):
                        loop1_now+=1
                    
                    if(line2=='当 (.*?)$'):
                        loop2_now+=1    

                    if(line2=='直到 (.*?)$'):
                        loop1_now-=1
                        self.clear_var()
                        if(loop1_now<0):
                            flag=False
                            self.exp="循环语法错误"

                    if(line2=='循环结束'):
                        loop2_now-=1
                        self.clear_var()
                        if(loop2_now<0):
                            flag=False
                            self.exp="循环语法错误"

            if(flag and not(self.check_mouse_move_pos(line1))):
                flag=False
            if(flag and not(self.check_mouse_move_spic(line1))):
                flag=False
            if(flag and not(self.check_mouse_move_lpic_spic(line1))):
                flag=False
            if(flag and not(self.check_mouse_move_word(line1))):
                flag=False
            if(flag and not(self.check_mouse_move_lpic_word(line1))):
                flag=False
            if(flag and not(self.check_get_key(line1))):
                flag=False
            if(flag and not(self.check_def_var(line1))):
                flag=False
            if(flag and not(self.check_ass_var(line1))):
                flag=False
            if(flag and not(self.check_branch_begin(line1))):
                flag=False
            if(flag and not(self.check_loop1_begin(line1))):
                flag=False
            if(flag and not(self.check_loop2_begin(line1))):
                flag=False
            if(flag and not(self.check_one_para(line1))):
                flag=False      
            if(flag and not(self.check_one_para_ari_str(line1))):
                flag=False          
            if(flag and not(self.check_left_click_fun(line1))):
                flag=False
            if(flag and not(self.check_right_click_fun(line1))):
                flag=False
            if(flag and not(self.check_wait_pic(line1))):
                flag=False

            if(flag==False):
                top+=1
                self.error_list.append('第'+str(i+empty_line)+'行，'+self.exp+'，其内容为：'+line1)
            
        if(i==0):
            top+=1
            self.error_list.append("无指令？")
            return False

        self.stage.append(loop1_now+loop2_now+branch_now)

        if(branch_now!=0):
            self.exp='条件语句尚未结束'
            top+=1
            self.error_list.append(self.exp)
        if(loop1_now!=0 or loop2_now!=0):
            self.exp='循环语句尚未结束'
            top+=1
            self.error_list.append(self.exp)
        print(top)
        if(top==0):
            return True
        else:
       #     for line in error_list:
       #         print(line)
            
            return False
        #self.equipment[]
        #self.part[]
        #self.action[]
        #self.parameters1[]
        #self.parameters2[]
    def get_error_list(self):
        return self.error_list

    def in_equipment(self,s):
        for line in self.equipment_list:
            if(re.findall(line,s)):
                return True
        return False

    def in_part(self,s):
        for line in self.part_list:
            if(re.findall(line,s)):
                return True
        return False

    def in_action(self,s):
        for line in self.action_list:
            if(re.findall(line,s)):
                return True
        return False

    def transfer_exp(self,str):
        parameters_list=[]
        temp=re.findall(self.get_spic_bool,str)
        if(temp):
            parameters_list.append('判断小图截屏')
            parameters_list.append(temp[0])
            return parameters_list
        temp=re.findall(self.get_spic_lpic_bool,str)
        if(temp):
            parameters_list.append('判断小图大图')
            parameters_list.append(temp[0][0])   
            parameters_list.append(temp[0][1])         
            return parameters_list

        unit=str.split(' ')

        for line2 in unit:
            if(line2.isdigit()):
                parameters_list.append(line2)
                continue
            if(line2 in self.boolean_list):
                parameters_list.append(self.boolean_mapping_list[line2])
                continue                                
            if(line2 in self.operator_unmapping_keyword_list):
                line2=self.operator_mapping_list[line2]
            if(line2 in self.operator_keyword_list):
                parameters_list.append(line2)
                continue

            if(line2 in self.cmpoper_unmapping_keyword_list):
                line2=self.cmpoper_mapping_list[line2]
            if(line2 in self.cmpoper_keyword_list):
                parameters_list.append(line2)
                continue

            if(line2 in self.prioper_unmapping_keyword_list):
                line2=self.prioper_mapping_list[line2]
            if(line2 in self.prioper_keyword_list):
                parameters_list.append(line2)
                continue
            
            if(line2 in self.word_picoperator_unmapping_keyword_list or line2 in self.picoperator_unmapping_keyword_list):
                line2=self.picoperator_mapping_list[line2]
            if(line2 in self.word_picoperator_keyword_list or line2 in self.picoperator_keyword_list):
                parameters_list.append(line2)     
                continue     
            if(line2 in self.const_list):
                parameters_list.append(line2)
                continue

            if(line2 not in self.keyword_list):
                parameters_list.append(line2)
            
        return parameters_list

    def transfer(self):
        temp=[]
        if(self.check()):
            hwnd = win32gui.FindWindow(None, "Macro")
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
            for line1 in self.user_command_list:
                self.equipment.append('')
                self.part.append('')
                self.action.append('')
                self.parameters.append([])  
                is_mouse_move_pos=False
                is_mouse_move_spic=False
                is_def_var=False        
                is_ass_var=False
                is_branch_begin=False
                is_loop1_end=False
                is_loop2_begin=False
                is_mouse_move_lpic_spic=False
                is_mouse_move_word=False
                is_mouse_move_lpic_word=False
                is_keyboard_op=False
                is_one_para=False
                is_print_word=False
                is_check_one_para_ari_str=False      
                is_check_left_click_fun=False
                is_check_right_click_fun=False
                is_check_wait_pic=False
                if(self.print_word(line1)):
                    self.equipment[self.top]="打印"
                    is_print_word=True                   
                if(self.keyboard_op(line1)):
                    self.equipment[self.top]="键盘"
                    is_keyboard_op=True
                     
       
       

        

                if(self.mouse_move_pos(line1)):
                    self.equipment[self.top]="鼠标"
                    self.action[self.top]="移动到"
                    self.parameters[self.top].append("坐标") #r'鼠标 移动到 横坐标 (.*?) 纵坐标 (.*?)$'
                    is_mouse_move_pos=True
                if(self.mouse_move_spic(line1)):
                    self.equipment[self.top]="鼠标"
                    self.action[self.top]="移动到"
                    self.parameters[self.top].append("小图截屏") #'鼠标 移动到 画面 (.*?) 图中$'
                    is_mouse_move_spic=True
                if(self.mouse_move_lpic_spic(line1)):
                    self.equipment[self.top]="鼠标"
                    self.action[self.top]="移动到"
                    self.parameters[self.top].append("小图大图") #r'鼠标 移动到 (.*?) 图的 (.*?) 图中$'
                    is_mouse_move_lpic_spic=True
                if(self.mouse_move_word(line1)):
                    self.equipment[self.top]="鼠标"
                    self.action[self.top]="移动到"
                    self.parameters[self.top].append("文字截屏") #r'鼠标 移动到 画面 (.*?) 文字中$'
                    is_mouse_move_word=True
                if(self.mouse_move_lpic_word(line1)):
                    self.equipment[self.top]="鼠标"
                    self.action[self.top]="移动到"
                    self.parameters[self.top].append("文字大图") #r'鼠标 移动到 (.*?) 图的 (.*?) 文字中$'
                    is_mouse_move_lpic_word=True

                if(self.def_var(line1)):
                    self.equipment[self.top]="定义"
                    self.action[self.top]=self.get_type(line1)
                    temp1=re.findall(self.get_var_val,line1)
                    temp2=temp1[0].split(' ')
                    self.part[self.top]=temp2[0].strip(' ')
                    is_def_var=True
                if(self.ass_var(line1)):
                    #print(line1)
                    self.equipment[self.top]="令"
                    self.part[self.top]=self.get_ass_name(line1)
                    is_ass_var=True
                    is_first=True
                if(self.branch_begin(line1)):
                    self.equipment[self.top]="如果"
                    is_branch_begin=True
                if(self.loop1_begin(line1)):
                    self.equipment[self.top]="直到"
                    is_loop1_end=True
                if(self.loop2_begin(line1)):
                    self.equipment[self.top]="当"
                    is_loop2_begin=True
                if(self.one_para(line1)):
                    temp=line1.split(' ')
                    for line2 in temp:
                        if(self.in_equipment(line2)):
                            self.equipment[self.top]=line2
                            continue
                        if(self.in_part(line2)):
                            self.part[self.top]=line2
                            continue
                        if(self.in_action(line2)):
                            self.action[self.top]=line2
                            continue      
                    is_one_para=True
                if(self.check_one_para_ari_str(line1)):
                    temp=line1.split(' ')
                    for line2 in temp:
                        if(self.in_equipment(line2)):
                            self.equipment[self.top]=line2
                            continue
                        if(self.in_part(line2)):
                            self.part[self.top]=line2
                            continue
                        if(self.in_action(line2)):
                            self.action[self.top]=line2
                            continue 
                    is_check_one_para_ari_str=True  
                if(self.left_click_fun(line1)):
                    self.equipment[self.top]="连点器"
                    self.part[self.top]="左键"
                    is_check_left_click_fun=True
                if(self.right_click_fun(line1)):
                    self.equipment[self.top]="连点器"
                    self.part[self.top]="右键"
                    is_check_right_click_fun=True
                if(self.wait_pic(line1)):
                    self.equipment[self.top]="等待图"
                    is_check_wait_pic=True                    

                temp=line1.split(' ')
                if(not(is_def_var or is_ass_var or is_loop1_end or is_loop2_begin or is_mouse_move_pos or is_mouse_move_spic or is_keyboard_op or is_one_para or is_print_word or is_check_one_para_ari_str or is_check_left_click_fun or is_check_right_click_fun or is_check_wait_pic)):
                    for line2 in temp:
                        if(self.in_equipment(line2)):
                            self.equipment[self.top]=line2
                            continue
                        if(self.in_part(line2)):
                            if(line2 not in self.mouse_key_list):
                                line2=line2.replace("键",'')
                            self.part[self.top]=line2
                            continue
                        if(self.in_action(line2)):
                            self.action[self.top]=line2
                            continue       
                        if(line2.isdigit() or line2 in self.var_list[1]):
                            self.parameters[self.top].append(line2)
                            continue                    
 
                if(is_def_var):
                    var=self.get_ass_type(self.part[self.top])
                    if(var==0):
                        
                        temp=max(line1.find('为'),line1.find('='))
                        if(temp>=0):
                            self.parameters[self.top].append(line1[temp+2:])
                     

                    if(var==1):
                        temp=max(line1.find('为'),line1.find('='))
                        if(temp>=0):
                            self.parameters[self.top]=self.transfer_exp(line1[temp+2:])                                              

                    if(var==2):
                        temp=max(line1.find('为'),line1.find('='))
                        if(temp>=0):
                            self.parameters[self.top].append(line1[temp+2:])
                    if(var==3):
                        temp=max(line1.find('为'),line1.find('='))
                        if(temp>=0):
                            self.parameters[self.top]=self.transfer_exp(line1[temp+2:])                                       
                    
                    #    temp=line1.find('为')
                      
                    #    if(temp>=0):
                    #        self.parameters[self.top].append(line1[temp+2:])
                    #    else:
                    #        self.parameters[self.top].append('false')

                if(is_ass_var):
                    var=self.get_ass_type(self.part[self.top])
                    if(var==0):
                        temp=max(line1.find('为'),line1.find('='))
                        if(temp>=0):
                            self.parameters[self.top].append(line1[temp+2:])

                    if(var==1):
                        temp=max(line1.find('为'),line1.find('='))
                        if(temp>=0):
                            self.parameters[self.top]=self.transfer_exp(line1[temp+2:])   

                    if(var==2):
                        temp=max(line1.find('为'),line1.find('='))
                        if(temp>=0):
                            self.parameters[self.top].append(line1[temp+2:])

                    if(var==3):
                        temp=max(line1.find('为'),line1.find('='))
                        if(temp>=0):
                            self.parameters[self.top]=self.transfer_exp(line1[temp+2:])    
                if(is_branch_begin):
                    self.parameters[self.top]=self.transfer_exp(line1[3:])
                if(is_loop1_end):
                    self.parameters[self.top]=self.transfer_exp(line1[3:])
                if(is_loop2_begin):
                    self.parameters[self.top]=self.transfer_exp(line1[2:])                    
                if(is_mouse_move_pos):
                    temp=re.findall(self.get_pos,line1)

                    self.parameters[self.top]+=self.transfer_exp(temp[0][0])
                    self.parameters[self.top]+=self.transfer_exp(temp[0][1])
                if(is_mouse_move_spic):
                   
                    temp=re.findall(self.get_spic,line1)
                    self.parameters[self.top]+=temp

                if(is_mouse_move_lpic_spic):
                    temp=re.findall(self.get_lpic_spic,line1)
                    self.parameters[self.top].append(temp[0][1])
                    self.parameters[self.top].append(temp[0][0])

                if(is_mouse_move_word):
                    temp=re.findall(self.get_word,line1)
                    self.parameters[self.top]+=temp

                if(is_mouse_move_lpic_word):
                    temp=re.findall(self.get_lpic_word,line1)
                    self.parameters[self.top].append(temp[0][1])
                    self.parameters[self.top].append(temp[0][0])
                if(is_keyboard_op):
                    temp=line1.split(' ')
                    self.action[self.top]=temp[1]
                    temp[2]=temp[2].replace("键",'')
                    self.part[self.top]=self.key_mapping_list[temp[2]]
                    if(len(temp)==5):
                        self.parameters[self.top].append(temp[4])

                if(is_one_para):
                    for line2 in self.one_para_list:
                        temp=re.findall(line2,line1)
                        if(temp):
                            self.parameters[self.top]=self.transfer_exp(temp[0])
                            continue

                if(is_print_word):
                    self.parameters[self.top].append(line1[3:])

                if(is_check_one_para_ari_str):
                    for line2 in self.one_para_ari_str_list:
                        temp=re.findall(line2,line1)
                        if(temp):
                            self.parameters[self.top]=self.transfer_exp(temp[0])
                            continue                    
                
                if(is_check_left_click_fun):
                    temp=re.findall(self.get_left_click_fun,line1)
                    
                    for line2 in temp[0]:
                        self.parameters[self.top]+=self.transfer_exp(line2)

                if(is_check_right_click_fun):
                    temp=re.findall(self.get_right_click_fun,line1)
                    for line2 in temp[0]:
                        self.parameters[self.top]+=self.transfer_exp(line2)

                if(is_check_wait_pic):
                    temp=re.findall(self.get_wait_pic,line1)
                    self.parameters[self.top].append(temp[0])

                if(len(self.parameters[self.top])==0 and (is_def_var or is_ass_var)):
                    self.parameters[self.top].append('0')
                self.top+=1
        else:
            print("编译不通过")
            return 
        print(self.equipment)#变量类型
        print(self.part)#变量名字
        print(self.action)#定义
        print(self.parameters)
    
        #self.equipment[]
        #self.part[]
        #self.action[]
        #self.parameters1[]
        #self.parameters2[]

    def get_top(self):
        return self.top

    def get_equipment(self):
        return self.equipment

    def get_part(self):
        return self.part

    def get_action(self):
        return self.action

    def get_paramters(self):
        return self.parameters

def check_run(file_path, Minimise = True):
    try:
        x=codetransfer(file_path)
        x.modify2()

        if(x.check()):
            return []
        else:
            return x.get_error_list()
    except TypeError:
        logger.error("codetransfer出错")


def modify_txt(file_path):
    x = codetransfer(file_path)
    return x.modified_file()

def test_run(file_path):
    x=codetransfer(file_path)
    x.modified_file()
    x.modify2()
    x.transfer()



if __name__=='__main__':
    file_path="D:\程序\软件项目\hello-world\hello-world\macro\modules\complier\\test.txt" 
    test_run(file_path)
    
    stemp = check_run(file_path)

    
    if(len(stemp) == 0):
        print("ok")
    for line in stemp:
        print(line)








