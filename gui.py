import tkinter as tk
import threading
import trainer
import tkinter.ttk as ttk


# 自定义的线程函数类
def thread_it(func, *args):
    '''将函数放入线程中执行'''
    # 创建线程
    t = threading.Thread(target=func, args=args)
    # 守护线程
    t.setDaemon(True)
    # 启动线程
    t.start()


def monitoring_interface(cfg):
    window = tk.Tk()
    window.title('循环取货路径规划软件 v0.1')
    window.geometry('400x400')

    var_epoch = tk.StringVar()  # epoch变量储存器
    var_batch = tk.StringVar()  # batch变量储存器
    var_loss = tk.StringVar()  # loss变量储存器
    var_reward = tk.StringVar()  # reward变量储存器
    var_result_tour_length = tk.StringVar()  # reward变量储存器
    var_result_tour_length.set("优化未完成，请等待")
    var_result_tour_index = tk.StringVar()  # reward变量储存器
    var_result_tour_index.set("优化未完成，请等待")
    var = [var_epoch, var_batch, var_loss, var_reward, var_result_tour_length, var_result_tour_index]

    title = tk.Label(window, text="训练过程监控界面", font=('Arial', 15))
    title.place(relx=0.30, rely=0)

    l1 = tk.Label(window,
                  textvariable=var_epoch,  # 使用 textvariable 替换 text, 因为这个可以变化
                  bg='white', font=('Arial', 12), width=18, height=2)
    l1.place(relx=0.4, rely=0.1)
    l1_r = tk.Label(window, text="epoch", font=('Arial', 12), width=8, height=2)
    l1_r.place(relx=0.18, rely=0.1)

    l2 = tk.Label(window,
                  textvariable=var_batch,  # 使用 textvariable 替换 text, 因为这个可以变化
                  bg='white', font=('Arial', 12), width=18, height=2)
    l2.place(relx=0.4, rely=0.2)
    l2_r = tk.Label(window, text="batch", font=('Arial', 12), width=8, height=2)
    l2_r.place(relx=0.18, rely=0.2)

    l3 = tk.Label(window,
                  textvariable=var_loss,  # 使用 textvariable 替换 text, 因为这个可以变化
                  bg='white', font=('Arial', 12), width=18, height=2)
    l3.place(relx=0.4, rely=0.3)
    l3_r = tk.Label(window, text="cr_loss", font=('Arial', 12), width=8, height=2)
    l3_r.place(relx=0.18, rely=0.3)

    l4 = tk.Label(window,
                  textvariable=var_reward,  # 使用 textvariable 替换 text, 因为这个可以变化
                  bg='white', font=('Arial', 12), width=18, height=2)
    l4.place(relx=0.4, rely=0.4)
    l4_r = tk.Label(window, text="reward", font=('Arial', 12), width=8, height=2)
    l4_r.place(relx=0.18, rely=0.4)

    l5 = tk.Label(window,
                  textvariable=var_result_tour_length,  # 使用 textvariable 替换 text, 因为这个可以变化
                  bg='white', font=('Arial', 12), width=18, height=2)
    l5.place(relx=0.4, rely=0.5)
    l5_r = tk.Label(window, text="tour_length", font=('Arial', 12), width=8, height=2)
    l5_r.place(relx=0.18, rely=0.5)

    l6 = tk.Label(window,
                  textvariable=var_result_tour_index,  # 使用 textvariable 替换 text, 因为这个可以变化
                  bg='white', font=('Arial', 12), width=18, height=2)
    l6.place(relx=0.4, rely=0.6)
    l6_r = tk.Label(window, text="tour_index", font=('Arial', 12), width=8, height=2)
    l6_r.place(relx=0.18, rely=0.6)

    b2 = tk.Button(window, text="关闭窗口", width=15, command=lambda: destroy(window))
    b2.place(relx=0.35, rely=0.75)

    l7 = tk.Label(window, text="注意：训练完成后的模型文件默认存放于vrp文件夹")
    l7.place(relx=0, rely=0.85)

    print('监控界面初始化')
    thread_it(trainer.begin_train, var, cfg)
    window.mainloop()


def trian_parameters(window):
    window.destroy()
    window = tk.Tk()
    window.title('循环取货路径规划软件 v0.1')
    window.geometry('350x250')

    lbl0 = tk.Label(window, text="训练参数设置界面", font=('Arial', 15))
    lbl0.grid(column=1, row=0)

    lbl1 = tk.Label(window, text="Number of cities")
    lbl1.grid(column=0, row=1)
    combo1 = ttk.Combobox(window)
    combo1['values'] = (10, 20, 50)
    combo1.current(0)
    combo1.grid(column=1, row=1)

    lbl2 = tk.Label(window, text="actor lr")
    lbl2.grid(column=0, row=2)
    combo2 = ttk.Combobox(window)
    combo2['values'] = (5e-3, 1e-3, 1e-2)
    combo2.current(0)
    combo2.grid(column=1, row=2)

    lbl3 = tk.Label(window, text="critic lr")
    lbl3.grid(column=0, row=3)
    combo3 = ttk.Combobox(window)
    combo3['values'] = (5e-3, 1e-3, 1e-2)
    combo3.current(0)
    combo3.grid(column=1, row=3)

    lbl4 = tk.Label(window, text="batch size")
    lbl4.grid(column=0, row=4)
    combo4 = ttk.Combobox(window)
    combo4['values'] = (128, 256, 512)
    combo4.current(0)
    combo4.grid(column=1, row=4)

    lbl5 = tk.Label(window, text="train size")
    lbl5.grid(column=0, row=5)
    combo5 = ttk.Combobox(window)
    combo5['values'] = (10000, 50000, 100000)
    combo5.current(0)
    combo5.grid(column=1, row=5)

    lbl6 = tk.Label(window, text="valid size")
    lbl6.grid(column=0, row=6)
    combo6 = ttk.Combobox(window)
    combo6['values'] = (10, 50, 100)
    combo6.current(0)
    combo6.grid(column=1, row=6)

    inputs = [combo1, combo2, combo3, combo4, combo5, combo6]

    b2 = tk.Button(window, text="开始训练", width=15, command=lambda: begain(window, inputs))
    b2.place(relx=0.35, rely=0.7)

    window.mainloop()
    monitoring_interface()


