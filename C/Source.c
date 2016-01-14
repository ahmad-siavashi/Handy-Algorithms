/* In his exalted name
* This algorithm evaluates an infix expression.
* C implementation by Ahmad Siavashi (ahmad.siavashi@gmail.com)
* Date: 5/12/2014
*/
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

typedef unsigned char byte;

char expr[100] = "-1+2*3";

void eval();

int main(){
	eval();
	printf("%d\n",operand_stack[0]);
}

long int operand_stack[100];
char operator_stack[100];

int operand_sp = 0, operator_sp = 0;
long int operand_pop(){
	return operand_stack[--operand_sp];
}
char operator_pop(){
	return operator_stack[--operator_sp];
}
void operand_push(long int item){
	operand_stack[operand_sp++] = item;
}
void operator_push(char item){
	operator_stack[operator_sp++] = item;
}
byte operator_isEmpty(){
	if(operator_sp==0)
		return 1;
	else
		return 0;
}

char operator_top(){
	return operator_stack[operator_sp-1];
}

byte operand_isEmpty(){
	if(operand_sp==0)
		return 1;
	else
		return 0;
}

int op_precedence(char op){
	switch(op){
	case '#':
		return 0;
	case '+':
	case '-':
		return 5;
	case '*':
	case '/':
		return 10;
	}
}

void eval(){
	long int op = 0;
	int i = 0;
	operator_push('#');
	for(i = 0; i < 100 && expr[i] != '\0' ; i++){
		if(expr[i] >= '0' && expr[i] <= '9'){
			op = (10 * op) + (expr[i] - '0');
		}else{
			operand_push(op);
			op = 0;
			//
			if(op_precedence(expr[i]) > op_precedence(operator_top())){
				operator_push(expr[i]);
			}else{
				do{
					int op2 = operand_pop();
					int op1 = operand_pop();
					switch (operator_pop())
					{
					case '+':
						operand_push(op1 + op2);
						break;
					case '-':
						operand_push(op1 - op2);
						break;
					case '*':
						operand_push(op1 * op2);
						break;
					case '/':
						operand_push(op1 / op2);
						break;
					default:
						break;
					}
				}while(op_precedence(expr[i]) <= op_precedence(operator_top()));
				operator_push(expr[i]);
			}


		}
	}
	if(op != 0 && expr[i] == '\0'){
		operand_push(op);
		op = 0;
	}

	{
		
		while(operator_top() != '#'){
			int op1 = operand_pop(), op2 = operand_pop();
			switch (operator_pop())
			{
			case '+':
				operand_push(op1 + op2);
				break;
			case '-':
				operand_push(op1 - op2);
				break;
			case '*':
				operand_push(op1 * op2);
				break;
			case '/':
				operand_push(op1 / op2);
				break;
			default:
				break;
			}
		}
	}
}
