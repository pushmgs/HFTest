# HFTest

HFTest is a tool to assist the micro-optimization of HFT hot-path code by feeding market-based simulations into any codebase using binary instrumentation.

## Features being implemented
* Ability to map simulated data into any internal format
* View callstacks between orders placed
* Full visual of hotpath disassembly
* Visuals on how certain data impacts a given hotpath by comparing things such as instruction count

## Requirements
HFTest requires Python 3.6 or greater.
```
pip3 install -Ur requirements.txt
```