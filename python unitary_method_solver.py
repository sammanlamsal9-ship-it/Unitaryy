def solve_percentage_done(days_a, days_b, days_worked):
    """Solves Question 1: % of work done after X days."""
    rate_a = 1 / days_a
    rate_b = 1 / days_b
    total_rate = rate_a + rate_b
    work_done = total_rate * days_worked
    return work_done * 100

def solve_fractional_work(fraction_a, time_a, fraction_b, time_b):
    """Solves Question 2: Working together when given fractional work info."""
    # If A does 5/6 work in 10 days, full work takes 10 / (5/6)
    full_time_a = time_a / fraction_a
    full_time_b = time_b / fraction_b
    
    combined_rate = (1 / full_time_a) + (1 / full_time_b)
    days_to_finish = 1 / combined_rate
    return days_to_finish

def solve_pipe_difference(diff, total_time):
    """Solves Question 3: Find time when one is X hours faster than other."""
    # This solves the quadratic: 1/x + 1/(x+diff) = 1/total_time
    # For Question 3: diff=5, total_time=6. Let B = x. A = x-5.
    # Resulting equation: x^2 - (2*total + diff)x + (total*diff) = 0
    import math
    a = 1
    b = -(2 * total_time + diff)
    c = total_time * diff
    
    # Quadratic formula: x = [-b + sqrt(b^2 - 4ac)] / 2a
    discriminant = b**2 - 4*a*c
    x = (-b + math.sqrt(discriminant)) / (2*a)
    return x

# --- Examples based on IMG_20260513_181138.jpg ---

print(f"Q1 Answer: {solve_percentage_done(20, 25, 3):.2f}%")
print(f"Q2 Answer: {solve_fractional_work(5/6, 10, 5/12, 10):.2f} days")
print(f"Q3 Answer (Pipe B): {solve_pipe_difference(5, 6):.2f} hours")
