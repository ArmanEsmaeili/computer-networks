import socket
import threading
from queue import Queue

# تنظیمات سرور
SERVER_HOST = 'localhost'
SERVER_PORT = 12345
MAX_PLAYERS = 2  # حداکثر تعداد بازیکنان برای یک بازی

# ذخیره بازیکنان در Queue
player_queue = Queue()

# تابع برای بررسی برنده بازی
def check_winner(board):
    # بررسی ردیف‌ها، ستون‌ها و قطرها
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

# تابع برای پردازش بازی برای هر دو بازیکن
def game_thread(player1_socket, player2_socket):
    board = [[" " for _ in range(3)] for _ in range(3)]  # تخته بازی
    players = [player1_socket, player2_socket]
    current_player = 0

    while True:
        # ارسال تخته به بازیکن فعلی
        board_state = "\n".join(["|".join(row) for row in board])
        players[current_player].send(f"Current board:\n{board_state}\nYour turn! (X)" if current_player == 0 else f"Current board:\n{board_state}\nYour turn! (O)".encode())

        # دریافت حرکت از بازیکن
        move = players[current_player].recv(1024).decode()
        try:
            row, col = map(int, move.split(","))
            if board[row][col] == " ":
                board[row][col] = "X" if current_player == 0 else "O"
                winner = check_winner(board)
                if winner:
                    players[0].send(f"Game Over! {winner} wins!".encode())
                    players[1].send(f"Game Over! {winner} wins!".encode())
                    break
                current_player = 1 - current_player  # نوبت بازیکن تغییر می‌کند
            else:
                players[current_player].send("Cell already taken, try again!".encode())
        except ValueError:
            players[current_player].send("Invalid input. Use row,col format.".encode())
        except IndexError:
            players[current_player].send("Invalid move. Out of board bounds.".encode())

# تابع برای مدیریت اتصال کاربران و شروع بازی
def handle_client(client_socket):
    player_queue.put(client_socket)
    if player_queue.qsize() == MAX_PLAYERS:
        player1 = player_queue.get()
        player2 = player_queue.get()
        threading.Thread(target=game_thread, args=(player1, player2)).start()

# تنظیمات سوکت سرور
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)

print(f"Server started on {SERVER_HOST}:{SERVER_PORT}... Waiting for players.")

# پذیرش اتصال کاربران
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Player {client_address} connected.")
    threading.Thread(target=handle_client, args=(client_socket,)).start()
