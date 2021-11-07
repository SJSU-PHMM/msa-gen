virusFamily = "consolidated"

pairs ={
	"pair1":{
		"8":"FGGDKNHB8-0DDGBBBVBVB-B-H---DEJNFGGDKNCCCBDBEV*VB9DFBHFDBDDTFV4DBBBI4DAAAHDDIYDADAHBNDMBAAAAAAAAAAAAAAAAAA",
		"9":"FGGDKNH-8C0DDGBBBV-VBFBBHFFBDEJNFGGDKNCCCBDBEV*VB9DFBHFDBDDTFV4DBBBI4DAAAHDDIYDADAHBNDMB----AAAAAAAAAAAAAA"
	},
	"pair2":{
		"8":"FGGDKN-------HB8-0DDGBBBVBVBBHDEJNFGGDKNCCCBD---BEV*VB9DFBHFDBDDTFV4DBBBI4DAAAHDDIYDADAHBNDMBAAAAAAAAAAAAAAAAAA",
		"4":"FGGDKNEBPBBBB-B8C0DDGBBBV-VBBHDEJNFGGDKNCCCBDBBBBEV*VB9DFBHFDBDDTFV4D---I4DAAAHDDIYDADAHBNDMBAAAAAAAAAAAA------"
	},
   "pair3":{
		"4":"FGGDKNEBPBBBBB8C0DDGBBBVVBBHDEJNFGGDKNCCCBDBBB-BEV*VB9DFBHFDBDDTFV4DI4DAAAHDDIYDADAHBNDMBAAAAAAAAAAAA----------------------------------",
		"6":"FGGDKN-------B8-0DDGBBB--BBHDEJNFGGDKN---B-BBBDBE---B9DFBHFDBDDTF-4DI4D---HDDIYD-D-HBNDMB------------BGDDDHWW3BHDEBDBBBHBBBBBBBBBBBBBBB"
	},
	"pair4":{
		"4":"FGGDKNEBPBBBBB8C0-------------------DDG-------BB---B-VVBBHD-EJN---------FGGDKNCCCBDB---BBBEV*VB9DFBHFDBDDTFV4DI4DAAA---HDDIYDADAHBNDMBAAAAAAAAAAAA------------",
		"5":"FGGDKN-B-BBBBB---BBHHEFFFFFFFFFFFFHGDD-*H*UUVFBB1FHBLVV---DCEJN**LVDJN26FGGDKN---B-BEEEBBB----B---B---B---F---------EKEH--------HB---B------------EBFFFEFFFFFF"
	},
	
	"pair5":{
		"2":"FGGDKNB----------H----------BBBB-B--9D-BHHB--BG-----------------B3--MBGB3***FFGDD-----BG-D-BIF8-B--HZ7QD26---------------",
		"6":"FGGDKNB80DDGBBBBBHDEJNFGGDKNBBBBDBEB9DFB-H-FDB-DDTF4DI4DHDDIYDDHB-NDMB-B------GDDDHWW3B-HDEB---DBBBH------BBBBBBBBBBBBBBB"
	},
	"pair6":{
		"1":"FGGDKNFFBBHBFFDNEXBBBB9D-HHBBGB--B---*----GDD-GFDDFFSSSSSSSSSSSSSS--F-------2*6",
		"2":"FGGDKN---BHB------BBBB9DBHHBBGB3MBGB3***FFGDDBG--D----------------BIF8BHZ7QD2-6"
	},
	"pair7":{
		"0":"FGGDKNB-B3BBBB--B--BB-B--B-B-**-FFHGDDH*BDRHHRRDRDMBGBGBBGCOORRIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIDAI-I-------DAI--",
		"2":"FGGDKNBHB-BBBB9DBHHBBGB3MBGB3***FF-G-----------D-D------BG----------------------------------------------D--BIF8BHZ7QD--26"
	},
	"pair8":{
		"2":"FGGDKNBHBBBB--B9DBHHBBGB3MBGB3***-FFGDDBGDBIF8BHZ7QD2--------6",
		"7":"FGGDKN------VVB--B-HBB-B--B-B----BFF---B--B-F------D-DH3HW*G36"
	},
	"pair9":{
		"3":"FGGDKN--BH-HBBFHBBBBHG-----DD---W*FFUMBGB5555555555555555555555555555555555555555555555555555555555555555555555--",
		"7":"FGGDKNVVB-BHBB--BBBB--FFBBFDDH3HW*-----G-----------------------------------------------------------------------36"
	}
}

