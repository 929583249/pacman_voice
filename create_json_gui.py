import tkinter as tk
from tkinter import simpledialog
import json

def save_text_to_json():
    # 创建一个新的Tkinter窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    
    # 弹出一个输入框让用户输入文本
    user_input = simpledialog.askstring("Input", "Please enter your text:")
    
    if user_input is not None:
        # 构建一个包含用户输入的字典
        data = {"text": user_input}
        
        # 将数据保存到package.json文件
        with open('package.json', 'w') as f:
            json.dump(data, f, indent=4)
    
    root.destroy()

if __name__ == "__main__":
    save_text_to_json()
