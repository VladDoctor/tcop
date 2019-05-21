from tkinter import *
from tkinter.ttk import Combobox
import glob
from tkinter import messagebox

class tCOP(object):
    def __init__(self, csv_objects, csv_indexer, result_path):
        self.result_path = result_path
        self.objects = csv_objects
        self.indexer = csv_indexer
        self.result = []
        self.index = {
            'first' : [],
            'second' : []
        }
        self.nan_list = []
        self.alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
        self.tfcolums()
        
    def find_matches_m(self):
        for num in self.objects['second']:
            for element in num:
                num[num.index(element)] = int(element + str(num.index(element)))
        for num in self.objects['first']:
            for element in num:
                num[num.index(element)] = int(element + str(num.index(element)))
        for intt in range(len(self.objects['first'])):
            self.objects['matches'] = set(self.objects['first'][intt]) - set(self.objects['second'][intt])
            self.objects['match'] = [self.objects['first'][intt].remove(i) for i in self.objects['matches'] if i in self.objects['first'][intt]]
        
    def find_matches_nm(self):
        for num in range(len(self.objects['first'])):
            self.index['first'].append([int(str(index)[-1:][0]) for index in self.objects['first'][num]])

    def nan(self):
        for list in range(len(self.indexer['first'])):
            self.index['second'].append([self.alphabet.split(' ')[self.indexer['first'][list].index(i)] for i in self.indexer['first'][list] if not self.indexer['first'][list].index(i) in self.index['first'][list]])
        self.result = self.index['second']
        
    def matrix(self):
        for strr in range(len(self.objects['first'])):
            self.objects['matrix'][str(strr)] = ', '.join([str(index)[-1:][0] for index in self.objects['first'][strr]])

    def log_table(self):
        self.result_table = []
        for string in self.result:
            if not len(string) == 0:
                string_indexer = self.indexer['first'][self.result.index(string)]
                self.result_table.append(str(self.result.index(string) + 1) + ', ,' + ','.join(string) + ', ,' + str(len(string)) + ',' + str(len(self.indexer['first'][self.result.index(string)]) - len(string)) + ', ,' + str(len(string)/len(string_indexer))[:5])
            else:
                continue
        self.result_table = '\n'.join(self.result_table)

    def write_result(self):
        with open(self.result_path + '/result.csv', 'w') as res_file:
            res_file.write(self.result_table)
        messagebox.showinfo('Final', 'Successfully completed!')
    
    def tfcolums(self):
        for column in self.objects['first']:
            column.append('0')
        for column in self.objects['second']:
            column.append('0')

if __name__ == '__main__':

    def csv_glob():
        directory_path = []
        with open('config.txt', 'r') as config:
            for read in config.readlines():
                directory_path.append(read.split(' : ')[1].split('\n')[0])
            pass
        pass
        begin_path = directory_path[0] + '/*.csv'
        return tuple(glob.glob(begin_path))

    def checked_start():

        csv_objects = {
            'first'   : [],
            'second'  : [],
            'matches' : [],
            'matrix'  : {}
        }
        csv_objects_for_indexer = {
            'first'  : [],
            'second' : []
        }

        first_path = selecter.get()
        second_path = selecter_s.get()
        result_path = '\\'.join(first_path.split('\\')[:-1])

        with open(first_path) as csv_object:
            for csv_o in csv_object.readlines():
                csv_objects['first'].append(csv_o.replace('\n', '').split(','))
                csv_objects_for_indexer['first'].append(csv_o.replace('\n', '').split(','))
            csv_object_s = open(second_path)
            for csv_o in csv_object_s.readlines():
                csv_objects['second'].append(csv_o.replace('\n', '').split(','))
                csv_objects_for_indexer['second'].append(csv_o.replace('\n', '').split(','))
            csv_object_s.close()
            
        reader = tCOP(csv_objects, csv_objects_for_indexer, result_path)
        reader.find_matches_m()
        reader.matrix()
        reader.find_matches_nm()
        reader.nan()
        reader.log_table()
        reader.write_result()

    def save():
        with open('config.txt', 'w') as config:
            if txt_s.get() == '':
                string = 'BEGIN : ' + txt.get() + '\n' + 'END : ' + txt_s.get()
                config.write(string)
                messagebox.showinfo('Save', 'Done!')
            elif (txt.get() == '') and (txt_s.get() == ''):
                messagebox.showerror('Save', 'Null values...')
            else:
                string = 'BEGIN : ' + txt.get() + '\n' + 'END : ' + txt_s.get()
                config.write(string)
                messagebox.showinfo('Save', 'Done!')         
        pass
    
    root = Tk()
    root.title('tCop 1.0 - Efimenko Vlad')
    root.geometry('450x450')

    label = Label(root, text="First table ->")  
    label.grid(column=0, row=0)  
    
    selecter = Combobox(root, width=50)
    selecter['values'] = csv_glob()
    selecter.current(0)
    selecter.grid(column=1, row=0)

    label_s = Label(root, text="Second table ->")  
    label_s.grid(column=0, row=1)  
    
    selecter_s = Combobox(root, width=50)
    selecter_s['values'] = csv_glob()
    selecter_s.current(1)
    selecter_s.grid(column=1, row=1)

    btn = Button(root, text='Compare', command=checked_start)  
    btn.grid(column=1, row=2)

    label_txt = Label(root, text="Tables directory")  
    label_txt.grid(column=0, row=3)
    btn_t = Button(root, text="Save", command=save)  
    btn_t.grid(column=2, row=3)  

    txt = Entry(root,width=50)  
    txt.grid(column=1, row=3)

    label_txt_s = Label(root, text="Result directory")  
    label_txt_s.grid(column=0, row=4) 

    txt_s = Entry(root,width=50)  
    txt_s.grid(column=1, row=4)
    btn_t_s = Button(root, text="Save", command=save)  
    btn_t_s.grid(column=2, row=4)

    label_form = Label(root, text="Form(result) example:")  
    label_form.grid(column=1, row=5)
    label_form = Label(root, text="STRING | COLUMN INDICES(W) | Wrong(W) | Loyal(L) | W/L")  
    label_form.grid(column=1, row=6) 
    
    root.mainloop()
    
else:
    exit()
