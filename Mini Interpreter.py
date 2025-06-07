class Interpreter:
    def __init__(self):
        self.variables = {}

    def eval(self, expr):
        """Evaluate an expression."""
        if isinstance(expr, int):
            return expr
        elif isinstance(expr, str):
            return self.variables.get(expr, 0)
        elif isinstance(expr, list):
            op = expr[0]
            if op == 'add':
                return self.eval(expr[1]) + self.eval(expr[2])
            elif op == 'sub':
                return self.eval(expr[1]) - self.eval(expr[2])
            elif op == 'mul':
                return self.eval(expr[1]) * self.eval(expr[2])
            elif op == 'div':
                return self.eval(expr[1]) // self.eval(expr[2])
            elif op == 'eq':
                return self.eval(expr[1]) == self.eval(expr[2])
            elif op == 'lt':
                return self.eval(expr[1]) < self.eval(expr[2])
            elif op == 'lte':
                return self.eval(expr[1]) <= self.eval(expr[2])
            elif op == 'gte':
                return self.eval(expr[1]) >= self.eval(expr[2])
            elif op == 'neq':
                return self.eval(expr[1]) != self.eval(expr[2])
            elif op == 'print':
                value = self.eval(expr[1])
                print(value)
                return value
            elif op == 'let':
                var_name = expr[1]
                value = self.eval(expr[2])
                self.variables[var_name] = value
                return value
            elif op == 'if':
                condition = self.eval(expr[1])
                if condition:
                    return self.eval(expr[2])
                elif len(expr) > 3:
                    return self.eval(expr[3])
                return None

    def run(self, program):
        """Run a list of statements."""
        for statement in program:
            self.eval(statement)

# Example usage
program = [
    ['let', 'x', 10],
    ['let', 'y', 20],
    ['let', 'z', ['add', 'x', 'y']],
    ['if', ['eq', 'z', 30], ['print', 'z'], ['print', 'z']]
]

interpreter = Interpreter()
interpreter.run(program)
