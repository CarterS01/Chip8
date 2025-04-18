class Chip8:

	def __init__(self):
		# Will later store opcodes
		self.__opcode = 0
		# Emulates 4K of memory
		memory[4096]
		# Set up the 16 registers (15 standard (V1-VE) and 1 carry flag (VF))
		V[16]
		# Set up index register and program counter
		I = 0
		PC = 0x200		# Starts at memory location 0x200
		# Set up delay and sound timers
		delayTimer = None
		soundTimer = None
		# Set up stack and stack pointer
		stack[16]
		SP = 0

		fontset = ['add fontset']

		# Initialize fontset into memory starting at address 0x50
		for i in range(len(fontset)):
			memory[i + 0x50] = fontset[i - 80]

	# Function to emulate the CHIP-8's cycle
	def cycle(self):
		# Get Opcode
		# Decode
		# Execute
		# Update timers
		pass