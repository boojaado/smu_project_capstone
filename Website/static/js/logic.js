$(document).ready(function() {
    console.log("page loaded");

    $("#filter").click(function() {
        makePrediction();
    });
});

//Call Flask API
function makePrediction() {
    var Returns = $("#Returns")
    var Volatility = $("#Volility")
    var Node = $("#Node")
    var Date = $("#Date")
    var Sit = $("#Sit")
    var INV = $("#INV")
    var DNG = $("#DNG")
    var QNG = $("#QNG") 
    var HHDiffit = $("#HHDiffit") //hhst - sit
    var Ft = $("#FT")
    var COT = $("#COT")

    //create payload
    var payload = {
        "Returns": Returns,
        "Volatility": Volatility,
        "Node": Node,
        "Date": Date,
        "Sit": Sit,
        "INV": INV,
        "DNG": DNG,
        "QNG": QNG,
        "HHDiffit": HHDiffit,
        "Ft": Ft,
        "COT": COT
    }

    //perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);

            $("#output").text(returnedData["prediction"])
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });
}