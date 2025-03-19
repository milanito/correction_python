def list_sum_limit (B, limit) :
    if B == None :
        return []
    else :
        cur = queue.Queue ()
        nxt = queue.Queue ()
        cur.enqueue(B)
        res = []
        while not cur . isempty () :
            size = 0
            while not cur.isempty() and size < limit :
                x = cur.dequeue ()
                size = size + x.key
                if x.left != None :
                    nxt . enqueue(x.left)
                if x.right != None :
                    nxt . enqueue(x.right)
            while not cur.isempty() :
                x = cur.dequeue()
                if x.left != None :
                    nxt.enqueue(x.left)
                if x . right != None :
                    nxt . enqueue(x.right)
            cur, nxt = nxt, cur
            if size < limit :
                res.append(siz e)
        return res

def aux_first (B) :
    if B . left == None :
        if B . right == None :
            return -1
        else :
            return B.key
    else :
        if B . right == None :
            return B . key
        else :
            rleft = aux_first ( B . left )
            if rleft != -1:
                return rleft
            else :
                return aux_first ( B . right )

def get_first_single ( B ) :
    if B == None :
        return -1
    else :
        return aux_first ( B)

def aux ( B ) :
    if B == None :
        return 0
    else :
        return 1 + aux ( B . left ) + aux ( B . right )

def get_root_order ( B ) :
    if B == None :
        return None
    else :
        left = aux ( B . left )
        return 1 , left + 1 , left + aux ( B . right ) + 1
