from collections import deque

def is_in_array(arr, value):
    """Check if a value is in an array"""
    return value in arr

def print_table_header(page_count):
    """Print table header"""
    print("\n" + "+------+" + "-------+" * page_count + "--------+")
    print("| Time |", end="")
    for i in range(page_count):
        print(f" Frame {i+1} |", end="")
    print(" Page  |")
    
    print("|      |", end="")
    for i in range(page_count):
        print("       |", end="")
    print(" Fault |")
    
    print("+------+" + "-------+" * page_count + "--------+")

def print_table_row(time, total_page, page_count, row, page_fault):
    """Print one row of the table"""
    print(f"| {time:4d} |", end="")
    
    for j in range(page_count):
        if total_page[j][row] == -1:
            print(f" {'-':6} |", end="")
        else:
            print(f" {total_page[j][row]:6d} |", end="")
    
    if page_fault == 1:
        print(f" {'Yes':5}  |", end="")
    else:
        print(f" {'No':5}  |", end="")
    print()

def main():
    print("========================================")
    print("        FIFO PAGE REPLACEMENT ALGORITHM")
    print("========================================\n")
    
    # Input number of page frames
    while True:
        try:
            page_count = int(input("Enter number of page frames (max 10): "))
            if 1 <= page_count <= 10:
                break
            else:
                print("Please enter a number from 1 to 10!")
        except ValueError:
            print("Please enter an integer!")
    
    # Input number of references
    while True:
        try:
            n = int(input("Enter number of references (max 20): "))
            if 1 <= n <= 20:
                break
            else:
                print("Please enter a number from 1 to 20!")
        except ValueError:
            print("Please enter an integer!")
    
    # Input reference sequence
    ref = []
    print(f"Enter reference sequence ({n} numbers, separated by space): ", end="")
    
    while True:
        try:
            ref_input = input().split()
            if len(ref_input) == n:
                ref = [int(x) for x in ref_input]
                break
            else:
                print(f"Please enter exactly {n} numbers! Enter again: ", end="")
        except ValueError:
            print("Please enter integers only! Enter again: ", end="")
    
    # Initialize arrays
    pre_array = [-1] * page_count  # -1 represents empty frame
    page_fault = [0] * n
    total_page = [[-1 for _ in range(n)] for _ in range(page_count)]
    
    number_page_fault = 0
    current_page = 0
    
    print("\n========================================")
    print("           EXECUTION PROCESS")
    print("========================================")
    
    # Main loop processing each reference
    for i in range(n):
        print(f"\n--- Time {i+1}: Reference to page {ref[i]} ---")
        
        # Check if page is already in memory
        if is_in_array(pre_array, ref[i]):
            # Page is already in memory
            page_fault[i] = 0
            print(f"Page {ref[i]} is already in memory. No page fault.")
        else:
            # Page is not in memory - page fault occurs
            number_page_fault += 1
            page_fault[i] = 1
            
            print(f"Page fault! Page {ref[i]} is not in memory.")
            
            # Check if memory is full
            if current_page == page_count:
                current_page = 0  # Return to beginning (FIFO)
                print(f"Memory is full. Replace page at frame {current_page + 1}.")
            else:
                print(f"Empty frame available. Add to frame {current_page + 1}.")
            
            # Add new page to memory
            pre_array[current_page] = ref[i]
            
            # Increment current_page for next time
            current_page = (current_page + 1) % page_count
        
        # Update status table
        if i == 0:
            # First time point
            for j in range(page_count):
                total_page[j][i] = pre_array[j]
        else:
            # Copy from previous state
            for j in range(page_count):
                total_page[j][i] = total_page[j][i-1]
            
            # Update with latest state
            for j in range(page_count):
                if pre_array[j] != -1:
                    total_page[j][i] = pre_array[j]
        
        # Print current state
        print("Current memory state: ", end="")
        for j in range(page_count):
            if pre_array[j] == -1:
                print("[ ] ", end="")
            else:
                print(f"[{pre_array[j]}] ", end="")
        print()
    
    # Print detailed result table
    print("\n========================================")
    print("           DETAILED RESULT TABLE")
    print("========================================")
    
    print_table_header(page_count)
    
    for i in range(n):
        print_table_row(i + 1, total_page, page_count, i, page_fault[i])
        
        if i < n - 1:
            print("+------+" + "-------+" * page_count + "--------+")
    
    print("+------+" + "-------+" * page_count + "--------+")
    
    # Summary results
    print("\n========================================")
    print("              SUMMARY RESULTS")
    print("========================================")
    
    # Print reference sequence
    print("Reference sequence:", " ".join(map(str, ref)))
    
    # Print positions where page faults occurred
    fault_positions = [str(i+1) for i in range(n) if page_fault[i] == 1]
    if fault_positions:
        print("Page fault positions:", ", ".join(fault_positions))
    else:
        print("Page fault positions: None")
    
    # Print total number of page faults
    print(f"Total number of page faults: {number_page_fault}")
    
    # Calculate page fault rate
    fault_rate = (number_page_fault / n) * 100
    print(f"Page fault rate: {fault_rate:.2f}%")
    
    # Display explanation
    print("\n========================================")
    print("                 NOTES")
    print("========================================")
    print("1. '-' indicates empty frame")
    print("2. 'Yes' in Page Fault column: page fault occurred")
    print("3. 'No' in Page Fault column: no page fault")
    print("4. FIFO: First page in is first page out")
    print("5. Memory state is updated after each reference")

def visualize_fifo_example():
    """Function to demonstrate a specific example"""
    print("\n" + "="*60)
    print("EXAMPLE DEMONSTRATION: FIFO PAGE REPLACEMENT ALGORITHM")
    print("="*60)
    
    # Example data
    page_count = 3
    ref = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3]
    n = len(ref)
    
    print(f"Number of frames: {page_count}")
    print(f"Reference sequence: {ref}")
    print(f"Number of references: {n}")
    print()
    
    # Initialize
    frames = [-1] * page_count
    page_faults = 0
    queue = []  # Queue to track entry order
    
    print("Step | Reference |  Memory Frames | Page Fault | Note")
    print("-" * 60)
    
    for i, page in enumerate(ref):
        fault = False
        note = ""
        
        if page not in frames:
            page_faults += 1
            fault = True
            
            if -1 in frames:
                # Empty frame available
                empty_idx = frames.index(-1)
                frames[empty_idx] = page
                queue.append(page)
                note = f"Add to frame {empty_idx + 1}"
            else:
                # Replace page
                oldest = queue.pop(0)
                idx = frames.index(oldest)
                frames[idx] = page
                queue.append(page)
                note = f"Replace page {oldest} at frame {idx + 1}"
        
        # Display result
        frames_display = " ".join([f"[{f}]" if f != -1 else "[ ]" for f in frames])
        fault_display = "Yes" if fault else "No"
        print(f"{i+1:4d} | {page:9d} | {frames_display:13s} | {fault_display:9s} | {note}")
    
    print("-" * 60)
    print(f"Total number of page faults: {page_faults}")
    print(f"Page fault rate: {(page_faults/n)*100:.2f}%")

if __name__ == "__main__":
    print("Select mode:")
    print("1. Run with keyboard input data")
    print("2. View example demonstration")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        main()
    elif choice == "2":
        visualize_fifo_example()
    else:
        print("Exit program")