def optim_parameters(window):
    window.destroy()
    window = tk.Tk()
    window.title('循环取货路径规划软件 v0.1')
    window.geometry('450x250')

    lbl0 = tk.Label(window, text="请输入模型文件地址", font=12)
    lbl0.place(relx=0.35, rely=0)

    lbl1 = tk.Label(window, text="地址：")
    lbl1.place(relx=0.05, rely=0.1)
    input1 = tk.Entry(window, width=50)
    input1.place(relx=0.15, rely=0.1)

    inputs = [input1]

    b1 = tk.Button(window, text="开始优化", width=15, command=lambda: optimization(window, inputs))
    b1.place(relx=0.38, rely=0.25)

    lbl1 = tk.Label(window, text="注意：")
    lbl1.place(relx=0, rely=0.5)
    lbl2 = tk.Label(window, text="地址格式：C:/Users/root/Desktop/Path planning/vrp/10/14_58_29.010789")
    lbl2.place(relx=0, rely=0.6)

    window.mainloop()
    optimization(window, inputs)


def begain(window, inputs):
    cfg = [inputs[0].get(), inputs[1].get(), inputs[2].get(), inputs[3].get(), inputs[4].get(), inputs[5].get()]
    window.destroy()
    monitoring_interface(cfg)


def optimization(window, inputs):
    cfg = [inputs[0].get()]
    window.destroy()
    optimization_interface(cfg)


def destroy(window):
    window.destroy()


def optimization_interface(cfg):
    window = tk.Tk()
    window.title('循环取货路径规划软件 v0.1')
    window.geometry('400x200')

    title = tk.Label(window, text="优化结果展示界面", font=('Arial', 15))
    title.place(relx=0.30, rely=0)

    var_tour_length = tk.StringVar()  # tour_length变量储存器
    var_tour_index = tk.StringVar()  # tour_length变量储存器
    var = [var_tour_length, var_tour_index]
    var[0].set("优化开始，请等待")
    var[1].set("优化开始，请等待")
    l1 = tk.Label(window,
                  textvariable=var_tour_length,
                  bg='white', font=('Arial', 12), width=30, height=2)
    l1.place(relx=0.3, rely=0.20)
    l1_r = tk.Label(window, text="tour_length", font=('Arial', 12), width=8, height=2)
    l1_r.place(relx=0.08, rely=0.20)
    l2 = tk.Label(window,
                  textvariable=var_tour_index,
                  bg='white', font=('Arial', 12), width=30, height=2)
    l2.place(relx=0.3, rely=0.45)
    l2_r = tk.Label(window, text="tour_index", font=('Arial', 12), width=8, height=2)
    l2_r.place(relx=0.08, rely=0.45)

    b1 = tk.Button(window, text="关闭界面", width=15, height=1, command=lambda: destroy(window))
    b1.place(relx=0.38, rely=0.7)

    print('优化界面初始化')
    thread_it(trainer.optimization, var, cfg)
    window.mainloop()


def tk_interface():
    window = tk.Tk()
    window.geometry('450x300')
    window.title('循环取货路径规划软件 v0.1')
    print('界面初始化')

    lbl1 = tk.Label(window, text="循环取货路径规划软件 v0.1", font=15)
    lbl1.place(relx=0.3, rely=0)
    b1 = tk.Button(window, text="模型训练", width=15, height=1, command=lambda: trian_parameters(window))
    b1.place(relx=0.38, rely=0.15)
    b2 = tk.Button(window, text="路线优化", width=15, height=1, command=lambda: optim_parameters(window))
    b2.place(relx=0.38, rely=0.3)

    lbl2 = tk.Label(window, text="注意：")
    lbl2.place(relx=0, rely=0.5)
    lbl3 = tk.Label(window, text="1、模型训练，对指定路线进的网络进行训练操作")
    lbl3.place(relx=0, rely=0.58)
    lbl4 = tk.Label(window, text="2、路线优化，指定训练文件，直接输出优化结果")
    lbl4.place(relx=0, rely=0.66)
    lbl5 = tk.Label(window, text="3、操作前，请将目标点二项图文件以graph命名存放与本软件tool文件夹下")
    lbl5.place(relx=0, rely=0.74)

    # 主循环
    window.mainloop()


if __name__ == '__main__':
    tk_interface()
