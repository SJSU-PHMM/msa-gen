Script to generate sequence from API call log
======================

## What does this project do? ##
This is a Python project to generate MSA from Virus API Logs.

#### Steps ####
~~~
    1. Load the log files generated from Buster Sandboxie Analyzer to ./data/ folder
    2. Run generate_seqence.sh shell script to run seq-gen.py script to translate API call logs to sequences.
    3. Shortlist 10 sequences which encompasses all symbols used to derive MSA
    4. Construct pairwise alignment using pairwise.py. Ensure you update the sequences and virusFamily name within pairwise.py file
        ```
        python3 scripts/pairwise.py
        ```
    5. You will have the pairsewiseAlignment for sequences in ./scripts/results/pairwiseAlign_virusFamily.txt
    6. Update the score in minSpanningTree.py and run this python script to generate minSpanningTree. Please note that this uses Kruskal Algorithm for minimum spanning tree and hence ensure you reverse the positive score to negative and vice-versa, since you want the maximum score to have higher precedence. 
        ```
        python3 scripts/minSpanningTree.py
        ```
    7. Once the MST edges are known pick up the edges to construct a pairs dictionary object representing the spanning tree for MSA derivation. 
    8. Final step is to generate MSA sequence. Set pairs dictionaty object in file msa-gen.py and also the virus family. And then execute msa-gen.py script
        ```
        python3 scripts/msa-gen.py
        ```
    9. MSA will be generated for the pairs and saved at ./data/msa/virusFamily_msa.txt

    You can use this MSA in R script to generate PHMM and to train the model. 
~~~

### Other individual commands ###

#### Script to generate sequence ####

    You can execute the below command to generate sequence from API call logs of different virus files or programs. 
    ```
    python3 scripts/seq-gen.py data/virus1.log  
    
    ```

    Script takes a single paramter which is the filename of the API calls log file.


    To generate sequence for all log files use generate_sequence.sh script
    ```
    scripts/generate_sequence.sh
    ```

#### Trunc Sequence ####
    This script can be used to truncate each sequence to a permissible 100 or 200 api sequences. 
    ```
    python3 scripts/truncSeq.py 
    ```

    

#### Char Count ####
    This script helps in counting the occurence of different characters in the sequence file.
    
    ```
    python3 scripts/charCount.py 
    ```

