import itertools
import operator

# operators
ops = [
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
    ('/', operator.truediv)
]

# five modes of algebraic operations
def generate_expressions(nums, op_symbols):
    a, b, c, d = nums
    op1, op2, op3 = op_symbols
    patterns = [
        f"(({a}{op1}{b}){op2}{c}){op3}{d}",
        f"({a}{op1}({b}{op2}{c})){op3}{d}",
        f"{a}{op1}(({b}{op2}{c}){op3}{d})",
        f"{a}{op1}({b}{op2}({c}{op3}{d}))",
        f"({a}{op1}{b}){op2}({c}{op3}{d})"
    ]
    return patterns

def solve_24(nums):
    """iterating through all the possible ways to findout the solutions"""
    solutions = []
    for num_perm in itertools.permutations(nums):
        for ops_choice in itertools.product(ops, repeat=3):
            symbols = [op[0] for op in ops_choice]
            funcs   = [op[1] for op in ops_choice]
            # generating expressions
            exprs = generate_expressions(num_perm, symbols)
            for expr in exprs:
                try:
                    # eval calculat, throwing an error when 0 is divided
                    if abs(eval(expr) - 24) < 1e-6:
                        solutions.append(expr)
                except ZeroDivisionError:
                    continue
    return solutions

def main():
    nums = list(map(int, input("Enter four numbers in [1,13], seperating them with spaces: ").split()))
    if len(nums) != 4 or any(n < 1 or n > 13 for n in nums):
        print("Make sure that the four numbers are not exceeding the range")
    else:
        solutions = solve_24(nums)
        if solutions:
            print(f"Found {len(solutions)} solution(s):")
            for i, solution in enumerate(solutions, 1):
                print(f"Solution {i}: {solution} = 24")
        else:
            print("NO SOLUTION")
if __name__ == '__main__':
    main()