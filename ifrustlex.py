
import ply.lex as lex

tokens=(
    'IF',
    'GREATER',
    'LESSER',
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'ELSE',
    'IDENTIFIER',
    'FLOWEROPEN',
    'FLOWERCLOSE',
    'SEMICOLON'
    
)


def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_LESSER(t):
    r'<'
    return t

def t_GREATER(t):
    r'>'
    return t

t_LPAREN = r'\('
t_RPAREN = r'\)'
# t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_IDENTIFIER=r'[a-zA-Z]\w*'
t_NUMBER=r'[0-9]\w*'
# t_EQUAL=r'\='
t_FLOWEROPEN=r'\{'
t_FLOWERCLOSE=r'\}'


t_ignore=' \t\n'

def t_error(t):
    print(f"illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer=lex.lex()

