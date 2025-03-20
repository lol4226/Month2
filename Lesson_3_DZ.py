class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
        
    @property
    def cpu(self):
        return self.__cpu
    
    @cpu.setter
    def cpu(self, cpuMemory):
        if type(cpuMemory) == int:
            self.__cpu = cpuMemory
        else:
            raise TypeError("Wrong type of cpu, need str")
        
    @property
    def memory(self):
        return self.__memory
    
    @memory.setter
    def memory(self, memory):
        if type(memory) == int:
            self.__memory = memory
        else:
            raise TypeError("Wrong type of memory, need int")
        
    def Make_Computations(self):
        return self.__memory * self.__cpu
    
    def __str__(self):
        return f"Cpu memory: {self.__cpu}, memory: {self.__memory}"
    
    def __eq__(self, value):
        return self.__memory == value
    
    def __gt__(self, value):
        return self.__memory > value
    
    def __lt__(self, value):
        return self.__memory < value
    
    def __ne__(self, value):
        return self.__memory != value
    
    def __ge__(self, value):
        return self.__memory >= value
    
    def __le__(self, value):
        return self.__memory <= value
    
class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list
        
    @property
    def sim_cards_list(self):
        return self.__sim_cards_list
    
    @sim_cards_list.setter
    def sim_cards_list(self, sim_cards: list):
        if type(sim_cards) == list:
            self.__sim_cards_list = sim_cards
        else:
            raise TypeError("Wrong type for sim_cards, need list")
    
    def call_to_number(self, sim_card_number, call_to_number):
        if self.__sim_cards_list[sim_card_number - 1]:
            print(f"Call to number: {call_to_number}")
        else:
            print("Dont find sim card")
     
    def __str__(self):
        return f"sim cards: {self.__sim_cards_list}"
    
            
class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list: list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)
    
    def use_gps(self, location):
        print(f"gps get location: {location}")
    
    def __str__(self):
        return f"Cpu memory: {self.cpu}, memory: {self.memory}, sim cards: {self.sim_cards_list}"
    
smartPhone_one = SmartPhone(5000, 32, [887875236, 893225556])
smartPhone_two = SmartPhone(2000, 8, [799325876, 755897266])
computer = Computer(20000, 256)
phone = Phone([899256237, 765922387])

Technic_list = [smartPhone_one, smartPhone_two, computer, phone]
for Technic in Technic_list:
    print(Technic)
    
print(computer > smartPhone_one)
print(computer < smartPhone_two)
phone.call_to_number(1, "888 895 238")
smartPhone_one.use_gps("location alien")
print(computer.Make_Computations())