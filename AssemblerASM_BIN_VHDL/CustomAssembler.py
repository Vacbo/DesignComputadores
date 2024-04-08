
#custom assembly assembler
comands = []
comments = []
labels = {}
symbols = {}
rom = []
mne =	{ 
       "NOP":   "0",
       "LDA":   "1",
       "SOMA":  "2",
       "SUB":   "3",
       "LDI":   "4",
       "STA":   "5",
       "JMP":   "6",
       "JEQ":   "7",
       "CEQ":   "8",
       "JSR":   "9",
       "RET":   "A",
       "AND":   "B",
}

#open ASM.txt file
with open("ContadorASM.txt") as f:
	for line in f.readlines():
		#strip and check if line is empty
		cmd = line.strip()
		#split comment from command
		cmd, *comment = cmd.split("#")
		comment = "" if not comment else "-- " + comment[0]
		if not cmd:
			continue #skip empty lines
		if cmd.startswith(":"):
			labels[cmd[1:]] = len(comands)
			continue
		elif cmd.startswith("!"):
			symbol, value = cmd[1:].split(" ")
			symbols[symbol] = int(value.strip())
			continue
		

		comands.append(cmd)
		comments.append(comment)
lines = []
with open("ROM.txt", "w") as f:
	for i in range(len(comands)):
		cmd = comands[i]
		comment = comments[i]
		op, *arg = cmd.split(" ")
		arg =  "" if not arg else arg[0]
		opcode = mne[op]
		if arg.startswith("!"):
			arg =  symbols[arg[1:]]
		elif arg.startswith("@"):
			arg = arg[1:]
			arg = labels.get(arg, arg)
		elif arg.startswith("$"):
			arg = arg[1:]
		arg = int(arg) if arg else 0
		op = int(opcode,16)
		binop = bin(arg).split("b")[1].zfill(9)
		hexlsb = hex(int(binop[1:], 2))[2:].upper().zfill(2)
		hexop = hex(op)[2:].upper().zfill(2)
		line = f"tmp({i}) := x\"{hexop}\" & '{binop[0]}' & x\"{hexlsb}\"; {comment}\n"
		lines.append(line)
		f.write(line)

	
	


with open("initROM.mif", "r") as f: #Abre o arquivo .mif
    headerMIF = f.readlines() #Faz a leitura das linhas do arquivo,

  
with open("CUSTOM.mif", "w") as f:  #Abre o destino .mif novamente
                                 #agora para preenchê-lo com o pograma

    cont = 0 #Cria uma variável para contagem
    
    #########################################
    #Preenche com o header lido anteriormente 
    for lineHeader in headerMIF:      
        if cont < 21:           #Contagem das linhas de cabeçalho
            f.write(lineHeader) #Escreve no arquivo se saída .mif o cabeçalho (21 linhas)
        cont = cont + 1         #Incrementa varíavel de contagem
   #-----------------------------------------
   ##########################################
  
    for line in lines: #Varre as linhas do código formatado para a ROM (VHDL)
    
        replacements = [('t', ''), ('m', ''), ('p', ''), ('(', ''), (')', ''), ('=', ''), ('x', ''), ('"', '')] #Define os caracteres que serão excluídos
        
        ##########################################
        #Remove os caracteres que foram definidos
        for char, replacement in replacements:
            if char in line:
                line = line.replace(char, replacement)
        #-----------------------------------------
        ##########################################
                
        line = line.split('#') #Remove o comentário da linha
        
        if "\n" in line[0]:
            line = line[0] 
        else:
            line = line[0] + '\n' #Insere a quebra de linha ('\n') caso não tenha

        f.write(line) #Escreve no arquivo initROM.mif
    f.write("END;") #Acrescente o indicador de finalização da memória. (END;)
