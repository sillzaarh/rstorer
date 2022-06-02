#!/usr/bin/env python3

import os, random, requests, threading, argparse, urllib3, hashlib
urllib3.disable_warnings()

# Required arguments are set
parser = argparse.ArgumentParser(description="Response Storer Tool")
parser.add_argument("-u", "--url", type=str, metavar="",  help="enter the URL (URL should be provided in proper format)")
parser.add_argument("-l", "--list", type=str, metavar="", help="enter the path to file of list of URLs")
parser.add_argument("-p", "--proxy", type=str, metavar="", help="enter the proxy URL")
parser.add_argument("-o", "--output", type=str, metavar="", help="enter the folder name to save the output")
args = parser.parse_args()

# This function request to the particualr URL and returns the response
def req(url, redirect=False):
    r = requests.get(url, allow_redirects=redirect)
    return r

# This function request to particular URl through proxy server and returns the response
def proxy_req(url, proxy, redirect=False):
    r = requests.get(url, allow_redirects=redirect, proxies=proxy, verify=False)
    return r

# This function is called when -u or --url argument is passed
def urlArg(url):
    # If proxy URl is given then the request will go through proxy server otherwise normal request will be made
    if args.proxy == None:
        try:
            res = req(url=url)
        except: return "Error"
    else:
        proxies = {'http': args.proxy, "https": args.proxy,}
        try:
            res = proxy_req(url=url, proxy=proxies)
        except: return "Error"
    
    # Create output directory
    output = "output" if args.output == None else args.output
    if os.path.isdir(output) == False: os.mkdir(output)

    
    if int(res.status_code) < 400 or int(res.status_code) == 403:
        print(url + ": " + str(res.status_code))
        # Encode URL into base64 and create a folder if not present
        encoded_url = hashlib.md5(res.url.encode()).hexdigest()
        if os.path.isdir(output + "/" + encoded_url) == False: os.mkdir(output + "/" + encoded_url)

        # Open headers and body file
        header = open(output + "/" + encoded_url + "/" + encoded_url + ".headers", "w")
        body = open(output + "/" + encoded_url + "/" + encoded_url + ".body", "w")
        
        # Write URL and status code in .headers file
        header.writelines(str(res.url) + "\n")
        header.writelines(str(res.status_code) + "\n")

        # Write headers in .headers file
        for h in res.headers: header.writelines(h + ": " + res.headers[h] + "\n")

        # Write body in .body file
        body.writelines(str(res.url) + "\n")
        body.writelines(res.text)

        # Close .headers and .body file
        header.close(); body.close()
    

    # Check if there is any redirects
    if int(res.status_code) >= 300 and int(res.status_code) < 400:
        # If proxy URl is given then the request will go through proxy server otherwise normal request will be made
        if args.proxy == None:
            try:
                red_res = req(url=res.url, redirect=True)
            except: return
        else:
            try:
                red_res = proxy_req(url=res.url, proxy=proxies, redirect=True)
            except: return
      
        if int(red_res.status_code) < 400:
            # Encode redirected URL into base64 and create a folder if not present
            red_encoded_url = hashlib.md5(red_res.url.encode()).hexdigest()
            if os.path.isdir(output + "/" + encoded_url + "/" + red_encoded_url) == False: os.mkdir(output + "/" + encoded_url + "/" + red_encoded_url)

            # Open headers and body file
            header = open(output + "/" + encoded_url + "/" + red_encoded_url + "/" + red_encoded_url + ".headers", "w")
            body = open(output + "/" + encoded_url + "/" + red_encoded_url + "/" + red_encoded_url + ".body", "w")

            # Write URL and status code in .headers file
            header.writelines(str(red_res.url) + "\n")
            header.writelines(str(red_res.status_code) + "\n")

            # Write headers in .headers file
            for h in red_res.headers: header.writelines(h + ": " + red_res.headers[h] + "\n")

            # Write body in .body file
            body.writelines(str(red_res.url) + "\n")
            body.writelines(red_res.text)

            # Close .headers and .body file
            header.close(); body.close()

# This function is called when -l or --list argument is passed        
def listArg(list):
    # Opens the file and stores the urls in a list
    f = open(list, "r")
    urls = f.readlines()
    f.close()

    # Take urls one by one from the list and make the request
    for url in urls:
        url = url.strip()
        try:
            t = threading.Thread(target=urlArg, kwargs={'url': url})
            t.start()
        except: pass
    
# Checks if -u or --url argument is set or not
if args.url != None: 
    if urlArg(url=args.url) == "Error": print("URL is not provided in proper format")

# Checks if -l or --list argument is set or not
try:
    if args.list != None: listArg(list=args.list)
except: print("File is not present in the given path")
