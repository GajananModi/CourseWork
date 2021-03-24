#include <mpi.h> 
#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include<bits/stdc++.h>
#include<time.h>
  
// size of array 

// Temporary array for slave process 
int a2[3000]; 
  
int main(int argc, char* argv[]) 
{ 
  
    int pid, np, 
        elements_per_process, 
        n_elements_recieved; 
     double elapse,elapse1;
    //int n = atoi(argv[1]);
    //int a[n];

    FILE * file = NULL;
    int n;

  if (argc!=3) 
  {
    fprintf(stderr, "Usage: mpirun -np <num_procs> %s <in_file> <out_file>\n", argv[0]);
    exit(1);
  }
  file = fopen(argv[1], "r");
  fscanf(file, "%d", &n);
  int a[n];
  for(int i=0;i<n;i++)
  {
           a[i]=i+1; 
  }
  MPI_Status status; 
  
    // Creation of parallel processes 
    MPI_Init(&argc, &argv); 
  
    // find out process ID, 
    // and how many processes were started 
    MPI_Comm_rank(MPI_COMM_WORLD, &pid); 
    MPI_Comm_size(MPI_COMM_WORLD, &np); 
  
    // master process 
    if (pid == 0) { 
        int index, i; 
        elements_per_process = n / np; 
        elapse =  MPI_Wtime();

        // check if more than 1 processes are run 
        if (np > 1) { 

            // distributes the portion of array 
            // to child processes to calculate 
            // their partial sums 
            for (i = 1; i < np - 1; i++) { 
                index = i * elements_per_process; 
  
                MPI_Send(&elements_per_process, 
                         1, MPI_INT, i, 0, 
                         MPI_COMM_WORLD); 
                MPI_Send(&a[index], 
                         elements_per_process, 
                         MPI_INT, i, 0, 
                         MPI_COMM_WORLD); 
            } 
  
            // last process adds remaining elements 
            index = i * elements_per_process; 
            int elements_left = n - index; 
  
            MPI_Send(&elements_left, 
                     1, MPI_INT, 
                     i, 0, 
                     MPI_COMM_WORLD); 
            MPI_Send(&a[index], 
                     elements_left, 
                     MPI_INT, i, 0, 
                     MPI_COMM_WORLD); 
        } 
  
        // master process add its own sub array 
        double sum = 0.0; 
        for (i = 0; i < elements_per_process; i++)
        {     double temp =1.0/(a[i]*a[i]);
            sum += temp; 

        }
  
        // collects partial sums from other processes 
        double tmp; 
        for (i = 1; i < np; i++) { 
            MPI_Recv(&tmp, 1, MPI_FLOAT, 
                     MPI_ANY_SOURCE, 0, 
                     MPI_COMM_WORLD, 
                     &status); 
            int sender = status.MPI_SOURCE; 
  
            sum += tmp; 
        } 
         
        elapse1 = MPI_Wtime();

        file = fopen(argv[2], "w");
    //fprintf(file, "%d\n", s);   // assert (s == n)
        
        fprintf(file, "%f\n",sum);
        fclose(file);
        printf("Time : %f\n", elapse1-elapse); 
    } 
    // slave processes 
    else { 
        MPI_Recv(&n_elements_recieved, 
                 1, MPI_INT, 0, 0, 
                 MPI_COMM_WORLD, 
                 &status); 
  
        // stores the received array segment 
        // in local array a2 
        MPI_Recv(&a2, n_elements_recieved, 
                 MPI_INT, 0, 0, 
                 MPI_COMM_WORLD, 
                 &status); 
  
        // calculates its partial sum 
        double partial_sum = 0.0; 
        for (int i = 0; i < n_elements_recieved; i++)
        { 
            double t1=1.0/(a2[i]*a2[i]);
            partial_sum += t1; 
        }
  
        // sends the partial sum to the root process 
        MPI_Send(&partial_sum, 1, MPI_FLOAT, 
                 0, 0, MPI_COMM_WORLD); 
    } 
    
  
    // cleans up all MPI state before exit of process 
    MPI_Finalize(); 
  
    return 0; 
} 