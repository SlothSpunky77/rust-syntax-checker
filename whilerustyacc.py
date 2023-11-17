import ply.yacc as yacc
from whilerustlex import tokens

start='declaration'

def p_declaration(p):
    '''
    declaration : WHILE LPAREN IDENTIFIER LESSER IDENTIFIER RPAREN FLOWEROPEN FLOWERCLOSE
                | WHILE LPAREN IDENTIFIER GREATER IDENTIFIER RPAREN FLOWEROPEN FLOWERCLOSE
                | WHILE LPAREN TRUE RPAREN FLOWEROPEN FLOWERCLOSE
                
    '''
    print('valid while declaration')

    #works for the following prompts
    # while(<variable> < <variable>){}
    # while(<variable> > <variable>){}
    # while(true){}
def p_error(p):
    if p:
        print(f"Syntax error")
    else:
        print("Syntax error at EOF")


parser=yacc.yacc()

if __name__=="__main__":
    while True:
        try:
            data=input('enter a while loop declaration  ')
            if not data:
                break
            parser.parse(data)
        except EOFError:
            break