# IntelliType
### Automate the typing process
The goal of IntelliType is to help you automate text-based processes. Create your script and see how it is executed. Then make a recording for example with a program of your choice, without having to start all over again


## Getting Started
### Installation
To get started
1. install python >=3
2. install pip
3. `pip install IntelliType`

### Usage
![Description](https://raw.githubusercontent.com/pmqtt/IntelliType/master/Images/IntelliType.gif)


`$>itt scirpt.yaml`

### The script
#### About YAML syntax for scripts
Script files use YAML syntax, and must have either a .yml or .yaml file extension. 
If you're new to YAML, see [Learn YAML in five minutes](https://www.codeproject.com/Articles/1214409/Learn-YAML-in-five-minutes).

#### scene
**scene** defines which program should be 
executed and allows to prepare a waiting
 time before the action starts

#### section name
**section** defines what should be automated. With the following properties, you can control the process:
* **keypseed:** Controls the typing speed. Allowed values are **FAST, MEDIUM, SLOW or HUMAN**
* **text:** The text to type. In Yaml you can use "|" to force line breaks
* **cmd:** Write a text with return
* **ctrl:** Trigger control keys. For example ctrl+c, ESC, ctrl+shift+t
* **wait:** Wait before the next section is executed 

#### Sample
```shell
scene:
  program: gedit
  wait: 5s
  countdown: true

section 0:
  keyspeed: MEDIUM
  cmd: vi main.cpp

section 1:
  ctrl: i

section 2:
  keyspeed: FAST
  text: |
    Write a text
    with linebreaks

section 3:
  ctrl: ESC
  wait: 1s

section 4:
  cmd: ":q!"
```
