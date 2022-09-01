while getopts "c" opt; do
    case ${opt} in 
        c) echo -e "cd project && cd s1 && docker exec -it s1 python create.py";;
    esac
done    