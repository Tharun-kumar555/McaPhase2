function printTable()
    {
    var number=parseInt(document.getElementById('txtNumber').value);
    var i=0;
    for( i=0 ; i<=10 ; i++)
        {
            document.write(`${number} * ${i} = ${num*i }` );
            document.write('<br/>');
            
        }
}