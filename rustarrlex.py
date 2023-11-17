import ply.lex as lex

tokens=(
    'IDENTIFIER',
    'LET',
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'SEMICOLON',
    'EQUAL',
   

)




def t_LET(t):
    r'let'
    return t

t_LPAREN = r'\['
t_RPAREN = r'\]'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_IDENTIFIER=r'[a-zA-Z]\w*'
t_NUMBER=r'[0-9]\w*'
t_EQUAL=r'\='

t_ignore=' \t'

def t_error(t):
    print(f"illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer=lex.lex()

