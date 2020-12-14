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
![](https://raw.githubusercontent.com/pmqtt/IntelliType/master/Images/IntelliType.gif)


`$>itt scirpt.yaml`

### The script
#### About YAML syntax for scripts
Script files use YAML syntax, and must have either a .yml or .yaml file extension. 
If you're new to YAML, see [Learn YAML in five minutes](https://www.codeproject.com/Articles/1214409/Learn-YAML-in-five-minutes).

#### scene
**scene** defines which program should be 
executed and allows to prepare a waiting
 time before the action starts

#### sections
**sections** defines what should be automated. You define your section names in a YAML-list, you can define them as you like! Each section defines control properties 
of the automation process. You can control the process with the following properties:
* **keypseed:** Controls the typing speed. Allowed values are **Fast, MEDIUM, SLOW, HUMAN or a TIME**.
* **Text:** The text to enter. In Yaml you can force line breaks with "|".
* **cmd:** Write a text with line break
* **ctrl:** Trigger control keys. For example Ctrl+c, ESC, Ctrl+Shift+t
* **wait:** Wait before the next section is executed 

#### Sample
```shell
scene:
  program: open -a Terminal "`pwd`"
  wait: 13s
  countdown: true
sections:
  initial_vi:
    - keyspeed: MEDIUM
    - cmd: vi IntelliType.cpp
    - ctrl: i
  write_lorem_ipsum:
    - keyspeed: FAST
    - text: |
        #include <iostream>
        using namespace std;
        int main(int argc,char**argv){
        std::cout<<"Lorem ipsum dolor sit amet, consetetur sadipscing elitr,";
        std::cout<<"sed diam nonumy eirmod tempor invidunt ut";
        std::cout<<"labore et dolore magna aliquyam erat, sed diam voluptua. ";
        return 0;
        }
  close_vi:
    - ctrl: ESC
    - wait: 1s
    - cmd: ":q!"
```
