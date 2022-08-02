#!/bin/bash
compile () {
    echo "[+] Compiling directory $dir"
    for file in ${files[@]}
    do
        if [[ $file == *".c" ]]; then
            echo "    [+] Compiling $file"
            gcc -c -fPIC ../source/$dir/$file -o $file.o
        fi
    done
}

dirs=($(ls ../source))
echo "Directories: ${dirs[@]}"

for dir in ${dirs[@]}; do
    files=($(ls ../source/$dir))
    compile
done

PWD=$(pwd)

dependencies=()
files=($(ls *.o))

for file in ${files[@]}
do
    dependencies[${#dependencies[@]}]="$PWD/$file"
done

ld -shared -o libopenv2g.so ${dependencies[@]} -lc
