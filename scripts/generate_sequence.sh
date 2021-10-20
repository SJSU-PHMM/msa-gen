#!/bin/bash

find ../data/winwebsec/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/winwebsec_ver2.txt
find ../data/harebot/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/harebot_ver2.txt
find ../data/smarthdd/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/smarthdd_ver2.txt
find ../data/cridex/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/cridex_ver2.txt
find ../data/Injector_Trojan/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/Injector_Trojan_ver2.txt
find ../data/zbot/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/zbot_ver2.txt
find ../data/zeroaccess/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/zeroaccess_ver2.txt
find ../data/trojan/ -exec python seq-gen.py {} \; &> ../data/sequences/trojan_ver2.txt
