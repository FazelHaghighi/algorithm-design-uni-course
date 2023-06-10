class BacktrackingSolver:
    def __init__(self, lst, number):
        self.lst = lst
        self.number = number
        self.result = []

    def solve(self):
        self.backtrack_helper(self.lst, self.number, [])
        return self.result

    def backtrack_helper(self, remaining_list, target_sum, current_combination):
        if target_sum == 0:
            self.result.append(current_combination)
            return
        elif target_sum < 0:
            return
        else:
            for i, num in enumerate(remaining_list):
                self.backtrack_helper(remaining_list[i:], target_sum - num, current_combination + [num])


class BranchAndBoundSolver:
    def __init__(self, lst, number):
        self.lst = lst
        self.number = number
        self.result = []

    def solve(self):
        self.branch_and_bound_helper(self.lst, self.number, [])
        return self.result

    def branch_and_bound_helper(self, remaining_list, target_sum, current_combination):
        if target_sum == 0:
            self.result.append(current_combination)
            return
        elif target_sum < 0:
            return
        elif len(remaining_list) == 0 or target_sum < min(remaining_list):
            return
        else:
            for i, num in enumerate(remaining_list):
                self.branch_and_bound_helper(remaining_list[i + 1:], target_sum - num, current_combination + [num])


def print_combinations(approach_name, combinations):
    index_color = "\033[92m"  # Bright green color for the index
    number_color = "\033[94m"  # Bright blue color for the numbers
    approach_color = "\033[93m"  # Yellow color for the approach name
    reset_color = "\033[0m"  # Reset color to default

    print(f"{approach_color}{approach_name}{reset_color}:")
    for i, combination in enumerate(combinations, start=1):
        colored_combination = ', '.join(f"{number_color}{num}{reset_color}" for num in combination)
        print(f"{index_color}{i}:{reset_color} {colored_combination}")


# Using BacktrackingSolver
backtracking_solver = BacktrackingSolver([3, 5, 6, 10], 15)
backtracking_result = backtracking_solver.solve()
print_combinations("Backtracking", backtracking_result)

# Using BranchAndBoundSolver
branch_and_bound_solver = BranchAndBoundSolver([3, 5, 6, 10], 15)
branch_and_bound_result = branch_and_bound_solver.solve()
print_combinations("Branch and Bound", branch_and_bound_result)
