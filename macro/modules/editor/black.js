require.config({ paths: { 'vs': 'node_modules/monaco-editor/dev/vs' } });
require(['vs/editor/editor.main'], function () {


    monaco.languages.register({id: "MacroLang"});

    //  定义token(语法高亮)
    monaco.languages.setMonarchTokensProvider("MacroLang", {
        tokenizer: {    // 分词器 [正则表达式， token名称]
            root: [
                [/Macro/, "command"],
                [/鼠标|键盘|画面|连点器/, "command"],
                [/延迟|出现/, "command"],
                [/[A-Za-z0-9]+键/, "command"],    // （字符串）键
                [/如果|那么|否则|条件结束/, "command"],
                [/循环开始|直到|当|循环结束|继续|退出循环|退出所有循环/, "command"],
                [/起点|终点/, "command"],
                [/定义|变量/, "command"],
                [/打印|输出/, "command"],
                [/等待图/, "command"],

                [/左移|右移|上移|下移/, "operation"],
                [/左键|右键|中键/, "operation"],
                [/上滚轮|下滚轮/, "operation"],
                [/双击|拖动|移动到|间隔/, "operation"],
                [/按下|松开|持续/, "operation"],
                [/为|令/, "operation"],

                [/不是|而且|或者/, "logic"],
                [/加|减|乘|除以/, "arith"],
                [/大于|小于|等于/, "arith"],

                [/的数字|次/, "signal"],
                [/（\s*\d+\s*）/, "signal"],
                [/\(\s*\d+\s*\)/, "signal"],
                [/\(|\)|（|）/, "signal"],

                [/横坐标|纵坐标/, "location"],
                [/图中|图的|文字中/, "location"],
                [/图存在于|文字存在于/, "location"],
                [/左上角|右下角/, "location"],

                [/#.*/, "exegesis"],

                [/[\u4e00-\u9fa5a-zA-Z0-9]/, "anything"],
                ]
        }
    });

    // 语言符号自动补全
    monaco.languages.setLanguageConfiguration("MacroLang", {
        brackets: [
            ["(", ")"],
            ["（", "）"],
        ],
        autoClosingPairs: [
            { open: "(", close: ")" },
            { open: "（", close: "）" },
        ],
    });

    // 自定义主题
    monaco.editor.defineTheme("MacroTheme", {
       base: 'vs-dark',
       //  background_color: '#818183',
       inherit: true,
       rules: [   // 定义规则，token名称 ~ style  foreground:字体颜色，fontStyle:字体样式
           {token: 'command', foreground: '#00FFFF'} ,   // blue
           {token: 'logic', foreground: '#FFCCFF'},   // purple
           {token: 'arith', foreground: '#FFCCFF'},   // purple
           {token: 'signal', foreground: '#FFFF99'},   // yellow
           {token: 'operation', foreground: '#33FF99'},   // green
           {token: 'location', foreground: '#FFFF99'},   // yellow
           {token: 'exegesis', foreground: '#909090'},   // grey
           {token: 'anything', foreground: '#FFFFFF'},   // white
       ],
        colors: {
                // 相关颜色属性配置
                // 'editor.foreground': '#000000',
                'editor.background': '#323232',     //背景色
                // 'editorCursor.foreground': '#8B0000',
                'editor.lineHighlightBackground': '#2F4F4F',
                // 'editorLineNumber.foreground': '#008800',
                // 'editor.selectionBackground': '#88000030',
                // 'editor.inactiveSelectionBackground': '#FFFF99'
            }
    //         'editor.background': '#323232',
    //         'editor.selectionHighlightBackground': '#737373',
    // }

    });

    // 语法补全
    monaco.languages.registerCompletionItemProvider('MacroLang', {
        provideCompletionItems: () => {
            var suggestions = [
            // 前提准备
                 {
			label: 's',
			kind: monaco.languages.CompletionItemKind.Text,
			insertText: ''
		    }, {
			label: 'n',
			kind: monaco.languages.CompletionItemKind.Text,
			insertText: ''
		    }, {
			label: 'f',
			kind: monaco.languages.CompletionItemKind.Text,
			insertText: ''
		    },{
			label: 't',
			kind: monaco.languages.CompletionItemKind.Text,
			insertText: ''
		    }, {
			label: 'x',
			kind: monaco.languages.CompletionItemKind.Text,
			insertText: ''
		    },{
			label: 'j',
			kind: monaco.languages.CompletionItemKind.Text,
			insertText: ''
		    },{
			label: 'y',
			kind: monaco.languages.CompletionItemKind.Text,
			insertText: ''
		    },{
			label: 'd',
			kind: monaco.languages.CompletionItemKind.Text,
			insertText: ''
		    },{
			label: 'l',
			kind: monaco.languages.CompletionItemKind.Text,
			insertText: ''
		    },{
			label: 'r',
			kind: monaco.languages.CompletionItemKind.Text,
			insertText: ''
		    },{
			label: 'z',
			kind: monaco.languages.CompletionItemKind.Text,
			insertText: ''
		    },
            // 关键词提示
                {
			label: '鼠标 左键 点击',
			kind: monaco.languages.CompletionItemKind.Keyword,
			insertText: '鼠标 左键 点击',
			insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet
		    }, {
			label: '鼠标 右键 点击',
			kind: monaco.languages.CompletionItemKind.Keyword,
			insertText: '鼠标 右键 点击',
			insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet
		    }, {
			label: '鼠标 左键 双击',
			kind: monaco.languages.CompletionItemKind.Keyword,
			insertText: '鼠标 左键 双击',
			insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet
		    }, {
			label: '鼠标 右键 双击',
			kind: monaco.languages.CompletionItemKind.Keyword,
			insertText: '鼠标 右键 双击',
			insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet
		    }, {
			label: '鼠标 左键 按下',
			kind: monaco.languages.CompletionItemKind.Keyword,
			insertText: '鼠标 左键 按下',
			insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet
		    }, {
			label: '鼠标 右键 按下',
			kind: monaco.languages.CompletionItemKind.Keyword,
			insertText: '鼠标 右键 按下',
			insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet
		    }, {
			label: '鼠标 左键 松开',
			kind: monaco.languages.CompletionItemKind.Keyword,
			insertText: '鼠标 左键 松开',
			insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet
		    }, {
			label: '鼠标 右键 松开',
			kind: monaco.languages.CompletionItemKind.Keyword,
			insertText: '鼠标 右键 松开',
			insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet
		    }, {
			label: '那么',
			kind: monaco.languages.CompletionItemKind.Keyword,
			insertText: '那么',
			insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet
		    }, {
			label: '否则',
			kind: monaco.languages.CompletionItemKind.Keyword,
			insertText: '否则',
			insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet
		    },{
			label: '条件结束',
			kind: monaco.languages.CompletionItemKind.Keyword,
			insertText: '条件结束',
			insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet
		    },{
			label: '循环开始',
			kind: monaco.languages.CompletionItemKind.Keyword,
			insertText: '循环开始',
			insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet
		    },{
			label: '循环结束',
			kind: monaco.languages.CompletionItemKind.Keyword,
			insertText: '循环结束',
			insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet
		    },{
			label: '继续',
			kind: monaco.languages.CompletionItemKind.Keyword,
			insertText: '继续',
			insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet
		    },{
			label: '退出循环',
			kind: monaco.languages.CompletionItemKind.Keyword,
			insertText: '退出循环',
			insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet
		    },{
			label: '退出所有循环',
			kind: monaco.languages.CompletionItemKind.Keyword,
			insertText: '退出所有循环',
			insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet
		    },
            // 函数提示
                {
            label: "延迟 （算数表达式）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "延迟 ${1:（算数表达式）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "鼠标 左移 （算数表达式）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "鼠标 左移 ${1:（算数表达式）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "鼠标 右移 （算数表达式）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "鼠标 右移 ${1:（算数表达式）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "鼠标 上移 （算数表达式）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "鼠标 上移 ${1:（算数表达式）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "鼠标 下移 （算数表达式）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "鼠标 下移 ${1:（算数表达式）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "鼠标 上滚轮 （算数表达式）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "鼠标 上滚轮 ${1:（算数表达式）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "鼠标 下滚轮 （算数表达式）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "鼠标 下滚轮 ${1:（算数表达式）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "鼠标 左键 拖动 起点 横坐标 （算数表达式） 纵坐标 （算数表达式） 终点 横坐标 （算数表达式） 纵坐标 （算数表达式）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "鼠标 左键 拖动 起点 横坐标 ${1:（算数表达式）} 纵坐标 ${2:（算数表达式）} 终点 横坐标 ${3:（算数表达式）} 纵坐标 ${4:（算数表达式）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "鼠标 右键 拖动 起点 横坐标 （算数表达式） 纵坐标 （算数表达式） 终点 横坐标 （算数表达式） 纵坐标 （算数表达式）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "鼠标 右键 拖动 起点 横坐标 ${1:（算数表达式）} 纵坐标 ${2:（算数表达式）} 终点 横坐标 ${3:（算数表达式）} 纵坐标 ${4:（算数表达式）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "鼠标 移动到 横坐标 （算数表达式） 纵坐标 （算数表达式）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "鼠标 移动到 横坐标 ${1:（算数表达式）} 纵坐标 ${2:（算数表达式）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "鼠标 移动到 画面 （图片变量名） 图中",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "鼠标 移动到 画面 ${1:（图片变量名）} 图中",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "鼠标 移动到 画面 （字符串） 文字中",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "鼠标 移动到 画面 ${1:（字符串）} 文字中",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "鼠标 移动到 （图片变量名） 图的 （图片变量名） 图中",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "鼠标 移动到 ${1:（图片变量名）} 图的 ${2:（图片变量名）} 图中",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "鼠标 移动到 （图片变量名） 图的 （字符串） 文字中",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "鼠标 移动到 ${1:（图片变量名）} 图的 ${2:（字符串）} 文字中",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "键盘 按下 （字符串）键 持续 （算数表达式）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "键盘 按下 ${1:（字符串）}键 持续 ${2:（算数表达式）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "键盘 按下 （字符串）键",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "键盘 按下 ${1:（字符串）}键",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "键盘 松开 （字符串）键",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "键盘 松开 ${1:（字符串）}键",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "定义 （变量类型） 变量 （变量名）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "定义 ${1:（变量类型）} 变量 ${2:（变量名）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "定义 （变量类型） 变量 （变量名） 为 （...）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "定义 ${1:（变量类型）} 变量 ${2:（变量名）} 为 ${3:（...）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "令 （变量名） 为 （...）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "令 ${1:（变量名）} 为 ${2:（...）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "如果 （布尔表达式）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "如果 ${1:（布尔表达式）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "直到 （布尔表达式）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "直到 ${1:（布尔表达式）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "当 （布尔表达式）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "当 ${1:（布尔表达式）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "打印 （字符串）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "打印 ${1:（字符串）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "输出 （表达式）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "输出 ${1:（表达式）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "连点器 （算数表达式） 次 横坐标 （算数表达式） 纵坐标 （算数表达式） 左键 间隔 （算数表达式）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "连点器 ${1:（算数表达式）} 次 横坐标 ${2:（算数表达式）} 纵坐标 ${3:（算数表达式）} 左键 间隔 ${4:（算数表达式）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "连点器 （算数表达式） 次 横坐标 （算数表达式） 纵坐标 （算数表达式） 右键 间隔 （算数表达式）",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "连点器 ${1:（算数表达式）} 次 横坐标 ${2:（算数表达式）} 纵坐标 ${3:（算数表达式）} 右键 间隔 ${4:（算数表达式）} ",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "等待图 （图片变量） 出现",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "等待图 ${1:（图片变量）} 出现",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "定义 整型 变量 （变量名） 为 画面 左上角 横坐标 （算数表达式） 纵坐标 （算数表达式） 右下角 横坐标 （算数表达式） 纵坐标 （算数表达式） 的数字",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "定义 整型 变量 ${1:（变量名）} 为 画面 左上角 横坐标 ${2:（算数表达式）} 纵坐标 ${3:（算数表达式）} 右下角 横坐标 ${4:（算数表达式）} 纵坐标 ${5:（算数表达式）} 的数字",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            }, {
            label: "令 变量 （变量名） 为 画面 左上角 横坐标 （算数表达式） 纵坐标 （算数表达式） 右下角 横坐标 （算数表达式） 纵坐标 （算数表达式） 的数字",
            kind: monaco.languages.CompletionItemKind.Function,
            documentation: "",
            insertText: "令 变量 ${1:（变量名）} 为 画面 左上角 横坐标 ${2:（算数表达式）} 纵坐标 ${3:（算数表达式）} 右下角 横坐标 ${4:（算数表达式）} 纵坐标 ${5:（算数表达式）} 的数字",
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            // range: range
            },
            ]
            return {
                suggestions: suggestions
            };
        }
    })

    // 创建model
    // 注释:在Monaco Editor中，每个用户可见的编辑器均对应一个IStandaloneCodeEditor。在构造时可以指定一系列选项，如行号、minimap等。
    // 其中，每个编辑器的代码内容等信息存储在ITextModel中。model保存了文档内容、文档语言、文档路径等一系列信息，当editor关闭后model仍保留在内存中
    //
    // 因此可以说，editor对应着用户看到的编辑器界面，是短期的、暂时的；model对应着当前网页历史上打开/创建过的所有代码文档，是长期的、保持的。
    let uri = monaco.Uri.parse("macro://model.txt");
    var model = monaco.editor.getModel(uri);
    if (!model)	// 否则创建新的model
	    model = monaco.editor.createModel("", 'MacroLang', uri);
    // 也可以不指定uri参数，直接使用model = monaco.editor.createModel(code, language)，会自动分配一个uri
    // createModel(code: 编辑器上显示的内容, language:自定义语言, uri:model的唯一标识符,不代表编辑会实时自动保存到本地文件)

    // 标记样式
    // monaco.editor.setModelMarkers(model, 'MacroLang', [
    //     {
    //     startLineNumber: 2,
    //     endLineNumber: 2,
    //     startColumn: 1,
    //     endColumn: 10,
    //     severity: monaco.MarkerSeverity.Error,
    //     message: `语法错误`,
    //     }],
    // );

    let editor = monaco.editor.create(document.getElementById("MacroEdi"),
	{
		value: "",
	    // value: getcode(),
		language: "MacroLang",
        fontFamily: "微软雅黑",
        fontSize: 17,
        lineHeight: 25,
		lineNumbersMinChars: 5,
		theme: "MacroTheme",
        model: model,
        renderLineHighlight: "all",
        tabSize: 8,
	}
    );

    // 快捷键
    function bindKeyWithAction(editor, key) {
        // var position = editor.getPosition();
	    editor.addCommand(key, function () {
	        let flag = 'withdraw';
            var selection = editor.getSelection();
            for (let i =selection.startLineNumber; i<=selection.endLineNumber; i++) {
                if (!model.getLineContent(i).trim().match(/^#/)) {
                    flag = 'exegesis';
                }
            }
            if (flag == 'exegesis') {   // 注释
                let id = {major: 1, minor: 1}
                for (let j = selection.startLineNumber; j <= selection.endLineNumber; j++) {
                    var range = new monaco.Range(j, 1, j, 1);
                    var text = '# ';
                    var op = {identifier: id, range: range, text: text, forceMoveMarkers: true};
                    editor.executeEdits("my-source", [op]);
                }
            }else {   // 撤销注释
                for (let k = selection.startLineNumber; k <= selection.endLineNumber; k++) {
                    var text = model.getLineContent(k).replace('#', '').trim() + '\n';
                    var range = new monaco.Range(k, 1, k, 1);
                    editor.executeEdits('log-source', [{
                            identifier: 'event_id',
                            range: new monaco.Range(k, 1, k + 1, 1),
                            text: null,
                            // forceMoveMarkers:true
                        }]
                    );
                    var id = {major: 1, minor: 1};
                    var op = {identifier: id, range: range, text: text, forceMoveMarkers: true};
                    editor.executeEdits('', [op]);
                }
            }
            })
    };
    bindKeyWithAction(editor, monaco.KeyMod.CtrlCmd | monaco.KeyCode.US_SLASH)

    function getcode() {
         return ["Command：",
         "鼠标、键盘、画面","延迟",
        "（字符串）键",
        "如果、那么、否则、条件结束",
        "循环开始、直到、当、循环结束、继续、退出循环、退出所有循环",
        "起点、终点",
        "定义、变量",

        "Operation：",
        "左移、上移、下移、右移",
        "左键、右键",
        "上滚轮、下滚轮",
        "双击、拖动、移动到",
        "按下、持续、松开",
        "为、令",


        "Logic：",
        "不是",
        "而且   （不是并且）",
        "或者",

        "Arith：",
        "加、减、乘、除以",
        "大于、小于、等于",

        "Signal：",
        "左括号、右括号（中英）",

        "location：",
        "横坐标、纵坐标",
        "图中、图的、文字中",
        ].join("\n")
    }
});