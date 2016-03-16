#!/usr/bin/env python
"""
An example using Graph as a weighted network.
"""

try:
    import matplotlib.pyplot as plt
except:
    raise
import traceback
import networkx as nx
G=nx.Graph()
id2stat={}
statpolut={}
#f = open('CUSPTubeDummy.csv','r')
avgpol=0.0
count = 0.0
stat2zone={}
distance={}
def mapid2stat():
    stations = open('stations.csv','r')
    for stat in stations:
        stat=stat.split(',')
        id2stat[stat[0]]=stat[3]
        stat2zone[stat[3]]=stat[5]
    stations.close()
def populate_graph(): 
    adj = open('lines.csv','r')      
    for ids in adj:
        ids= ids.split(",")    
        try:
            G.add_edge(id2stat[ids[0]],id2stat[ids[1]])
        except:
            pass
    adj.close()

def populate_polution():
    poldata= open('CUSPTubeDummy.csv','r')
    avgpol=0.0  
    count =0.0      
    for line in poldata:
        line = line.split(',')
        try:
            avgpol+=float(line[2])
            count+=1.0
            #print float(line[2])        
            statpolut['"'+line[1]+'"']={'p':float(line[2]),'depth':line[5].replace('\n','') }
        except Exception as e:
            print e
            pass
    poldata.close()
    return (avgpol/count)

def populate_graph2(avgpol):
    adj = open('lines.csv','r')
    err=0
    for ads in adj:
        ids= ads.split(",")
        mean = 0.0        
        try:
            avg2 = 0.0
            avg1 = 0.0        
            if  (not id2stat[ids[0]] in statpolut):
                #print "==================="
                lstnbr = list(G.neighbors(id2stat[ids[0]]))
                for  nbr in lstnbr:
                    if nbr in statpolut:
                        avg1+=statpolut[nbr]['p']
                        #print avg,len(lstnbr)
                if avg1 <= 0.0:
                    avg1 = avgpol   
                #print list(G.neighbors(id2stat[ids[0]]))
                else:
                    avg1 = avg1/(len(lstnbr)*1.0)
                statpolut[id2stat[ids[0]]] ={'p':avg1}
            else:                
                avg1 = statpolut[id2stat[ids[0]]]['p']
                
            if  (not id2stat[ids[1]] in statpolut):            
                #print "==================="
                lstnbr = list(G.neighbors(id2stat[ids[1]]))
                for  nbr in lstnbr:
                    if nbr in statpolut:
                        avg2+=statpolut[nbr]['p']
                        #print avg,len(lstnbr)
                if avg2 <= 0.0:
                    avg2 = avgpol
                else:
                    avg2 = avg2/(len(lstnbr)*1.0)
                statpolut[id2stat[ids[1]]] ={'p':avg2}
            else:
                avg2 = statpolut[id2stat[ids[1]]]['p']
                #print avg
            mean = (avg1+avg2)/2.0
            G.remove_edge(id2stat[ids[0]],id2stat[ids[1]])  
            G.add_edge(id2stat[ids[0]],id2stat[ids[1]],weight=mean)           
            
        except Exception as e:
            print e
            err+=1
            #traceback.print_stack()
            #print statpolut[id2stat[lines[0]]]
    adj.close()       
def generate_paths():
    path = nx.all_pairs_shortest_path(G)
    distance = nx.all_pairs_shortest_path_length(G)
    return path,distance
def get_path(src,dest):
    return path[src][dest],distance[src][dest] 

path = {}
mapid2stat()
populate_graph()
avgpol=populate_polution()
populate_graph2(avgpol)
path,distance = generate_paths()
path,distance= get_path('"Croxley"','"Queen\'s Park"')
print path,distance
sum= 0.0
for p in path:    
    sum+=statpolut[p]['p']
    print p,stat2zone[p],statpolut[p]['p']
print sum
