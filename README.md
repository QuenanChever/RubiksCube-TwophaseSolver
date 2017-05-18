# RubiksCube-TwophaseSolver

## Overview 
This project implements the two-phase-algorithm in its fully developed form to solve Rubik's cube in Python. Though Python is much slower than for example C++ or even Java the implementation is sufficiently fast to solve random cubes in less than 20 moves on average on slow hardware like the Raspberry Pi3 within a few seconds.

If you just want to solve Rubik's cube and play around with its patterns [Cube Explorer](http://kociemba.org/cube.htm) may be the better choice. But if you want to get a better understanding of the two-phase-algorithm details, you work on a project to build a cube solving robot or you write software for an NxNxN cube and use the reduction method this may be the right place to look.

## Fork
This repository is forked from the Rubiks 3x3x3 solver created by Herbert Kociemba: [hkociemba/RubiksCube-TwophaseSolver](https://github.com/hkociemba/Rubiks2x2x2-OptimalSolver).
Unlike the original repository, this version is meant to be used from the command line.

## Setup
Make sure that you use Python 3. You must also have the numpy package installed:
```
sudo apt-get install python3-numpy
```
Then, you need to make the main script executable:
```
sudo chmod +x kociemba-3x3x3
```
To make the solver available on the command line, you must create a symlink (feel free to change the path if necessary):
```
sudo ln -s "$(pwd)/kociemba-3x3x3" /usr/local/bin/kociemba-3x3x3
```
There are several tables which must be created on the first run. These need about 80 MB disk space and it takes from about 1/2 to 6 hours to create them, depending on the hardware. You can generate these tables behorehand by executing this command:
```
kociemba-3x3x3 --init
```

## Usage
The following command returns a solving maneuver for the given cubestring:
```
kociemba-3x3x3 <cubestring>
```

For example:
```
$ kociemba-3x3x3 DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD
D2 R3 D3 F2 B1 D1 R2 D2 R3 F2 D3 F2 U3 B2 L2 U2 D1 R2 U1
```