import re


class GPTLangInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def parse(self, code):
        lines = code.strip().split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Handle variable assignment
            if line.startswith('VAR'):
                self.assign_variable(line)
            # Handle function definition
            elif line.startswith('DEF'):
                self.define_function(line)
            # Handle function calls
            else:
                self.call_function(line)

    def assign_variable(self, line):
        _, name_and_type, _, value = line.split(' ', 3)
        name, _ = name_and_type.split(':')
        self.variables[name] = self.evaluate_expression(value)

    def parse_line(self, line):
        if line.startswith("FUNC "):
            self.parse_function_definition(line)
        elif line.startswith("VAR "):
            self.parse_variable_declaration(line)
        else:
            self.parse_expression(line)

    def parse_function_definition(self, line):
        function_name = re.search(r"def (\w+)", line).group(1)
        arg_list = re.search(r"\((.*?)\)", line).group(1).split(",")
        arg_list = [arg.strip() for arg in arg_list]
        function_body = re.search(r"\{(.*?)\}", line, re.DOTALL).group(1)
        self.functions[function_name] = {"args": arg_list, "body": function_body}

    def parse_variable_declaration(self, line):
        name, value = line[4:].split("=")
        name = name.strip()
        value = value.strip()
        self.variables[name] = self.evaluate_expression(value)

    def parse_expression(self, line):
        return self.evaluate_expression(line)

    def evaluate_expression(self, expression):
        expression = expression.strip()
        if re.match(r'^\d+$', expression):
            return int(expression)
        elif expression in self.variables:
            return self.variables[expression]
        elif '+' in expression:
            left, right = expression.split('+')
            left_value = self.evaluate_expression(left.strip())
            right_value = self.evaluate_expression(right.strip())
            return left_value + right_value
        else:
            raise Exception(f"Invalid expression: {expression}")

    def call_function(self, function_name, args):
        function = self.functions[function_name]
        if function is None:
            raise Exception(f"Function {function_name} not found.")

        # Save the current state of variables
        original_variables = self.variables.copy()

        # Set up the function's local variables
        for i, arg in enumerate(function["args"]):
            self.variables[arg] = self.evaluate_expression(args[i])

        # Execute the function's body
        result = self.parse(function["body"])

        # Restore the original state of variables
        self.variables = original_variables

        return result


# Example usage:
interpreter = GPTLangInterpreter()
code = """
    VAR x:int = 10
    VAR y:int = 20
    VAR z:int = x + y
"""
interpreter.parse(code)
print(interpreter.variables)  # Output: {'x': 10, 'y': 20, 'z': 30}
