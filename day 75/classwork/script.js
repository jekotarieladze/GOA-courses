let globalValue = {
    nestedValue: null
};

function setNestedValue(newValue){
    let localValue = newValue;
    globalValue.nestedValue = localValue;
}

setNestedValue("jeko, tarieladze");

console.log(globalValue.nestedValue);