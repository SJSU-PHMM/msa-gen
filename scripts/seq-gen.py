#!/usr/bin/python

import sys
import pandas as pd

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
def generate_map(file):
    global ascii_value
    file = open(file[0], 'r')
    Lines = file.readlines()
    # Strips the newline character
    for line in Lines:
        apiCall = line[0:line.find('(')]
        if apiCall not in seq_map:
            seq_map[apiCall] = chr(ascii_value)
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
    #api_csv(sys.argv[1:])
    main(sys.argv[1:])
