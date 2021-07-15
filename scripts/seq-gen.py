#!/usr/bin/python

import sys

seq_map = {
    'GetModuleHandle': 'AA',
    'QuerySystemInformation': 'AB',
    'QueryProcessInformation': 'AC',
    'CreateThread':	'AD',
    'ResumeThread':	'AE',
    'VirtualAllocEx': 'AF',
    'LdrFindEntryForAddress': 'AG',
    'OpenProcessToken':	'AH',
    'TerminateProcess': 'AI',
    'CreateProcess': 'AJ',
    'WriteProcessMemory': 'AK',
    'AdjustTokenPrivileges': 'AL',
    'GetUserName': 'AM',
    'SystemParametersInfo': 'AN',
    'OpenProcess': 'AO',
    'GetProcessDEPPolicy': 'AP'
}

#ascii_value = 33
ascii_value = 65
#seq_map = {}

"""
Simple function to automatically map system calls to a unique ASCII character
"""
def generate_map(argv):
    global ascii_value
    file = open(argv[0], 'r')
    Lines = file.readlines()
    seq = ''
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        apiCall = line[0:line.find('(')]
        if apiCall not in seq_map:
            seq_map[apiCall] = chr(ascii_value)
            ascii_value += 1

def main(argv):
    inputfile = argv[0]
    file1 = open(inputfile, 'r')
    Lines = file1.readlines()
    seq = ''
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        apiCall = line[0:line.find('(')]
        seq = seq + seq_map[apiCall]

    print(" ")
    print(" ")
    print("Getting Sequence...")
    print('Final Sequence: '+seq)
    print(" ")
    print(" ")


if __name__ == "__main__":
    #generate_map(sys.argv[1:])
    main(sys.argv[1:])
