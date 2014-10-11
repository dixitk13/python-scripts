
import math
from datetime import datetime
import operator

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

# in links
in_links = {}


# d is the PageRank damping/teleportation factor; use d = 0.85 as is typical
d = 0.85

#file_path = "test.txt"
#file_path = "wt2g_inlinks_3.txt"
file_path = "wt2g_inlinks.txt"
#file_path = "wt2g_inlinks_2.txt"

dt = datetime.today()
output = open("pagerank_loop.txt", "w+")

def calculate_in_links(M):
	C ={}
	for k,v in M.items():
		i=0
		for val in v:
			i+=1
		C[k]=i
	return sorted(C.items(), key=lambda x: x[1], reverse=True)

def calculate_perplexity(page_rank):

    entropy = 0
    for v in page_rank.values():
        entropy += v*math.log(1/v, 2)

    return 2**entropy


def populate_data(arg_file_path, M, out_links, pages, sink):
    file = open(arg_file_path, 'r')
    print('[START populate_data]', dt.now())
    output.write('[START populate_data_from_file]' + str(dt.now()) + '\n' + '\n')
    #print('filepath',file_to_be_read)
    for everyline in file:
        words = everyline.split()
        page = words[0]
        if page in pages:
            #if not words[1:]:
            M[page] += words[1:]
            M[page] = set(M[page])
        else:
            pages.append(page)
            M[page] = words[1:]

    for k, v in M.items():
        for node in v:
            temp = 1
            #print('v',v)
            if node in out_links:
                temp = out_links[node]
                temp += 1
            out_links[node] = temp

    print('Finished checking lines')
    for value in out_links:
        if value not in pages:
            #print('Do I add them Pages?? -> ', value)
            pages.append(value)
    for val in pages:
        if val not in out_links:
            sink.append(val)
    print('[END populate_data_from_file]', dt.now())
    output.write('[END populate_data_from_file]' + str(dt.now()) + '\n' + '\n')
    #print('sink',sink)

populate_data(file_path, M, out_links, pages, sink)

N = float(len(pages))
print('N--> ', N)
print('outlinks', out_links)
print('m', M)
print('pages',pages)
print('sink',sink)
output.write('N---> ' + str(N) + '\n' + '\n')
output.write('M---> ' + str(M) + '\n' + '\n')
output.write('outlinks---> ' + str(out_links) + '\n' + '\n')
output.write('Pages---> ' + str(pages) + '\n' + '\n')
output.write('SINK---> ' + str(sink) + '\n' + '\n')





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

            if p in M.keys():
                for q in M[p]:

                    newPR[p] += d*page_rank[q]/out_links[q]

        for p in pages:
            page_rank[p] = newPR[p]
            i += 1
    print('pagerank', page_rank)
    print('[END pagerank]', dt.now())
    output.write('[END pagerank]' + str(dt.now()) + ' Pagerank is : ' + str(page_rank) + '\n' + '\n')
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
    j = 0
    print('pagerank',page_rank)
    while True:
        j += 1
        perplexity_string += str(perplexity) + '\n'
        print('perplexity', perplexity)
        print('prev_perplexity', prev_perplexity)
        output.write('Loop -> '+  str(i) + 'perplexity' + str(perplexity) + '     ' + 'prev_perplexity' + str(prev_perplexity) + '\n' + '\n')
        if abs(int(perplexity) - int(prev_perplexity)) < 1:
            i += 1
        else:
            i = 1
        if i == 4:
            print('breaking out')
            output.write('breaking out' + '\n' + '\n')
            break
        sinkPR = 0

        for s in sink:
            sinkPR += page_rank[s]

        for p in pages:
            newPageRank[p] = (1 - d)/N + d*sinkPR/N
            if p in M.keys():
                for q in M[p]:
                    if out_links[q] != 0:
                         newPageRank[p] = newPageRank[p] + d*page_rank[q]/out_links[q]

        for p in pages:
            page_rank[p] = newPageRank[p]

        prev_perplexity = perplexity
        perplexity = calculate_perplexity(page_rank)
        print('Page: '+ str(j) +  str(dt.now()) +' perplexity ' + str(perplexity) + '\n' + '\n')
    print('[END page_rank_rel]', dt.now())
    output.write('perplexity' + str(perplexity_string) + '\n' + '\n')
    output.write('[END page_rank_rel]' + str(dt.now()) + '\n' + '\n')
    return page_rank


page_rank_fun_o_p = page_rank_fun(page_rank, pages, out_links, sink, M, d, N)
print('rel_page_rank',page_rank_fun_o_p)
output.write('rel_page_rank' + str(page_rank_fun_o_p) + '\n' + '\n')

sorted_page_rank = sorted(page_rank_fun_o_p.items(), key=lambda x: x[1], reverse=True)
print('sorted_page_rank',sorted_page_rank)
output.write('sorted_page_rank' + str(sorted_page_rank) + '\n' + '\n')

in_links = calculate_in_links(M)
print('in links', in_links)
output.write('in links' + str(in_links) + '\n')