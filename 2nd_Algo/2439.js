let input = Number(require('fs').readFileSync('/dev/stdin').toString().split('\n')[0])

let star = '';
let blank='';
for (let i = 0; i < input; i++) {
    star += '*';
    for (let j = input - i; j > 1; j--) {
        blank += ' ';
    }
    console.log(blank + star);
    blank = '';
}