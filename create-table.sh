while getopts "c" opt; do
    case ${opt} in 
        c) echo -e "docker exec -it s1 python create.py";;
    esac
done