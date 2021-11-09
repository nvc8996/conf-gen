import os
import re

VAR_PATTERN = '\$\{\w+;[a-zA-Z]+;[\w ]+\}\$'
TEMP_DIR = "./templates"
OUT_DIR = "./configs"

def place(data, line):
    vars = re.findall(VAR_PATTERN, line)
    for var in vars:
        value = data[Variable(var).name].value
        if value == "":
            raise Exception("Not all fields are filled!!!")
        line = line.replace(var, value)
    return line

class Variable:
    def __init__(self, inp):
        inp = inp[2:-2]
        self.name, self.type, self.desc = [s.strip() for s in inp.split(';')]
        self.name = self.name.upper()
        self.type = self.type.upper()

    def __str__(self):
        return self.name + ' - ' + self.type
    
    def __eq__(self, o: object) -> bool:
        return self.name == o.name and self.type == o.type and self.desc == o.desc

    def __ne__(self, o: object) -> bool:
        return self.name != o.name or self.type != o.type or self.desc != o.desc
    
    def __hash__(self) -> int:
        return hash(self.name+self.type+self.desc)

class LoopPart:
    def __init__(self, lines, pos, name):
        self.name = name
        self.structure = []
        self.vars = []
        self.loops = []
        self.loop_count = 0
        self.end_pos = pos
        self.get_vars(lines, pos)
    
    def get_end_pos(self):
        return self.end_pos
    
    def get_vars(self, lines, pos):
        i = pos
        while i < len(lines):
            line = lines[i]

            if line.strip() == 'BEGIN_LOOP':
                self.loop_count += 1
                self.structure.append(LoopPart(lines, i + 1, f'{self.name}-{self.loop_count}'))
                self.loops.append(self.structure[-1])
                i = self.loops[-1].get_end_pos() + 1
                continue

            if line.strip() == 'END_LOOP':
                self.end_pos = i
                return

            self.structure.append(line)
            for x in re.findall(VAR_PATTERN, line):
                tmp = Variable(x)
                if tmp not in self.vars:
                    self.vars.append(tmp)
            i += 1

    def generate_one(self, data):
        result = []
        for line in self.structure:
            if type(line) is str:
                result.append(place(data, line))
            else:
                result += line.generate(data[line.name])
        return result
    
    def generate(self, dataset):
        result = []
        for data in dataset:
            result += self.generate_one(data)
        return result

class TemplateEngine:
    def __init__(self, controller, filename, temp_dir=TEMP_DIR):
        self.controller = controller
        self.name = filename[:-4]
        self.temp_dir = temp_dir
        self.vars = []
        self.lines = []
        self.structure = []
        self.loops = []
        self.loop_count = 0
        self.data = {}
        self.result = []
        self.enabled = True

        self.load(filename)
        self.get_vars()

    def load(self, filename):
        if not os.path.exists(self.temp_dir):
            return
        
        with open(os.path.join(self.temp_dir, filename), 'r') as f:
            self.lines = f.readlines()

    def set_enabled(self):
        try:
            self.enabled = self.checkBox.isChecked()
        except:
            self.enabled = True
        
        self.controller.render_inputs()
        
    def get_vars(self):
        i = 0
        while i < len(self.lines):
            line = self.lines[i]
            if line.strip() == 'BEGIN_LOOP':
                self.loop_count += 1
                self.structure.append(LoopPart(self.lines, i + 1, f'{self.name}-{self.loop_count}'))
                self.loops.append(self.structure[-1])
                i = self.loops[-1].get_end_pos() + 1
                continue

            self.structure.append(line)
            for x in re.findall(VAR_PATTERN, line):
                tmp = Variable(x)
                if tmp not in self.vars:
                    self.vars.append(tmp)
            i += 1
    
    def generate(self):
        if not self.enabled:
            return

        data = self.controller.data
        self.result = []
        for line in self.structure:
            if type(line) is str:
                self.result.append(place(data, line))
            else:
                self.result += line.generate(self.data[line.name])
    
    def export(self, out_dir=OUT_DIR):
        if not self.enabled:
            return
        
        self.generate()

        # Create output directory if does not exist
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        
        # Open and write data to file
        with open(os.path.join(out_dir, self.name), 'w') as f:
            f.writelines(self.result)