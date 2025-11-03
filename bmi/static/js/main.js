const btn= document.getElementById("btn");
btn.addEventListener("click",function(){
    const height = Number(document.getElementById("height").value);
    const weight = Number(document.getElementById("weight").value);
    const bmi = weight / (height/100) / (height/100);
    document.getElementById("result").innerText = `あなたのbmiは${bmi}です。`
    if(bmi<25){
        document.getElementById("result").innerText += "あなたは普通体重です。"
    }

})