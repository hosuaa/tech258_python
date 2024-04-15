# JSON

## What is it?

JS - JavaScript <br>
O - Object <br>
N - Notation

JSON is a syntax for exchanging data between a client/browser and server.

It is really popular because it is considered system agnostic. It doesn't really matter what the two systems are written
in; they can both exchange JSON

Documentation can be found [here](https://www.json.org/).

Documentation for working with JSON found [here](https://docs.python.org/3/library/json.html)

## JSON syntax

Data is in name/value pairs (similar to python dictionaries):
```json
"Name":"Value"
```
Curly braces hold objects:
```json
{"Name":"Value"}
```
Data can be seperated by commas:
```json
{"Name":"Value", "Name2":"Value2"}
```
Square brackets can be used for arrays (lists):
```json
{"Name":["Value1", "Value2"]}
```