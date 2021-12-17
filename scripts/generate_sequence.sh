#!/bin/bash

<<<<<<< HEAD
find data/winwebsec/ -iname "log_api.txt"  -exec python scripts/seq-gen.py {} \; &> data/sequences/winwebsec_ver2.txt
find data/harebot/ -iname "log_api.txt"  -exec python scripts/seq-gen.py {} \; &> data/sequences/harebot_ver2.txt
find data/smarthdd/ -iname "log_api.txt"  -exec python scripts/seq-gen.py {} \; &> data/sequences/smarthdd_ver2.txt
find data/cridex/ -iname "log_api.txt"  -exec python scripts/seq-gen.py {} \; &> data/sequences/cridex_ver2.txt
find data/Injector_Trojan/ -iname "log_api.txt"  -exec python scripts/seq-gen.py {} \; &> data/sequences/Injector_Trojan_ver2.txt
find data/zbot/ -iname "log_api.txt"  -exec python scripts/seq-gen.py {} \; &> data/sequences/zbot_ver2.txt
find data/zeroaccess/ -iname "log_api.txt"  -exec python scripts/seq-gen.py {} \; &> data/sequences/zeroaccess_ver2.txt
find data/securityshield/ -iname "log_api.txt"  -exec python scripts/seq-gen.py {} \; &> data/sequences/securityshield_ver2.txt
find data/trojan/ -exec python scripts/seq-gen.py {} \; &> data/sequences/trojan_ver2.txt
find data/obfuscationLogs/ -iname "log_api.txt" -exec python scripts/seq-gen.py {} \; &> data/sequences/enigma_protect.txt
find data/appLogs/ -exec python scripts/seq-gen.py {} \; &> data/sequences/app_trunc100.txt
find data/ransom/ -iname "log_api.txt"  -exec python scripts/seq-gen.py {} \; &> data/sequences/ransom_ver2.txt
=======
find ../data/winwebsec/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/winwebsec_ver2.txt
find ../data/harebot/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/harebot_ver2.txt
find ../data/smarthdd/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/smarthdd_ver2.txt
find ../data/cridex/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/cridex_ver2.txt
find ../data/Injector_Trojan/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/Injector_Trojan_ver2.txt
find ../data/zbot/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/zbot_ver2.txt
find ../data/zeroaccess/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/zeroaccess_ver2.txt
find ../data/securityshield/ -iname "log_api.txt"  -exec python seq-gen.py {} \; &> ../data/sequences/securityshield_ver2.txt
find ../data/trojan/ -exec python seq-gen.py {} \; &> ../data/sequences/trojan_ver2.txt

find ../data/obfuscationLogs/enigma_protect/ -iname "log_api.txt" -exec python seq-gen.py {} \; &> ../data/sequences/enigma_protect.txt

find ../data/obfuscationLogs/enigma_protect/cridex_protected/ -iname "log_api.txt" -exec python seq-gen.py {} \; &> ../data/sequences/cridex_protect.txt
find ../data/obfuscationLogs/enigma_protect/harebot_protected/ -iname "log_api.txt" -exec python seq-gen.py {} \; &> ../data/sequences/harebot_protect.txt
find ../data/obfuscationLogs/enigma_protect/winwebsec_protected/ -iname "log_api.txt" -exec python seq-gen.py {} \; &> ../data/sequences/winwebsec_protect.txt
find ../data/obfuscationLogs/enigma_protect/zbot_protected/ -iname "log_api.txt" -exec python seq-gen.py {} \; &> ../data/sequences/zbot_protect.txt
find ../data/obfuscationLogs/enigma_protect/zeroaccess_protected/ -iname "log_api.txt" -exec python seq-gen.py {} \; &> ../data/sequences/zeroaccess_protect.txt
>>>>>>> 404048e (update sequence shell script)
