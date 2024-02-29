function Flight(flightCode, flightStatus) {
    this.flightCode = flightCode;
    this.flightStatus = flightStatus;
}


let flight1 = new Flight("ABC123", "On Time");
let flight2 = new Flight("XYZ789", "Delayed");