score=0
file_name=`echo ${@:1:1}`
input_folder=`echo ${@:2:1}`
result_folder=`echo ${@:3:1}`	
no_of_input_files=`ls $input_folder | wc -l`

remove_file="rm -f result.txt"
eval $remove_file

for((i=1; i<=$no_of_input_files; i++))
do
	eval `echo "" >> result.txt`
	eval `echo "Test Case $i" >> result.txt`
	input_file="$input_folder/input$i"
	result_file="$result_folder/result$i"
	output_file="output$i"
	no_of_processes=5

	remove_file="rm -f $output_file"
	eval $remove_file
	
	compile="mpic++ $file_name"
	eval $compile
	
	total_time=`mpirun -np $no_of_processes a.out $input_file $output_file`
	if [[ "$?" != "0" ]]; then
		eval `echo "Seg Fault" >> result.txt`
		eval `echo $total_time >> result.txt`
		continue
	fi

	o1=`cat $result_file | sed 's/[\n ]*$//'`
	o2=`cat $output_file | sed 's/[\n ]*$//'`
	
	temp="echo $o1 > $result_file"
	eval $temp
	temp="echo $o2 > $output_file"
	eval $temp

	if cmp --silent "$result_file" "$output_file";
	then
		eval `echo "AC" >> result.txt`
		eval `echo $total_time >> result.txt`
		((score=score+1))
	else
		eval`echo "WA" >> result.txt`
		eval `echo $total_time >> result.txt`
	fi
done
eval `echo "" >> result.txt`
eval `echo "Final Score = $score" >> result.txt`