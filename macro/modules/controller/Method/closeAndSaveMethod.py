import sys
sys.path.append("")

from macro.modules.controller.Method.methodInterface import MethodInterface
from macro.config import config

class closeAndSaveMethod(MethodInterface):
    def justDoit(self, controller):
        controller.fileManagerHandler.mkdir('/macro/config')
        with open(config.TMP_DIR + "/macro/config/last_file.txt", "w", encoding="utf-8") as f:
            f.write(config.TMP_FILE_PATH)
            f.close()


