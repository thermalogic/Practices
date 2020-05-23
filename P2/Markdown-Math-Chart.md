

# Enhanced Markdown 

## Math

$X^{34}$


## Flowchart

* flowchart: https://github.com/adrai/flowchart.js

### Example1

```flow
st=>start
e=>end
op1=>operation: My Operation
st->op1->e
```

### Example2

```flow
st=>start
ed=>end
op1=>operation: My Operation
isCnd=>condition: if i>0
responseTrue=>operation: Operation on True
responseFalse=>operation: Operation on False

st->op1->isCnd

isCnd(yes)->responseTrue->ed
isCnd(no)->responseFalse->ed
```