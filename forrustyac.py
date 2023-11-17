import ply.yacc as yacc
from forrustlex import tokens

start='declaration'


def p_declaration(p):
    '''
    declaration : FOR IDENTIFIER IN NUMBER DOT NUMBER FLOWEROPEN FLOWERCLOSE
                | FOR IDENTIFIER IN IDENTIFIER FLOWEROPEN FLOWERCLOSE
                
                
    '''
    print('valid for declaration')

    #works for the following prompts
    #for <variable> in <number>..<number>{}
    #for <variable> in <variable>{}

def p_error(p):
    if p:
        print(f"Syntax error")
    else:
        print("Syntax error at EOF")


parser=yacc.yacc()

if __name__=="__main__":
    while True:
        try:
            data=input('enter a for loop declaration  ')
            if not data:
                break
            parser.parse(data)
        except EOFError:
            break