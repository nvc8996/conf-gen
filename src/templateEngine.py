import os
import re

VAR_PATTERN = '\$\{\w+;[a-zA-Z_]+;[\w ]+\}\$'
TEMP_DIR = "./templates"
OUT_DIR = "./configs"

# Function to place user's input data into template's line
def place(template_data, data, line):
    # Get all variables in line
    vars = re.findall(VAR_PATTERN, line)

    # Go through all variables
    for var_str in vars:
        # Get value of input data
        var = Variable(var_str)
        value = ""
        if var.name in data.keys():
            value = data[var.name].value
        elif var.name in template_data.keys():
            value = template_data[var.name].value

        # Raise exception if no value
        if value == "":
            raise Exception("Not all fields are filled!!!")

        # Place value into line
        line = line.replace(var_str, value)

    return line

# Class to handle variable - name, type and description
class Variable:
    # Init variable from string
    def __init__(self, inp):
        # Exclude boudaries '${' and '}$'
        inp = inp[2:-2]

        # Extract information
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

# Class for handling Loop part in template
class LoopPart:
    # Continuously init loop from template's lines from starting line with index 'pos' and loop's name 'name'
    def __init__(self, lines, pos, name, template_vars):
        # Init variables
        self.name = name
        self.structure = []
        self.vars = []
        self.loops = []
        self.loop_count = 0
        self.end_pos = pos

        # Load loop part
        self.get_vars(lines, pos, template_vars)
    
    def get_end_pos(self):
        return self.end_pos
    
    # Load loop's content: variables, sub-loops 
    def get_vars(self, lines, pos, template_vars):
        i = pos
        while i < len(lines):
            line = lines[i]

            # Handle sub-loop
            if line.strip() == 'BEGIN_LOOP':
                self.loop_count += 1

                # Load sub-loop and add to loop's structure
                self.structure.append(LoopPart(lines, i + 1, f'{self.name}-{self.loop_count}', template_vars))
                self.loops.append(self.structure[-1])
                i = self.loops[-1].get_end_pos() + 1
                continue
            
            # Finish loading loop's content
            if line.strip() == 'END_LOOP':
                self.end_pos = i
                return

            # Read loop's lines and extract required variables
            self.structure.append(line)
            for x in re.findall(VAR_PATTERN, line):
                tmp = Variable(x)

                if tmp in template_vars:
                    continue

                # Add only new variables
                if tmp not in self.vars:
                    self.vars.append(tmp)
            i += 1

    # Generate one sample of the loop
    def generate_one(self, data, template_data):
        result = []
        for line in self.structure:
            if type(line) is str:
                result.append(place(template_data, data, line))
            else:
                result += line.generate(data[line.name])
        return result
    
    # Generate loop based on input dataset
    def generate(self, dataset, template_data):
        result = []
        for data in dataset:
            result += self.generate_one(data, template_data)
        return result

# Class for template handling
class TemplateEngine:
    # Init template
    def __init__(self, controller, filename, temp_dir=TEMP_DIR):
        # Init variables
        self.controller = controller

        # Remove '.txt' from template to get configuration file's name
        self.name = filename[:-4]
        self.vars = []
        self.lines = []
        self.structure = []
        self.loops = []
        self.loop_count = 0
        self.data = {}
        self.result = []
        self.enabled = True

        # Load template's lines
        self.load(filename, temp_dir)

        # Load template's structure
        self.get_vars()

    # Load template's lines from file with given filename
    def load(self, filename, temp_dir):
        if not os.path.exists(temp_dir):
            return
        
        with open(os.path.join(temp_dir, filename), 'r') as f:
            self.lines = f.readlines()

    # Function for setting template selection status
    def set_enabled(self):
        # Set to value from checkbox
        try:
            self.enabled = self.checkBox.isChecked()
        except:
            self.enabled = True

        # Re-render inputs after updating
        self.controller.render_inputs()
    
    # Process all lines to build template's structure
    def get_vars(self):
        i = 0
        while i < len(self.lines):
            line = self.lines[i]

            # Handle loop
            if line.strip() == 'BEGIN_LOOP':
                self.loop_count += 1
                
                # Load loop and add to template's structure
                self.structure.append(LoopPart(self.lines, i + 1, f'{self.name}-{self.loop_count}', self.vars))
                self.loops.append(self.structure[-1])
                i = self.loops[-1].get_end_pos() + 1
                continue

            # Add line to structure
            self.structure.append(line)

            # Extract variables from line
            for x in re.findall(VAR_PATTERN, line):
                tmp = Variable(x)

                # Add only new variable
                if tmp not in self.vars:
                    self.vars.append(tmp)
            i += 1
    
    # Conduct result from user's input
    def generate(self):
        # Quit if template is not selected
        if not self.enabled:
            return

        # Get input data from controller (basic variables only)
        data = self.controller.data

        # Init result
        self.result = []

        # Go through all lines in structure
        for line in self.structure:
            # place data if is normal line
            if type(line) is str:
                self.result.append(place(data, data, line))

            # Generate loop samples if is loop part
            else:
                self.result += line.generate(self.data[line.name], data)
    
    # Generate configuration file
    def export(self, out_dir=OUT_DIR):
        # Quit if template is not selected
        if not self.enabled:
            return
        
        # Conduct result
        self.generate()

        # Create output directory if does not exist
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        
        # Open and write data to file
        with open(os.path.join(out_dir, self.name), 'w') as f:
            f.writelines(self.result)