N = 8

index = { 0: [[] for i in range(N)], 1: [[] for i in range(N)], 2: [[] for i in range(2*N-1)], 3: [[] for i in range(2*N-1)] }
#0: 열
#1: 행
#2: 오른쪽 위 대각선
#3: 오른쪽 아래 대각선

mark = {'P': ['♟', '♙'], 'R': ['♜', '♖'], 'N': ['♞', '♘'], 'B': ['♝', '♗'], 'Q': ['♛', '♕'], 'K': ['♚', '♔']}

value = {}

def locate(piece, cord):
    piece.cord = cord
    index[0][cord[0]].append(piece)
    index[1][cord[1]].append(piece)
    index[2][cord[0] - cord[1] + N - 1].append(piece)
    index[3][cord[0] + cord[1]].append(piece)

def hold(piece):
    c = piece.cord
    index[0][c[0]].remove(piece)
    index[1][c[1]].remove(piece)
    index[2][c[0] - c[1] + N - 1].remove(piece)
    index[3][c[0] + c[1]].remove(piece)

def move(piece, cord):
    hold(piece)
    locate(piece, cord)

def findex(cord):
    ret = []
    ret.append(index[0][cord[0]])
    ret.append(index[1][cord[1]])
    ret.append(index[2][cord[0] - cord[1] + N - 1])
    ret.append(index[3][cord[0] + cord[1]])

    return ret

def inBoard(cord):
    return ( 0 <= cord[0] < N ) and ( 0 <= cord[1] < N )

class Piece:
    cord = list()
    movble = list()
    type = ''
    team = 0 #0:white, 1:black

    def __init__(self, cord, type, team):
        self.cord = list()
        self.movble = list()
        self.type = type
        self.team = team
        locate(self, cord)

        if type == 'P':
            # find movable locations
            for a in range(-1, 2):
                if inBoard([cord[0] + a, cord[1] + 1]): self.movble.append([cord[0], cord[1] + 1])

        elif type == 'R':
            for i in range(N):
                if i != cord[0]: self.movble.append([i, cord[1]])
                if i != cord[1]: self.movble.append([cord[0], i])

        elif type == 'N':
            a, b = (1, 2)
            for i in range(2):
                a *= -1
                for j in range(2):
                    b *= -1
                    if inBoard([cord[0] + a, cord[1] + b]): self.movble.append([cord[0] + a, cord[1] + b])
                    if inBoard([cord[0] + b, cord[1] + a]): self.movble.append([cord[0] + b, cord[1] + a])

        elif type == 'B':
            a = 1
            for i in range(1, N - abs(cord[0]-cord[1])):
                if not inBoard([cord[0] + a, cord[1] + a]): a -= N
                if not inBoard([cord[0] + a, cord[1] + a]): a -= min(cord[0] + a, cord[1] + a)
                self.movble.append([cord[0] + a, cord[1] + a])
                a += 1
            a = 1
            for i in range(1, N - abs(cord[0] + cord[1] - N + 1)):
                if not inBoard([cord[0] + a, cord[1] - a]): a -= N
                if not inBoard([cord[0] + a, cord[1] - a]): a += max(abs(cord[0] + a), abs(cord[1] - a - N + 1))
                self.movble.append([cord[0] + a, cord[1] - a])
                a += 1

        elif type == 'Q':
            for i in range(N):
                if i != cord[0]: self.movble.append([i, cord[1]])
                if i != cord[1]: self.movble.append([cord[0], i])
            a = 1
            for i in range(1, N - abs(cord[0] - cord[1])):
                if not inBoard([cord[0] + a, cord[1] + a]): a -= N
                if not inBoard([cord[0] + a, cord[1] + a]): a -= min(cord[0] + a, cord[1] + a)
                self.movble.append([cord[0] + a, cord[1] + a])
                a += 1
            a = 1
            for i in range(1, N - abs(cord[0] + cord[1] - N + 1)):
                if not inBoard([cord[0] + a, cord[1] - a]): a -= N
                if not inBoard([cord[0] + a, cord[1] - a]): a += max(abs(cord[0] + a), abs(cord[1] - a - N + 1))
                self.movble.append([cord[0] + a, cord[1] - a])
                a += 1

        elif type == 'K':
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if not (a == 0 and b == 0):
                        if inBoard([cord[0] + a, cord[1] + b]): self.movble.append([cord[0] + a, cord[1] + b])

def encode(cord):
    res = chr(cord[0] + 97)
    res += str(cord[1] + 1)
    return res

def decode(cord):
    res = [ord(cord[0]) - 97, int(cord[1]) - 1]
    return res

def print_board():
    for i in range(N-1, -2, -1):
        if i == -1:
            print('  Ⓐ Ⓑ Ⓒ Ⓓ Ⓔ Ⓕ Ⓖ Ⓗ ')
        else:
            print(i+1, end=' ')
            for j in range(N):
                flag = 1
                for p in index[1][i]:
                    if p in index[0][j]:
                        print('%s' % mark[p.type][p.team], end=' ')
                        flag = 0
                        break
                if flag: print('⋯', end=' ')
        print()

def main():
    #first = list(map(int, input().split()))

    B1 = Piece(decode('b3'), 'B', 1)
    K1 = Piece(decode('h4'), 'K', 1)
    N1 = Piece(decode('f4'), 'N', 0)
    R1 = Piece(decode('g4'), 'R', 0)

    print_board()

    hold(K1)
    for loc in K1.movble:
        for ind in findex(loc):
            for p in ind:
                if loc in p.movble:
                    print("%s: %sx%s" % (encode(loc), p.type, encode(loc)))


main()