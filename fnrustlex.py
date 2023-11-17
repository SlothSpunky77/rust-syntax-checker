import ply.lex as lex

tokens=(
    'IDENTIFIER',
    'FN',
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'FLOWEROPEN',
    'FLOWERCLOSE',
    'COLON',
    'SEMICOLON',
    'ARROW',
    'INT',
    'CHAR',
    'COMMA',

)


def t_INT(t):
    r'i32'
    return t

def t_CHAR(t):
    r'char'
    return t

def t_FN(t):
    r'fn'
    return t
def t_ARROW(t):
    r'->'
    return t

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_IDENTIFIER=r'[a-zA-Z]\w*'
t_NUMBER=r'[0-9]\w*'
t_FLOWEROPEN=r'\{'
t_FLOWERCLOSE=r'\}'
t_COMMA=r'\,'
t_ignore=' \t\n'

def t_error(t):
    print(f"illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer=lex.lex()

