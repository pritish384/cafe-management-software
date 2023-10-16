function createSalesChart(sales_data) {
  
    var salesChartCanvas = $('#salesChart').get(0).getContext('2d')
    var salesChartData = {
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July' , 'August', 'September', 'October', 'November', 'December'],
      datasets: [
        {
          label: 'Sales',
          data: JSON.parse(sales_data),
          backgroundColor: 'transparent',
          borderColor: '#007bff',
          pointRadius: 4,
          pointBackgroundColor: '#007bff',
          pointBorderColor: 'rgba(0, 123, 255, 0.9)',
          pointHoverRadius: 7,
          pointHoverBackgroundColor: 'rgba(0, 123, 255, 0.9)',
          pointHoverBorderColor: 'rgba(0, 123, 255, 0.9)',
          pointHitRadius: 10,
          pointBorderWidth: 2,
          borderWidth: 2,
          fill: false
        }
      ]
    }
    var maxSales = Math.max(...salesChartData.datasets[0].data);
    var salesChartOptions = {
      maintainAspectRatio: false,
      responsive: true,
      legend: {
        display: false
      },
      scales: {
        xAxes: [{
          gridLines: {
            drawOnChartArea: false
          }
        }],
        yAxes: [{
          ticks: {
            beginAtZero: true,
            maxTicksLimit: 5,
            stepSize: Math.ceil(maxSales / 5),
            max: maxSales
          },
          gridLines: {
            display: false
          }
        }]
      },
      elements: {
        line: {
          tension: 0.4
        },
        point: {
          radius: 4,
          borderWidth: 2,
          hoverRadius: 4,
          hoverBorderWidth: 2
        }
      }
    }

    // This will get the first returned node in the jQuery collection.
    var salesChart = new Chart(salesChartCanvas, {
      type: 'line',
      data: salesChartData,
      options: salesChartOptions
    })
  }



document.addEventListener("DOMContentLoaded", function () {
  createSalesChart(salesChartData);
});