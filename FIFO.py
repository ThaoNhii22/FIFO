from collections import deque

# CORE FUNCTIONS - ALGORITHM LOGIC
def fifo_page_replacement(pages, frame_size):
    """
    Simulates the FIFO (First-In, First-Out) page replacement algorithm
    
    Parameters:
    ----------
    pages : list
        List of page references
    frame_size : int
        Number of page frames in memory
        
    Returns:
    -------
    tuple: (total_page_faults, history_state, notes)
    """
    frames = deque()  # Queue to store pages in memory
    page_faults = 0
    history = []  # Store state history
    notes = []    # Store step notes
    
    for i, page in enumerate(pages):
        note = ""
        
        # Check for page fault
        if page not in frames:
            page_faults += 1
            
            # If memory is full, remove oldest page
            if len(frames) == frame_size:
                removed = frames.popleft()
                note = f"Replace page {removed}"
            else:
                note = "Add to empty frame"
            
            # Add new page to memory
            frames.append(page)
            fault = True
        else:
            note = "Page already in memory"
            fault = False
        
        # Save current state
        history.append(list(frames))
        notes.append((page, fault, note))
    
    return page_faults, history, notes

# DISPLAY FUNCTIONS
def display_step_by_step(pages, frame_size, history, notes):
    """Display each step of the algorithm execution"""
    print("\nStep | Page Ref | Memory State               | Page Fault | Note")
    print("-" * 80)
    
    for i in range(len(pages)):
        page, fault, note = notes[i]
        frames_state = history[i]
        
        # Display memory state
        display_frames = []
        for j in range(frame_size):
            if j < len(frames_state):
                display_frames.append(f"[{frames_state[j]}]")
            else:
                display_frames.append("[ ]")
        
        frames_str = " ".join(display_frames)
        fault_str = "YES" if fault else "NO"
        
        print(f"{i+1:4d} | {page:8d} | {frames_str:25s} | {fault_str:10s} | {note}")


def display_summary(pages, page_faults):
    """Display summary of results"""
    n = len(pages)
    fault_rate = (page_faults / n) * 100 if n > 0 else 0
    
    print("-" * 80)
    print(f"Total page faults: {page_faults}")
    print(f"Page fault rate: {fault_rate:.2f}%")
    
    print("\n" + "="*50)
    print("STATISTICS")
    print("="*50)
    print(f"- Total accesses: {n}")
    print(f"- Page faults: {page_faults}")
    print(f"- Successful accesses: {n - page_faults}")
    print(f"- Success rate: {100 - fault_rate:.2f}%")


def display_results(pages, frame_size, page_faults, history, notes):
    """Display detailed results"""
    n = len(pages)
    
    print("\n" + "="*80)
    print("FIFO PAGE REPLACEMENT ALGORITHM - RESULTS")
    print("="*80)
    
    print(f"Number of frames: {frame_size}")
    print(f"Reference string: {pages}")
    print(f"Number of references: {n}")
    
    # Display step by step
    display_step_by_step(pages, frame_size, history, notes)
    
    # Display summary
    display_summary(pages, page_faults)

# INPUT FUNCTIONS
def get_frame_size_from_user():
    """Get number of frames from user"""
    while True:
        try:
            frame_size = int(input("Enter number of frames (1-10): "))
            if 1 <= frame_size <= 10:
                return frame_size
            else:
                print("Please enter a number between 1 and 10!")
        except ValueError:
            print("Please enter a valid number!")


def get_pages_from_user():
    """Get reference string from user"""
    print("\nEnter page reference string (numbers separated by spaces):")
    print("Example: 7 0 1 2 0 3 0 4 2 3 0 3")
    
    while True:
        try:
            input_str = input("Reference string: ")
            pages = [int(x) for x in input_str.split()]
            if len(pages) > 0:
                return pages
            else:
                print("String cannot be empty!")
        except ValueError:
            print("Please enter only numbers!")


def get_input_from_user():
    """Get all input data from user"""
    print("\n" + "="*60)
    print("USER INPUT")
    print("="*60)
    
    frame_size = get_frame_size_from_user()
    pages = get_pages_from_user()
    
    return pages, frame_size


# EXAMPLE AND EXPLANATION FUNCTIONS
def explain_fifo_algorithm():
    """Explain the FIFO algorithm"""
    print("\n" + "="*80)
    print("FIFO ALGORITHM EXPLANATION:")
    print("="*80)
    print("1. FIFO (First-In, First-Out): First page in is first page out")
    print("2. Uses a queue to track the order of pages in memory")
    print("3. When page replacement is needed:")
    print("   - Remove the page at the front of the queue (oldest)")
    print("   - Add new page to the back of the queue")
    print("4. Page fault occurs when requested page is not in memory")
    print("="*80)


def explain_example_results(pages, page_faults):
    """Explain example results"""
    print("\n" + "="*80)
    print("RESULTS EXPLANATION:")
    print("="*80)
    print(f"With reference string of {len(pages)} pages:")
    print(f"- {page_faults} page faults occurred")
    print(f"- Page fault rate is {(page_faults/len(pages))*100:.2f}%")
    print("\nThis means:")
    print(f"• {page_faults}/{len(pages)} accesses required loading from disk")
    print(f"• {len(pages)-page_faults}/{len(pages)} accesses found page in RAM")
    print(f"• Performance: {100-(page_faults/len(pages))*100:.2f}% fast accesses")


def run_example():
    """Run example demonstration"""
    print("\n" + "="*80)
    print("EXAMPLE DEMONSTRATION: FIFO PAGE REPLACEMENT ALGORITHM")
    print("="*80)
    
    # Example data
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3]
    frame_size = 3
    
    print(f"Number of frames: {frame_size}")
    print(f"Reference string: {pages}")
    print(f"Number of references: {len(pages)}")
    
    # Explain algorithm
    explain_fifo_algorithm()
    
    # Run simulation
    page_faults, history, notes = fifo_page_replacement(pages, frame_size)
    
    # Display results
    display_results(pages, frame_size, page_faults, history, notes)
    
    # Explain results
    explain_example_results(pages, page_faults)


# MAIN CONTROL FUNCTIONS
def run_simulation_from_input():
    """Run simulation with user input"""
    pages, frame_size = get_input_from_user()
    page_faults, history, notes = fifo_page_replacement(pages, frame_size)
    display_results(pages, frame_size, page_faults, history, notes)


def ask_to_continue():
    """Ask user if they want to continue"""
    cont = input("\nPress Enter to continue, or 'q' to quit: ")
    return cont.lower() != 'q'


def display_main_menu():
    """Display main menu"""
    print("\n" + "="*60)
    print("FIFO PAGE REPLACEMENT ALGORITHM SIMULATOR")
    print("="*60)
    print("1. Enter data from keyboard and run simulation")
    print("2. View example demonstration")
    print("3. Exit program")
    print("="*60)


def handle_menu_choice(choice):
    """Handle menu choice"""
    if choice == "1":
        run_simulation_from_input()
        return ask_to_continue()
    elif choice == "2":
        run_example()
        return ask_to_continue()
    elif choice == "3":
        print("Thank you for using the program!")
        return False
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
        return True


def main_menu():
    """Main program menu controller"""
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-3): ").strip()
        
        if not handle_menu_choice(choice):
            break

# ENTRY POINT
if __name__ == "__main__":
    main_menu()