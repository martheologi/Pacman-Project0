import heapq

class priorityQueue:

    def __init__(pq):
        pq.heap = []        #keni heap
        pq.count = 0        #arxikopoieitai me adeia heap

    def push(pq, item, priority):
        heapq.heappush(pq.heap, (priority, item))   #gia na ta taksinomisei me vasi tin protereotita
        pq.count+=1                                 #auksanw ton ari8mo twn stoixeiwn
        return

    def pop(pq):
        pq.count-=1                     #meiwnw ton ari8mo twn stoixeiwn
        min = heapq.heappop(pq.heap)[1] #epistrefw to mikrotero stoixeio
        return min

    def isEmpty(pq):
        return len(pq.heap) == 0

    def update(pq, item, priority):
        found = False
        for x in range(len(pq.heap)):                           #gia ka8e stoixeio tis heap
            if pq.heap[x][1]==item:                             #an uparxei idio task
                found = True                                        #enimerwnw oti exw vrei idio task
                if pq.heap[x][0]<=priority:                     #kai an einai <= apo to priority min kaneis tipota
                    break
                else:                                           #alliws an exei megalutero priority apo auto pou pira
                    pq.heap.remove(pq.heap[x])                  #diegrapse to stoixeio pou uparxei sti heap
                    heapq.heappush(pq.heap, (priority, item))   #kai vale to kainourio me to mikrotero priority gia na mpei taksinomimeno
                    return
        if not found:
            pq.push(item, priority)                             #an den exei idio task pros8ese to stoixei sti heap

def PQSort(intList):
    pq = priorityQueue()                    #ftixnw keni pq
    for int in intList:                     #vazw ka8e stoixeio tiw listas stin keni pq
        pq.push(int, int)
    for x in range(len(pq.heap)):               #epistrefw ta stoixeia sti lista taksinomimena
        intList[x] = pq.pop()                   #i pop dinei to mikrotero ka8e fora
    return intList
