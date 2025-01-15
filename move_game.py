import tkinter as tk
import bili_listener
import threading
import asyncio


class MoveDotGame:
    def __init__(self, root):
        self.root = root
        self.root.title("移动红点游戏")
        
        # 创建画布
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack(padx=20, pady=20)

        # 创建红点
        self.dot = self.canvas.create_oval(190, 190, 210, 210, fill="red")  # 初始位置

        # # 创建输入框
        # self.input_entry = tk.Entry(self.root, width=20)
        # self.input_entry.pack(pady=10)
        # self.input_entry.bind("<Return>", self.move_dot)  # 绑定回车键事件

        self.listener = None
        self.start_listener()

    def move_dot(self, user_name, direction):
        """根据输入移动红点"""
        print('%s 执行操作: %s' % (user_name, direction))

        # direction = self.input_entry.get().strip().lower()  # 获取输入并处理
        # self.input_entry.delete(0, tk.END)  # 清空输入框

        if direction == "上":
            self.canvas.move(self.dot, 0, -10)  # 向上移动
        elif direction == "下":
            self.canvas.move(self.dot, 0, 10)  # 向下移动
        elif direction == "左":
            self.canvas.move(self.dot, -10, 0)  # 向左移动
        elif direction == "右":
            self.canvas.move(self.dot, 10, 0)  # 向右移动
        else:
            print("无效的指令！请使用 '上'、'下'、'左'、'右'")

    def start_listener(self):
        """启动网络监听"""
        self.listener = bili_listener.BiliListener(self.move_dot)
        listener_thread = threading.Thread(target=self.run_listener)
        listener_thread.daemon = True
        listener_thread.start()

    def run_listener(self):
        """运行网络监听"""
        asyncio.run(self.listener.main())

def main():
    root = tk.Tk()
    game = MoveDotGame(root)
    root.mainloop()

if __name__ == "__main__":
    main() 