#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

//prioriza leitores

#define NUM_LEITORES 3
#define NUM_ESCRITORES 2

pthread_mutex_t mutex_leitores = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t mutex_escritores = PTHREAD_MUTEX_INITIALIZER;
int num_leitores = 0;

void *leitor(void *arg) {
    while (1) {
        pthread_mutex_lock(&mutex_leitores);
        num_leitores++;
        if (num_leitores == 1) {
            pthread_mutex_lock(&mutex_escritores); 
        }
        pthread_mutex_unlock(&mutex_leitores);

        
        printf("Leitor lendo...\n");
        usleep(1000000); 

        pthread_mutex_lock(&mutex_leitores);
        num_leitores--;
        if (num_leitores == 0) {
            pthread_mutex_unlock(&mutex_escritores); 
        }
        pthread_mutex_unlock(&mutex_leitores);

        usleep(1000000); 
    }
    return NULL;
}

void *escritor(void *arg) {
    while (1) {
        pthread_mutex_lock(&mutex_escritores);

        
        printf("Escritor escrevendo...\n");
        usleep(2000000); 

        pthread_mutex_unlock(&mutex_escritores);

        usleep(2000000); 
    }
    return NULL;
}

int main() {
    pthread_t leitores[NUM_LEITORES];
    pthread_t escritores[NUM_ESCRITORES];
    
    for (int i = 0; i < NUM_LEITORES; i++) {
        pthread_create(&leitores[i], NULL, leitor, NULL);
    }
    
    for (int i = 0; i < NUM_ESCRITORES; i++) {
        pthread_create(&escritores[i], NULL, escritor, NULL);
    }
    
    for (int i = 0; i < NUM_LEITORES; i++) {
        pthread_join(leitores[i], NULL);
    }
    
    for (int i = 0; i < NUM_ESCRITORES; i++) {
        pthread_join(escritores[i], NULL);
    }

    return 0;
}
