class State(object):
    nursery=[]
    row=-1
    col=0
    q_count=0
    lizard_pos=[]
    def __init__(self,row,col,q_count,lizard_pos):
        self.row=row
        self.col=col
        self.q_count=q_count
        self.lizard_pos=lizard_pos

class State1(object):
    nursery=[]
    lizard_pos=[]
    conflicts=0
    def __init__(self,lizard_pos,conflicts):
        self.lizard_pos=lizard_pos
        self.conflicts



def soln_print(lizard_pos):
    count = 0
    for temp in lizard_pos:
        nursery[temp[0]][temp[1]]=1
    for p in range(0, len(nursery), 1):
        for q in range(0, len(nursery), 1):
            if nursery[p][q] == 1:
                count += 1
    f = open('output.txt', 'w')
    if c_lizard == count:

        f.write('OK\n')
        for temp in nursery:
            for i in range(0, len(temp), 1):
                if i != len(temp) - 1:
                    #z = str(temp[i])
                    f.write(str(temp[i]))
                    #print temp[i],
                else:
                    f.write(str(temp[i]) + '\n')
                    #print temp[i]
    else:
        f.write('FAIL\n')
    f.close()


def soln_print_1(lizard_pos,conflicts):

    for temp in lizard_pos:
        nursery[temp[0]][temp[1]]=1
    f = open('output.txt', 'w')
    if conflicts==0:
        f.write('OK\n')
        for temp in nursery:
            for i in range(0, len(temp), 1):
                if i != len(temp) - 1:
                    f.write(str(temp[i]))
                    #print temp[i],
                else:
                    f.write(str(temp[i]) + '\n')
                    #print temp[i]
    else:
        f.write('FAIL\n')
    f.close()

def Not_conflict(temp,lizard_pos):

    if [temp[0],temp[1]] in tree:
        return False

    for i in range(temp[1]-1,-1,-1):
        if [temp[0],i] in tree:
            break
        elif [temp[0],i] in lizard_pos:
            return False
    for i in range(temp[0]-1,-1,-1):
        if [i,temp[1]] in tree:
            break
        elif [i,temp[1]] in lizard_pos:
            return False
    for i,j in zip(range(temp[1]-1,-1,-1),range(temp[0]-1,-1,-1)):
        if [j,i] in tree:
            break
        elif [j,i] in lizard_pos:
            return False
    for i,j in zip(range(temp[1]+1,len(nursery),1),range(temp[0]-1,-1,-1)):
        if [j,i] in tree:
            break
        elif [j,i] in lizard_pos:
            return False

    return True

def Check_conflict(lizard_pos):
    conflicts=0
    lizard_pos.sort()
    for temp in lizard_pos:
        if [temp[0],temp[1]] in tree:
            break
        for i in range(temp[1]+1 ,len(nursery), 1):
            if [temp[0], i] in tree:
                break
            elif [temp[0], i] in lizard_pos:
                conflicts+=1
                break

        for i in range(temp[0] +1, len(nursery), 1):
            if [i, temp[1]] in tree:
                break
            elif [i, temp[1]] in lizard_pos:
                conflicts+=1
                break
        for i, j in zip(range(temp[1]+1 , len(nursery), 1), range(temp[0]+1 , len(nursery), 1)):
            if [j, i] in tree:
                break
            elif [j, i] in lizard_pos:
                conflicts+=1
                break
        for i, j in zip(range(temp[1]-1 , -1, -1), range(temp[0]+1 , len(nursery), 1)):
            if [j, i] in tree:
                break
            elif [j, i] in lizard_pos:
                conflicts+=1
                break
    return conflicts


def DFS():
    dfs_start_time=datetime.now()
    soln_find1 = 0
    soln_find = 0
    row = -1
    col = 0
    Lizard_queue = deque()
    q_count = 0
    lizard_pos = []
    X = State(row, col, q_count, lizard_pos)
    Lizard_queue.append(X)

    while (len(Lizard_queue) and (datetime.now()-dfs_start_time).seconds<=294):
        #next_row_check = 0
        if soln_find == 1:
            X2 = copy.deepcopy(X3)
            break
        X2 = Lizard_queue.pop()
        count_tree = 0
        set_flag = 0
        tree_set = 0
        next_row_check=0
        if c_lizard != X2.q_count:
            for temp in tree:
                if temp[0] == X2.row and temp[1] > X2.col and temp[1] < len(nursery) - 1:
                    tree_set = 1
                    row = X2.row
                    col_temp = temp[1] + 1
                    break
            if tree_set == 0:
                row = X2.row + 1
                col_temp = 0

            for temp in tree:
                if (temp[0] == X2.row and temp[1] > X2.col):
                    count_tree += 1
                if temp[0] > X2.row:
                    count_tree += 1

            if count_tree == 0 and (c_lizard - X2.q_count) > (len(nursery) - X2.row - 1):
                #print "break here"
                set_flag = 1


            for j in range(row,len(nursery),1):
                 #if next_row_check!=0:
                 #   break
                if j!=row:
                    col_temp=0
                if j < len(nursery) and set_flag==0:
                    for i in range(col_temp, len(nursery), 1):
                        X3 = copy.deepcopy(X2)
                        if Not_conflict([j, i], X2.lizard_pos):
                             X3.lizard_pos.append([j, i])
                             X3.q_count += 1
                             Obj = State(j, i, X3.q_count, X3.lizard_pos)
                             Lizard_queue.append(Obj)
                             if c_lizard == X3.q_count:
                                  soln_find = 1
                                  break

        elif c_lizard == X2.q_count:
            soln_find1 = 0
            break
    # print 'Hi'
    if len(Lizard_queue) == 0 or (datetime.now()-dfs_start_time).seconds>293:
        soln_print(X2.lizard_pos)

    if soln_find == 1 or soln_find1 == 1:
        soln_print(X2.lizard_pos)


