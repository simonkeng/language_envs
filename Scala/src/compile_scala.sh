#!/usr/bin/env bash

# compile
scalac helloworld.scala 

# or compile to java executible
scalac helloworld.scala -d hello.jar

# execute with:
scala helloworld.scala
# or 
scala hello.jar