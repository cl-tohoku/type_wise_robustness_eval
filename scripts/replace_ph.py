import sys
from collections import deque

def main(args):
    with open(args[1]) as f_mt, open(args[2]) as f_ph:
        for l1, l2 in zip(f_mt, f_ph):
            l1 = l1.strip()
            l2 = l2.strip()
            if l2:
                phs = deque(l2.split('|||'))
                while phs:
                    l1 = l1.replace('<PH>', phs.popleft(), 1)
            l1 = l1.replace('<PH>', ' ')
            print(l1)
        
if __name__ == '__main__':
    args = sys.argv
    main(args)
