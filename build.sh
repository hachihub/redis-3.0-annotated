#!/usr/bin/env sh

make clean
make 
make PREFIX=`pwd` install
