// Parser feito para corrigir o arquivo de CNPJ do Ministério da Economia
// O problema é a incidência de ";" no meio do texto, o que quebra as colunas

#include <stdio.h>
#include <wchar.h>

int main(){
  char a;
  int estado;
  char b;

  estado = 0;
  while (estado != 4) {
    a = getchar();
    if (a == EOF) estado = 4;
    switch (estado) {
    case 0:
      putchar(a);
      estado = 1;
      break;
    case 1:
      switch (a){
      case '"':
	putchar(a);
	estado = 2;
	break;
      case ';':
	putchar(' ');
	break;
      default:
	putchar(a);
	break;
      }
      break;
    case 2:
      switch (a){
      case '"':
	putchar(a);
	estado = 2;
	break;
      case ';':
	b = a;
	estado = 3;
	break;
      default:
	putchar(a);
	estado = 1;
	break;
      }
      break;
    case 3:
      if (a == '"') {
	putchar(b);
	putchar(a);
	estado = 1;
      } else {
	putchar(a);
	estado = 1;
      }
      break;
    }
  }
  return 0;
} 
