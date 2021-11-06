import os
import re

VAR_PATTERN = '\$\{\w+\}\$'
TEMP_DIR = "./templates/"
OUT_DIR = "./configs"

def place(data, line):
    vars = re.findall(VAR_PATTERN, line)
    for var in vars:
        line = line.replace(var, data[var[2:-2].upper()])
    return line

class LoopPart:
    def __init__(self, lines):
        self.lines = lines
        self.vars = set()
        self.get_vars()
        self.params = []

    def add_params(self, data):
        self.params.append(data)
    
    def get_vars(self):
        for line in self.lines:
            self.vars |= set([x[2:-2].upper() for x in re.findall(VAR_PATTERN, line)])

    def generate_one(self, data):
        return [place(data, line) for line in self.lines]

    def export(self):
        result = []
        for data in self.params:
            result += self.generate_one(data)
        return result

class TemplateEngine:
    def __init__(self, filename, temp_dir=TEMP_DIR):
        self.name = filename[:-4]
        self.temp_dir = temp_dir
        self.vars = set()
        self.loops = []
        self.lines = []
        self.structure = []
        self.result = []

        self.load(filename)
        self.get_vars()

    def load(self, filename):
        with open(os.path.join(self.temp_dir, filename), 'r') as f:
            self.lines = f.readlines()
    
    def get_vars(self):
        in_loop = False
        loop_content = []
        for line in self.lines:
            if line.strip() == 'BEGIN_LOOP':
                in_loop = True
                loop_content = []
            
            if line.strip() == 'END_LOOP':
                in_loop = False
                self.structure.append(LoopPart(loop_content))
                loop_content = []

            if in_loop:
                loop_content.append(line)
            else:
                self.structure.append(line)
                self.vars |= set([x[2:-2].upper() for x in re.findall(VAR_PATTERN, line)])
    
    def generate(self, data):
        self.result = []
        for line in self.structure:
            if type(line) is str:
                self.result.append(place(data, line))
            else:
                self.result += line.export()
    
    def export(self, data, out_dir=OUT_DIR):
        # Create output directory if does not exist
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        
        # Open and write data to file
        with open(os.path.join(out_dir, self.name), 'w') as f:
            f.writelines(self.result)

if __name__ == '__main__':
    fname = 'qlkt.sh.txt'
    e = TemplateEngine(fname)
    data = {'CON_X' : 'NVC', 'MY_NTP' : '202111061200'}
    print(e.name, e.vars)
    e.export(data)