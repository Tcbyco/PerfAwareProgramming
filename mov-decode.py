'''
Decodes an intel 8086 binary register to register MOV instruction and outputs the assembly instruction

Structure of a binary instruction:
  Byte 1      Byte 2
|--------|  |---------|
000000 0 0  00  000 000
|----| | |  ||  |-| |-|
opcode d w  mod reg r/m

opcode: encodes the operation (eg MOV)
d: 0 -> reg is source, 1-> reg is destination
w: 0 -> using half the register, 1 -> using the full register width
mod: indicates whether an operand is in memory. in this case, it will always be '11' -> both operands are registers.
reg: register field. encodes one of 8 registers, which includes full and half widths. as such, it depends on the w bit.
r/m: register/memory. encodes the other location, which is either a register or memory.
'''

#Given a binary register encoding and the W field (aka fullWidth flag), print the register
def decodeReg(reg, fullWidth):
  match reg:
    case b'000':
      print('AX') if fullWidth else print('AL')
    case b'001':
      print('CX') if fullWidth else print('CL')
    case b'010':
      print('DX') if fullWidth else print('DL')
    case b'011':
      print('BX') if fullWidth else print('BL')
    case b'100':
      print('SP') if fullWidth else print('AH')        
    case b'101':
      print('BP') if fullWidth else print('CH')        
    case b'110':
      print('SI') if fullWidth else print('DH')        
    case b'111':
      print('DI') if fullWidth else print('BH')
    case _:
      print('unknown')

decodeReg(b'000')
decodeReg(b'111')