// zombie.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main() {
    pid_t pid = fork();
    if (pid == 0) {
        printf("Дочерний процесс выполняется...\n");
        exit(0); 
    } else if (pid > 0) {
        printf("Родительский процесс ожидает...\n");
        sleep(14);
    } else {
        perror("fork");
        return 1;
    }
    return 0;
}