#!/bin/bash

HAS_N=""
HAS_C=""

search()
{
	for i in $(ls)
	do
		if [[ "$i" == *.tar.gz || "$i" == *.tgz ]]
		then
			mkdir temp_extract_9999
			tar -xf "$i" --directory temp_extract_9999 
			cd temp_extract_9999
			search "$@"
			cd ..
			rm -r temp_extract_9999
		else
			if [ -d $i ]
			then 
				cd $i
				search "$@"
				cd ..
			else
				grep "much Open such Stack" $i -H $HAS_C $HAS_C
			fi
		fi
	done
}

verify_file_name()
{
	if [ -e "$1" ]
	then 	
		if [[ "$1" == *.tar.gz || "$1" == *.tgz ]]
		then
			mkdir /tmp/temp_unzip
			tar -xf "$1" --directory "/tmp/temp_unzip"
			cd /tmp/temp_unzip
			search "$@"
			cd ..
			rm -r temp_unzip
		else
			if [ -d "$1" ]
			then
				cd "$1"
				search "$@"
			else
				echo "File name must be a directory or a .tar.gz or tgz type"
				exit 1
			fi 
			
		fi
	else
		echo "File name does not exist"
		exit 1
	fi
}


parse_command()
{
	file_name=0

	while (("$#"))
	do
		if [ "$1" == "-n" ]
		then 
			HAS_N="-n"
		else
			if [ "$1" == "-c" ]
			then 
				HAS_C="-c"
			else
				file_name="$1"
			fi
		fi

		shift	
	done

	verify_file_name "$file_name" "$@"
}


parse_command_test()
{
	if [ "$#" -le "0" ]
	then 
		echo "File name missing"
		exit 1
	else
		parse_command "$@"
	fi
}


main()
{
	USR_ID=$UID

	if [ $USR_ID -ne "0" ]
	then
		parse_command_test "$@"
	else
		echo "You must be non-root user"
		exit 1
	fi
}


main "$@"

