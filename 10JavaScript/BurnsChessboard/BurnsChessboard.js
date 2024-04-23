let size = parseInt(prompt("What integer value should the size of the chessboard be?"))

for (let i = 0; i < size; i++){
    let row = '';
    for (let j = 0; j < size; j++){
        if ((i + j) % 2 == 0){
            row += '#';
        }
        else{
            row += ' ';
        }
    } console.log(row)
}
