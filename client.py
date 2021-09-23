#!/usr/bin/env python3
import requests, sys
localhost = "http://127.0.0.1:8081"

# Posting new data to the web service
def post_data(key, value):
    data = {'key': key, 'value': value}
    #Sending Post request to create a new resource
    r = requests.post(localhost+'/post', data)
    try:
        print(r.json()["result"])
    except:
        print(r.json()["error"])

#Getting the current value of the selected key
def get_data(key):
    #Sending Get request to obtain information about a resource
    r = requests.get(localhost + '/get/' + key)
    try:
        print(r.json()["value"])
    except:
        print(r.json()["error"])

#Getting the whole history (all values) of the selected key
def get_history(key):
    #Sending Get request to retrieve a list
    r = requests.get(localhost + '/history/' + key)
    try:
        for item in r.json():
            print(str(item["value"]) +" ===> Version" + str(item["version"]))
    except:
        print(r.json()["error"])


def main():
    try:
        if (sys.argv[1] == "set"):
            post_data(sys.argv[2],sys.argv[3])

        elif (sys.argv[1] == "get"):
            get_data(sys.argv[2])

        elif (sys.argv[1] == "history"):
            get_history(sys.argv[2])

        else:
            print("Error! Please check your command!")
    except:
        print("Error! Please check your command!")

if __name__ == "__main__":
    main()