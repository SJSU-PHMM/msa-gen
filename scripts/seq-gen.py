#!/usr/bin/python

import sys
import os
import pandas as pd

seq_map =  {
            'AdjustTokenPrivileges': '!',
            'AreAnyAccessesGranted': '\"',
            'bind': '#',
            'CheckRemoteDebuggerPresent': '$',
            'connect': '%',
            'ConnectNamedPipe': '&',
            'ConnectServerWMI': '\'',
            'Copy': '(',
            'CreateDirectory': ')',
            'CreateEvent': '*',
            'CreateFile': '+',
            'CreateFileMapping': '-',
            'CreateMutex': '.',
            'CreateNamedPipe': '/',
            'CreateProcess': '0',
            'CreateRemoteThread': '1',
            'CreateThread': '2',
            'CreateToolhelp32Snapshot': '3',
            'CryptDecrypt': '4',
            'CryptEncrypt': '5',
            'CryptHashData': '6',
            'DeleteFile': '7',
            'DeleteUrlCacheEntry': '8',
            'ExecQueryWMI': '9',
            'ExitProcess': ':',
            'FindNextFile': ';',
            'FindWindow': '<',
            'FreeLibrary': '=',
            'GetAsyncKeyState': '>',
            'GetComputerName': '?',
            'GetCurrentHwProfile': '@',
            'GetFileAttributes': 'A',
            'GetForegroundWindow': 'B',
            'GetKeyboardState': 'C',
            'GetKeyState': 'D',
            'GetModuleHandle': 'E',
            'GetProcessDEPPolicy': 'F',
            'GetProcessImageFileName': 'G',
            'GetSystemDefaultLangID': 'H',
            'GetUserName': 'I',
            'GetVolumeInformation': 'J',
            'HttpOpenRequest': 'K',
            'HttpSendRequest': 'L',
            'InternetConnect': 'M',
            'InternetOpen': 'N',
            'InternetReadFile': 'O',
            'InternetSetOption': 'P',
            'IsDebuggerPresent': 'Q',
            'LdrFindEntryForAddress': 'R',
            'lstrcmpi': 'S',
            'Move': 'T',
            'NetLocalGroupDel': 'U',
            'NetLocalGroupDelMembers': 'V',
            'NtQueryInformationProcess': 'W',
            'OpenFile': 'X',
            'OpenMutex': 'Y',
            'OpenProcess': 'Z',
            'OpenProcessToken': '[',
            'OpenSCManager': '\\',
            'OpenService': ']',
            'QueryFullProcessImageName': '^',
            'QueryProcessInformation': '_',
            'QuerySystemInformation': '`',
            'QueueUserAPC': 'a',
            'ReadProcessMemory': 'b',
            'RegCloseKey': 'c',
            'RegCreateKeyEx': 'd',
            'RegEnumValue': 'e',
            'RegOpenKeyEx': 'f',
            'RegSetValueEx': 'g',
            'RemoveDirectory': 'h',
            'ResumeThread': 'i',
            'SetNamedSecurityInfo': 'j',
            'SetSecurityInfo': 'k',
            'SetTimer': 'l',
            'Sleep': 'm',
            'SuspendThread': 'n',
            'SystemParametersInfo': 'o',
            'TerminateProcess': 'p',
            'VirtualAllocEx': 'q',
            'VirtualQueryEx': 'r',
            'WriteProcessMemory': 's',
            'SetProcessDEPPolicy':'t'
        }

ascii_value = 33
#ascii_value = 86
#seq_map = {}

"""
Simple function to automatically map system calls to a unique ASCII character
"""
def generate_map(virus_data):
    global ascii_value
    file = open(virus_data, 'r')
    Lines = file.readlines()
    # Strips the newline character
    for line in Lines:
        apiCall = line[0:line.find('(')]
        if apiCall not in seq_map:
            seq_map[apiCall] = chr(ascii_value)
            ascii_value += 1
            if ascii_value == 44:
                #skip comma because we may not want to use it to make saving to csv funky
                ascii_value += 1

"""
use pandas to take an API sequence and save to a CSV to be read by aphid or some PHMM algorithm
"""
def api_csv(arg1):
    """TODO: Docstring for api_csv.

    :arg1: TODO
    :returns: TODO

    """
    api_sequence = []
    api_sequence = parse_virus_log(arg1)
    #df = pd.DataFrame(api_sequence, columns=['Sequence'], index=['virus1', 'virus2'])
    #df = pd.DataFrame(api_sequence, columns=['API Sequence'])
    df = pd.DataFrame(api_sequence)
    df.to_csv('api_seq.csv', mode='a', header=True)
    pass

def parse_virus_log(argv):
    inputfile = argv[0]
    file1 = open(inputfile, 'r')
    Lines = file1.readlines()
    api_sequence = []
    # Strips the newline character
    for line in Lines:
        apiCall = line[0:line.find('(')]
        api_sequence.append(seq_map[apiCall])
    return api_sequence

    print(" ")
    print(" ")
    print("Getting Sequence...")
    print('Final Sequence: '+seq)
    print(" ")
    print(" ")

def main(argv):
    inputfile = argv[0]
    file1 = open(inputfile, 'r')
    Lines = file1.readlines()
    seq = ''
    virus_name = ''
    count = 0
    # Strips the newline character
    #print(seq_map);
    for line in Lines:
        if "Executing: " in line:
            #Pretty sureExecuting is a Sandboxie/BSA message, not from the Malware itself
            #will use it to grab malware name
            if not virus_name:
                virus_path = line.split("\\")[-1]
                virus_name = os.path.basename(virus_path).strip()
            continue
        count += 1
        apiCall = line[0:line.find('(')]
        #print(apiCall)
        seq = seq + seq_map[apiCall]

    #print(" ")
    #print(" ")
    #print("Getting Sequence...")
    print(virus_name+': '+seq)
    #print('Final Sequence: '+seq)
    #print(" ")
    #print(seq_map)
    #print(" ")
    #print(" ")


if __name__ == "__main__":
    #generate_map("./data/uniq_api.txt")
    #print(seq_map)
    #generate_map(sys.argv[1:])
    #api_csv(sys.argv[1:])
    main(sys.argv[1:])
