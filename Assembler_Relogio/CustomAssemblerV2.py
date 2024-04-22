# Custom Assembly Assembler
commands = []
comments = []
labels = {}
symbols = {}
mnemonics = { 
    "NOP":   "00000",
    "LDA":   "00001",
    "SOMA":  "00010",
    "SUB":   "00011",
    "LDI":   "00100",
    "STA":   "00101",
    "JMP":   "00110",
    "JEQ":   "00111",
    "CMP":   "01000",
    "JSR":   "01001",
    "RET":   "01010",
    "AND":   "01011",
    "JNE":   "01100",
    "CMPI":  "01101",
    "ADDI":  "01110",
    "ANDI":  "01111",
    "JGT":   "10000",
    "JLT":   "10001",
    "SUBI":  "10010",
    "NOT":   "10011",
}

jmps = ["JMP", "JEQ", "JNE", "JGT", "JLT", "JSR"]

def extract_value(value):
    """ Extrai o número inteiro após '@' se presente, ou retorna o valor como inteiro. """
    if value.startswith('@'):
        value = value[1:]
    return int(value)

def process_asm_file():
    """ Processa o arquivo ASM e armazena comandos, símbolos e rótulos. """
    with open("ASM.txt", "r") as file:
        for line in file.readlines():
            cleaned_line = line.strip()
            if not cleaned_line:
                continue  # Ignora linhas vazias

            command, *comment = cleaned_line.split('#')
            comment = "#" + comment[0].strip() if comment else ""
            
            if command.startswith('!'):
                symbol, value = command[1:].split()
                symbols[symbol.strip()] = extract_value(value.strip())
                continue
            elif command.startswith(':'):
                label = command[1:].strip()
                labels[label] = len(commands)  # Armazena a posição do rótulo para uso em desvios
                continue

            commands.append((command.strip(), comment))

def format_rom_output():
    """ Formata e escreve os comandos processados no arquivo ROM. """
    with open("ROM.txt", "w") as file:
        for i, (command, comment) in enumerate(commands):
            parts = command.split(',')
            first_part = parts[0].split()
            op = first_part[0]
            opcode = mnemonics[op]
            if op == "NOP" or op == "RET":
                line = f'tmp({i}) := "{opcode}" & "00000000000"; -- {command} {comment}\n'
            elif op in jmps:
                arg = first_part[1]
                if arg.startswith("@"):
                    if arg[1:] in labels:
                        arg = labels.get(arg[1:], 0)  # Usa a posição do rótulo
                    else:
                        arg = int(arg[1:])
                arg = bin(arg)[2:].zfill(11)
                line = f'tmp({i}) := "{opcode}" & "{arg}"; -- {command} {comment}\n'
            elif len(parts) == 1:
                reg_address = bin(int(first_part[1][1:]))[2:].zfill(2)
                line = f'tmp({i}) := "{opcode}" & "{reg_address}" & "000000000"; -- {command} {comment}\n'
            else:
                reg_address = bin(int(first_part[1][1:]))[2:].zfill(2)
                arg = parts[1].strip()
                if arg.startswith("@") or arg.startswith("$"):
                    if arg[1:] in symbols:
                        arg = symbols.get(arg[1:], 0)
                    else:
                        arg = int(arg[1:])
                arg = bin(arg)[2:].zfill(9)
                line = f'tmp({i}) := "{opcode}" & "{reg_address}" & "{arg}"; -- {command} {comment}\n'
            
            file.write(line)

# Executa as funções de processamento e formatação
process_asm_file()
format_rom_output()

# mif ainda não está implementado