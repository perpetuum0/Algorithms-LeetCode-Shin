import heapq

def get_huffman_table(table, node, prefix=""):
    if type(node) is str:
        table[node] = prefix
    else:
        get_huffman_table(table, node[0], prefix+"0")
        get_huffman_table(table, node[1], prefix+"1")

def encode(s: str) -> tuple[str, dict]:
    if not s:
        return "", {}
    
    freq_table = dict()
    for ch in s:
        if not ch in freq_table:
            freq_table[ch] = 1
        else:
            freq_table[ch] += 1
            
    heap = [(freq, 0, ch) for ch, freq in freq_table.items()]
    heapq.heapify(heap)

    tie_breaker=1
    while len(heap)>1:
        tie_breaker+=1
        freq1, _, children1 = heapq.heappop(heap)
        freq2, _, children2 = heapq.heappop(heap)
        new = (freq1+freq2, tie_breaker, (children1, children2))
        heapq.heappush(heap, new)
    
    huffman_table = dict()
    get_huffman_table(huffman_table, heap[0][2])
    
    return "".join(huffman_table[ch] for ch in s), huffman_table


def decode(encoded: str, table: dict):
    table = {b: a for a, b in table.items()}

    prefix=""
    result=""
    for ch in encoded:
        if prefix=="":
            prefix=ch
        else:
            prefix+=ch
        if prefix in table:
            result+=table[prefix]
            prefix=""

    return result

if __name__ == "__main__":
    s = "This is a test string."
    encoded, table = encode(s)
    result = decode(encoded, table)
    print(result)
    
    s='f'*5+'e'*9+'c'*12+'b'*13+'d'*16+'a'*45
    print(decode(*encode(s)))