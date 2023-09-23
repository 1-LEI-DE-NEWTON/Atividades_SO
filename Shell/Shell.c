#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

#define MAX_COMMAND_LENGTH 100

int shouldPrintPrompt = 1;

void sigintHandler(int sig_num) {
    printf("\nCTRL+C não pode interromper o Shell\nUtilize CTRL+Z ou 'exit' para sair\n");   
    printf("MeuShell> ");
    fflush(stdout);
}

void ReadCommand(char *command) {
    if (shouldPrintPrompt) {
        printf("MeuShell> ");
    }
    fgets(command, MAX_COMMAND_LENGTH, stdin);   
    command[strcspn(command, "\n")] = '\0';    
}

int main() {
    char input[MAX_COMMAND_LENGTH];

    signal(SIGINT, sigintHandler);
    
    while (1) {
        ReadCommand(input);       
                
        if (strcmp(input, "exit") == 0) {
            break;
        }
                
        pid_t pid = fork();
        
        if (pid == -1) {
            perror("Erro ao criar processo filho");
            exit(EXIT_FAILURE);
        } 
        else if (pid == 0) {
            signal(SIGINT, SIG_DFL);                   
            
            char *args[] = {"/bin/bash", "-c", input, NULL};            
            execvp("/bin/bash", args);
            perror("Erro ao executar o comando");
            exit(EXIT_FAILURE);
        } 
        else {
            int status;            
            waitpid(pid, &status, 0);
        }
    }    
    return 0;
}
