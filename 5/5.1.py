infile = open("input.txt", 'r')
contents = infile.read()
codes = contents.split('\n')


def code_to_row(code):
    row_code = code[0:7]
    F = '0'
    B = '1'

    binary_code = row_code.replace('F', F).replace('B', B)
    row_int = int(binary_code, 2)
    return row_int


def code_to_seat(code):
    seat_code = code[7:]
    R = '1'
    L = '0'

    binary_code = seat_code.replace('R', R).replace('L', L)
    seat_int = int(binary_code, 2)
    return seat_int


def code_to_id(code):
    if not code:
        return 0
    row = code_to_row(code)
    seat = code_to_seat(code)
    seat_id = row * 8 + seat
    return seat_id


ids = list(map(code_to_id, codes))

ids.sort()
prev = 850
for seat in ids:
    if seat - prev > 1:
        print(seat)
    prev = seat
