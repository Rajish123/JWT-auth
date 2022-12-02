function Calculation(n,c){
    if(!c){
        c= 0;
    }
    if(n<2){
        throw new Error('Invalid Input');
    }
    while(n>2){
        if(n==2){
            return res = 1/ n+c;
        }
        else{
            c = c+1/(n*(n-1));
        }
        n--;
    }
}