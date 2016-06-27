# -*- coding= utf-8 -*-
from Tkinter import *
import tkMessageBox
import tkFileDialog
import time
import os


class Utils():

    def __init__(self, master=None):
        # Frame.__init__(self, master)
        # self.grid(row=0, column=0, sticky="nsew")
        self.create_frame()    # 初始化frame

    def get_current_timestamp(self):
        self.entry_content_get_current_timestamp.set(int(time.time()))

    def timestamp_to_time(self):
        if self.entry_before_content_timestamp_to_time.get() == '':
            tkMessageBox.showinfo(title='dialog', message='请输入时间戳')
            return
        else:
            self.entry_after_content_timestamp_to_time.set(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(self.entry_before_content_timestamp_to_time.get()))))

    def time_to_timestamp(self):
        self.entry_after_content_time_to_timestamp.set(int(time.mktime(time.strptime(self.entry_before_content_time_to_timestamp.get(),'%Y-%m-%d %H:%M:%S'))))

    def select_file_dir(self):
        file_dir = tkFileDialog.askdirectory(initialdir="/",title='Pick a directory')
        self.entry_directory.delete(0,END)
        self.entry_directory.insert(0, file_dir)

    def get_files_name(self):
        self.file_path = self.entry_directory.get()
        if self.file_path is None or self.file_path == '':
            tkMessageBox.showinfo(title='dialog', message='请选择文件目录')
            raise AssertionError('请选择文件目录')
        self.files_name_list = []
        files_name = ''
        for root, dirs, files in os.walk(self.file_path):
            self.files_name_list = ['']*len(files)
            for i in range(len(files)):
                self.files_name_list[i] = files[i].decode('gbk')
                files[i] = files[i].decode('gbk') + '\n'
            if root == self.file_path:
                files_name = files_name.join(files)
                break
        # print self.files_name_list
        # print files_name
        self.text_files_name.delete('1.0', END)
        self.text_files_name.insert('1.0', files_name)

    def replace_files_name(self):
        self.get_files_name()
        if self.entry_string_to_be_replaced.get() == '':
            tkMessageBox.showinfo(title='dialog', message='请输入需要替换的内容')
            return
        for i in range(len(self.files_name_list)):
            if os.path.basename(self.files_name_list[i]).find(self.entry_string_to_be_replaced.get()) == -1:
                pass
            else:
                name = os.path.basename(self.files_name_list[i])
                name = name.replace(self.entry_string_to_be_replaced.get(), self.entry_string_replace.get())
                name = "/" + name
                full_name = self.file_path + name
                # print self.file_path + self.files_name_list[i]
                # print full_name
                os.rename(self.file_path + "/" + self.files_name_list[i], full_name)
        self.get_files_name()

    def create_frame(self):
        top = Tk()
        top.title("Testing Tools")
        top.geometry('700x500')

        """
        初始化row，赋值随意，每行的值累加即可，没有其他实际意义。
        只需修改行在row列表中的位置，即可更新所在行数。
        """
        row_label_time_change = 0
        row_get_current_timestamp = 1
        row_timestamp_to_time = 2
        row_time_to_timestamp = 3
        row_get_files_name = 4
        row_replace_files_name = 5
        row_batch_modify_file_names = 6
        row_text_files_name = 7
        row = [row_label_time_change, row_get_current_timestamp, row_timestamp_to_time, row_time_to_timestamp,
               row_batch_modify_file_names, row_get_files_name, row_replace_files_name, row_text_files_name]

        # pack方式
        # Button(top, text="获取当前时间戳", command = get_current_timestamp, width=12, height=1, font=('Arial', 10)).pack(side=LEFT, fill=X)
        # s = Text(width=15, height=2)
        # s.pack(side=LEFT, fill=X)

        # grid方式
        Label(top, text="时间转换", bg="green", font=("Arial", 10), width=8, height=1).grid(row=row.index(row_label_time_change), sticky=W)  # sticky值有：N/S/E/W

        # 获取当前时间戳
        Button(top, text="获取当前时间戳", command=self.get_current_timestamp, width=16, height=1, font=('Arial', 10)).grid(row=row.index(row_get_current_timestamp), column=0, sticky=S)
        self.entry_content_get_current_timestamp = StringVar()
        self.entry_get_current_timestamp = Entry(top, textvariable=self.entry_content_get_current_timestamp)
        self.entry_get_current_timestamp.grid(row=row.index(row_get_current_timestamp), column=1, sticky=W)

        # 时间戳转换为时间
        self.entry_before_content_timestamp_to_time = StringVar()
        self.entry_before_timestamp_to_time = Entry(top, textvariable=self.entry_before_content_timestamp_to_time)
        self.entry_before_timestamp_to_time.grid(row=row.index(row_timestamp_to_time), column=0, sticky=W)
        Button(top, text="时间戳   >   时间", command=self.timestamp_to_time, width=18, height=1, font=('Arial', 10)).grid(row=row.index(row_timestamp_to_time), column=1, sticky=S)
        self.entry_after_content_timestamp_to_time = StringVar()
        self.entry_after_timestamp_to_time = Entry(top, textvariable=self.entry_after_content_timestamp_to_time)
        self.entry_after_timestamp_to_time.grid(row=row.index(row_timestamp_to_time), column=2)

        # 时间转换为时间戳
        self.entry_before_content_time_to_timestamp = StringVar()
        self.entry_before_content_time_to_timestamp.set(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))  # 默认显示当前时间
        self.entry_before_time_to_timestamp = Entry(top, width=20, textvariable=self.entry_before_content_time_to_timestamp)
        self.entry_before_time_to_timestamp.grid(row=row.index(row_time_to_timestamp), column=0, sticky=W)
        Button(top, text="   时间     >  时间戳", command=self.time_to_timestamp, width=18, height=1, font=('Arial', 10)).grid(row=row.index(row_time_to_timestamp), column=1, sticky=S)
        self.entry_after_content_time_to_timestamp = StringVar()
        self.entry_after_time_to_timestamp = Entry(top, textvariable=self.entry_after_content_time_to_timestamp)
        self.entry_after_time_to_timestamp.grid(row=row.index(row_time_to_timestamp), column=2)

        # 或取某一目录下所有文件名，并批量替换文件名中的字符串
        Label(top, text="批量修改文件名称", bg="green", font=("Arial", 10), width=16, height=1).grid(row=row.index(row_batch_modify_file_names), sticky=W)
        Label(top, text='文件目录:  ').grid(row=row.index(row_get_files_name), column=0, sticky=E)
        self.entry_directory = Entry(top, width=20)
        self.entry_directory.grid(row=row.index(row_get_files_name), column=1, sticky=W)
        Button(top, text="选择文件目录", command=self.select_file_dir, width=10, height=1, font=('Arial', 10)).grid(row=row.index(row_get_files_name), column=2, sticky=W)
        self.file_path = self.entry_directory.get()
        Button(top, text="获取该目录下所有文件名", command=self.get_files_name, width=18, height=1, font=('Arial', 10)).grid(row=row.index(row_get_files_name), column=3, sticky=W)
        # 需要替换的字符串
        Label(top, text='需要替换的内容:  ').grid(row=row.index(row_replace_files_name), column=0, sticky=E)
        self.entry_string_to_be_replaced = Entry(top, width=20)
        self.entry_string_to_be_replaced.grid(row=row.index(row_replace_files_name), column=1, sticky=W)
        # 替换成的字符串
        Label(top, text='替换成的内容:  ').grid(row=row.index(row_replace_files_name), column=2, sticky=E)
        self.entry_string_replace = Entry(top, width=20)
        self.entry_string_replace.grid(row=row.index(row_replace_files_name), column=3, sticky=W)
        # 执行替换
        Button(top, text="执行替换", command=self.replace_files_name, width=8, height=1, font=('Arial', 10)).grid(row=row.index(row_replace_files_name), column=4, sticky=S)

        # 文件名文本框
        self.text_files_name = Text(width=90, height=20)
        self.text_files_name.grid(row=row.index(row_text_files_name), column=0, sticky=S, columnspan=5)

        top.mainloop()

if __name__ == "__main__":
    Utils()
