"""
Мои попытки написания кода самостоятельно,
не привели к успеху в отведенное время.
А попытки гугления по сложным моментам в конце концов привели
к понимаю того что это уже не мой код.
Вместо разбора ДЗ
переписал и полностью разобрался как работает
нижеприведенная реализация алгоритма  кодирования Хаффмана
"""
import heapq
from collections import Counter, namedtuple

class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class Leaf (namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"

def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _cont1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(freq, _count, root)] = h
        root.walk(code, "")

    return code

def main():
    s = input()
    code = huffman_encode(s)
    encode = "".join(code[ch] for ch in s)
    print(len(code), len(encode))
    for ch in sorted(code):
        print("{}: {}".format(ch, code [ch]))
    print(encode)

if __name__ == "__main__":
    main()

