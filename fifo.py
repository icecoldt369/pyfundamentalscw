global cache, requests, max_page

cache = []
requests = []
max_page = 8
  
def fifo():
    global cache, requests, max_page
    for request in requests:
        if len(cache) < max_page and request not in cache:
            print("miss")
            cache.append(request)
        elif len(cache) >= max_page and request not in cache:
            print("miss")
            cache.pop(0)
            cache.append(request)
        elif request in cache:
            print("hit")
    print(cache)
    requests.clear()
    cache =[]


def lfu():
    global cache, requests
    request_map = {}
    freqs_map = {}
    page = 0
    for page in requests:
        if page not in cache and len(cache) < max_page :
            print("miss")
            cache.append(page)
            if page not in request_map.keys() :
                request_map[page] = 0
            request_map[page] = request_map[page] +1
        elif page not in cache and len(cache) >= max_page :
            print("miss")
            for k in request_map.keys() :
                if k in cache :
                    freqs_map[k] = request_map[k]
                
            min_pages = [i for i in freqs_map.keys() if freqs_map[i] == min(freqs_map.values())]
            freqs_map.clear()
            min_page = min(min_pages)
            cache.remove(min_page)
            cache.append(page)
            if page not in request_map.keys() :
                request_map[page] = 0
            request_map[page] = request_map[page] +1
        elif page in cache :
            print ("hit")
            request_map[page] = request_map[page] +1
    print(cache)
    requests.clear()
    cache =[]


def read_requests():
    page = -1
    while page != 0:
        request = input()
        if(request.isdigit()):
            page = int(request)
            if(page < 1):
                break
            requests.append(page)
        else:
           # print("The entered Page Number %s is not valid (The page number must be greater than 0. Try again\n" %request)
            return request.count

while True:
    read_requests()
    choice = input()
    if choice=="1":
        fifo()
    elif choice=="2":
        lfu()
    elif choice=="Q":
        break
    else:
        print("try again")
