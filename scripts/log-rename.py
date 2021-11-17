import os
  
# Function to rename multiple files
def main():
  
    for count, filename in enumerate(os.listdir("Logs1")):
        src = "Logs1/"+filename;
        if (src.endswith('.txt')):
            dst = src[src.index('_')+1: src.index(' ')];
            dst ='seq-gen/data/injector/'+ dst+'.txt';
            print(src);
            
            # rename() function will
            # rename all the files
            os.rename(src, dst)
            
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()