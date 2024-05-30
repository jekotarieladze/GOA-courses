const foods = [
    {name :"borjomi", 
    name2:"cupcake", 
    name3:"adjaruli"
    }];

foods.forEach(foods => {
    foods.getName2 = function(){
        return this.name2;
    };

    foods.getName = function(){
        return this.name1
    };

    foods.getName = function(){
        return this.name
    };
});


function manualReduce(arr, func, startingValue){
    let result = startingValue;
    for (let i = 0; i < arr.length; i++){
        result = func(result, arr[i])
    }
    return result;
}

const strArr = "data".split("")

const result = manualReduce(strArr, function(result, nextElement){
    return result + nextElement
}, "data")

console.log(result)