def addGap(seq, position):
    return seq[:position] + '-'+seq[position:]


#Send sequence pairs in dictionary (pair1 to pair 10 in order)
def msaGen(pairs):
      
    #Initialize msa with 1st pair
    
    msa = {} 
    
    for pairsKey in pairs:
        if(pairsKey == "pair1"):
            msa = pairs[pairsKey]
        else:
            pairSeqList = list(pairs[pairsKey].keys())
            print(pairSeqList)
            # If First seq in pair is present in msa
            if(pairSeqList[0] in msa):
                refSeq = 0
                addSeq = 1
            else:
                refSeq = 1 
                addSeq = 0
            
            msaSeqLen = len(msa[pairSeqList[refSeq]])
            pairSeqLen = len(pairs[pairsKey][pairSeqList[refSeq]])
            print(msa[pairSeqList[refSeq]])
            print(pairs[pairsKey][pairSeqList[refSeq]])
            seqLength = max(msaSeqLen,pairSeqLen)
            i=0
            print("Index of pair:"+pairSeqList[refSeq])
            msaSeqStr = msa[pairSeqList[refSeq]]
            print(msaSeqLen)
            print(pairSeqLen)
            while ((i < msaSeqLen) or (i < pairSeqLen)):
                msaSeqStr = msa[pairSeqList[refSeq]]
                pairSeqStr = pairs[pairsKey][pairSeqList[refSeq]]
                if(i== pairSeqLen):
                    numberOfGaps = msaSeqLen-pairSeqLen
                    gapsAdded=0
                    newSeqToBeAdded=pairs[pairsKey][pairSeqList[addSeq]]
                    while (gapsAdded < numberOfGaps):
                        newSeqToBeAdded = newSeqToBeAdded + "-"
                        gapsAdded = gapsAdded+1
                    pairs[pairsKey][pairSeqList[addSeq]]=newSeqToBeAdded
                    break
                else:
                    if(i == msaSeqLen):
                        numberOfGaps = pairSeqLen - msaSeqLen
                        for msaKey in msa:
                            msaSeqStri = msa[msaKey] 
                            gapsAdded=0
                            while (gapsAdded < numberOfGaps):
                                msaSeqStri = msaSeqStri + "-"
                                gapsAdded = gapsAdded+1
                            msa[msaKey]=msaSeqStri
                        break
                        
                            
                if (msaSeqStr[i] == pairSeqStr[i]):
                    i=i+1
                else:
                    if (msa[pairSeqList[refSeq]][i] =='-'): 
                        pairs[pairsKey][pairSeqList[refSeq]]=addGap(pairSeqStr,i)
                        pairs[pairsKey][pairSeqList[addSeq]]=addGap(pairs[pairsKey][pairSeqList[addSeq]],i)
                        pairSeqLen=pairSeqLen+1
                        print(pairSeqLen)
                    else:
                        for msaKey in msa:
                            msa[msaKey]=addGap(msa[msaKey],i)
                        msaSeqLen=msaSeqLen+1
                    i=i+1
            msa[pairSeqList[addSeq]]=pairs[pairsKey][pairSeqList[addSeq]]
                    
    msaFile = open("./data/msa/"+virusFamily+"_msa.txt", "w")
    for finalKey in sorted(msa):                
        msaFile.write(finalKey+" ==> "+msa[finalKey]+"\n")
    
msaGen(pairs)




    