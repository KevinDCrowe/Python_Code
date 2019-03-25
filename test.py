#include "simpletools.h"                      
#include "adcDCpropab.h"                      
#include "stdio.h"
#include "stdlib.h"

int main(){
 
  sd_mount(22,23,24,25);
  adc_init(21,20,19,18);
  int a[1000];
  for (int i=0;i<1000;i++){
  a[i]=adc_in(3);
  
}
FILE *fp = fopen("test.txt","w");
fwrite(&a,sizeof(a),1,fp);
fclose(fp);


