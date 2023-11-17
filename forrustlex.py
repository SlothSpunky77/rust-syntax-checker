
import ply.lex as lex

tokens=(
    'FOR',
    'IN',
    'DOT',
    'NUMBER',
    'IDENTIFIER',
    'FLOWEROPEN',
    'FLOWERCLOSE',
   
    
)
def t_IN(t):
    r'in'
    return t



def t_FOR(t):
    r'for'
    return t


t_IDENTIFIER=r'[a-zA-Z]\w*'
t_NUMBER=r'[0-9]\w*'
t_DOT=r'\.\.'
t_FLOWEROPEN=r'\{'
t_FLOWERCLOSE=r'\}'


t_ignore=' \t\n'

def t_error(t):
    print(f"illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer=lex.lex()

