
file_input = "./data/sequences/ver2_allsequences.txt"
seqFile = open(file_input, 'r') 
seqLines = seqFile.readlines()

truncatedFile = open("./data/sequences/ver2_allsequences_truncated.txt", 'w')

for line in seqLines:
  startIndex = line.find(": ")+2
  truncLine = line[startIndex:startIndex+100]
  if "\n" not in truncLine:
    truncLine = truncLine + "\n"
  truncatedFile.writelines(truncLine)

  