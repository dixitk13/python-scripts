__author__ = 'Dixit_Patel'
import math
from datetime import datetime

# List(Strings) - is the sink nodes in the graph, i.e., pages that have no out links
#S = []
sink =[]

# List(Strings) - is the set of all pages
#P = []
pages =[]

# <key, value> -> <String, List(String)> -  is the set (without duplicates) of pages that link to page p
M = {}

# <key, value> -> < String, number > - is the number of out-links (without duplicates) from page q
#L = {}
out_links ={}

# Page Rank Value <key, value> -> < String, number >
page_rank = {}
#page_rank_val = {}



# d is the PageRank damping/teleportation factor; use d = 0.85 as is typical
d = 0.85

file_path = "test.txt"
#file_path = "wt2g_inlinks_3.txt"
##file_path = "wt2g_inlinks.txt"

dt = datetime.today()
output = open("pagerank_loop.txt", "w+")

def calculate_perplexity(page_rank):

    entropy = 0
    for v in page_rank.values():
        entropy += v*math.log(1/v, 2)

    return 2**entropy


def populate_data(arg_file_path, M, out_links, pages, sink):
    file = open(arg_file_path, 'r')
    print('[START populate_data]', dt.now())
    output.write('[START populate_data_from_file]' + str(dt.now()) + '\n')
    #print('filepath',file_to_be_read)
    for everyline in file:
        #print('-----------')
        words = everyline.split()
        page = words[0]
        print('append->', page)
        pages.append(page)

        M[page] = words[1:]

        print('M',M)
        for k, v in M.items():
            #print('kv',k,v)

            if k == page: # added
                #print('Page + k', page, k )
                for node in v:
                    temp = 1
                    print('v',v)
                    if node in out_links:
                        print('v-> ', v,'node-->', node)
                        temp = out_links[node]

                        #print('outlink', out_links)
                        temp += 1
                    out_links[node] = temp
                    # if node not in pages:
                    #     print('append', node)
                    #     pages.append(node)
                    # if node=='WT01-B01-2':
                    #     print('out_links[WT01-B01-2] ', out_links)
        #M.clear()
        #print('out_links',out_links)
    print('Finished checking lines')
    for val in pages:
        if val not in out_links:
            sink.append(val)
    print('[END populate_data_from_file]', dt.now())
    output.write('[END populate_data_from_file]' + str(dt.now()) + '\n')
    #print('sink',sink)

populate_data(file_path, M, out_links, pages, sink)

N = float(len(pages))
print('N--> ', N)
print('outlinks', out_links)
print('m', M)
print('pages',pages)
print('sink',sink)
output.write('N---> ' + str(N) + '\n')
output.write('M---> ' + str(M) + '\n')
output.write('outlinks---> ' + str(out_links) + '\n')
output.write('Pages---> ' + str(pages) + '\n')
output.write('SINK---> ' + str(sink) + '\n')


def page_rank_function(page_rank, pages, out_links, sink, M, d, N):
    print('[START pagerank]', dt.now())
    output.write('[START pagerank]' + str(dt.now()) + '\n')
    for p in pages:
        #print('p',p)
        page_rank[p] = 1/N
        newPR = {}

        prev_perplexity = 0.0
        perplexity = calculate_perplexity(page_rank)
        #print('perplexity is ', perplexity)
        i = 0
    print('before pagerank',page_rank)
    while i < 100:
        sinkPR = 0

        for s in sink:
            sinkPR += page_rank[s]
        for p in pages:
            newPR[p] = ( 1 - d )/N + d*sinkPR/N
            #print("Mp", M[p])
            for q in M[p]:
                #print("inside", q)
                #temp_val = newPR[p]
                #temp_val += d*page_rank[q]/out_links[q]
                newPR[p] += d*page_rank[q]/out_links[q]
                #print('new PR', newPR)
        for p in pages:
            page_rank[p] = newPR[p]
            i += 1
    print('pagerank', page_rank)
    print('[END pagerank]', dt.now())
    output.write('[END pagerank]' + str(dt.now()) + ' Pagerank is : ' + str(page_rank) + '\n')
    return page_rank



def page_rank_fun(page_rank, pages, out_links, sink, M, d, N):
    print('[START page_rank_rel]', dt.now())
    output.write('[START pagerank]' + str(dt.now()) + '\n')
    for p in pages:
        newPageRank = {}
        page_rank[p] = 1/N

        prev_perplexity = 0.0
        # perplexity string
        perplexity_string = ''
        perplexity = calculate_perplexity(page_rank)
        #print('perplexity is', perplexity)
        i = 0
    print('pagerank',page_rank)
    while True:
        perplexity_string += str(perplexity) + '\n'
        #print('perplexity', perplexity)
        #print('prev_perplexity', prev_perplexity)
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
        for s in sink:
            sinkPR += page_rank[s]
            #print('--------P', P)
        for p in pages:
            newPageRank[p] = (1 - d)/N + d*sinkPR/N
            for q in M[p]:
                if out_links[q] != 0:
                    #temp_val = newPageRank[p]
                    #temp_val += d*page_rank[q]/out_links[q]
                    print('Q',q)
                    print('newpagerank', newPageRank[p])
                    print('page_rank p ', page_rank[p])
                    print('page_rank q ', page_rank[q])
                    print('outlinks', out_links[q])
                    newPageRank[p] = newPageRank[p] + d*page_rank[q]/out_links[q]
        #print('newPageRank', newPageRank)
        for p in pages:
            page_rank[p] = newPageRank[p]
        prev_perplexity = perplexity
        perplexity = calculate_perplexity(page_rank)
    print('[END page_rank_rel]', dt.now())
    output.write('perplexity_string' + str(perplexity_string) + '\n')
    output.write('[END page_rank_rel]' + str(dt.now()) + '\n')
    return page_rank


# page_rank_fun_o_p = page_rank_function(page_rank, pages, out_links, sink, M, d, N)
# print('rel_page_rank',page_rank_fun_o_p)
# output.write('rel_page_rank' + str(page_rank_fun_o_p) + '\n')
