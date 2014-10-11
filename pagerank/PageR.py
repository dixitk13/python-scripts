__author__ = 'Dixit_Patel'
import math
from datetime import datetime
# <k, v> :: < String, List(String) >
M = {}
# <k, v> :: < String, number >
L = {}
# List(Strings) - Contains all the nodes
P = []
# List(Strings) - List of the sink nodes.
S = []

page_rank_val = {}
d = 0.85

#file_to_be_read_path = "wt2g_inlinks.txt"
file_to_be_read_path = "test.txt"

dt = datetime.today()

#output file
output = open("outputpagerank_test.txt", "w+")

def populate_data_from_file( file_to_be_read_path, M, outlinks, Pages, Sink ):
    file_to_be_read = open(file_to_be_read_path, 'r')
    print('[START populate_data_from_file]', dt.now())
    output.write('[START populate_data_from_file]' + str(dt.now()) + '\n')
    #print('filepath',file_to_be_read)
    for line in file_to_be_read:
        #print('-----------')
        words = line.split()
        #print('words',words)
        page = words[0]
        #print('page',page)
        Pages.append(page)
        #print('pages',Pages)
        M[page] = words[1:]
        #print('M[page]',M)
        for k, v in M.items():
            if k == page: # added
                #print('v',v)
                for node in v:
                    temp = 1
                    if node in outlinks:
                        #print('node',node)
                        temp = outlinks[node]
                        #print('outlink',outlinks)
                        temp += 1
                        outlinks[node] = temp
                    #print('outlinks',outlinks[node])\
        #M.clear()
        #print('outlinks',outlinks)
    for val in Pages:
        if val not in outlinks:
            Sink.append(val)
    print('[END populate_data_from_file]', dt.now())
    output.write('[END populate_data_from_file]' + str(dt.now()) + '\n')
    #print('sink',Sink)

populate_data_from_file( file_to_be_read_path, M, L, P, S)

N = float(len(P))
print('N--> ',N)
output.write('N--> ' + str(N) + '\n')
print('--is L populated?', L)

def get_perplexity( page_rank ):
    has_converged = False
    perplexity = 0
    entropy = 0
    for v in page_rank.values():
        entropy += v*math.log(1/v, 2)
    perplexity = 2**entropy
    return perplexity


page_1 =  {'C': 0.1513061506319007, 'B': 0.1393055926315782, 'F': 0.1513061506319007, 'A': 0.2521279082949524, 'E': 0.18704623580229016, 'D': 0.11890796200737797}
#print('get_perplexity',get_perplexity(page_1))

page_rank = {}


def page_rank_fun(page_rank, pages, out_links, sink, M, d, N):
    print('[START pagerank]', dt.now())
    output.write('[START pagerank]' + str(dt.now()) + '\n')
    for p in P:
        print('p',p)
        page_rank[p] = 1/N
        newPR = {}

        prev_perplexity = 0.0
        perplexity = get_perplexity(page_rank)
        i = 0
    while i < 100:
        sinkPR = 0

        for s in S:
            sinkPR += page_rank[s]
        for p in P:
            newPR[p] = ( 1 - d )/N + d*sinkPR/N
            print("Mp", M[p])
            for q in M[p]:
                print("inside", q)
                temp_val = newPR[p]
                temp_val += d*page_rank[q]/L[q]
                newPR[p] = temp_val
                print('new PR', newPR)
        for p in P:
            page_rank[p] = newPR[p]
            i += 1
    print('pagerank', page_rank)
    print('[END pagerank]', dt.now())
    output.write('[END pagerank]' + str(dt.now()) + ' Pagerank is : ' + str(page_rank) + '\n')
    return page_rank

#print('pagerank',page_rank_fun(page_rank, P, L, S, M, d, N ))

print('pagerank',page_rank)
#populate_data_from_file( file_to_be_read_path , M, L, P, S)

print('M-->', M)
print('L-->', L)
print('P-->', P)
print('S-->', S)

output.write('M-->' + str(M) + '\n')
output.write('L-->' + str(L) + '\n')
output.write('P-->' + str(P) + '\n')
output.write('S-->' + str(S) + '\n')

def page_rank_rel(page_rank, P, L, S, M, d, N):
    print('[START page_rank_rel]', dt.now())
    output.write('[START pagerank]' + str(dt.now()) + '\n')
    for p in P:
        newPR = {}
        page_rank[p] = 1/N
        per_str = ''
        prev_perplexity = 0.0
        per_str = ''
        perplexity = get_perplexity(page_rank)
        #print('perplexity is', perplexity)
        i = 0
    while True:
        per_str += str(perplexity) + '\n'
        print('perplexity', perplexity)
        print('prev_perplexity',prev_perplexity)
        output.write('perplexity' + str(perplexity) + '     ' + 'prev_perplexity' + str(prev_perplexity) + '\n')
        if abs(int(perplexity) - int(prev_perplexity)) == 0:
            i += 1
        else:
            i = 1
        if i == 4:
            print('breaking out')
            output.write('breaking out' + '\n')
            break
        sinkPR = 0
        #print('------S', S)
        for s in S:
            sinkPR += page_rank[s]
            #print('--------P', P)
        for p in P:
            newPR[p] = (1 - d)/N + d*sinkPR/N
            print('new PR', newPR)
            print('mp', M)
            print('L', L)
            print('page_rank',page_rank)
            for q in M[p]:
                #if L[q] != 0:
                    #temp_val = newPR[p]
                    #temp_val += d*page_rank[q]/L[q]
                newPR[p] = newPR[p] + d*page_rank[q]/L[q]
        #print('newpr', newPR)
        for p in P:
            page_rank[p] = newPR[p]
            prev_perplexity = perplexity
            perplexity = get_perplexity(page_rank)
    print('[END page_rank_rel]', dt.now())
    output.write('[END page_rank_rel]' + str(dt.now()) + '\n')
    return page_rank

print('rel_page_rank', page_rank_rel(page_rank, P, L, S, M, d, N ))
output.write('rel_page_rank' + str(page_rank_rel(page_rank, P, L, S, M, d, N )) + '\n')