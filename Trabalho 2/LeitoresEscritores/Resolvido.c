#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

//prioriza escritores

#define NUM_LEITORES 3
#define NUM_ESCRITORES 2

pthread_mutex_t mutex_leitores = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t mutex_escritores = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t turno_escritor = PTHREAD_MUTEX_INITIALIZER;
int num_leitores = 0;
int num_escritores_esperando = 0;

void *leitor(void *arg) {
    while (1) {
        pthread_mutex_lock(&mutex_leitores);
        num_leitores++;
        if (num_leitores == 1) {
            pthread_mutex_lock(&turno_escritor); 
        }
        pthread_mutex_unlock(&mutex_leitores);

        printf("Leitor lendo...\n");
        usleep(100); 

        pthread_mutex_lock(&mutex_leitores);
        num_leitores--;
        if (num_leitores == 0) {
            pthread_mutex_unlock(&turno_escritor); 
        }
        pthread_mutex_unlock(&mutex_leitores);

        usleep(100); 
    }
    return NULL;
}

void *escritor(void *arg) {
    while (1) {
        pthread_mutex_lock(&mutex_escritores);
        num_escritores_esperando++;
        pthread_mutex_unlock(&mutex_escritores);

        pthread_mutex_lock(&turno_escritor);
        pthread_mutex_unlock(&turno_escritor);

        
        printf("Escritor escrevendo...\n");
        usleep(200); 

        pthread_mutex_lock(&mutex_escritores);
        num_escritores_esperando--;
        pthread_mutex_unlock(&mutex_escritores);

        usleep(200); 
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
