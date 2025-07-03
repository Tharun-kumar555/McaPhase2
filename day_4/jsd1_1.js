function add()
{
    var num1,num2,Ans;
    num1=parseInt(document.getElementById("txtfirstnumber").value);
    num2=parseInt(document.getElementById("txtsecondnumber").value);
    Ans=num1+num2
    document.getElementById("txtanswer").value=Ans;
   


}
function sub()
{
    var num1,num2,Ans;
    num1=parseInt(document.getElementById("txtfirstnumber").value);
    num2=parseInt(document.getElementById("txtsecondnumber").value);
    Ans=num1-num2
    document.getElementById("txtanswer").value=Ans;
   
 
}
function clean()
{
    
    document.getElementById("txtfirstnumber").value = "";
    document.getElementById("txtsecondnumber").value = "";
    document.getElementById("txtanswer").value = "";
}
function mul(){
    var num1,num2,mul;
    num1=parseInt(document.getElementById("txtfirstnumber").value);
    num2=parseInt(document.getElementById("txtsecondnumber").value);
    mul=num1*num2;
    document.getElementById("txtanswer").value=mul;
}
function div(){
    var num1,num2,mul;
    num1=parseInt(document.getElementById("txtfirstnumber").value);
    num2=parseInt(document.getElementById("txtsecondnumber").value);
    div=num1/num2;
    document.getElementById("txtanswer").value=div;
}