#!/usr/bin/python

import sys
import os

#Update mapping to use only Characters and Numbers
#This helps in Substitution Matrix as well as in creating an MSA that encompasses all Characters. 
seq_map = {
            'AdjustTokenPrivileges': 'W',
            'AreAnyAccessesGranted': '*',
            'bind': '*',
            'CheckRemoteDebuggerPresent': '0',
            'connect': '*',
            'ConnectNamedPipe': '*',
            'ConnectServerWMI': '*',
            'Copy': '1',
            'CreateDirectory': '*',
            'CreateEvent': '*',
            'CreateFile': '*',
            'CreateFileMapping': '*',
            'CreateMutex': 'U',
            'CreateNamedPipe': '*',
            'CreateProcess': 'L',
            'CreateRemoteThread': '*',
            'CreateThread': 'K',
            'CreateToolhelp32Snapshot': 'M',
            'CryptDecrypt': '*',
            'CryptEncrypt': '*',
            'CryptHashData': '*',
            'DeleteFile': '*',
            'DeleteUrlCacheEntry': '*',
            'ExecQueryWMI': 'S',
            'ExitProcess': '2',
            'FindNextFile': '*',
            'FindWindow': 'T',
            'FreeLibrary': '*',
            'GetAsyncKeyState': '*',
            'GetComputerName': '*',
            'GetCurrentHwProfile': '*',
            'GetFileAttributes': '*',
            'GetForegroundWindow': '*',
            'GetKeyboardState': '*',
            'GetKeyState': '*',
            'GetModuleHandle': 'F',
            'GetProcessDEPPolicy': '8',
            'GetProcessImageFileName': 'Y',
            'GetSystemDefaultLangID': '*',
            'GetUserName': '*',
            'GetVolumeInformation': '*',
            'HttpOpenRequest': '*',
            'HttpSendRequest': '*',
            'InternetConnect': '*',
            'InternetOpen': '*',
            'InternetReadFile': '*',
            'InternetSetOption': '*',
            'IsDebuggerPresent': '*',
            'LdrFindEntryForAddress': 'E',
            'lstrcmpi': '5',
            'Move': '*',
            'NetLocalGroupDel': '*',
            'NetLocalGroupDelMembers': '*',
            'NtQueryInformationProcess': '*',
            'OpenFile': 'V',
            'OpenMutex': '*',
            'OpenProcess': 'I',
            'OpenProcessToken': 'H', 
            'OpenSCManager': 'Z',
            'OpenService': '7',
            'QueryFullProcessImageName': '4',
            'QueryProcessInformation': 'D',
            'QuerySystemInformation': 'G',
            'QueueUserAPC': 'Q',
            'ReadProcessMemory': 'A', 
            'RegCloseKey': 'R',
            'RegCreateKeyEx': '*',
            'RegEnumValue': 'O',
            'RegOpenKeyEx': 'P',
            'RegSetValueEx': '*',
            'RemoveDirectory': '*',
            'ResumeThread': 'N',
            'SetNamedSecurityInfo': '*',
            'SetSecurityInfo': '*',
            'SetTimer': '*',
            'Sleep': '3',
            'SuspendThread': 'X',
            'SystemParametersInfo': '9',
            'TerminateProcess': '6',
            'VirtualAllocEx': 'B',
            'VirtualQueryEx': 'C',
            'WriteProcessMemory': 'J',
            'SetProcessDEPPolicy':'*',
            'OutputDebugString':'*',
            'StartService':'*',
            'CreateService':'*',
            'ControlService':'*',
            'DeleteService':'*',
            'GetKeyboardLayoutList':'*',
            'GetWindowTextLength':'*',
            'SetWindowPos':'*',
            'DeviceIoControl':'*',
            'NtSetInformationThread':'*',
            'DeviceIoControl':'*'
        }


ascii_value = 33
#ascii_value = 86
#seq_map = {}

seq_len_lower_bound = 35
seq_len_upper_bound = 250

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
        if apiCall in seq_map:
            api_sequence.append(seq_map[apiCall])
        else:
            api_sequence.append('*')
            
    return api_sequence

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
                virus_name = inputfile[16:48]
            continue
        count += 1
        apiCall = line[0:line.find('(')]
        #print(apiCall)
        if apiCall in seq_map:
            seq = seq + seq_map[apiCall]
        else:
            seq = seq + '*'
        #If you need to truncate the files
        #if(count > 100):
            #break
        

   
    print(seq)
    


if __name__ == "__main__":
    #generate_map("./data/uniq_api.txt")
    #print(seq_map)
    #generate_map(sys.argv[1:])
    #api_csv(sys.argv[1:])
    main(sys.argv[1:])
