
-module('2019201049_2').

-export([main/1, readlines/1]).

string_to_list(String) ->
    lists:map(fun(X) -> {Int, _} = string:to_integer(X), 
                        Int end, 
              L=string:tokens(String,"\n")),
                L.



readlines(FileName) ->
    	{ok, File} = file:open(FileName,[read]),
        {ok, Txt} = file:read(File,1024 * 1024), 
        L = string_to_list(Txt),
        io:fwrite("~p~n",[L]),
        {P,[]} = string:to_integer(lists:nth(1,L)),
        [M,N]=string:tokens(lists:nth(2,L), " "),
        N1 = string:to_integer(M),
        M1 = string:to_integer(N),
        {S1,[]}=string:to_integer(lists:nth(8,L)).
        %io:fwrite("Source:~p\n",[Source]).
        
        %io:fwrite("~p~n",[maps:put(3,[{1,4}],Graph)]),
        %Iterator = iterator(3, Value)

        %Vertices = lists:seq(1,V),
         %io:fwrite("~p",[MSSS]).
    	



main(Args) ->
	[Input, Output] = Args,
        {ok, _} = file:open(Output, [write]),
	readlines(Input),
	io:fwrite("Hellow world").
	%Processes = [spawn(?MODULE, nodefun, [X,Output]) || X  <- lists:seq(0, N-1)]
	%ProcessesArr = lists:zip(Processes, tl(Processes) ++ [hd(Processes)]),
	%sendMessage(V, N, ProcessesArr).