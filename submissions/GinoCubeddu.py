import sys

def say_hello(name):
    print("Hello {0}! Nice to meet you! My name is Gino".format(name))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            say_hello(sys.argv[i])
    else:
        print("Please tell me your name(s)! Use me as shown below :)")
        print("python GinoCubeddu.py YOUR_NAME")
