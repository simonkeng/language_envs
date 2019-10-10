#!/bin/bash

build_image () {
    exec docker build -t rust_dev .
}

run_rust () {
    exec docker run -it -v $(pwd):/tmp bash
}