#include <linux/init.h>
#include <linux/module.h>
MODULE_LICENSE("Dual BSD/GPL");
static int init(void)
{
      printk(KERN_ALERT "Tarixy OS\n");
      return 0;
}
static void exit(void)
{
      printk(KERN_ALERT "Based on Yocto Project\n");
}
module_init(init);
module_exit(exit);
