document.addEventListener("DOMContentLoaded", selectDefaultBusStops)
    
function getSchedule(stop_id){

    let xhttp = new XMLHttpRequest() 
    xhttp.open('GET', `http://127.0.0.1:5000/{stop_id}`)
    xhttp.timeout = 2000
    xhttp.onerror = () => { console.log("xhttp error") }
    xhttp.onreadystatechange = updateSchedule

    // () => {
    //     console.log(xhttp.status)
    //     console.log(xhttp.responseText)
    // }

    }


    function selectDefaultBusStops(){
        // something with location services
    }


    let bus_stops = document.getElementById("bus_stop")
    bus_stops.addEventListener("click", getSchedule)
    
    let nearestBusStops = [0, 1]
    nearestBusStops.forEach(
        stop => { bus_stops[stop].setAttribute('selected', "selected") })

    let bus_stops_selected = bus_stops.selectedOptions

    function getSchedule(){
        console.log("get that schedule")
        // bus_stops.forEach((stop)=>console.log(stop.label))
    }

    function updateSchedule(api_response){
        api_response = '{"r1": [34, 49], "r2": [36, 51], "r3": [38, 53]}'
    }