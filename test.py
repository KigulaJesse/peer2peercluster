from os.path import exists

FILE_PATH = "peerFiles/"

file_exists = exists(FILE_PATH + "peer1/kkps.txt")
print(file_exists)