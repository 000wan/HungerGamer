N = 8

index = [[list()] * N, [list()] * N, [list()] * (2*N-1), [list()] * (2*N-1)]
#0: 행
#1: 열
#2: 오른쪽 위 대각선
#3: 오른쪽 아래 대각선

#piece = {}
value = {}

def findex(cord):
    ret = []
    ret.append(index[0][cord[0]])
    ret.append(index[1][cord[1]])
    ret.append(index[2][cord[0] - cord[1] + N - 1])
    ret.append(index[3][cord[0] + cord[1]])

    return ret

def locate(piece, cord):
    piece.cord = cord
    index[0][cord[0]].append(piece)
    index[1][cord[1]].append(piece)
    index[2][cord[0] - cord[1] + N - 1].append(piece)
    index[3][cord[0] + cord[1]].append(piece)

def inBoard(cord):
    return ( 0 <= cord[0] < N ) and ( 0 <= cord[1] < N )

class Piece:
    cord = list()
    movble = list()

    def __init__(self, cord):
        self.cord = list()
        self.movble = list()
        locate(self, cord)

class Pawn:
    cord = list()
    movble = list()
    def __init__(self, cord):
        self.cord = list()
        self.movble = list()
        locate(self, cord)

        #find movable locations
        for a in range(-1, 2):
            if inBoard([cord[0] + a, cord[1] + 1]): self.movble.append([cord[0], cord[1] + 1])

class Rook:
    cord = list()
    movble = list()

    def __init__(self, cord):
        self.cord = list()
        self.movble = list()
        locate(self, cord)

        # find movable locations
        for i in range(N):
            if i != cord[0]: self.movble.append([i, cord[1]])
            if i != cord[1]: self.movble.append([cord[0], i])

class Knight:
    cord = list()
    movble = list()

    def __init__(self, cord):
        self.cord = list()
        self.movble = list()
        locate(self, cord)

        # find movable locations
        a, b = (1, 2)
        for i in range(2):
            a *= -1
            for j in range(2):
                b *= -1
                if inBoard([cord[0] + a, cord[1] + b]): self.movble.append([cord[0] + a, cord[1] + b])
                if inBoard([cord[0] + b, cord[1] + a]): self.movble.append([cord[0] + b, cord[1] + a])

class Bishop:
    cord = list()
    movble = list()

    def __init__(self, cord):
        self.cord = list()
        self.movble = list()
        locate(self, cord)

        # find movable locations

class King:
    cord = list()
    movble = list()
    def __init__(self, cord):
        self.cord = list()
        self.movble = list()
        locate(self, cord)

        #find movable locations
        for a in range(-1, 2):
            for b in range(-1, 2):
                if not (a == 0 and b == 0):
                    if inBoard([cord[0] + a, cord[1] + b]): self.movble.append([cord[0] + a, cord[1] + b])

def main():
    first = list(map(int, input().split()))
    K = King(first)

    for loc in K.movble:
        flag = 0
        for ind in findex(loc):
            for p in ind:
                if loc in p.movble:
                    printf("")

main()