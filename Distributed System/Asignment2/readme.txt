Roll Number:2019201049


- Basic Input, Output 
	This is implemented by taking the input as a string from the INPUT file, and then it is splitted on the basis of " " & "\n" character is removed, further list of integers in form of string is obtained (for e.g. ["0", "1", "-1"] ), then it is converted into [ 0, 1, -1] by some inbuilt function and send back to the main function. i.e. "start".


- Question1
    For this question -
	1. First N number of processes are spawned and each one is assigned MyID
	   ( and each process calls a function nodefun with argmuments as MyID).
	2. Then for passing the token once along complete ring, array of PID ( Process Ids) of N 
Processes is transformed into pairs of PIDS i.e. { PID1, PID2 } where PID1 is the sender of the token, and PID2 is the receiver of the token.
	3. Then to start the message starting process, a function is called to init the message passing, and sends message to "Process 0", so it can start passing messages to the next PID in the ring.
	4. Once a token is recieved by the current Process, it passes to the next Process in the ring, and the count of total number of message passes ( CNT ) is decremented each time.
	5. At last, when Process 0 inturn recieves the from Nth node, CNT becomes 0 and last message is printed and further passing of tokens is stopped.



- Question2
    For this question - 
	
