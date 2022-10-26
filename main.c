#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void echo(char *txt){
    puts(txt);
}

void cls(){
    system("cls");
}

void qut(){
    exit(0);
}

void mk(char fname[255]){
    FILE *fileptr = NULL;
    fileptr = fopen(fname,"w");
    fclose(fileptr);
}