## Practice 2(12)

**Object-oriented Programming**：The  vapor-compression refrigeration cycle simulator 

**Deadline:**  2023.05.27

## 地源热泵循环分析

以[SimVCCE](https://gitee.com/thermalogic/simvcce)中的Python语言版本为基础进行设计，使其可计算如下地源热泵循环(Page670 Ex11-43)

A heat pump with R134a as the working fluid is used to keep a space at `25°C` by **absorbing heat from geothermal water** that enters the evaporator at `50°C` at a rate of `0.065 kg/s` and leaves at `40°C`. 

The refrigerant enters the evaporator at `20°C` with a quality of `23 percent` and leaves at the inlet pressure as saturated vapor. 

The refrigerant **loses `300 W` of heat to the surroundings** as it flows through the compressor and the refrigerant leaves the compressor at `1.4 MPa` at the same entropy as the inlet.

**Determine**

1. the degrees of subcooling of the refrigerant in the condenser (`3.8°C`)
2. the mass flow rate of the refrigerant (`0.0194 kg/s`)
3. the heating load and the COP of the heat pump (`3.07kW, 4.68`)
4. the theoretical minimum power input to the compressor for the same heating load (`0.238kW`)

![](./img/heatpump_11_43.jpg)

## 编码(6分)

* 增加设备类： evaporator absorbing heat from geothermal water 

![](./img/evaporator_hp.jpg)

* Condenser类：增加the degrees of subcooling of the refrigerant计算
* VCCycle类：增加the theoretical minimum power input计算

#### 编码提示

```python
"""
EvaporatorHeatExchange

the combined evporator and the water duct

                         ↓   iPort refrigerant
                   ┌─────┼─────┐
                   │ → ┌─┼─┐←  │
        oPortW   ← ┤ Q │ Z │ Q │← iPortW
                   │ → └─┼─┘←  │
                   └─────┼─────┘
                         ↓      oPort refrigerant

json example
 {
            "name": "Evaporator",
            "devtype": "EVAPORATOR_HEAT_EXCHANGER",
            "iPort": {},
            "oPort": {
                "x": 1.0
            },
            "iPortW": {
                "p": 0.1,
                "t": 50.0,
                "mdot":0.065,
                "refrigerant": "WATER"
            },
            "oPortW": {
                "p": 0.1,
                "t": 40.0,
                "refrigerant": "WATER"
            }
        }
"""
from components.port import Port

class EvaporatorHeatExchanger:

    energy = "QIN"
    devtype = "EVAPORATOR_HEAT_EXCHANGER"

    def __init__(self, dictDev):
        """ Initializes the EVAPORATOR_HEATIN_EXCHANGER """
        self.name = dictDev['name']
        self.iPort = Port(dictDev['iPort'])
        self.oPort = Port(dictDev['oPort'])
        self.iPortW = Port(dictDev["iPortW"])
        self.oPortW = Port(dictDev["oPortW"])
```

## 循环json文件(1分)

* compressor有散热

## Markdown文档(5分)

* 设计方案
  * 端口、设备、连接器、循环分析类设计（含UML类图）
  * 端口连接、端口物性计算、循环计算等算法(含算法流程图)
  * 循环json数据文件设计：端口、热泵设备、端口连接关系等
  
* 小结：
   * 练习中遇到的问题、解决过程和方法


#### 文档提示

* 数学公式使用：`LaTex` 

* UML、流程图使用: [PlantUML文本描述](https://gitee.com/thermalogic/simvcce/tree/B2023/uml)

#### 安装软件

VSCode插件

* [Markdown Preview Enhanced](https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/)

* [PlantUML](https://github.com/qjebbs/vscode-plantuml/)

PlantUML

* [Java](https://www.java.com/en/download/) Platform for PlantUML running.

* [Graphviz](https://graphviz.org) PlantUML requires it to calculate positions in diagram.

  
### 工作目录

```txt
 
|── <P2>
     │ 
     │── README.md: Markdown文档
     | 
     |── <img> Markdown文档使用的图形文件
     |
     |── vccapp_json.py
     |
     |── <components> 
     |
     |── <vcc> 
     |
     |── <jsonmodel> 循环json数据文件
     |
     |── <result> 计算结果数据文件 
```  

## 提交：

* 电邮： cmh@seu.edu.cn
  * 主题：学号-姓名-2
  * 附件：工作目录压缩文件： **学号-姓名-2.zip** 其中，必须有**计算结果文件**

 