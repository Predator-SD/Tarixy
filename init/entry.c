#include "types.h"
#include "screen.h"
extern unsigned char keyboard_map[128];
extern void keyboard_handler(void);
extern char read_port(unsigned short port);
extern void write_port(unsigned short port, unsigned char data);
extern void load_idt(unsigned long *idt_ptr);
int kern_entry(){
  	const char *str = "*Tarixy OS*";
	clear();
	log(str);
	new();
	idt_init();
	kb_init();
	while(1);
	return 0;
}
