import os



if __name__=="__main__":
    IS_LOCAL = os.environ.get("LOCAL_RUNTIME")
    if IS_LOCAL:
        print(IS_LOCAL)
    else:
        print("npo")