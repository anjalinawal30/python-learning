#FileNotFoundError, PermissionError, BlockingIOError , TimeOutError 
#def main():
#    try:
#        configuration = open("open.txt")    #create a directory name as day2.txt
#    except FileNotFoundError:
#        print("File Not Found")

#if __name__ == '__main__':
#    main()
    
def main():
    try:
        configuration = open("open.txt")    #it will work
    except Exception as err:
        print("File Not Found", err)
        
    #output = File Not Found [Errno 13] Permission denied: 'open.txt'
        
    try:
        open("open.txt")
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the open.txt file!")
        elif err.errno == 13:
            print("Found open.txt but couldn't read it")

if __name__ == '__main__':
    main()