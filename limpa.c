// Limpa foi feito como complemento para parser.c
// O problema é que outros dados também foram separados por ';' apesar de pertencerem ao mesmo campo.
// Quase funcionou, mas em alguns momentos perdia o '\n' e acabava não separando linhas, colocando mais de um município na mesma linha

#include <stdio.h>

int main(){
  char a;
  int ia;
  int estado;
  int conta = 0;

  estado = 0;
  while (estado != 3) {
    a = getchar();
    if (a == EOF) estado = 3;
    if (a == '\n') conta = 0;
    switch (estado) {
    case 0:
      if (a == ';') {
	putchar(a);
	conta++;
	if (conta == 5) estado = 1;
      } else
	putchar(a);
      break;
    case 1:
      ia = a - '0';
      if ((ia >= 0) && (ia <= 9)) {
	putchar(a);
	estado = 0;
      };
      break;
      }
  }
  return 0;
} 
