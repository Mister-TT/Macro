import sys
sys.path.append("")

from macro.modules.controller.Method.methodInterface import MethodInterface
from macro.config import config
import webbrowser

class openMethod(MethodInterface):
    def justDoit(self, controller):
        filepath = controller.returnOpenFile()
        call = controller.returnCallOfSave()

        if(filepath == ""):
            filepath = controller.fileManagerHandler.controllerOpen()

        if(filepath == ""):
            return 
            
        with open(filepath, 'r', encoding='utf-8') as f:
            controller.editorHandler.setPlainText(f.read())
            config.TMP_FILE_PATH = filepath
            f.close()
        
        if(call):
            controller.debugWindowHandler.append(
                "打开文件 " + config.TMP_FILE_PATH + " 成功!")


