from multiprocessing import Pool
import numpy as np
import time
import json
arr_all = np.load('arr_all.npy')

def similar(A):
    global arr_all
    s=map(lambda x:(np.dot(A,x) / (np.linalg.norm(A)*np.linalg.norm(x))),arr_all)
    s=np.array(list(s))
    topK=5
    top_k_index=s.argsort()[::-1][1:topK+1]
    return top_k_index.tolist()

if __name__ == '__main__':
    start=time.time()
    num=10000
    with Pool(6) as p: # 6 cpu
        s=p.map(similar,arr_all[:num]) # 做上方function
    dict1={}
    for i in range(num-10000,num):
        dict1[str(i)]=s[i]
    with open('book_%s.json'%(num),'w') as f:
        f.write(json.dumps(dict1))
    end=time.time()
    print('耗時:',end-start)
