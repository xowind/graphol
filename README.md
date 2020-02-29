
# graphol

graphol means Graph On Line. Drawing graph or charts with Markdown.

## Install

`docker build -t graphol .`

`docker run -d --name graphol -p 12580:80 graphol`

## Usage

### Sample 1
```
<img src='http://127.0.0.1:12580/g?
  digraph G {
    aize ="4,4";
    main [shape=box];
    main -> parse [weight=8];
    parse -> execute;
    main -> init [style=dotted];
    main -> cleanup;
    execute -> { make_string; printf}
    init -> make_string;
    edge [color=red];
    main -> printf [style=bold,label="100 times"];
    make_string [label="make a string"];
    node [shape=box,style=filled,color=".7 .3 1.0"];
    execute -> compare;
  }
'>
```
![sample1](./doc/sample1.png)

### Sample 2
```
<img src='http://127.0.0.1:12580/g?
@startuml;
actor User;
participant "First Class" as A;
participant "Second Class" as B;
participant "Last Class" as C;
User -> A: DoWork;
activate A;
A -> B: Create Request;
activate B;
B -> C: DoWork;
activate C;
C --> B: WorkDone;
destroy C;
B --> A: Request Created;
deactivate B;
A --> User: Done;
deactivate A;
@enduml
'>
```
![sample2](./doc/sample2.png)
