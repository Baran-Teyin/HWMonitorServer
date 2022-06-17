/*
    @author: xhico
 */

let chart1, chart2, chart3;
let chartNames = ["temp_c", "temp_f", "humidity"];

function timeBtn() {
    let numberTime = document.getElementById("numberTime").value;
    let unitTime = document.getElementById("unitTime").value;
    chart1.destroy();
    chart2.destroy();
    chart3.destroy();
    initCharts(numberTime, unitTime);
}

function drawStuff(chartName, JSON) {
    let seriesData = JSON[chartName];
    let chartTitle;
    if (chartName === "temp_c") {
        chartTitle = "Temperature History (ºC)";
    } else if (chartName === "temp_f") {
        chartTitle = "Temperature History (ºF)";
    } else if (chartName === "humidity") {
        chartTitle = "Humidity History (%)";
    }

    let chartOptions = {
        chart: {renderTo: chartName},
        title: {text: chartTitle},
        exporting: {enabled: false},
        credits: {enabled: false},
        legend: {enabled: false},
        yAxis: {title: {text: chartTitle.replace(" History ", " ")}},
        xAxis: {
            title: {text: ''}, type: 'string', labels: {
                enabled: true,
                formatter: function () {
                    return seriesData[this.value][0];
                },
            }
        },
        series: [{
            name: chartTitle.replace(" History ", " "), data: seriesData
        }]
    }

    if (chartName === "temp_c") {
        chart1 = new Highcharts.Chart(chartOptions);
    } else if (chartName === "temp_f") {
        chart2 = new Highcharts.Chart(chartOptions);
    } else if (chartName === "humidity") {
        chart3 = new Highcharts.Chart(chartOptions);
    }
}

async function initCharts(numberTime, unitTime) {
    // Get Ambient Data
    console.log("Get Ambient Data");
    let JSON = await $.ajax({
        method: "post", url: "/json/ambientInfo", data: {numberTime: numberTime, unitTime: unitTime}, success: function (data) {
            return data;
        }
    });

    // Set charts
    chartNames.forEach(function (chartName) {
        drawStuff(chartName, JSON);
    });
}

window.addEventListener('DOMContentLoaded', async function main() {
    console.log("---------------------");
    document.getElementById("navbar_humidity").classList.add("active");
    initCharts(8, "hour");
});