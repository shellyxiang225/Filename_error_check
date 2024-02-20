# CheckError使用说明
## 使用的库
### 用于遍历文件夹，得到文件属性的库
datetime os pathlib filedialog
### 用于构建GUI界面并将文件属性写入界面的库
Thread
queue
tkinter
ttkbootstrap 
### 用于判断文件名是否合法的库
re
openpyxl

## 运行方式
请点击名为CheckError的exe文件，跳出选框，分别在文本框输入内容后进行点选，可在树形图中得到文件列表
下方的格式检查按钮，选择文件夹后，根据正则表达式对文件名进行判断，并生成excel文件。

**需要注意**

1. ttkbootstrap 自带的树形图现行只能在传入固定数据时建立鼠标点击事件。
想要识别导入需要换库。
2. 由于语法不一致，本程序同时使用了tkinter ttkbootstrap库，尚不清楚是否会冲突
3. 此外由于链接excel使用的是openpyxl，暂时无法批量将文件路径在列表中生成超链接，还需用户手动在excel中添加函数
4. 打开程序时请注意**是否已经点开excel文件**，否则将无法正常写入，并报错文件损坏