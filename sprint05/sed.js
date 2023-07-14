function factorial(n) {
    // your code
    let result = [];
    let prev = 1
    for (let i=1; i<=n;i++){

    result.push(prev*i);
    prev=prev*i;
    }

    return result;
}

function processArray(arr, factorial){
    let
    for ( let i of arr){
         factorial(i);
    }
}

console.log(processArray([1, 2, 3, 4, 5, 6], factorial));