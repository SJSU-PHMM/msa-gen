import sys

#MSA you want to check to see if there is a mistake in the alignment
msa = """FGGDKN-----------B80DD-G---B------BB----BB--HDEBJNFGGDKNBDBEB9DFBHF-D-BDD-BTF4DBBI4DHDDIYDDH-BND-MBBGDDDHWW3B--BH----------------------D------------------------------EBDBBBHBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBDDBBBM------------GBXD-EEEEEEEEEEEEEEEEEG8DGGGDID4HDDBGGFGFBI-FHHFBFZ7QEELHDN3BGB7B3B2-66
FGGDKN-------F---B----F-B-HB--FFDN----EXBBBB-----------------9D--H------------------H-------B------------------B--GB--------B*GDD-GFD--DFFSSSSSSSSSSSSSS----F-----------------------------------------------------------------------------------------------------------------------------------------2*-6
FGGDKNXBFFB-------------B-HB--FFD-------BBB------------------9D--H------------------H-------B------------------B--GB--------B*GDD-GFD--DFFSSSSSSSSSSSSSS----F-----------------------------------------------------------------------------------------------------------------------------------------2*-6
FGGDKN--------------------HB------------BBB------------------9D-BH------------------H-------BB-----------------B--GB----FBFDB*GDD-GFD--DFFSSSSSSSSSSSSSS*---F-----------------------------------------------------------------------------------------------------------------------------------------2*-6
FGGDKN------------------B-HB------BB----BBB------------------9D--H------------------H-------BB--G----------3-M-B--GB3***F-F---GDDBG--BBD-----------------BIBF8--HZ7QBD------------------------------------------------------------------------------------------------------------------------------3-2--6
FGGDKN--------------------HB------BB----BBB------------------9D-BH------------------H-------BB--G----------3-M-B--GB3***F-F---GDDBG----D------------------------------------------------------------------B------------IBF8BBHZ7Q-D-------------------------------------------------------------------2--6
FGGDKN------------------B-HB------BB----BB-------------------9D-BH------------------H-------BB--G--B-------3-M-B--GB3***F-F---GDDBG----D------------------------------------------------------------------B------------I-F8B-HZ7Q-D-------------------------------------------------------------------2--6
FGGDKN------*FHG----DD--B8-B*-----BB----BB-------------------9DFBH------------------H--------------B-------3--3B--GB------F------B-----D------------------------------------------------------------------B-----------------------DG---B-------------------D---D---------F-F--*F----------------------2*-6
FGGDKN------*FHG----DD--B8-B------BB----B--------------------9DFBH------------------H--------B-----B-------3--3B--GB------F------B-----D------------------------------------------------------------------B-----------------------DG--D--------------------D-------------F-F--*F----------------------2*-6
FGGDKN-------FHG----DD--B--B------BB----B--------------------9DFBH------------------H--------B-------------3--3B-BGB------F------B-----D------------------------------------------------------------------B-----------------------DG--D--------------------D-------------F-F--*F----------------------2*-6"""

if len(sys.argv) == 2: 
    #will take in parameter for file to check
    with open(sys.argv[1], 'r') as file:
        msa = file.read()
    #msa = str(sys.argv[1])
msa_validator = msa.split('\n')
for index in range(len(msa_validator[0])):
    new_char = msa_validator[0][index]
    for seq_index in range(1, len(msa_validator)-1):
        if msa_validator[seq_index][index] in '-':
            #can never cause conflicts as it is a spacer character
            continue
        if msa_validator[seq_index][index] not in new_char:
            if new_char in '-':
                new_char = msa_validator[seq_index][index]
            else:
                print("Alignment Conflict found at column " + str(index+1) + " with characters:"+new_char+","+msa_validator[seq_index][index])
    #print(msa[index])
    pass
