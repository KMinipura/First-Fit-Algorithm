# Simulation of First Fit Algorithm in Dynamic Memory Allocation
#kalana

class MemoryBlock:
    def __init__(self, size):
        self.size = size
        self.is_free = True

class FirstFitMemory:
    def __init__(self, total_memory):
        self.blocks = [MemoryBlock(total_memory)]  # Initialize memory with a single large block

    def allocate(self, request_size):
        """Allocate memory using the First Fit algorithm."""
        for block in self.blocks:
            if block.is_free and block.size >= request_size:
                if block.size > request_size:
                    # Split the block
                    remaining_size = block.size - request_size
                    self.blocks.insert(self.blocks.index(block) + 1, MemoryBlock(remaining_size))
                block.size = request_size
                block.is_free = False
                print(f"Allocated {request_size} units.")
                return True
        print("Allocation failed: No suitable block found.")
        return False

    def deallocate(self, request_size):
        """Deallocate memory of a specific size."""
        for block in self.blocks:
            if not block.is_free and block.size == request_size:
                block.is_free = True
                print(f"Deallocated {request_size} units.")
                self.merge_free_blocks()
                return True
        print("Deallocation failed: Block not found.")
        return False

    def merge_free_blocks(self):
        """Merge adjacent free blocks to reduce fragmentation."""
        i = 0
        while i < len(self.blocks) - 1:
            if self.blocks[i].is_free and self.blocks[i + 1].is_free:
                self.blocks[i].size += self.blocks[i + 1].size
                del self.blocks[i + 1]
            else:
                i += 1

    def display_memory(self):
        """Display the current state of memory blocks."""
        print("Memory Blocks:")
        for i, block in enumerate(self.blocks):
            status = "Free" if block.is_free else "Allocated"
            print(f"Block {i + 1}: {block.size} units - {status}")

if __name__ == "__main__":
    total_memory = int(input("Enter the total memory size: "))
    memory = FirstFitMemory(total_memory)

    while True:
        print("\nOptions:")
        print("1. Allocate memory")
        print("2. Deallocate memory")
        print("3. Display memory")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            size = int(input("Enter the size to allocate: "))
            memory.allocate(size)
        elif choice == "2":
            size = int(input("Enter the size to deallocate: "))
            memory.deallocate(size)
        elif choice == "3":
            memory.display_memory()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
