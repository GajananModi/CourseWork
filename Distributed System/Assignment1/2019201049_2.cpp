#include<bits/stdc++.h>
#include <mpi.h>
#include <time.h>

double startTime;

/* swap entries in array v at positions i and j; used by quicksort */
static inline /* this improves performance; Exercise: by how much? */

void swap(int* a, int* b)  
{  
    int t = *a;  
    *a = *b;  
    *b = t;  
}  

int * merge(int arr1[],int n1, int arr2[],
                             int n2) 
{ 
    int i = 0, j = 0, k = 0; 
    int * arr3 = (int *)malloc((n1 + n2) * sizeof(int));

  
    // Traverse both array 
    while (i<n1 && j <n2) 
    { 
        // Check if current element of first 
        // array is smaller than current element 
        // of second array. If yes, store first 
        // array element and increment first array 
        // index. secondwise do same with second array 
        if (arr1[i] < arr2[j]) 
            arr3[k++] = arr1[i++]; 
        else
            arr3[k++] = arr2[j++]; 
    } 
  
    // Store remaining elements of first array 
    while (i < n1) 
        arr3[k++] = arr1[i++]; 
  
    // Store remaining elements of second array 
    while (j < n2) 
        arr3[k++] = arr2[j++]; 

    return arr3;
} 

int partition (int arr[], int low, int high)  
{  
    int pivot = arr[high]; // pivot  
    int i = (low - 1); // Index of smaller element  
  
    for (int j = low; j <= high - 1; j++)  
    {  
        // If current element is smaller than the pivot  
        if (arr[j] < pivot)  
        {  
            i++; // increment index of smaller element  
            swap(&arr[i], &arr[j]);  
        }  
    }  
    swap(&arr[i + 1], &arr[high]);  
    return (i + 1);  
}  
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quicksort(int arr[], int low, int high)  
{  
    if (low < high)  
    {  
        /* pi is partitioning index, arr[p] is now  
        at right place */
        int pi = partition(arr, low, high);  
  
        // Separately sort elements before  
        // partition and after partition  
        quicksort(arr, low, pi - 1);  
        quicksort(arr, pi + 1, high);  
    }  
}  



int main(int argc, char ** argv)
{
  int n,c,s,o,part;
  int * complete_array = NULL;
  int * first_part;
  int * second;
  int p, id;
  MPI_Status status;
  double e1,e2;
  FILE * file = NULL;
  int i;

  if (argc!=3) {
    fprintf(stderr, "I/p error %s \n", argv[0]);
    exit(1);
  }

  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &p);
  MPI_Comm_rank(MPI_COMM_WORLD, &id);

  if (id == 0) {
    // read size of complete_array
    file = fopen(argv[1], "r");
    fscanf(file, "%d", &n);
    // compute first_part size
    c=n/p;
    if(c==0)
    {
      c=1;
    }
    if(n%p!=0 && n>=p)
    {
      c=n/p+1;
    }
   
    
    // read complete_array from file
    complete_array = (int *)malloc(p*c * sizeof(int));
    for (i = 0; i < n; i++)
      fscanf(file, "%d", &(complete_array[i]));
    fclose(file);
    // pad complete_array with 0 -- doesn't matter
    for (i = n; i < p*c; i++)
      complete_array[i] = 0;
  }

  // start the timer
  MPI_Barrier(MPI_COMM_WORLD);
  e1= MPI_Wtime();

  // broadcast size
  MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);

  // compute first_part size
  c = n/p;
 
   if(c==0)
    {
      c=1;
    }
    if(n%p!=0 && n>=p)
    {
      c=n/p+1;
    }

  // scatter complete_array
  first_part = (int *)malloc(c * sizeof(int));
  MPI_Scatter(complete_array, c, MPI_INT, first_part, c, MPI_INT, 0, MPI_COMM_WORLD);
  free(complete_array);
  complete_array = NULL;

  // compute size of own first_part and sort it
  s = (n >= c * (id+1)) ? c : n - c * id;
  quicksort(first_part, 0, s-1);

  // up to log_2 p merge parts
  for (part = 1; part < p; part = 2*part) {
    if (id % (2*part) != 0) {
      // id is no multiple of 2*part: send first_part to id-part and exit loop
      MPI_Send(first_part, s, MPI_INT, id-part, 0, MPI_COMM_WORLD);
      break;
    }
    // id is multiple of 2*part: merge in first_part from id+part (if it exists)
    if (id+part < p) {
      // compute size of first_part to be received
      o = (n >= c * (id+2*part)) ? c * part : n - c * (id+part);
      // receive second first_part
      second = (int *)malloc(o * sizeof(int));
      MPI_Recv(second, o, MPI_INT, id+part, 0, MPI_COMM_WORLD, &status);
      // merge and free memory
      complete_array = merge(first_part, s, second, o);
      free(first_part);
      free(second);
      first_part = complete_array;
      s = s + o;
    }
  }

  // stop the timer
  e2 = MPI_Wtime();

  // write sorted complete_array to out file and print out timer
  if (id == 0) {
    file = fopen(argv[2], "w");
    //fprintf(file, "%d\n", s);   // assert (s == n)
    for (i = 0; i < s; i++)
      fprintf(file, "%d ", first_part[i]);
    fclose(file);
    printf("Quicksort %d ints on %d procs: %f secs\n", n, p, e2-e1);
  }

  MPI_Finalize();
  return 0;
}