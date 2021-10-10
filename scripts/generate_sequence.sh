#!/bin/bash

find ../data/winwebsec/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/winwebsec.txt
find ../data/harebot/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/harebot.txt
find ../data/smarthdd/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/smarthdd.txt
find ../data/zeroaccess/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/zeroaccess.txt
find ../data/cridex/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/cridex.txt
find ../data/Injector_Trojan/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/Injector_Trojan.txt
find ../data/zbot/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/zbot.txt
find ../data/trojan/ -exec python seq-gen.py {} \; &> ../data/sequences/trojan.txt
