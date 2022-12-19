// Parser feito para corrigir o arquivo gerado pelo SNIS, que usava o delimitador ';' para
// separar dados que deveriam estar no mesmo campo (sequência de nomes de prestadores de serviços
// Tive que converter o aquivo original de UTF-16 para UTF-8
// iconv -f UTF-16 -t UTF-8 original.csv > convertivo.csv
// Para terminar de limpar, fiz o limpa.c

#include <stdio.h>
#include <wchar.h>

int main(){
  char a;
  int estado;

  estado = 0;
  while (estado != 3) {
    a = getchar();
    if (a == EOF) estado = 3;
    switch (estado) {
    case 0:
      if (a == '[') {
	putchar(a);
	estado = 1;
      } else putchar(a);
      break;
    case 1: 
      if (a == ';') {
	estado = 2;
      } else putchar(a);
      break;
    case 2:
      if (a == '[') {
	printf("| [");
	estado = 1;
      } else if (a != ' ') {
	printf(";%c", a);
	estado = 0;
      }
    }
  }
  return 0;
} 
