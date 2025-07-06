# membuat ai tower of hanoi sederhana

state = {
    "A" : [4,3,2, 1],
    "B" : [],
    "C" : []
}

def print_tower_state():
    print(f"tiang A: {state["A"]}")
    print(f"tiang B: {state["B"]}")
    print(f"tiang C: {state["C"]}")
    print(40*"_")

def move(n, tower, awal, tujuan, bantu):
    langkah = 0
    if n == 1:
        cakram = tower[awal].pop()
        tower[tujuan].append(cakram)
        print(f"pindahkan cakram {cakram} dari {awal} ke {tujuan}")
        print_tower_state()
        return
    
    move(n-1, tower, awal, bantu, tujuan)
    move(1, tower, awal, tujuan, bantu)
    move(n-1, tower, bantu, tujuan, awal)

move(4, state, "A", "C", "B")