class List:
    def __init__(self, size):
        if size <= 0: # proverka na razmer
            raise ValueError("Error")
        self.size = size
        self.N_index = 0
        self.Z_V = [0] * size # Znacheniya/znacheniya
        self.write_count = 0
        self.read_count = 0

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Error")
        self.read_count += 1
        return self.Z_V[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Error")
        if not (-100 <= value <= 100):
            raise ValueError("Error")
        self.Z_V[index] = value
        self.write_count += 1
        if index >= self.N_index:  
            self.N_index = index + 1
    def resize(self):
        new_size=self.size + 1
        new_list = [0] * new_size
        for i in range(self.size):
            new_list[i] = self.Z_V[i]
        self.Z_V = new_list
        self.size = new_size

    def append(self, value):
        if not (-100 <= value <= 100):
            raise ValueError("Erroe")

        if self.N_index >= self.size:
            self.resize()

        self.Z_V[self.N_index] = value
        self.N_index += 1
        self.write_count += 1

    def summ(self, other):
        if self.N_index > other.N_index:
            max_size = self.N_index
        else:
            max_size = other.N_index
        new_list = List(max_size)
        for i in range(max_size):
            if i < self.N_index:
                value1 = self.Z_V[i]
            else:
                value1 = 0
            if i < other.N_index:
                value2 = other.Z_V[i]
            else:
                value2 = 0
            new_list.append(value1 + value2)
        return new_list
    def minus(self, other):
        if self.N_index > other.N_index:
            max_size = self.N_index
        else:
            max_size = other.N_index
        new_list = List(max_size)
        for i in range(max_size):
            if i < self.N_index:
                value1 = self.Z_V[i]
            else:
                value1 = 0
            if i < other.N_index:
                value2 = other.Z_V[i]
            else:
                value2 = 0
            new_list.append(value1 - value2)
        return new_list
    def display(self):
        print(self.Z_V[:self.N_index])
        self.read_count += 1 #Если чтение всего массива считается вместе с чтением отдельного элемента

    def get_counters(self):
        return (f'Сколько прочитали: {self.read_count}', f'Сколько написали:{self.write_count}')


my_list = List(5)

my_list[0] = 7
my_list[1] = -20
my_list[2] = 1
my_list[3] = 33
my_list[4] = 52
my_list.display() # Chteinye massiva

print(my_list[2]) # element


print( my_list.get_counters())
my_list.append(5)
my_list.display()

my_list1 = List(5)

my_list1[0] = 74
my_list1[1] = -2
my_list1[2] = 14
my_list1[3] = 2
my_list1[4] = 5
result_list = my_list1.summ(my_list)
result_list.display()
result_list = my_list1.minus(my_list)
result_list.display()