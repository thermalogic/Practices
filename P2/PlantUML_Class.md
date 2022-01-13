# PlantUML Class Diagrams

* [PlantUML: The Class Diagram ](https://plantuml.com/zh/class-diagram)

## The Class Diagram

```puml
class Compressor {
 + {static} devtype: str
 + {static} energy: str
 + name: str
 + iPort: Port[1]
 + oPort: Port[1]
 + portdict : dict port
 + ef: float
 + Wc: float
 + isos: float

 + {static} Compressor(dictDev)
 + balance()
 + state()
 + __str()__:str
}
note left of Compressor::devtype
  类属性，设备类型
end note
note left of Compressor::energy
  类属性，设备能量类型
end note
note left of Compressor::iPort
  设备的输入端口
end note
note left of Compressor::oPort
  设备的输出端口
end note
note right of Compressor::__str()__
  输出实例文本串
end note
```

![](img/plantuml-class.jpg)