const person(name, surname, age) = {
    this.name: 'jeko',
    this.surname: 'tarieladze',
    this.age: 14,

    this.info = function( ) {
        console.log('hello and welocme ${this.name} ${this.lastname} $(this.age}'); //hello and welcome jeko tarieladze 14
    }
}

const NewPerson = new person("jeko","tarieladze",14)
NewPerson.inforamtion( );