# membuat ai tower of hanoi sederhana
import os

state = {
    "A" : [4,3,2, 1],
    "B" : [],
    "C" : []
}

# fungsi untuk meampilkan pemindahan cakram ke terminal
def print_tower_state():
    print(f"tiang A: {state["A"]}")
    print(f"tiang B: {state["B"]}")
    print(f"tiang C: {state["C"]}")
    print(40*"_")

# fungsi utama menyelesaikan game
def tower_of_hanoi(n, tower, awal, tujuan, bantu):
    langkah = 0
    if n == 1:
        cakram = tower[awal].pop()
        tower[tujuan].append(cakram)
        print(f"pindahkan cakram {cakram} dari {awal} ke {tujuan}")
        print_tower_state()
        return
    
    tower_of_hanoi(n-1, tower, awal, bantu, tujuan)
    tower_of_hanoi(1, tower, awal, tujuan, bantu)
    tower_of_hanoi(n-1, tower, bantu, tujuan, awal)

while True:
    os.system('clear')
    print(state)
    print(20*"=" + "TOWER OF HANOI" + 20*"=")
    print_tower_state()
    tower_goal_state = input("Masukan tiang tujuan(A, B, atau C): ").upper().strip()
    for tower in state:
        if state[tower] == [4,3,2,1]:
            initial_state = tower
        
        if state[tower] != [4,3,2,1] and tower != tower_goal_state:
            empty_tower = tower
    
    if tower_goal_state == "A" and "A" != initial_state:
        tower_of_hanoi(4, state, initial_state, tower_goal_state, empty_tower)

    elif tower_goal_state == "B" and "B" != initial_state:
        tower_of_hanoi(4, state, initial_state, tower_goal_state, empty_tower)
        
    elif tower_goal_state == "C" and "C" != initial_state:
        tower_of_hanoi(4, state, initial_state, tower_goal_state, empty_tower)
        
    elif tower_goal_state == initial_state:
        print(f"tower {tower_goal_state} adalah kedaan awal atau initial state")
        
    else:
        print("kamu memasukan opsi yang salah")
    
    isLanjut = input("Mulai ulang dari awal(y/n): ")
    if isLanjut.lower() == "n":
        print("terimakasih sudah bermain")
        break    
    else:
        continue
print("program selesai")