def BFS():
    bfs_start_time = datetime.now()
    soln_find1 = 0
    soln_find = 0
    row = -1
    col = 0
    Lizard_queue = deque()
    q_count = 0
    lizard_pos = []
    X = State(row, col, q_count, lizard_pos)
    Lizard_queue.append(X)

    while (len(Lizard_queue) and (datetime.now()-bfs_start_time).seconds<294):
        if soln_find == 1:
            X2 = copy.deepcopy(X3)
            # print X2
            break
        X2 = Lizard_queue.popleft()
        count_tree = 0
        set_flag = 0
        tree_set = 0
        if c_lizard != X2.q_count:
            for temp in tree:
                if temp[0] == X2.row and temp[1] > X2.col and temp[1] < len(nursery) - 1:
                    tree_set = 1
                    row = X2.row
                    col_temp = temp[1] + 1
                    break

            if tree_set == 0:
                row = X2.row + 1
                col_temp = 0

            for temp in tree:
                if (temp[0] == X2.row and temp[1] > X2.col):
                    count_tree += 1
                if temp[0] > X2.row:
                    count_tree += 1

            if count_tree == 0 and (c_lizard - X2.q_count) > (len(nursery) - X2.row - 1):
                #print "break here"
                set_flag = 1
            for j in range(row,len(nursery),1):
                if j!=row:
                    col_temp=0

                if j < len(nursery) and set_flag == 0:
                    for i in range(col_temp, len(nursery), 1):
                        X3 = copy.deepcopy(X2)
                        if Not_conflict([j, i], X2.lizard_pos):
                            X3.lizard_pos.append([j, i])
                            X3.q_count += 1
                            Obj = State(j, i, X3.q_count, X3.lizard_pos)
                            Lizard_queue.append(Obj)
                            if c_lizard == X3.q_count:
                                soln_find = 1
                                break

        elif c_lizard == X2.q_count:
            soln_find1 = 0
            break
    if len(Lizard_queue) == 0 or (datetime.now()-bfs_start_time).seconds>293:
        soln_print(X2.lizard_pos)

    if soln_find == 1 or soln_find1 == 1:
        soln_print(X2.lizard_pos)

def SA(empty_pos):

    call_to_dfs = 0
    temperature = 100000.0
    loop_count = 2
    lizard_pos = []
    conflicts = 0
    X_curr = State1(lizard_pos, conflicts)
    count_lizard = c_lizard
    if empty_pos==0:
        DFS()
        return
    while (count_lizard != 0 ):

        row = random.randint(0, n - 1)
        col = random.randint(0, n - 1)
        temp = [row, col]
        if temp not in tree and temp not in lizard_pos:
            X_curr.lizard_pos.append(temp)
            count_lizard -= 1
            empty_pos-=1
            if count_lizard>empty_pos:
                break
    conflict_curr = Check_conflict(X_curr.lizard_pos)
    X_curr.conflicts = conflict_curr
    while ((datetime.now() - t1).seconds <= 300):

        if len(X_curr.lizard_pos) == c_lizard and X_curr.conflicts == 0:
            answer_found=1
            break
        #print 'Conflict_curr', X_curr.conflicts
        X_next = copy.deepcopy(X_curr)
        current_pick_set = 0
        while (current_pick_set != 1):
            row_next = random.randint(0, n - 1)
            col_next = random.randint(0, n - 1)
         #   print 'Current pick', row_next, col_next
            row_col = random.choice(X_curr.lizard_pos)
            if [row_next, col_next] not in X_curr.lizard_pos and [row_next,col_next] not in tree:
                X_next.lizard_pos.remove(row_col)
                X_next.lizard_pos.append([row_next, col_next])
                break
        conflict_next = Check_conflict(X_next.lizard_pos)
        X_next.conflicts = conflict_next
        delta = conflict_next - conflict_curr
        try:
            prob = math.exp(-1*delta / temperature)
        except OverflowError:
            prob = float('inf')
        random_number = random.uniform(0, 1)

        if delta < 0:
            X_curr = copy.deepcopy(X_next)
        elif random_number <= prob:
            X_curr = copy.deepcopy(X_next)
        temperature=math.log10(1+1/temperature)
        #temperature = temperature / math.log10(n + c_lizard)
        loop_count += 1

    if call_to_dfs==0:
        soln_print_1(X_curr.lizard_pos,X_curr.conflicts)


import time
import copy
import math
import random
from datetime import datetime
from collections import deque
start_code=time.time()
t1=datetime.now()
q_count=0
empty_pos=0
with open('input.txt','r') as f:
    i=1
    nursery=[]
    tree=[]
    for line in f:
        line=line.strip()
        if line!="":
            if i==1:
                fn=line
                i+=1
            elif i==2:
                n=int(line)
                i+=1
            elif i==3:
                c_lizard=int(line)
                i+=1
            else:
                arr=[]
                for j in range(len(line)):
                    if line[int(j)] == '2':
                        tree.append([int(i-4), int(j)])
                    else:
                        empty_pos+=1
                    arr.append(line[int(j)])
                nursery.append(arr)
                i+=1
        else:
            break


if fn =="DFS":
    DFS()
elif fn=="BFS":
    BFS()
elif fn=="SA":
    SA(empty_pos)
