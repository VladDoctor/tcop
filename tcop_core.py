class tCOP(object):
    def __init__(self, csv_objects, csv_indexer):
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
        with open('tables/result.csv', 'w') as res_file:
            res_file.write(self.result_table)
        pass
    
    def tfcolums(self):
        for column in self.objects['first']:
            column.append('0')
        for column in self.objects['second']:
            column.append('0')

if __name__ == '__main__':
    
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
    
    with open('tables/1.csv') as csv_object:
        for csv_o in csv_object.readlines():
           csv_objects['first'].append(csv_o.replace('\n', '').split(','))
           csv_objects_for_indexer['first'].append(csv_o.replace('\n', '').split(','))
        csv_object_s = open('tables/2.csv')
        for csv_o in csv_object_s.readlines():
           csv_objects['second'].append(csv_o.replace('\n', '').split(','))
           csv_objects_for_indexer['second'].append(csv_o.replace('\n', '').split(','))
        csv_object_s.close()
    reader = tCOP(csv_objects, csv_objects_for_indexer)
    reader.find_matches_m()
    reader.matrix()
    reader.find_matches_nm()
    reader.nan()
    reader.log_table()
    reader.write_result()
else:
    pass
