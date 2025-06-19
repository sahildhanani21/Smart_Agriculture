

fetch("https://agriitech.000webhostapp.com/API/fetchSecurityapi.php").then((data)=>{
    return data.json();
}).then((completedata1)=>{
    completedata1.security[completedata1.security.length-1].sec_value;
    document.getElementById("sec").innerText=completedata1.security[completedata1.security.length-1].sec_value;
})



fetch("https://agriitech.000webhostapp.com/API/fetchWaterlevelapi.php").then((data)=>{
    return data.json();
}).then((completedata2)=>{
    // console.log(completedata2);
    completedata2.Waterlevel[completedata2.Waterlevel.length-1].wl_value;
    document.getElementById("water").innerText=completedata2.Waterlevel[completedata2.Waterlevel.length-1].wl_value;
})


fetch("https://agriitech.000webhostapp.com/API/fetchSmokeapi.php").then((data)=>{
    // console.log(data);
    return data.json();
}).then((completedata3)=>{
    completedata3.Smoke[completedata3.Smoke.length-1].smoke_value
    document.getElementById("smoke").innerText=completedata3.Smoke[completedata3.Smoke.length-1].smoke_value;
})


fetch("https://agriitech.000webhostapp.com/API/fetchfireapi.php").then((data)=>{
    return data.json();
}).then((completedata4)=>{
    completedata4.fire[completedata4.fire.length-1].fire_value;
    document.getElementById("fire").innerText=completedata4.fire[completedata4.fire.length-1].fire_value;
})


fetch("https://agriitech.000webhostapp.com/API/fetchSoilapi.php").then((data)=>{
    // console.log(data);
    return data.json();
}).then((completedata5)=>{
    completedata5.Soil[completedata5.Soil.length-1].soil_value
    document.getElementById("Soil").innerText=completedata5.Soil[completedata5.Soil.length-1].soil_value;
})


fetch("https://agriitech.000webhostapp.com/API/fetchrainapi.php").then((data)=>{
    return data.json();
}).then((completedata6)=>{
    completedata6.rain[completedata6.rain.length-1].sec_value
    document.getElementById("rain").innerText=completedata6.rain[completedata6.rain.length-1].rain_value;
})
    
