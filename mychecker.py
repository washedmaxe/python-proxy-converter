import re, requests, time
#YOU NEED PYTHON3 OR HIGHER
#YOU NEED PIP
#ONCE YOU HAVE BOTH; OPEN CMD AND TYPE  'pip install requests'
#YOU NEED TO CREATE A FOLDER; GIVE THIS FILE A NAME
#YOU ALSO NEED TO CREATE THE FILES: 'input.text' and 'output.txt'
#PLACE YOUR PROXIES IN THE 'input.txt' file

print("---PROXY CHECKER w/ timeout checker---")
print("---made by Maxe ---")
print("____________________")

website = input("Type/Paste the site we will check: ( like https://www.footpatrol.com) ")
#website = "https://www.thehipstore.co.uk"
timeo = float(input("Type the timeout in seconds: (0.5 etc also allowed): "))
#timeo = 2

headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
 'upgrade-insecure-requests':'1',
 'referer':website,
 'cache-control':'private, max-age=0, no-cache',
 "Pragma": "no-cache",
 'accept-language':'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
 'accept-encoding':'utf-8',
 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'}

f = open('input.txt', 'r')
open('output.txt', 'w').close()     #clearing old output file
s = open('output.txt', 'a')

proxycounter = 0

for x in f:
    #print(x)
    spli = x.split(":")
    final = {
           'http': f'http://{spli[2]}:{spli[3]}@{spli[0]}:{spli[1]}'                           #formatting
    }
    try:
        print("Checking Proxy: " + str(proxycounter))
        source = requests.get(website, headers = headers, timeout = timeo, proxies = final)   #sending request
        if source.status_code == 200:                                                         #checking response status
            print("Valid proxy: " + str(source.status_code))
            s.write(x)                                                                       #writing valid proxy to output file
            proxycounter += 1
        elif source.status_code in (503, 500):
            print("Website down, try again later: " + str(source.status_code))                #NOT an proxy error
        else:
            print("Invalid proxy: " + str(source.status_code))
            proxycounter += 1

    except Exception as e:
        if "timed out" in str(e):
            print("Proxy: " + str(proxycounter) + " timed out")
        else:
            print(e)                                                                         #error not caused by
        proxycounter += 1

f.close()
s.close()
print("_______________________")
print("Finished, check the output.txt file for valid proxies for " + website)
