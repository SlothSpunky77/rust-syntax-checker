import ply.lex as lex

tokens=(
    'IDENTIFIER',
    'WHILE',
    'LPAREN',
    'RPAREN',
    'GREATER',
    'LESSER',
    'TRUE',
    'FLOWEROPEN',
    'FLOWERCLOSE',
    
  

)




def t_WHILE(t):
    r'while'
    return t

def t_TRUE(t):
    r'true'
    return t
def t_GREATER(t):
    r'>'
    return t
def t_LESSER(t):
    r'<'
    return t

t_LPAREN = r'\('
t_RPAREN = r'\)'

# t_SEMICOLON = r'\;'
t_IDENTIFIER=r'[a-zA-Z]\w*'
# t_NUMBER=r'[0-9]\w*'
t_FLOWEROPEN=r'\{'
t_FLOWERCLOSE=r'\}'

t_ignore=' \t\n'

def t_error(t):
    print(f"illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer=lex.lex()